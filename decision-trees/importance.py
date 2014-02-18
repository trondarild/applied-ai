#
# put description here
#
import readarff
import math

def Remainder(attribute,examples,attributes,p,n):

	sum = 0
	for v in attributes[attribute]:
		pi=0
		ni=0
		for example in examples:
			if example[0][attribute]==v:
				if example[1]=='Yes':
					pi+=1
				else:
					ni+=1
		if pi > 0 or ni > 0:
			sum+=float(pi+ni)/float(p+n)*I(float(pi)/float(pi+ni),float(ni)/float(pi+ni))
	return sum

def I(x,y):
	if x==0 or y==0 :
		return 0
	else :
		return float(-x*math.log(x,2)-y*math.log(y,2))

#def Gain(attribute,examples):
	
	#return I(float(p)/float(p+n),float(n)/float(p+n)) - Remainder(attribute,examples)

def importance(attribute, examples, attributes):
	# todo
	p = 0
	n = 0
	for example in examples:
		if example[1] == 'Yes':
			p += 1
		else:
			n += 1
	#print attribute, I(float(p)/float(p+n),float(n)/float(p+n)) - Remainder(attribute,examples,attributes,p,n)

	return I(float(p)/float(p+n),float(n)/float(p+n)) - Remainder(attribute,examples,attributes,p,n)

if __name__ == '__main__':
	examples,attributes = readarff.read_arff('restaurant-domain.arff')
	#print I(0,1)
	print importance('Pat',examples,attributes)