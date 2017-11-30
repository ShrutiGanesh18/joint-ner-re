from maxent import MaxentModel

def get_index(x):
	args = x[1].split(' ')
	
	i = int(args[0])

	if len(args) > 1:
		j = int(args[1])
	else:
		j = i
	return i , j

def resolve(l,e):
	i_2 , j_2 = get_index(e)

	for elem in l:
		i_1 , j_1 = get_index(elem)

		if (i_1 <= j_2 and i_2 <= i_1) or (j_1 <= j_2 and i_2 <= j_1):
			l.remove(elem)

	l.append(e)
		

def resolve_conflicts(n1,o1,final):
	name = final[0]
	org = final[1]

	if final[3] > 0.8 :
		resolve(o1,org)
	if final[3] > 0.9:
		resolve(o1,org)

def append_surround_arg2(context,i,j,sent,isgreatthan):
	if not isgreatthan:
		i = i-1
		j = i-1
	else:
		i = j+1
		j = i+1

	if i < 0 or i >= len(sent):
		context.append('SM2F=BOUNDARY')
	else:
		context.append('SM2F='+str(sent[i]))

	if j < 0 or j >= len(sent):
		context.append('SM2L=BOUNDARY')
	else:
		context.append('SM2L='+str(sent[i]))

def append_surround_arg1(context,i,j,sent,islessthan):
	if islessthan:
		i = i-1
		j = i-1
	else:
		i = j+1
		j = i+1

	if i < 0 or i >= len(sent):
		context.append('SM1F=BOUNDARY')
	else:
		context.append('SM1F='+str(sent[i]))

	if j < 0 or j >= len(sent):
		context.append('SM1L=BOUNDARY')
	else:
		context.append('SM1L='+str(sent[i]))
		

def get_context(name,org,sent):
	context = []
	args = name[1].split(' ')
	i_arg1 = int(args[0])

	if len(args) == 1:
		j_arg1 = int(args[0])
	else:
		j_arg1 = int(args[1])

	args = org[1].split(' ')
	i_arg2 = int(args[0])

	if len(args) == 1:
		j_arg2 = int(args[0])
	else:
		j_arg2 = int(args[1])

	if i_arg1 == i_arg2 and j_arg1 == j_arg2:
		#print 'arg1 and arg2 are same'
		return

	if (i_arg1 <= j_arg2 and i_arg2 <= i_arg1) or (j_arg1 <= j_arg2 and i_arg2 <= j_arg1):
		#print 'overlapping'
		return

	if j_arg1 < j_arg2:
		i = j_arg1+1
		j = i_arg2-1
	else:
		i = j_arg2+1
		j = i_arg1-1

	if i > j:
		context.append('WBNULL')
	else:
		if i == j :
			context.append('WBFL='+str(sent[i]))

		else:
			k = i
			for word in sent[i:j+1]:
				if k == i:
					context.append('WBF='+str(sent[k]))

				else :
					if k == j:
						context.append('WBL='+str(sent[k]))
					else:
						context.append('WBO='+str(sent[k]))

				k = k + 1

	append_surround_arg1(context,i_arg1,j_arg1,sent,i_arg1<i_arg2)
	append_surround_arg2(context,i_arg2,j_arg2,sent,i_arg1<i_arg2)

	return context

				
				

	

def predict_tags(best_1_name,best_1_org,best_3_name,best_5_org,sentences,f,op):
	rel = ['others','director','analyst','advisor','head','manager','spokesperson','founder','professor','leave','lawyer']
	me = MaxentModel()
	me.load('../training/models/lbfgs/model3')
	count = 0
	for n1, o1, n3, o5, sent in zip(best_1_name,best_1_org,best_3_name,best_5_org, sentences):
		if len(n3) == 0 or len(o5) == 0:
			op.write(str((n1,o1))+'\n')
		else:
			j = ('','','',0.0)
			d = {}
			for name in n3:
				for org in o5:
					context = get_context(name,org,sent)
					
					relation = ''
					prob = 0.0
					if context != None:
						
						
						for r in rel:
							y = me.eval(context,r)
							if y > prob:
								prob = y
								relation = r
						#set_r.append((name,org,relation,prob))
						d[(name,org)] = relation
						if prob > j[3] and relation != 'others':
							j = (name,org,relation,prob)

					else:

						d[(name,org)] = 'others'
			#print str(count)+' before : '+str(n1)+'\t'+str(o1)
			resolve_conflicts(n1,o1,j)
			#print str(count)+' after : '+str(n1)+'\t'+str(o1)
			#x = raw_input()
			op.write(str((n1,o1))+'\n')		
			f.write(str(j)+'\n')
		count = count + 1


def get_lists():
	best_1_name = []
	with open('tagged_datasets/best1nametagsset','r') as f:
		for line in f:
			line = line.rstrip()
			best_1_name.append(eval(line))

	best_1_org = []
	with open('tagged_datasets/best1orgtagsset','r') as f:
		for line in f:
			line = line.rstrip()
			best_1_org.append(eval(line))

	best_3_name = []
	with open('tagged_datasets/best3nametagsset','r') as f:
		for line in f:
			line = line.rstrip()
			best_3_name.append(eval(line))

	best_5_org = []
	with open('tagged_datasets/best5orgtagsset','r') as f:
		for line in f:
			line = line.rstrip()
			best_5_org.append(eval(line))

	sentences = []
	with open('tagged_datasets/train_data_sentences','r') as f:
		for line in f:
			line = line.rstrip()
			sentences.append(line.split(' '))

	return best_1_name, best_1_org, best_3_name, best_5_org, sentences


if __name__=='__main__':
	
	best_1_name, best_1_org, best_3_name, best_5_org, sentences = get_lists()

	
	if len(best_1_name) == len(best_3_name) == len(best_1_org) == len(best_5_org) == len(sentences):
		f = open('rel_set.txt','w')
		op = open('entities.txt','w')
		predict_tags(best_1_name,best_1_org,best_3_name,best_5_org,sentences,f,op)
		f.close()
		op.close()
	else:
		print 'no'

