fp = open("115party.txt", "r")

namedict = {}

for line in fp:
	l = line.strip().split('\t')
	namedict[l[0]] = l[1]

groupList = eval(open("comm_no_office.txt").read())

for group in groupList:
	r = 0
	d = 0
	i = 0
	for g in group:
		if namedict[g] == "r":
			r+=1
		else:
			if namedict[g] == "d":
				d+=1
			else:
				i+=1
	print()
	print(r)
	print(d)
	print(i)
	print()

# fp = open("115list.txt", "r")

# namedict = {}

# for line in fp:
# 	l = line.strip().split('\t')
# 	jobs = []
# 	for i in l:
# 		if i != l[0]:
# 			jobs.append(i)
# 	jobs.sort()
# 	namedict[l[0]] = jobs

# groupList = eval(open("comm_no_office.txt").read())

# for group in groupList:
# 	for g in group:
# 		print(namedict[g])
# 	print()

# groupList = eval(open("comm_no_office.txt").read())

# for group in groupList:
# 	for g in group:
# 		print(g)
# 	print()
