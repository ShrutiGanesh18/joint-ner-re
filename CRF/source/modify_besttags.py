#Create a file of only entities and their tags recognized for a sentence grouped together inside SENTENCE - i for ith sentence in final_data.
#Do this for N1,N3,O1,O3

#O3
f = open("final_data_best3tags", "r")
g = open("final_data_best3tags_mod", "w")

index=0
sent_no=0
for line in f:
	if line=="\n":
		#g.write("\n")	
		index=0	
	elif line.split()[0]=="#":
		#g.write("\n")	
		if line.split()[1]=="0":
			#g.write("\n")	
			g.write("SENTENCE - "+str(sent_no)+"\n")
			sent_no+=1				
	else:
		if line.split()[4]=="I-PER":
			g.write(line.split()[0]+" "+str(index)+"\n")
		index=index+1
g.close()
f.close()

#O5
f = open("final_data_best5tags", "r")
g = open("final_data_best5tags_mod", "w")

index=0
sent_no=0
for line in f:
	if line=="\n":
		#g.write("\n")	
		index=0	
	elif line.split()[0]=="#":
		#g.write("\n")	
		if line.split()[1]=="0":
			#g.write("\n")	
			g.write("SENTENCE - "+str(sent_no)+"\n")
			sent_no+=1				
	else:
		if line.split()[4]=="I-ORG":
			g.write(line.split()[0]+" "+str(index)+"\n")
		index=index+1
g.close()
f.close()


#N1
f = open("final_data_best1nametags", "r")
g = open("final_data_best1nametags_mod", "w")

index=0
sent_no=0
for line in f:
	if line=="\n":
		#g.write("\n")	
		index=0	
	elif line.split()[0]=="#":
		#g.write("\n")	
		if line.split()[1]=="0":
			#g.write("\n")	
			g.write("SENTENCE - "+str(sent_no)+"\n")
			sent_no+=1				
	else:
		if line.split()[4]=="I-PER":
			g.write(line.split()[0]+" "+str(index)+"\n")
		index=index+1
g.close()
f.close()


#O1
f = open("final_data_best1orgtags", "r")
g = open("final_data_best1orgtags_mod", "w")

index=0
sent_no=0
for line in f:
	if line=="\n":
		#g.write("\n")	
		index=0	
	elif line.split()[0]=="#":
		#g.write("\n")	
		if line.split()[1]=="0":
			#g.write("\n")	
			g.write("SENTENCE - "+str(sent_no)+"\n")
			sent_no+=1				
	else:
		if line.split()[4]=="I-ORG":
			g.write(line.split()[0]+" "+str(index)+"\n")
		index=index+1
		
g.close()
f.close()
