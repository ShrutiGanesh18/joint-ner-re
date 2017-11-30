#create sentences from the eng.testb data.
f = open("../dataset/eng.testb", "r")
g = open("train_data_sentences", "w")

for line in f:
	if line=="\n":
		g.write("\n")
	else:
		g.write(line.split()[0]+" ")

f.close()
g.close()
