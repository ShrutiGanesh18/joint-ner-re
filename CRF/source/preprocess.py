import string
#trim down the input files for training removing all other tags than PER and ORG from the final column
f = open("../dataset/eng.train", "r")
g = open("eng.train1", "w")

for line in f:
	if line=="\n":
		g.write("\n")
	elif line.strip():
		if any(char.isdigit() or char in string.punctuation for char in line.split()[0]):	#checks if token contains a digit
			g.write(" ".join(line.split()[:3])+" 1 "+line.split()[3]+"\n")
		else:
			g.write(" ".join(line.split()[:3])+" 0 "+line.split()[3]+"\n")

g.close()
f.close()


#trim down the input files for testing removing all other tags than PER and ORG from the final column
f = open("../dataset/eng.testa", "r")
g = open("eng.test1", "w")

for line in f:
	if line=="\n":
		g.write("\n")
	elif line.strip():
		if any(char.isdigit() or char in string.punctuation for char in line.split()[0]):	#checks if token contains a digit
			g.write(" ".join(line.split()[:3])+" 1 "+line.split()[3]+"\n")
		else:
			g.write(" ".join(line.split()[:3])+" 0 "+line.split()[3]+"\n")

g.close()
f.close()

#trim down the input files for final data removing all other tags than PER and ORG from the final column
f = open("../dataset/eng.testb", "r")
g = open("final_data1", "w")

for line in f:
	if line=="\n":
		g.write("\n")
	elif line.strip():
		if any(char.isdigit() or char in string.punctuation for char in line.split()[0]):	#checks if token contains a digit
			g.write(" ".join(line.split()[:3])+" 1 "+line.split()[3]+"\n")
		else:
			g.write(" ".join(line.split()[:3])+" 0 "+line.split()[3]+"\n")

g.close()
f.close()
