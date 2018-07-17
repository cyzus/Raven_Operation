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
