#read the final_data_best3tags_mod an final_data_best5tags_mod files into a list, one by one, where each line is an element of this list 
#create best-n sets where each line in output file gives the corresponding named entities for each sentence in final_data
import sys
lines = [line.rstrip('\n') for line in open(sys.argv[1],"r")]

names=[]
indices=[]
name=""
index=""
ind=""
i=0
while(i<len(lines)):
	if(lines[i].split()[1]!="-"):
		if(i+1<len(lines) and lines[i+1].split()[1]!="-" and int(lines[i].split()[1])+1==int(lines[i+1].split()[1])):
			name=name+lines[i].split()[0]+" "
			index=index+lines[i].split()[1]+" "
		else:
			name=name+lines[i].split()[0]
			index=index+lines[i].split()[1]
			if(len(index.split())>2):
				start=index.split()[0]
				end=index.split()[-1]
				ind=start+" "+end
				indices.append(ind)
			else:
				indices.append(index)	
			index=""
			ind=""
			names.append(name)
			name=""
	else:
		#if(len(names)!=0):
		zipped=zip(names,indices)
		zipped=list(set(zipped))
		print zipped
		names[:]=[]
		indices[:]=[]
	i=i+1

zipped=zip(names,indices)
zipped=list(set(zipped))
print zipped




