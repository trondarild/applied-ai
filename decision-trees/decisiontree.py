#
# Decision tree algorithm
#
from utils import argmax
from pluralityvalue import *
from importance import *
from tree import *

def is_same(examples):
		if len(examples) == 0:
			return (False, None)

		classification = []
		class_instance = examples[0][1]
		classification.append(class_instance)
		#isSame = True
		for example in examples[1:] :
			if example[1] in classification:
				continue
			else:
				return (False, None)
				
		return (True, classification[0])

def remove_dict_entry(key, dictionary):
		retval = dict(dictionary)
		del retval[key]
		return retval

def decision_tree_learning(examples, attributes, parent_examples):
	
	#
	# Checks if the given examples have the same classification
	# examples: [{exampledictionary}, 'class']
	# return: pair with (true/false, the classification)
	
	sameclass,classification = is_same(examples)

	if len(examples)==0: return Tree(plurality_value(parent_examples))
	elif sameclass: return Tree(classification)
	elif len(attributes)==0: return Tree(plurality_value(examples))
	else:
		
		attributename = argmax(attributes.keys(), lambda ((a)): importance(a, examples, attributes))
		'''
		if len(examples)==6:
			for a in attributes.keys():
				print a,importance(a, examples, attributes)
			
			print "choose: "+attributename
		'''
		tree = Tree(attributename)
		
		for vk in attributes[attributename]:
			exs = []
			for example in examples:
				exvalues = example[0]
				if exvalues[attributename] == vk:
					exs.append(example)

			newattributes = remove_dict_entry(attributename, attributes) #remove_member(attribute, attibutes)
			subtree = decision_tree_learning(exs, newattributes, examples)
			# make a label by combining attribute name with a spacific
			# attribute value
			label = vk #{attribute.key:vk} 
			tree.add_branch(label, subtree)

		return tree
