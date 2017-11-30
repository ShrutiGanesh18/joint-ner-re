
def add_surrounding_arg2_tags(context,sentence,pos_tags,arg1,isgreaterthan):
	if isgreaterthan:
       		i = arg1+1
        	j = arg1+2
    	else:
        	i = arg1-1
        	j = arg1-2

    	if i < 0 or i >= len(sentence):
        	context.append('SM2F=BOUNDARY')
    	else:
        	context.append('SM2F='+sentence[i])

    	if j < 0 or j >= len(sentence):
        	context.append('SM2L=BOUNDARY')
    	else:
    	    context.append('SM2L='+sentence[j])

def add_surrounding_arg1_tags(context,sentence,pos_tags,arg1,islessthan):
    	if islessthan:
        	i = arg1-1
        	j = arg1-2
    	else:
        	i = arg1+1
        	j = arg1+2

    	if i < 0 or i >= len(sentence):
        	context.append('SM1F=BOUNDARY')
    	else:
        	context.append('SM1F='+sentence[i])

    	if j < 0 or j >= len(sentence):
        	context.append('SM1L=BOUNDARY')
    	else:
        	context.append('SM1L='+sentence[j])

def make_context_for(sentence,pos_tags,rel):
    	arg1 = sentence.index('arg1')
    	arg2 = sentence.index('arg2')

    	context = []

    	if arg1 < arg2 :
		i = arg1+1
		j = arg2-1
    	else:
        	i = arg2+1
        	j = arg1-1

    	if j == i-1 :
        	context.append('WBNULL')
    	else:
        	if j == i:
            		context.append('WBFL='+str(sentence[i]))
        	else:
            		k = i
            		for e1, e2 in zip(sentence,pos_tags)[i:j+1]:
                		if k == i:
                    			context.append('WBF='+str(e1))
                		else:
                    			if k == j:
                        			context.append('WBL='+str(e1))
                    			else:
                        			context.append('WBO='+str(e1))
                		k = k + 1

    	add_surrounding_arg1_tags(context,sentence,pos_tags,arg1,arg1<arg2)
    	add_surrounding_arg2_tags(context,sentence,pos_tags,arg2,arg1<arg2)
    	return context

def create_relations():
    	rel = dict()
    	with open('rel_labels.txt','r') as f:
        	for line in f:
			line = line.rstrip()
			toks = line.split('\t')

		if len(toks) == 2:
	                rel[int(toks[0])] = toks[1]
	return rel

def make_contexts(rel):
	with open('datasets/NYT.txt','r') as f:
		op = open('contexts3.txt','w')
        	sentence = []
        	pos_tags = []
        	flag = 0
        	count = 0
        	for line in f:
			line = line.rstrip()
            		toks = line.split('\t')

            		if toks[0] == '':
                		if flag == 0:
                    			t = 'others'
                		else:
                    			t = rel[count]
                	context = make_context_for(sentence,pos_tags,t)
                	op.write(t+':'+str(context)+'\n\n')
                	sentence = []
                	pos_tags = []
                	count = count + 1

            	else:
                	if toks[0] == 'NYT-'+str(count):
                    		flag = int(toks[1])
                	else:
                    		sentence.append(toks[1])
                    		pos_tags.append(toks[3])


if __name__=='__main__':
	relations = create_relations()
	make_contexts(relations)
