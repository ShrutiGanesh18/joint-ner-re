#trim down the final_data removing last column
f = open("final_data1", "r")
g = open("final_data", "w")

for line in f:
	if line=="\n":
		g.write("\n")
	else:
		g.write(" ".join(line.split()[:4])+"\n")

g.close()
f.close()
