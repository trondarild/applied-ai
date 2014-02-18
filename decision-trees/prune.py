from math import log
from math import pow

class1='YesClass'
class2='NoClass'

def calc_chisquared(a, b):
	return pow((a-b), 2)/b

# return a dict of (attribute name:information gain)
def calculate_information_gains(examples, attributes):
	
	def calc_entropy(count1, count2):
		if count1==0 and count2==0:
			return 0.0

		p1 = count1/(count1+count2)
		p2 = count2/(count1+count2)
		
		#print value+": "+str(p1)+', '+str(p2)
		if p1>0 and p2>0 :
			return -p1*log(p1,2) -p2*log(p2,2)
		return 0.0

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

def do_chisquared_test(examples, attributes):
	# for all attributes
	# null hypothesis: attribute contributes nothing
	# compare observed positive and negatives with expected

	# statdata[attributename][attributevaluename][class] == number of instances
	informationgain, statdata = calculate_information_gains(examples, attributes)
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

		return {attribute:chiceck}

	expectedpos[attribute] = totalpositive* (positive[attribute]+negative[attribute])
	# check against the chi squared table
	'''
	retval = {}	
	for attributename, attributevalues in statdata.iteritems():
		sumarray = []
		sum2 = 0
		sum3 = 0
		observedvals = []	# this wastes space, but makes it easier to think about
		# calculate the sums:
		for attributevalue, classes in attributevalues.iteritems():
			#sumarray.append(statdata[attributename][attributevalue][class1] +
			#	statdata[attributename][attributevalue][class2])
			sumarray.append(classes[class1]+classes[class2])
			observedvals.append([classes[class1], classes[class2]])
			sum2 += classes[class1]
			sum3 += classes[class2]

		# calculate expected values, and the sum of chisquared
		expectedvals = []
		chisquaredsum = 0
		sum4 = sum(sumarray)
		for i in range(len(sumarray)):
			expval1 = sumarray[i]*sum2/sum4
			expval2 = sumarray[i]*sum3/sum4
			expectedvals.append([expval1, expval2])
			chisquaredsum += calc_chisquared(observedvals[i][0], expval1)
			chisquaredsum += calc_chisquared(observedvals[i][1], expval2)
		
		# do chisquared check
		degreesoffreedom = len(attributevalues)-1
		chicheck = chisquaredsum >= chisquaredtable[degreesoffreedom]
		retval[attributename] = chicheck
	
	return retval

#
# Prunes the tree
# tree - the tree to prune
# examples - list of examples used to calculate entropy gain
# attributes - list of attributes used to calculate entropy gain
# returns a pruned tree
#
def prune(tree, examples, attributes):
	# start with complete tree
	# eliminate irrelevant nodes:
	# look at test node with *only* leaf nodes as children
	# if test gives irrelevance (how  to check this?) - only noise in data - eliminate and replace with leaf
	# do this for every test with leaf nodes
	# repeat 
	# irrelevance test: information gain close to zero
	
	def irrelevance_evaluation(children):
		# todo
		# get statistical split point for the attribute
		# and compare with its information gain
		return 0

	def get_branch_list(children):
		retval = []
		for key, branch in children.iteritems():
			if len(branch.children) != 0:
				retval.append(key)
		return retval

	children = tree.children
	branchnames = get_branch_list(children)
	# check if all children are leaves 
	# (note this could be done with a lambda applied on set of all children)

	# if no branches, only leaves, do irrelevance evaluation
	if  len(branchnames) == 0 :
		# do irrelevance evaluation
		return Tree(irrelevance_evaluation(children))
		
	else:
		# do recursive call on  branches that have children
		for branchname in branchnames:
			children[branchname] = prune(children[branchname])

		# check if now have only leaves
		branchnames = get_branch_list(children)
		'''
		# note: ugly repetition, can it be removed?
		'''
		if  len(branchnames) == 0 :
			# do irrelevance evaluation
			return Tree(irrelevance_evaluation(children))
		else:
			return tree
		