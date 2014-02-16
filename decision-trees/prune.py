#
# Prunes the tree
# tree - the tree to prune
# returns a pruned tree
#
def prune(tree):
	# start with complete tree
	# eliminate irrelevant nodes:
	# look at test node with *only* leaf nodes as children
	# if test gives irrelevance (how  to check this?) - only noise in data - eliminate and replace with leaf
	# do this for every test with leaf nodes
	# repeat 
	# irrelevance test: information gain close to zero
	
	def irrelevance_evaluation(children):
		# todo

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
		