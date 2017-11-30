# this program will update test file in the format of HMM test format, which contain sentence then in next line POS tag then indexing for words in next line and also will make a file for all sentence in line order..

f = open("eng.testb", "r")
g = open("new_test.txt", "w")
fp = open("sentence.txt", "w")

row = f.readlines()
lis = []
i = 0

for line in row:
	if line != '\n':
		info = line.split()	# split line into words
		var = (info[0], info[1], i)	# making tuple for word, POS, index of word.
		lis.append(var)
		i = i + 1
	else :
		for x in lis:
			g.write(x[0])
			g.write("  ")
			fp.write(x[0])
			fp.write(" ")
		g.write('\n')
		fp.write('\n')
		for x in lis:
			g.write(x[1])
			g.write(" ")
		g.write('\n')
		for x in lis:
			g.write(str(x[2]))
			g.write(" ")
		g.write('\n')
		lis = []
		i = 0
for x in lis:
	g.write(x[0])
	g.write(" ")
	fp.write(x[0])
	fp.write(" ")
g.write('\n')
fp.write('\n')
for x in lis:
	g.write(x[1])
	g.write(" ")
g.write('\n')
for x in lis:
	g.write(str(x[2]))
	g.write(" ")
f.close()
g.close()
fp.close()

