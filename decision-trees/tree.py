#
# Tree class
#

class Tree(object):
	def __init__(self, label):
		# this is a specific attrbiute - value dictionary
		self.label = label

		# a dictionary of attribute - tree 
		self.children = {}

	def add_branch(self, label, subtree):
		self.children[label] = subtree

	def __repr__(self):
		# return a string with the tree
		retstr = str(self.label) 
		for key, value in self.children:
			retstr+='; '+str(value)
		return retstr