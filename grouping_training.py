import random

def import_spam():
	spams = []
	for i in range(1, 20000):
		file_name = 'Spam/' + str(i) + '.txt'
		try:
			with open(file_name, 'r'):
#				print('open spam')
				spams.append([file_name, 0])
		except:
			break
	
	return spams
	

def import_norm():
	norms = []
	for i in range(1, 20000):
		file_name = 'Normalset/' + str(i) + '.txt'
		try:
			with open(file_name, 'r'):
				norms.append([file_name, 0])
		except:
			break
	return norms

def group(spams, norms):
	grouped = []
#	group_length = int((len(spams)+len(norms))/5) + ((len(spams)+len(norms))%5)
	group_1 = []
	group_2 = []
	group_3 = []
	group_4 = []
	group_5 = []
	
	for i in range(len(spams)):
		spams[i][1] = random.randint(1, 6)
		if spams[i][1] == 1: group_1.append(spams[i])
		elif spams[i][1] == 2: group_2.append(spams[i])
		elif spams[i][1] == 3: group_3.append(spams[i])
		elif spams[i][1] == 4: group_4.append(spams[i])
		elif spams[i][1] == 5: group_5.append(spams[i])
	
	for j in range(len(norms)):
		norms[j][1] = random.randint(1, 6)
		if norms[j][1] == 1: group_1.append(norms[j])
		elif norms[j][1] == 2: group_2.append(norms[j])
		elif norms[j][1] == 3: group_3.append(norms[j])
		elif norms[j][1] == 4: group_4.append(norms[j])
		elif norms[j][1] == 5: group_5.append(norms[j])


	grouping = [group_1, group_2, group_3, group_4, group_5]
	
	for i in range(5):
		random.shuffle(grouping[i])
	
	return grouping
	
def get_impruties(grouping, spams, norms):
	impurities = []
	for i in range(5):
		spam_count = 0
		norm_count = 0
		impurity = 1
		for fl in grouping[i]:
			if fl in spams:
				spam_count += 1
			elif fl in norms:
				norm_count += 1
		prob = spam_count/float(len(grouping[i]))
		impurity -= prob**2
		
		impurities.append(impurity)
		
	return impurities
		

#spams = import_spam()
#norms = import_norm()
#grouping = group(spams, norms)
#impurities = get_impruties(grouping, spams, norms)

	

#for i in range(5):
#	print('##################################')
#	print(grouping[i])
#	print(impurities[i])





