#
# Decision tree algorithm
#
from utils import argmax

def plurality-value(examples):
	# todo
	return examples

def importance(attribute, examples):
	# todo
	return floatvalue

def decision-tree-learning(examples, attributes, parent_examples):
	def is_same(examples):
		classification = []
		classification.append(examples[0][1])
		isSame = True
		for example in examples[1:] :
			if example[1] in classication:
				continue
			else:
				return (False, None)
				
		return (True, classication[0])

def remove_member(member, list):
	# todo
	newlist=[]
	return newlist

	sameclass,classification = is_same(examples)

	if len(examples)==0:
		return plurality-value(parent_examples)
	elif sameclass: return classification
	elif len(attributes)==0: return plurality-value(examples)
	else:
		attribute = argmax(attributes, importance)
		node = Node(argumentlist)
		exs = []
		for vk in attribute.value:
			for example in examples:
				exvalues = example[0]
				if exvalues[attribute.key] == vk:
					exs.append(example)

			newattributes = remove_member(attribute, attibutes)
			subtree = decision-tree-learning(exs, newattributes, examples)
			# make a label by combining attribute name with a spacific
			# attribute value
			label = {attribute.key:vk} 
			node.add_branch(label, subtree)

