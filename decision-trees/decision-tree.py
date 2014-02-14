#
# Decision tree algorithm
#
from utils import argmax
import plurality-value
import importance
import tree


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

	
	sameclass,classification = is_same(examples)

	if len(examples)==0:
		return plurality-value(parent_examples)
	elif sameclass: return classification
	elif len(attributes)==0: return plurality-value(examples)
	else:
		attribute = argmax(attributes, lambda ((a, e)): importance(a, e))
		tree = Tree(attribute)
		exs = []
		for vk in attribute.value:
			for example in examples:
				exvalues = example[0]
				if exvalues[attribute.key] == vk:
					exs.append(example)

			newattributes = attributes.remove(attribute)#remove_member(attribute, attibutes)
			subtree = decision-tree-learning(exs, newattributes, examples)
			# make a label by combining attribute name with a spacific
			# attribute value
			label = {attribute.key:vk} 
			tree.add_branch(label, subtree)

		return tree
