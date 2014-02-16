#
# somehow displays a tree
#
def visualize(tree):
	'''
	print out tree with tabs, such that children are one tab 
	away from parent, recursively
	
	tree: subtree to print
	parentstr: a series of '|\t', which places the output at the correct distance
	'''
	def tree_to_str(tree, parentstr):
		# get the label, i.e. attribute name, and add it to parentstr
		# will need this later to print out children
		labelstr = parentstr + str(tree.label)
		
		# if have no children, just print out the label, 
		# it should be one of the final class, i.e. yes or no
		if len(tree.children)==0:
			return labelstr +'\n'

		# recursive calls through children. For each child
		# print out own attribute and the attribute's value
		# then print out every branch corresponding to that
		# attribute value
		retstr=''
		for key, value in tree.children.iteritems() :
			retstr += labelstr + '==' + key + ':\n' 
			retstr += tree_to_str(value, parentstr + '|\t')
		
		return retstr


	print tree_to_str(tree, '')

