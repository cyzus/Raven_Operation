import grouping_training
import naive_bayes

spams = grouping_training.import_spam()
norms = grouping_training.import_norm()
grouping = grouping_training.group(spams, norms)
impurities = grouping_training.get_impruties(grouping, spams, norms)

training_data = grouping[0]

# list of algorithm at use
algos = [naive_bayes.naive_bayes]


class Algorithms:
	
	# a class to hold algorithms used
	# with utilities included
	def __init__(self, algo_call):
		self.algo_call = algo_call
		
	def __repr__(self):
		return 'algorithims: %s' % (self.algo_call)
	
	# if a piece of text is spam (true) according to the algo
	def match(self, text):
		true_set, false_set = self.algo_call(training_data)############
		if text in true_set: return True
		elif text in false_set: return False


class Leaf:
	
	# holds the leaves formed as last
	# class -> how many times it appears in the data set 
	# that reaches the leaf
	def __init__(self, data):
		self.leaf = count_labels(data)
		

class Node:
	
	# holds the nodes where tree asks question and split data
	def __init__(self, algo, true_branch, false_branch):
		self.algo = algo
		self.true_branch = true_branch
		self.false_branch = false_branch



# counts how many records belongs to each labels
def count_labels(data):
	counts = {}
	for rec in data:
		label = rec[0]
		if label not in counts:
			counts[label] = 0
		counts[label] += 1
	return counts


# function that split a data set into two subsets
def split(data, algo):
	true_set, false_set = algo(data)  #########################################################
	
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
	
	
def find_best_algo(data):
	best_algo = None
	best_gain = 0
	start_gini = get_gini_impurity(data)
	
	for al in algos:
		algorithm = Algorithms(al)
		true_set, false_set = algorithm.algo_call(data)
		
		# if the algo does not divide the data
		# skip the algo
		if len(true_set) == 0 or len(false_set) == 0:
			continue
	
		info_gain = get_info_gain(true_set, false_set, start_gini)
		
		if info_gain >= best_gain: 
			best_gain = info_gain
			best_algo = algorithm
			
	# best_algo: an object of class Algorithms		
	return best_algo, best_gain
	
	
# building
def build_tree(data):
	
	algo, gain = find_best_algo(data) 
	
	# reach leaf
	if gain == 0:
		return Leaf(data)
	
	true_set, false_set = split(data, algo)
	
	true_branch = build_tree(true_set)
	
	false_branch = build_tree(false_set)

	return Node(algo, true_branch, false_branch)
	
	
def print_tree(node, spacing = ''):
	
	if isinstance(node, Leaf):
		print(spacing, 'Predict:', node.leaf)
		return
		
	print(spacing + str(node.algo))
	
	print(spacing + '-> True')
	print_tree(node.true_branch, spacing + '  ')
	
	print(spacing + '-> False')
	print_tree(node.false_branch, spacing + '  ')

	
def classify(text, node):
	
	if isinstance(node, Leaf):
		return node.leaf
		
	if node.algo.match(text):
		return classify(text, node.true_branch)
	else:
		return classify(text, node.false_branch)
	
# takes in Leaf object (dict containing results)
# returns printing content
def print_leaves(prediction):
	print('leaf')
	return prediction
	
	
# main
my_tree = build_tree(training_data)

print_tree(my_tree)
test_data = grouping[1]

for row in test_data:
	print(print_leaves(classify(row, my_tree)))













	
	
	
	