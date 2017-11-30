
def check_for_relations():
	relations = ['director','spokesperson','founder','head','manager','lawyer','advisor','analyst','professor','leave','staff','others']
	d = dict()
    	l_d = dict()
    	num = 0
    	with open('NYT_labels.txt','r') as f:
        	for line in f:
        	    line = line.rstrip()
        	    toks = line.split('[')
        	    if toks[0] != '':
        	        l = toks[0].split(':')
        	        if l[0] == 'line ':
        	            num = int(l[1])
        	        if l[0] != 'line ' and l[0] != 'count':
        	            d[toks[0].lower()] = d.get(toks[0].lower(),0)+1
        	            l_d[num] = toks[0].lower()

    	with open('rel_labels.txt','w') as k:
        	for key in l_d:
        	    k.write(str(key) + "\t" + str(l_d[key])+'\n')


def extract_sentences(files):

    	for f in files:
        	label = f.split('.')[0]
        	count = 0
        	k = 0
        	op = open(label+'_sentences.txt','w')
        	sentence = ''
        	flag = 0
        	with open("datasets/"+f,'r') as reader:
        	    for line in reader:
        	        line = line.rstrip()
        	        toks = line.split('\t')
        	        if toks[0] != '':
        	            if toks[0] == label+'-'+str(count):
        	                k = k + 1
        	                op.write("\n\n\nline : "+str(count-1)+'\n')
        	                op.write(str(sentence)+"\n")
        	                flag = int(toks[1])
        	                count = count + 1
        	                sentence = ''
        	            else:
        	                sentence = sentence + ' ' +str(toks[1])
        	op.write('\n\n\ncount is :'+str(k))
        	op.close()
def extract_relations_from(files):

    	for f in files:
    	    label = f.split('.')[0]
    	    count = 0
    	    k = 0
    	    op = open(label+'_preprocessed.txt','w')
    	    sentence = []
    	    relation = []
    	    flag = 0
    	    with open("datasets/"+f,'r') as reader:
    	        for line in reader:
    	            line = line.rstrip()
    	            toks = line.split('\t')
    	            if toks[0] != '':
    	                if toks[0] == label+'-'+str(count):
    	                    if flag == 1:
    	                        k = k + 1
    	                        op.write("\n\n\nline : "+str(count-1))
    	                        #op.write(str(sentence)+"\n")
    	                        op.write(str(relation)+"\n")
    	                    flag = int(toks[1])
    	                    count = count + 1
    	                    sentence = []
    	                    relation = []
    	                else:
    	                    sentence.append(toks[1])

    	                    if toks[-1] != 'O':
    	                        relation.append(toks[1]+" : " + toks[-1])
    	    op.write('\n\n\ncount is :'+str(k))
    	    op.close()

if __name__=="__main__":
  	files = ['NYT.txt']

    	extract_relations_from(files)
    	#check_for_relations()
    	#extract_sentences(files)

    
