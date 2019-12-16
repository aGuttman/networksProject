import networkx as nx
import copy
from webweb import Web
from networkx.algorithms import bipartite
import numpy as np
import os
import matplotlib.pyplot as plt

def createGraph(edges, names, jobs):
	fp = open(edges, 'r')

	B = nx.Graph()

	fp1 = open(names)
	namelist = []
	for line in fp1:
		namelist.append(line.strip())

	fp2 = open(jobs)
	joblist = []
	for line in fp2:
		joblist.append(line.strip())

	print(len(namelist))
	print(len(joblist))

	B.add_nodes_from(namelist, bipartite=0)
	B.add_nodes_from(joblist, bipartite=1)

	for line in fp:
		l = line.strip().split('\t')
		for i in l:
			if i != l[0]:
				B.add_edge(l[0],i)

	bottom_nodes, top_nodes = bipartite.sets(B)

	top_nodes = {n for n, d in B.nodes(data=True) if d['bipartite']==0}

	G = bipartite.projected_graph(B, top_nodes)
	print(G.number_of_nodes())
	# Web(nx.to_numpy_matrix(G)).show()
	return G


def mod(G):

	Qs = []
	groupsList = []
	# Q=0

	# for node in G.nodes:
	# 	Q += -(G.degree[node]/(2*G.number_of_edges()))**2

	mat = [[0 for y in range(G.number_of_nodes())] for x in range(G.number_of_nodes())]

	sens = list(G.nodes())
	sens.sort()

	xcount = 0
	for x in sens:
		ycount = 0
		row = mat[xcount]
		for y in sens:
			mat[xcount][ycount] = (G.has_edge(x, y)/(2*G.number_of_edges()))
			ycount+=1
		xcount+=1

	q = 0
	for x in range(len(mat)):
		q += mat[x][x] - sum(mat[x])**2

	Qs.append(q)

	groups = [[s] for s in sens]

	groupsList.append(list.copy(groups))

	while(len(mat) > 1):
		maxx = float("-inf")
		merge = (-1,-1)
		for x in range(len(mat)):
			for y in range(len(mat[x])):
				if x != y:
					dq = 2*(mat[x][y] - sum(mat[x])*sum(mat[y]))
					if (dq > maxx):
						maxx = dq
						merge = (x,y)

		diag = mat[merge[0]][merge[0]] + mat[merge[0]][merge[1]] + mat[merge[1]][merge[0]] + mat[merge[1]][merge[1]]
		mat[merge[0]] = [sum(x) for x in zip(mat[merge[0]],mat[merge[1]])]
		for row in mat:
			row[merge[0]] = row[merge[0]] + row[merge[1]]

		mat[merge[0]][merge[0]] = diag

		del mat[merge[1]]
		for row in mat:
			del row[merge[1]]

		groups[merge[0]] += groups[merge[1]]
		del groups[merge[1]]
		print(groups)
		groupsList.append(copy.deepcopy(groups))

		q += maxx
		Qs.append(q)

	print(Qs)
	print(max(Qs))
	print(groupsList[Qs.index(max(Qs))])

	nummerge = [x for x in range(len(Qs))]

	plt.plot(nummerge, Qs)
	plt.xlabel('Number of Merges')
	plt.ylabel('Q')
	plt.plot([-1, 106], [0, 0], "--", color="grey", zorder=1)
	plt.title('Q vs Merges')
	plt.xlim([-1,106])
	plt.show()

	# pos=nx.spring_layout(G)
	# nx.draw_networkx_nodes(G,pos,
	#                        nodelist=[1, 6, 17, 7, 5, 11, 12, 20],
	#                        node_color='r')
	# nx.draw_networkx_nodes(G,pos,
	#                        nodelist=[2, 18, 22, 3, 10, 4, 13, 8, 14],
	#                        node_color='g')
	# nx.draw_networkx_nodes(G,pos,
	#                        nodelist=[9, 31, 23, 33, 15, 16, 19, 24, 27, 30, 34, 28, 25, 26, 32, 29, 21],
	#                        node_color='b')
	# nx.draw_networkx_edges(G,pos,width=1.0,alpha=0.5)
	# nx.draw_networkx_labels(G,pos)
	# plt.show()

# G = createGraph("115edges.txt", "115names.txt", "cats.txt")
G = createGraph("115list.txt", "115names.txt", "cats_no_o.txt")



mod(G)
# print("\n")
# print(G.nodes())