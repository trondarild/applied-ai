#
# put description here
#
import readarff
import math

def Remainder(attribute,examples,attributes,p,n,classes_list):

	sum = 0
	for v in attributes[attribute]:
		pi=0.0
		ni=0.0
		for example in examples:
			if example[0][attribute]==v:
				if example[1]==classes_list[0]:
					pi+=1.0
				else:
					ni+=1.0

		if pi == 0.0 and ni == 0.0:
			continue
		#sum+=float(pi+ni)/float(p+n) * I( float(pi)/float(pi+ni), float(ni)/float(pi+ni) )
		sum += (pi+ni)/(p+n) * I( pi/(pi+ni), ni/(pi+ni) )

	return sum

def I(x,y):
	if x==0 or y==0 :
		return 0
	else :
		return -x*math.log(x,2)-y*math.log(y,2)


def importance(attribute, examples, attributes,classes_list):
	# todo
	p = 0.0
	n = 0.0
	for example in examples:
		if example[1] == classes_list[0]:
			p += 1
		else:
			n += 1

	if p==0 and n==0:
		print "Error:no examples to calculate importance"
	#print attribute, I(float(p)/float(p+n),float(n)/float(p+n)) - Remainder(attribute,examples,attributes,p,n)
	gain = I(p/(p+n),n/(p+n))-Remainder(attribute,examples,attributes,p,n,classes_list)
	if gain<1.0e-15: gain=0
	return gain

import operator

if __name__ == '__main__':
	examples,attributes,classification = readarff.read_arff('restaurant-domain.arff')
	#print I(1.0/3,2.0/3)
	print attributes
	infgains={}
	for attr, attval in attributes.iteritems():
		infgains[attr] = importance(attr ,examples,attributes, classification)
	sorted_x = sorted(infgains.iteritems(), key=operator.itemgetter(1))
		#print attr +': ' + str(importance(attr ,examples,attributes, classification))
	for i in sorted_x: print i
