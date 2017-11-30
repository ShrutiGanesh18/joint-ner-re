from maxent import MaxentModel

for i in range(5):
	m = MaxentModel()
	context = []
	m.begin_add_event()
	with open('contexts/contexts'+str(i+1)+'.txt','r') as f:
		for line in f:
			line = line.rstrip()
			try:
				ind = line.index(':')
				if line[:ind] != '':
					rel = line[:ind]
					l = eval(line[ind+1:])
					m.add_event(l,rel,1)
			except:
				pass
	m.end_add_event()

	m.train(100,'lbfgs')
	s_name = "models/lbfgs/model"+str(i+1)
	m.save(s_name)

