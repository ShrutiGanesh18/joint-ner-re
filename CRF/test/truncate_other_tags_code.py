f = open("evaluate_test_output", "r")
g = open("evaluate_test_output_truncated_tags", "w")

other='O'
for line in f:
	if line=="\n":
		g.write("\n")
	elif line.strip():
		if line.split()[2]=="B-ORG" or line.split()[2]=="I-ORG" or line.split()[2]=="B-PER" or line.split()[2]=="I-PER":
			g.write(" ".join(line.split()[:])+"\n")
		else:
			g.write(" ".join(line.split()[:2])+" "+other+" ".join(line.split()[3])+"\n")


f.close()
g.close()

f = open("evaluate_test_output", "r")
g = open("evaluate_test_output_truncated_tags", "w")

other='O'
for line in f:
	if line=="\n":
		g.write("\n")
	elif line.strip():
		if line.split()[3]=="B-ORG" or line.split()[3]=="I-ORG" or line.split()[3]=="B-PER" or line.split()[3]=="I-PER":
			g.write(" ".join(line.split()[:])+"\n")
		else:
			g.write(" ".join(line.split()[:3])+" "+other+"\n")


f.close()
g.close()

