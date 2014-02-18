#
# Reads a arff file
#
# filename - the file to read
# returns a pair of list of examples, dictionary of attribute names-attribute value list
# (list of (dictionary of attribute-value), yvalue))
# [	[{'Alt':'True', 'Bar':'False', 'Fri':False, 'Hun':'True', 'Pat':'some', 'Price':'$$$', 'Rain':'False', 'Res':'True', 'Type':'french', 'Est':'0-10'},'True'],
# ] 
#
# {'pat':['some', 'none', 'full'], 'price':['$', '$$', '$$$']}
'''
@attribute Alt {Yes, No}
@attribute Bar {Yes, No}
@attribute Fri {Yes, No}
@attribute Hun {Yes, No}
@attribute Pat {Full, Some, None}
@attribute Price {$, $$, $$$}
@attribute Rain {Yes, No}
@attribute Res {Yes, No}
@attribute Type {French, Thai, Burger, Italian}
@attribute Est {0-10, 10-30, 30-60, >60}
@attribute WillWait {Yes, No}

@data
Yes,No,No,Yes,Some,$$$,No,Yes,French,0-10,Yes
Yes,No,No,Yes,Full,$,No,No,Thai,30-60,No
No,Yes,No,No,Some,$,No,No,Burger,0-10,Yes
Yes,No,Yes,Yes,Full,$,Yes,No,Thai,10-30,Yes
Yes,No,Yes,No,Full,$$$,No,Yes,French,>60,No
No,Yes,No,Yes,Some,$$,Yes,Yes,Italian,0-10,Yes
No,Yes,No,No,None,$,Yes,No,Burger,0-10,No
No,No,No,Yes,Some,$$,Yes,Yes,Thai,0-10,Yes
No,Yes,Yes,No,Full,$,Yes,No,Burger,>60,No
Yes,Yes,Yes,Yes,Full,$$$,No,Yes,Italian,10-30,No
No,No,No,No,None,$,No,No,Thai,0-10,No
Yes,Yes,Yes,Yes,Full,$,No,No,Burger,30-60,Yes
'''
import arff
def read_arff(filename):
	# todo
	'''
	attributes={'Alt':['Yes', 'No'],'Bar':['Yes','No'],'Fri': ['Yes', 'No'],\
	'Hun': ['Yes', 'No'],'Pat':['some', 'none', 'full'], 'Price':['$', '$$', '$$$'],\
	'Rain': ['Yes', 'No'],'Res': ['Yes', 'No'],'Type': ['French', 'Thai', 'Burger', 'Italian'],\
	'Est': ['0-10', '10-30', '30-60', '>60']}
	'''
	new_attributes=dict()
	new_examples=[]
	data = arff.load(open(filename,'rb'))
	attributes = data['attributes']
	examples = data['data']
	for row in examples:
		example=[]
		d=dict()
		n=0
		for item in row[:-1]:
			d[attributes[n][0]]=item
			n+=1
		example.append(d)
		example.append(row[-1])
		new_examples.append(example)

	for row in attributes[:-1]:
		new_attributes[row[0]]=row[1]		
	classification = attributes[-1][1]
	
	return new_examples,new_attributes, classification

if __name__ == '__main__':
	examples,attributes = read_arff('restaurant-domain.arff')