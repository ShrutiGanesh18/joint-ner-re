# It will convert output of HMM that was is the form like per tag then its index but now it will like for each sentence, tagged entity with its index for sentence.

'''g = open("output_hmm.txt", "r")
f = open("eng.testb", "r")'''
g=open("b.txt","r")
f=open("a.txt","r")

fp = open("NER_HMM.txt", 'w')

row = f.readlines()
row_o = g.readlines()
len_line = 0
#name=""
#index=""
#names=[]
#indices=[]
flag = 1
var=""
# taking each sentence one by one and for each word of that sentence we will check is there any PER taging.
for line in row:
	if line != '\n':
			info1 = line.split()	# split the sentence to words.
			print info1[0]
			#for x, k in enumerate(info1):
			#ind = x + len_line	# ind will store of word at corpus level.
			for line2 in row_o:	# for each line of HMM output's.
				info2 = line2.split()
				print info2
				#if info2[0] == "PER":
				for y, l in enumerate(info2):
					a = info2[y].split("-")	# split interval and match with first interval to index of selected word.
					if( a[0] == str(len_line)):
						flag = 0
						if info1[3] == "O":	
							var = info1[0] +" " + info1[1] + " " + info1[3] + " " + info2[0]
						else:
							e = info1[3].split("-")
							#print e
							var = info1[0] +" " + info1[1] + " " + e[1] + " " + info2[0]	
			if flag == 1:
				if info1[3] != "O":	
					var = info1[0] +" " + info1[1] + " " + e[1] + " " + "O"
				else:
					e = info1[3].split("-")
					var = info1[0] +" " + info1[1] + " " + str(e) + " " + "O"
				
				#elif (info2[0] == "ORG"):
				'''for y, l in enumerate(info2):
					a = info2[y].split("-")	# split interval and match with first interval to index of selected word.
					if( a[0] == str(len_line)):
		
						if info1[3] != "O":	
							var = info1[0] +" " + info1[1] + " " + e[1] + " " + "ORG"
						else:
							var = info1[0] +" " + info1[1] + " " + e + " " + "ORG" 
				break
				#elif info2[0] == "MISC":
				for y, l in enumerate(info2):
					a = info2[y].split("-")	# split interval and match with first interval to index of selected word.
					if( a[0] == str(len_line)):
		
						if info1[3] != "O":	
							var = info1[0] +" " + info1[1] + " " + e[1] + " " + "MISC"
						else:
							var = info1[0] +" " + info1[1] + " " + e + " " + "MISC" 
				break
				#elif info2[0] == "LOC":
				for y, l in enumerate(info2):
					a = info2[y].split("-")	# split interval and match with first interval to index of selected word.
					if( a[0] == str(len_line)):
		
						if info1[3] != "O":	
							var = info1[0] +" " + info1[1] + " " + e[1] + " " + "LOC"
						else:
							var = info1[0] +" " + info1[1] + " " + e + " " + "LOC" 
				break
						
				#else:
					if info1[3] != "O":	
						var = info1[0] +" " + info1[1] + " " + e[1] + " " + "O"
					else:
						var = info1[0] +" " + info1[1] + " " + e + " " + "O" '''
			len_line = len_line + 1
	else:
		fp.write(var)
		fp.write('\n')
		var = ""	
	
	# it will make list of tuples for each sentence.
	'''zipped=zip(names,indices)
	zipped=list(set(zipped))
	print zipped
	names = []
	indices = []'''
f.close()
g.close()
fp.close()
