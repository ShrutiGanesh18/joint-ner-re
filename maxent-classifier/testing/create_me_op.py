
def tag_sent(sent,n,key):
	args = n[1].split(' ')

	i = int(args[0])

	if len(args) > 1:
		j = int(args[1])
	else:
		j = i

	for s in sent[i:j+1]:
		s[3] = key
	

def process(sent,r,op):
	#op.write(str(sent)+'\t'+str(r)+'\n')

	names = eval(r)[0]
	orgs = eval(r)[1]

	for n in names:
		tag_sent(sent,n,'I-PER')

	for o in orgs:
		tag_sent(sent,o,'I-ORG')

	for s in sent:
		k = s[2].split('-')

		if len(k) > 1:
			if k[1] == 'LOC' or k[1] == 'MISC':
				s[2] = 'O'

		if s[3] == '':
			s[3] = 'O'

		for l in s:
			op.write(l+' ')
		op.write('\n')
	op.write('\n')		


if __name__=='__main__':
	sent = []
	with open('tagged_datasets/eng.testb','r') as f:
		op = open('op.txt','w')
		with open("entities.txt","r") as f1:
    			r = f1.readlines()
		count = 0
		for line in f:
			if line == '\n':
				process(sent,r[count],op)
				count = count + 1
				sent = []
			else:
				line = line.rstrip()
				args = line.split(' ')
				sent.append([args[0],args[1],args[3],''])
