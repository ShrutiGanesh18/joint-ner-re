# this program will update input data in the format of HMM training, in which 1st line is sentence, 2nd line is POS tagging and 3rd line is NER tagging.

f = open("eng.train", "r")
g = open("new_train.txt", "w")

row = f.readlines()
lis = []

for line in row:
	if line != '\n':
		info = line.split()	# split line into words.
		var = (info[0], info[1], info[3])	# making tuples for word, POS tag , NER tag
		lis.append(var)
	else :
		for x in lis:
			g.write(x[0])
			g.write("  ")
		g.write('\n')
		for x in lis:
			g.write(x[1])
			g.write("  ")
		g.write('\n')
		for x in lis:
			g.write(x[2])
			g.write("  ")
		g.write('\n')
		lis = []
for x in lis:
	g.write(x[0])
	g.write("  ")
g.write('\n')
for x in lis:
	g.write(x[1])
	g.write("  ")
g.write('\n')
for x in lis:
	g.write(x[2])
	g.write("  ")

