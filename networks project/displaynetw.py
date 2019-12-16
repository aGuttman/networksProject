import networkx as nx
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

def showGraph(G, file):
	groupList = eval(open(file, "r").read())
	pos=nx.spring_layout(G)
	nx.draw_networkx_nodes(G,pos,
	                       nodelist=groupList[0],
	                       node_color='r',
	                       node_size=10)
	nx.draw_networkx_nodes(G,pos,
	                       nodelist=groupList[1],
	                       node_color='g',
	                       node_size=10)
	nx.draw_networkx_nodes(G,pos,
	                       nodelist=groupList[2],
	                       node_color='b',
	                       node_size=10)
	nx.draw_networkx_nodes(G,pos,
	                       nodelist=groupList[3],
	                       node_color='y',
	                       node_size=10)
	nx.draw_networkx_edges(G,pos,width=1.0,alpha=0.5)
	# nx.draw_networkx_labels(G,pos)
	plt.show()

G = createGraph("115list.txt", "115names.txt", "cats_no_o.txt")
showGraph(G, "comm_no_office.txt")

G = createGraph("115edges.txt", "115names.txt", "cats.txt")
showGraph(G, "comm_w_office.txt")