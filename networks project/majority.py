# fp = open("decent.txt")

# ppl = []
# for line in fp:
# 	if line[0] != "-":
# 		line = line.strip()
# 		ppl.append(line)

# ppl = set(ppl)
# print(ppl)
# print(len(ppl))

# fp = open("115names.txt")

# suckers = []

# for line in fp:
# 	line = line.strip()
# 	suckers.append(line)

# suckers = set(suckers)

# suckers = list(suckers - ppl)

# for s in suckers:
# 	print(s)

groupslist = eval(open("comm_no_office.txt").read())

writefile = open("suckers_no_office.txt", "w")

fp = open("suckers.txt")

for line in fp:
	line = line.strip()
	if line in groupslist[0]:
		writefile.write(line)
		writefile.write("\t")
		writefile.write("1")
		writefile.write("\n")
	if line in groupslist[1]:
		writefile.write(line)
		writefile.write("\t")
		writefile.write("2")
		writefile.write("\n")
	if line in groupslist[2]:
		writefile.write(line)
		writefile.write("\t")
		writefile.write("3")
		writefile.write("\n")
	if line in groupslist[3]:
		writefile.write(line)
		writefile.write("\t")
		writefile.write("4")
		writefile.write("\n")
