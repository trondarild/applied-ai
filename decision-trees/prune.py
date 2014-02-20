from math import log
from math import pow
from collections import Counter
from tree import Tree

#class1='Yes'
#class2='No'

def calc_chisquared(a, b):
    if b>0 :
	    return pow((a-b), 2)/b
    return 0.0

#
# todo: split into get_stat_data(examples, attributes) and
# calculate_information_gains()
#
# return a dict of (attribute name:information gain)
def calculate_information_gains(examples, attributes, classes):


	def calc_entropy(count1, count2):
		if count1==0 and count2==0:
			return 0.0

		p1 = count1/(count1+count2)
		p2 = count2/(count1+count2)

		#print value+": "+str(p1)+', '+str(p2)
		if p1>0 and p2>0 :
			return -p1*log(p1,2) -p2*log(p2,2)
		return 0.0
	class1 = classes[0]
	class2 = classes[1]
	classcount = {}
	attrentropy = {}
	totalclasscount = {class1:0.0, class2:0.0}
	informationgain = {}

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

	# calculate the total entropy of the goal classes
	totalentropy = calc_entropy(totalclasscount[class1],
		totalclasscount[class2])
	#print totalentropy

	# for each attribute name and value, calculate the entropy
	for attrname, attvalues in attrentropy.items():
		# print attrname
		attrtotalclasscount = 0
		remainder = 0
		for value in attvalues:
			entropy =  calc_entropy(classcount[attrname][value][class1],
				classcount[attrname][value][class2]) #-p1*log(p1,2) -p2*log(p2,2)
			attrentropy[attrname][value] = entropy

			count = classcount[attrname][value][class1]
			count += classcount[attrname][value][class2]
			attrtotalclasscount+=count
			# (sum yes+no counts for each attrvalue)*entropy
			remainder += count*entropy

		# can now calculate remainder
		remainder *= 1.0/attrtotalclasscount
		#print 'remainder: '+ str(remainder)
		# calculate entropy gain: entropy - remainder
		informationgain[attrname] = totalentropy-remainder
		#print "information gain :" + str(retval[attrname])

	return (informationgain, classcount)

def get_stat_data(examples, attributes, classes):
    infgain, statdata = calculate_information_gains(examples, attributes, classes)
    return statdata

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
# note rewrite this to get_expected_values(examples, attributes)
# and do_chisquared_test(expectedvalues, observedvalues)
#
def old_do_chisquared_test(examples, attributes, classification):
	# for all attributes
	# null hypothesis: attribute contributes nothing
	# compare observed positive and negatives with expected

	# statdata[attributename][attributevaluename][class] == number of instances
	statdata = get_stat_data(examples, attributes, classification)
	chisquaredtable = {1:3.84, 2:5.99, 3:7.81, 4:9.49}
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

		chi squared
					|yesclass 		| noclass 		|
		valuename0	|(a-a')^2/a'   	| (b-b')^2/b'  	|
		valuename1	|(c-c')^2/c'  	| (d-d')^2/d'  	|
		...			-----------------------------------------

		totalchisquared = chisq00 + chisq01 + chisq10 + chisq11 ..
		degrees of freedom: df = numvaluenames-1
		chicheck: chisquaredtable[df] < totalchisquared ?

		return {attribute:chiceck}, {attribute:{attvalue:[expectedvals]}}

	expectedpos[attribute] = totalpositive* (positive[attribute]+negative[attribute])
	# check against the chi squared table
	'''
	class1 = classification[0]
	class2 = classification[1]
	retval = {}
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
		chisquaredsum = 0
		sum4 = sum(sumarray)
		i=0
		for attributevalue, classes in attributevalues.iteritems():
			expval1 = sumarray[i]*sum2/sum4
			expval2 = sumarray[i]*sum3/sum4


			#expectedvals.append([expval1, expval2])
			expectedvals[attributename][attributevalue] = [expval1, expval2]

			chisquaredsum += calc_chisquared(observedvals[i][0], expval1)
			chisquaredsum += calc_chisquared(observedvals[i][1], expval2)
			i+=1

		# do chisquared check
		degreesoffreedom = len(attributevalues)-1
		chicheck = chisquaredsum >= chisquaredtable[degreesoffreedom]
		retval[attributename] = chicheck

	return retval, expectedvals

def get_expected_values(examples, attributes, classes):
    chisq, expected = old_do_chisquared_test(examples, attributes, classes)
    return expected

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
		leaf = c.most_common(1)[0][0]
		return leaf

'''
tsttree = Tree('type')
tsttree.add_branch('italian',Tree('No'))
tsttree.add_branch('french',Tree('No'))
tsttree.add_branch('burger',Tree('No'))
tsttree.add_branch('thai',Tree('Yes'))
expvals = {'italian':[2,2], 'french':[2,2], 'burger':[1,1], 'thai':[1,1]}
cls = ['Yes', 'No']
#print tsttree.children
print irrelevance_evaluation(tsttree, expvals, cls)
'''

#
# Prunes the tree
# tree - the tree to prune
# examples - list of examples used to calculate entropy gain
# attributes - list of attributes used to calculate entropy gain
# returns a pruned tree
#
def prune(tree, examples, attributes, classification, expectedvals):
	# start with complete tree
	# eliminate irrelevant nodes:
	# look at test node with *only* leaf nodes as children
	# if test gives irrelevance (how  to check this?) - only noise in data - eliminate and replace with leaf
	# do this for every test with leaf nodes
	# repeat
	# irrelevance test: information gain close to zero


	def get_branch_list(children):
		retval = []
		for key, branch in children.iteritems():
			if len(branch.children) != 0:
				retval.append(key)
		return retval

    # get expected values for leaves
 	# expectedvals = get_expected_values(examples, attributes, classification)

	children = tree.children
	branchnames = get_branch_list(children)
	# check if all children are leaves
	# (note this could be done with a lambda applied on set of all children)

	# if no branches, only leaves, do irrelevance evaluation
	if  len(branchnames) == 0 :
		# do irrelevance evaluation
		return irrelevance_evaluation(tree, expectedvals[tree.label], classification)

	else:
		# do recursive call on  branches that have children
		for branchname in branchnames:
			children[branchname] = prune(children[branchname], examples, attributes, classification, expectedvals)

		# check if now have only leaves
		branchnames = get_branch_list(children)
		'''
		# note: ugly repetition, can it be removed?
		'''
		if  len(branchnames) == 0 :
			# do irrelevance evaluation
			return irrelevance_evaluation(tree, expectedvals[tree.label], classification)
		else:
			return tree
