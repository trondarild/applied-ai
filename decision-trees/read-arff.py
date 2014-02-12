#
# Reads a arff file
#
# filename - the file to read
# returns a pair of list of examples, dictionary of attribute names-attribute value list
# (list of (dictionary of attribute-value), yvalue))
# [	[{'alt':True, 'bar':False, 'fri':False, 'hun':True, 'pat':'some', 'price':'$$$', 'rain':False, 'res':True, 'type':'french', 'est':'0-10'}, True],
# ] 
#
# {'pat':['some', 'none', 'full'], 'price':['$', '$$', '$$$']}

def read_arff(filename):
	# todo