from readarff import *
from visualize import *
from decisiontree import *



def isRight(tree,example):
	if tree.children == {}:
		if tree.label == example[1]:
			return True
		else:
			return False
	else:
		branch=example[0][tree.label]
		return isRight(tree.children[branch],example)



def d_fold_cross_validation(examples,attributes,classification,d):
	'''return precsion rate with d fold cross validation'''
	rightNumber = 0
	for i in range(d):
		#testset=[]
		testset = examples[i]

		trainset=[]
		for j in range(d):
			if j==i:
				continue
			else:
				trainset.append(examples[j])

		tree = decision_tree_learning(trainset,attributes,[],classification)
		if isRight(tree,testset):
			rightNumber+=1

	precision_rate = rightNumber/float(d)
	return precision_rate

if __name__ == '__main__':
	examples,attributes,classification = read_arff('restaurant-domain.arff')
	d = len(examples)
	precision_rate = d_fold_cross_validation(examples,attributes,classification,d)
	print "with "+str(d)+"-fold cross validation, the precision rate is:" + str(precision_rate)