#
# put description here
#

import readarff

def plurality_value(examples):
	# todo
	p = 0
	n = 0
	ls = []
	for example in examples:
		if example[1]=='Yes':
			p += 1
		else:
			n += 1
	if p>n:
		return 'Yes'
	else:
		return 'No'

if __name__ == '__main__':
	examples,attributes = readarff.read_arff('restaurant-domain.arff')
	print plurality_value(examples)