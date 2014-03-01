
'''
Visualizes the wumpus world
size - pair of ints (x, y) - dimensions of world
agentpos- pair of ints (x, y) - position of player
golds - list of pair of ints [(x, y),..] - positions of gold
wumpuses - list of pair of ints [(x,y), ..] - position of wumpuses
pits - list of pair of ints [(x,y),..] - position of pits
'''
def visualize (size, agentpos, golds, wumpuses, stenches, pits, breezes) :
	'''
	-----------------
	| G | W | # | ~ |
	-----------------
	|   | # | ~ | P |
	-----------------
	|   |   |   | ~ |
	-----------------
	| A |   |   |   |
	-----------------
	'''

	def fill_map(lst, viz, usecounter):
		counter = 0
		retval = {}

		for itm in lst:
			counter +=1
			retval[itm] = viz  + (str(counter) if usecounter else '')
		return retval
		

	goldviz = 'G'
	angentviz ='Ag'
	pitviz = 'P'
	wumpusviz = 'W'
	breezeviz = '~~'
	stenchviz = '##'
	# make mappings
	counter = 0

	symbolmap = {}

	symbolmap = dict(symbolmap.items() + fill_map(golds, goldviz, True).items())
	symbolmap = dict(symbolmap.items() + fill_map(wumpuses, wumpusviz, True).items())
	symbolmap = dict(symbolmap.items() + fill_map(stenches, stenchviz, False).items())
	symbolmap = dict(symbolmap.items() + fill_map(pits, pitviz, True).items())
	symbolmap = dict(symbolmap.items() + fill_map(breezes, breezeviz, False).items())

	symbolmap[agentpos] = angentviz
	

	# add 
	retval = ''
	rowstr = ''
	sep = '-----'
	sep = ' ' + ''.join([sep for x in range(size[1])]) + '\n'

	#retval +='   | a | b | c | d | e | f | g | h |\n'
	retval += sep

	for i in range(0, size[0]):
	   
	   rowstr = '|'
	   for j in range(0,size[1]):
	       if (i,j) in symbolmap.keys():
	           rowstr += ' '+ symbolmap[(i,j)]+' |'
	       else:
	           rowstr += '    |'

	   retval += rowstr + '\n'
	   retval += sep


	
	return retval

size = (5,5)
agentpos = (0,0)
golds = [(2,2)]
wumpuses = [(3,3)]
stenches = [(2,3)]
pits = [(0,1)]
breezes = [(0,2)]

print visualize(size, agentpos, golds, wumpuses, stenches, pits, breezes)