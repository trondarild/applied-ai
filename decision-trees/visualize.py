#
# somehow displays a tree
#
def visualize(tree):
	# todo
	# print out with tabs
	def tree_to_str(tree, parentstr):
		
		retstr = parentstr + str(tree.label) + '\n'
		if len(tree.children)==0:
			return retstr

		for key, value in tree.children.iteritems() :
			 retstr += tree_to_str(value, parentstr+'|\t')
		
		return retstr


	print tree_to_str(tree, '')

	'''
	retstr = self.label[0] + ' == ' + self.label[1]
		if len(self.children) > 0:
			retstr += 'num children= ' + str(len(self.children)) + ' \n'
			#retstr += '|\t'
			for key, value in self.children.iteritems():
				retstr +=  '|\t' +str(value) 
		else:
			retstr+='\n'
		return retstr
	'''