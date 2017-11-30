f = open("test_output", "r")
g = open("evaluate_test_output", "w")

for line in f:
	if line=="\n":
		g.write("\n")
	else:
		args=line.split()
		g.write(args[0]+" "+args[1]+" "+args[4]+" "+args[5]+"\n")


f.close()
g.close()

