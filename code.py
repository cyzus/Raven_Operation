transpose
def transpose(self,m):
	 Matrix = [[0 for x in range(len(m))] for y in range(len(m[0]))]
	 for row in range(len(m)):
			 for col in range(len(m[0])):
					 Matrix[col][row] = m[row][col]
	 return Matrix
#CSV input：
#read a csv document with first row showing the class. Record the rest of the row into an 2D list recorded by record.
def csv_to_list(filename):
		import csv
		with open(filename,'r') as dataset:
				csvread = csv.reader(dataset)
				csvlist = list(csvread)
				for rowindex in range(1,len(csvlist)):
						for columnindex in range(len(csvlist[0])):
								if columnindex == 0:
										pass
								else:
										csvlist[rowindex][columnindex] = float(csvlist[rowindex][columnindex])
				csvlist.pop(0)
		return csvlist
#Normal distribution：
# for copy only
def pdf(x,mean,variance):
			 import math  
			 return (1/(math.sqrt(variance)*(2*math.pi)**0.5))*math.exp(-((x-mean)**2)/2*variance)
#Naive Bayes:
#Naive bayes user this should work 
#might have some minor mistakes, will fix them later
class naive_bayes():
		def __init__(self,training_set):
				
				self.training_set = training_set    
		def pdf(self,x,mean,variance):
					 import math 
					 return (1/(math.sqrt(variance)*(2*math.pi)**0.5))*math.exp(-((x-mean)**2)/2*variance)
		def naive_bayes_model(self):
				#Analysis training set
				import numpy as np
				training_set = self.training_set
				np.transpose(training_set)
				success_data=[]
				failure_data=[]
				
				for record in self.training_set:
					 #for each class 1
					 if record[0] == 'success':
							 temp = []
							 for i in range(1,len(record)):
									 temp.append(record[i])
							 success_data.append(temp)
					 #for each class 2
					 elif record[0] == 'failure':
							 temp = []
							 for i in range(1, len(record)):
									 temp.append(record[i])
							 failure_data.append(temp)
					 else:
							 continue
					 np.transpose(success_data)
					 np.transpose(failure_data)
				return success_data,failure_data
		def naive_bayes_test(self,sample,success_data,failure_data):
				import numpy as np
				#e.g sample = ["N",6,130,8]
				possibility_success = len(success_data) / (len(success_data)+len(failure_data))
				possibility_failure = 1-possibility_success
				posterior_success = 1*possibility_success
				posterior_failure = 1*possibility_failure
				
				#bayesian rule:
				for i in range(len(success_data[0])):
						
						
						posterior_success = posterior_success*(self.pdf(sample[1],np.mean(success_data[i]),np.var(success_data[i])))
						
				for i in range(len(failure_data[0])):
						posterior_failure = posterior_failure*(self.pdf(sample[1],np.mean(failure_data[i]),np.var(failure_data[i])))
						
				#check which one has a larger possibility
				
				if (posterior_success > posterior_failure):
						sample[0] = 'success'
				elif (posterior_success < posterior_failure):
						sample[0] = 'failure'
				else:
						sample[0] = 'none'
				return sample[0]
'''
sample = ["N",6,130,8]
nbmodel = naive_bayes(traindata)
success,failure = nbmodel.naive_bayes_model()
print(nbmodel.naive_bayes_test(sample,success,failure))
'''
#K-nn：
#K-NN application on classifying gender given height,weight, and foot size.
#K is the arbitrary number
class Knn():
	 def __init__(self,training_set):
			 self.training_set = training_set
	 def transpose(self, m):
			 Matrix = [[0 for x in range(len(m))] for y in range(len(m[0]))]
			 for row in range(len(m)):
					 for col in range(len(m[0])):
							 Matrix[col][row] = m[row][col]
			 return Matrix
	 #Guassian application for classifiying continuous numbers
	 def pdf(self,x,mean,variance):
			import math
			return (1/(math.sqrt(variance)*(2*math.pi)**0.5))*math.exp(-((x-mean)**2)/2*variance)
	 #positive or negative
	 def Ztime(self,x,mean,variance):
			 import math
			 return ((x-mean)/math.sqrt(variance))
	 def secondnorm(self,point1,point2):
			 import math
			 temp = 0
			 for i in range(1,len(point1)):
					 temp += (point1[i]-point2[i])**2
			 return math.sqrt(temp)
	 def knn_buildgrid(self):
			 import numpy as np
			 '''success_data=[]
			 failure_data=[]
			 for record in self.training_set:
					 if record[0] == 'M':
							temp = []
							for i in range(1,len(record)):
									temp.append(record[i])
							success_data.append(temp)
					 else:
							temp = []
							for i in range(1, len(record)):
									temp.append(record[i])
							failure_data.append(temp)
				'''
			 self.training_set=self.transpose(self.training_set)
			 #normalize grid
			 for i in range(1,len(self.training_set)):
					 mean=np.mean(self.training_set[i])
					 variance=np.var(self.training_set[i])
					 for t in range(len(self.training_set[i])):
							 self.training_set[i][t] = self.Ztime(self.training_set[i][t],mean,variance)
					 sample[i] = self.Ztime(sample[i],mean,variance)
			 self.training_set = self.transpose(self.training_set)
	 def knn_checkk(self,sample,k):
			 distanceSet=[]
			 for index in range(len(self.training_set)):
					 temp = []
					 temp.append(self.training_set[index][0])
					 temp.append(self.secondnorm(training_set[index],sample))
					 distanceSet.append(temp)
			 distanceSet=sorted(distanceSet,key=lambda x:x[len(distanceSet[0])-1])
			 Mnum=0
			 for i in range(k):
					 if distanceSet[i][0]=='M':
							 Mnum+=1
			 if Mnum<(k-Mnum):
					 return 'failure'
			 elif Mnum>(k-Mnum):
					 return 'success'
			 else:
					 return 'No solution'
'''
k = 3
training_set = [
	 #   sex;height;weight;footsize
			['M',6,180,12],
			['M',5.92,190,11],
			['M',5.58,170,12],
			['M',5.92,165,10],
			['F',5,100,6],
			['F',5.5,150,8],
			['F',5.42,130,7],
			['F',5.75,150,9]
	 ]
sample = ["N",6,130,8]
model = Knn(training_set=training_set)
model.knn_buildgrid()
print(model.knn_checkk(sample=sample,k=k))
'''
