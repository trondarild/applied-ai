#
# Tree class
#

class Tree(object):
	__init__(self):
		# this is a specific attrbiute - value dictionary
		self.label = {}

		# a dictionary of attribute - tree 
		self.children = {}

	def add_branch(self, label, subtree):
		self.children[label] = subtree