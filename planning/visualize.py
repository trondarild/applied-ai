
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


	goldviz = 'G'
	angentviz ='A'
	pitviz = 'P'
	wumpusviz = 'W'
	breezeviz = '~'
	stenchviz = '#'
	# make mappings
	symbolmap = {}
	for gold in golds:
		symbolmap[gold] = goldviz
	for wumpus in wumpuses:
		symbolmap[wumpus] = wumpusviz
	for stench in stenches:
		symbolmap[stench] = stenchviz
	for pit in pits:
		symbolmap[pit] = pitviz
	for breeze in breezes:
		symbolmap[breeze] = breezeviz
	symbolmap[agentpos] = angentviz
	

	# add 
	retval = ''
	rowstr = ''
	sep = '----'
	sep = ' ' + ''.join([sep for x in range(size[1])]) + '\n'

	#retval +='   | a | b | c | d | e | f | g | h |\n'
	retval += sep

	for i in range(0, size[0]):
	   
	   rowstr = '|'
	   for j in range(0,size[1]):
	       if (i,j) in symbolmap.keys():
	           rowstr += ' '+ symbolmap[(i,j)]+' |'
	       else:
	           rowstr += '   |'

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