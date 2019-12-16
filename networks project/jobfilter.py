fp = open("cats.txt", "r")
joblist = []
for line in fp:
	l = line.strip().split('\t')
	for i in l:
		joblist.append(i)
jobset = set(joblist)
joblist = list(jobset)
joblist.sort()
for job in joblist:
	print(job)

# fp = open("jobcat.txt","r")
# jobdict = {}

# for line in fp:
# 	l = line.strip().split('\t')
# 	jobdict[l[0]] = l[1]

# print(jobdict)

# fp = open("115jobs.txt")


# outfile = open("115jobscat.txt","w") 

# for line in fp:
# 	l = line.strip().split('\t')
# 	for i in l:
# 		outfile.write(jobdict[i])
# 		outfile.write("\t")
# 	outfile.write("\n")

# outfile = open("115list2.txt","w")
# with open("115list.txt") as textfile1, open("115office.txt") as textfile2: 
#     for x, y in zip(textfile1, textfile2):
#         x = x.strip()
#         y = y.strip()
#         if y == "yes":
#         	y = "office"
#         else:
#         	y = ""
#         outfile.write("{0}\t{1}".format(x, y))
#         outfile.write("\n")