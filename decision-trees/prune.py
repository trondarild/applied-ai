from math import log
from math import pow
from collections import Counter
from tree import Tree


#
# collect statistics data for attributes and attribute vales
#
def get_stat_data(examples, attributes, classes):
	class1 = classes[0]
	class2 = classes[1]
	classcount = {}
	attrentropy = {}
	totalclasscount = {class1:0.0, class2:0.0}

	# initialize data structure
	for attname, attvalues in attributes.items():
		classcount[attname] = {}
		attrentropy[attname] = {}
		for attvalue in attvalues:
			# initialize for counting
			classcount[attname][attvalue] = {}
			classcount[attname][attvalue][class1]=0.0
			classcount[attname][attvalue][class2]=0.0
			attrentropy[attname][attvalue] = 0.0

	# go through examples, and for each attribute,
	# count the number of classifications (yes/no)
	for examplerow in examples:
		example = examplerow[0]
		#print example
		totalclasscount[examplerow[1]]+=1
		for attname, attvalue in example.items():
			classcount[attname][attvalue][examplerow[1]] += 1
	return classcount

#
# do chi squared statistical test on observed data, compare with
# expected. Assume both lists same length
# observedlist: {attributeval:[numpos, numneg], ...}
# expectedlist: {attributeval:[numpos, numneg], ...}
def do_chisquared_test(observedlist, expectedlist):
	chisquaredtable = {1:3.84, 2:5.99, 3:7.81, 4:9.49}
	# count number of instances of classes in observedlist
	chisq = 0.0
	for i in range(len(observedlist)):
		obs = observedlist.items()[i][1]
		exp = expectedlist.items()[i][1]
		chisq += pow((obs[0]-exp[0]),2)/exp[0]
		chisq += pow((obs[1]-exp[1]),2)/exp[1]

	tableval = chisquaredtable[len(observedlist)-1]
	return chisq >= tableval

#
# calculate expected values based on statistical data
#
def get_expected_values(examples, attributes, classes):
 	statdata = get_stat_data(examples, attributes, classes)
	'''
		observed:
					|yesclass 	| noclass 	|
		valuename0	|	a		|	b		| sum0=a+b
		valuename1	|	c		|	d		| sum1=c+d
		...			------------------------------
					 sum2=a+c	| sum3=b+d	| sum4=sum0+sum1

		expected:
					|yesclass 		| noclass 		|
		valuename0	|sum0*sum2/sum4	|sum0*sum3/sum4	| sum0
		valuename1	|sum1*sum2/sum4	|sum1*sum3/sum4	| sum1
		...			-----------------------------------------
					 sum2			| sum3			| sum4=sum0+sum1

		chi squared (not used here)
					|yesclass 		| noclass 		|
		valuename0	|(a-a')^2/a'   	| (b-b')^2/b'  	|
		valuename1	|(c-c')^2/c'  	| (d-d')^2/d'  	|
		...			-----------------------------------------


		return expectedvals

	expectedpos[attribute] = totalpositive* (positive[attribute]+negative[attribute])
	# check against the chi squared table
	'''
	class1 = classes[0]
	class2 = classes[1]
	expectedvals = {}
	for attributename, attributevalues in statdata.iteritems():
		sumarray = []
		sum2 = 0
		sum3 = 0
		#expectedvals[attributename] = {}
		attvalueexpvals = {}
		observedvals = []	# this wastes space, but makes it easier to think about
		# calculate the sums:
		for attributevalue, classes in attributevalues.iteritems():
			attvalueexpvals[attributevalue] = {}
			#sumarray.append(statdata[attributename][attributevalue][class1] +
			#	statdata[attributename][attributevalue][class2])
			sumarray.append(classes[class1]+classes[class2])
			observedvals.append([classes[class1], classes[class2]])
			sum2 += classes[class1]
			sum3 += classes[class2]
		expectedvals[attributename] = attvalueexpvals

		# calculate expected values, and the sum of chisquared
		sum4 = sum(sumarray)
		i=0
		for attributevalue, classes in attributevalues.iteritems():
			expval1 = sumarray[i]*sum2/sum4
			expval2 = sumarray[i]*sum3/sum4

			#expectedvals.append([expval1, expval2])
			expectedvals[attributename][attributevalue] = [expval1, expval2]
			i+=1
			
	return expectedvals    

#
# checks if tree is irrelevant
# if it is, return a tree which is a leaf, otherwise, return given tree
def irrelevance_evaluation(tree, expectedvalues, classification):
	children = tree.children
	# convert children into same form as expectedvalues
	observed = {}
	for valuename, classname in children.iteritems():
		# leaves are trees without children, so use label 
		# to get string value of classificaiton
		observed[valuename] = [0.0,0.0]
		if classname.label == classification[0]:
			observed[valuename][0] +=1.0
		else:
			observed[valuename][1] +=1.0

	relevant = do_chisquared_test(observed, expectedvalues)
	if relevant:
		return tree
	else:
		c = Counter(tree.children.values())
		# most_common returns a list with tuples, and
		# want the leaf which is the first of the tuple
		# and which is already a Tree object
		leaf = c.most_common(1)[0][0]
		return leaf


#
# Prunes the tree
# tree - the tree to prune
# examples - list of examples used to calculate entropy gain
# attributes - list of attributes used to calculate entropy gain
# classification - a list of 2 classification names ['class1', 'class2'] 
# expectedvals - dictionary of 
#	attributename:{attributevaluename:[expectedclass1, expectedclass2]..}..}
# returns a pruned tree
#
def prune(tree, examples, attributes, classification, expectedvals):
	# start with complete tree
	# eliminate irrelevant nodes:
	# 		look at test node with *only* leaf nodes as children
	# 		if test gives irrelevance (how  to check this?) - only noise in data - eliminate and replace with leaf
	# 		do this for every test with leaf nodes
	# 		repeat
	# irrelevance test: information gain close to zero

	# get a list of children nodes which themselves have children|
	def get_branch_list(children):
		retval = []
		for key, branch in children.iteritems():
			if len(branch.children) > 0:
				retval.append(key)
		return retval

	children = tree.children
	branchnames = get_branch_list(children)
	# check if all children are leaves
	# (note this could be done with a lambda applied on set of all children)
	#retval = Tree()
	# if no branches, only leaves, do irrelevance evaluation

	if len(branchnames) > 0:
		for branchname in branchnames:
			children[branchname] = prune(children[branchname], examples, attributes, classification, expectedvals)
		# if pruning returned branches, just return the tree
		if len(get_branch_list(children))>0:
			return tree

	return irrelevance_evaluation(tree, expectedvals[tree.label], classification)
