training_data = [
	['Green', 3, 'Apple'],
	['Yellow', 3, 'Apple'],
	['Red', 1, 'Grape'],
	['Red', 1, 'Grape'],
	['Yellow', 3, 'Lemon'],
]


#headers of the training data
data_headers = ['color', 'diameter', 'label']



def decision_tree(data):

	# helper function to check if a value is a number
	def is_number(value):
		return isinstance(value, int) or isinstance(value, float)

	class Question:
		
		# holds 1)the feature the question is looking at
		# and 2)the value the question is expecting
		# feature: column index
		# value: value to compare to
		def __init__(self, feature, value):
			self.feature = feature
			self.value = value
		
		# for printing the question	
		def __repr__(self):
			if is_number(self.value): condition = '>='
			else: condition = '=='
			return 'Is %s %s %s ?' % (data_headers[self.feature], 
			                          condition, 
									  self.value)
		
		# function that check if a record mathces the question	
		def match(self, record):
			val = record[self.feature]
			if is_number(val):
				if val >= self.value: return True
			else:
				if val == self.value: return True

	class Leaf:
		
		# holds the leaves formed as last
		# class -> how many times it appears in the data set 
		# that reaches the leaf
		def __init__(self, data):
			self.leaf = count_labels(data)
			

	class Node:
		
		# holds the nodes where tree asks question and split data
		def __init__(self, question, true_branch, false_branch):
			self.question = question
			self.true_branch = true_branch
			self.false_branch = false_branch


	# counts how many records belongs to each labels
	def count_labels(data):
		counts = {}
		for rec in data:
			label = rec[-1]
			if label not in counts:
				counts[label] = 0
			counts[label] += 1
		return counts

			
	# function that split a data set into two subsets
	def split(data, question):
		true_set = []
		false_set = []
		for rec in data:
			if question.match(rec):
				true_set.append(rec)
			else:
				false_set.append(rec)
		return true_set, false_set
		
	# calculate the gini impurity of the set at hand 	
	def get_gini_impurity(data):
		labels = count_labels(data)
		impurity = 1
		for lbl in labels:
			label_num = labels[lbl]
			prob_i = label_num / float(len(data))
			impurity -= prob_i**2
		return impurity
		
	def get_info_gain(true_branch, false_branch, starting_impurity):
		true_impurity = get_gini_impurity(true_branch)
		false_impurity = get_gini_impurity(false_branch)
		true_weight = float(len(true_branch)) / float(len(true_branch) + len(false_branch))
		
		new_impurity = true_weight*true_impurity + (1-true_weight)*false_impurity
		info_gain = starting_impurity - new_impurity
		return info_gain
		
	def get_best_split(data):
		best_info_gain = 0 
		best_question = None
		starting_gini = get_gini_impurity(data)
		num_of_features = len(data[0]) - 1 #last column is label not feature
		
		#col: which feature to look at
		#val: feature value of the object
		for col in range(num_of_features):
			vals = set([rec[col] for rec in data]) # unique values in data set
			for val in vals:
				question = Question(col, val) # raise a question
				true_set, false_set = split(data, question) 
				
				#skip the question if it does not split the data
				if len(true_set) == 0 or len(false_set) == 0:
					continue
				
				info_gain = get_info_gain(true_set, false_set, starting_gini)
				
				if info_gain >= best_info_gain:
					best_info_gain = info_gain
					best_question = question
		
		return best_question, best_info_gain
		
	def build_tree(data):
		question, gain = get_best_split(data)
		
		# cannot be purer by splitting -> reahces the leaf
		if gain == 0:
			return Leaf(data) # data that reaches the leaf
			
		true_set, false_set = split(data, question)
		
		true_branch = build_tree(true_set)
		
		false_branch = build_tree(false_set)

		return Node(question, true_branch, false_branch)


	def print_tree(node, spacing = ''):
		
		if isinstance(node, Leaf):
			print(spacing, 'Predict:', node.leaf)
			return
			
		print(spacing + str(node.question))
		
		print(spacing + '-> True')
		print_tree(node.true_branch, spacing + '  ')
		
		print(spacing + '-> False')
		print_tree(node.false_branch, spacing + '  ')




	my_tree = build_tree(training_data)

	print_tree(my_tree)
	









	