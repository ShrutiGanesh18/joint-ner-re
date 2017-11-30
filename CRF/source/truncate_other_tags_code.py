f = open("evaluate_test_output", "r")
g = open("evaluate_test_output_truncated_tags_from4", "w")

other='O'
for line in f:
	if line=="\n":
		g.write("\n")
	elif line.strip():
		args=line.split()
		if args[2]=="B-ORG" or args[2]=="I-ORG" or args[2]=="B-PER" or args[2]=="I-PER":
			g.write(" ".join(line.split()[:])+"\n")
		else:
			g.write(args[0]+" "+args[1]+" "+other+" "+args[3]+"\n")

f.close()
g.close()

f = open("evaluate_test_output_truncated_tags_from4", "r")
g = open("evaluate_test_output_truncated_tags", "w")

other='O'
for line in f:
	if line=="\n":
		g.write("\n")
	elif line.strip():
		args=line.split()
		if line.split()[3]=="B-ORG" or line.split()[3]=="I-ORG" or line.split()[3]=="B-PER" or line.split()[3]=="I-PER":
			g.write(" ".join(line.split()[:])+"\n")
		else:
			g.write(" ".join(line.split()[:3])+" "+other+"\n")


f.close()
g.close()

