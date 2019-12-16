fp = open("decent.txt")

names = {}

for line in fp:
	line = line.strip()
	if line[0] != "-":
		if line in names:
			names[line] = names[line]+1
		else:
			names[line] = 1
lnames = [(k,v) for k,v in names.items()]
lnames.sort(key = lambda x: x[1])
lnames.reverse()

print (lnames)