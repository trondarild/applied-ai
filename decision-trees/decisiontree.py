#
# Decision tree algorithm
#
from utils import argmax_random_tie, argmax
from pluralityvalue import *
from importance import *
from tree import *

#
# checks if all given examples have same classification
# return true if so, and which class it is
#
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

def decision_tree_learning(examples, attributes, parent_examples, classes_list):
	
	#
	# Checks if the given examples have the same classification
	# examples: [{exampledictionary}, 'class']
	# return: pair with (true/false, the classification)
	sameclass,classification = is_same(examples)

	if len(examples)==0: return Tree(plurality_value(parent_examples))
	elif sameclass: return Tree(classification)
	elif len(attributes)==0: return Tree(plurality_value(examples))
	else:
		# create a list of the attribute names (attributes.keys()), calculate the importance of each of
		# them, then get the one with highest value
		attributename = argmax(attributes.keys(), lambda ((a)): importance(a, examples, attributes,classes_list))
		#attributename = argmax_random_tie(attributes.keys(), lambda ((a)): importance(a, examples, attributes,classes_list))
		
		tree = Tree(attributename)
		
		for vk in attributes[attributename]:
			exs = []
			for example in examples:
				exvalues = example[0]
				if exvalues[attributename] == vk:
					exs.append(example)

			newattributes = remove_dict_entry(attributename, attributes) #remove_member(attribute, attibutes)
			subtree = decision_tree_learning(exs, newattributes, examples,classes_list)
			#subtree = decision_tree_learning(exs, attributes, examples,classes_list)

			# make a label by combining attribute name with a spacific
			# attribute value
			label = str(vk) #{attribute.key:vk} 
			tree.add_branch(label, subtree)

		return tree
