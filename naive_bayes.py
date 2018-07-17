#Naive Bayes:
#Naive bayes user this should work 
#might have some minor mistakes, will fix them later

def pdf(x,mean,variance):
	 import math 
	 return (1/(math.sqrt(variance)*(2*math.pi)**0.5))*math.exp(-((x-mean)**2)/2*variance)


def naive_bayes_model(training_set):
	#Analysis training set
	import numpy as np

	np.transpose(training_set)
	success_data=[]
	failure_data=[]
	
	for record in training_set:
		#for each class 1
		temp = []

		if record[0][0] == 'S':

			for i in range(1,len(record)):
				temp.append(record[i])
			success_data.append(temp)
		#for each class 2

		else:

			for i in range(1, len(record)):
				temp.append(record[i])

			failure_data.append(temp)

		np.transpose(success_data)
		np.transpose(failure_data)

	return success_data,failure_data

# classify a record
def naive_bayes_test(sample,success_data,failure_data):
	import numpy as np
	#e.g sample = ["N",6,130,8]
	possibility_success = len(success_data) / (len(success_data)+len(failure_data))
	possibility_failure = 1-possibility_success
	posterior_success = 1*possibility_success
	posterior_failure = 1*possibility_failure
	
	#bayesian rule:
	for i in range(len(success_data[0])):
			meansuccess = np.mean(success_data[i])
			varsuccess = np.var(success_data[i])
			if varsuccess==0:
				varsuccess =1

			posterior_success = posterior_success*(pdf(sample[1],meansuccess,varsuccess))
			
	for i in range(len(failure_data[0])):
			meanfailure = np.mean(failure_data[i])
			varfailure = np.var(failure_data[i])
			if varfailure== 0:
				varfailure = 1

			posterior_failure = posterior_failure*(pdf(sample[1],meanfailure,varfailure))
			
	#check which one has a larger possibility
	
	if (posterior_success > posterior_failure):
			sample[0] = 'success'
	elif (posterior_success < posterior_failure):
			sample[0] = 'failure'
	else:
			sample[0] = 'none'
	return sample[0]

def naive_bayes(training_data):
	true_set = []
	false_set = []
	success_data,failure_data = naive_bayes_model(training_data)
	for i in range(len(training_data)):
		result = naive_bayes_test(training_data[i], success_data, failure_data)
		if result == 'success': true_set.append(training_data[i])
		elif result == 'failure': false_set.append(training_data[i])
	return true_set, false_set
	
	
	

'''
sample = ["N",6,130,8]
nbmodel = naive_bayes(traindata)
success,failure = nbmodel.naive_bayes_model()
print(nbmodel.naive_bayes_test(sample,success,failure))
'''
