import sys
from random import *
from visualize import *

M=2
N=3
numberOfWumpus=2
numberOfPits=1
numberOfGold=1

def placeAround(position, dims):
	row = position[0]
	col = position[1]
	aroundPosition=[]
	if row-1>0:
		aroundPosition.append((row-1,col))
	if col-1>0:
		aroundPosition.append((row,col-1))
	if row+1<=dims[0]:
		aroundPosition.append((row+1,col))
	if col+1<=dims[1]:
		aroundPosition.append((row,col+1))
	return aroundPosition

def generate():
	'''return a world dictionary(coordinate as key, a list of string of the object as value), which is like below
	
	{1: {1: ['agent-1', 'stench'], 2: ['stench', 'breeze', 'gold-1'], 3: ['wumpus-2']}, 
	 2: {1: ['wumpus-1', 'breeze'], 2: ['stench', 'pit-1'], 3: ['stench', 'breeze']}}

	'''

	goldviz = 'G'
	angentviz ='Ag'
	pitviz = 'P'
	wumpusviz = 'W'
	breezeviz = '~~'
	stenchviz = '##'
	filename = ''
	if not sys.argv[1:]:
		print "Usage: python generator.py [OPTIONS]"
		print "Options are:"
		print "-M, the number of the rows in the world"
		print "-N, the number of colomns in the world"
		print "-W, the number of Wumpus"
		print "-P, the number of Pits"
		print "-G, the number of Gold"
		print "-F, the file name"
		return

	i=1
	while (i<len(sys.argv)) :
		arg = sys.argv[i]
		if arg=='-M':
			i+=1
			M = int(sys.argv[i])
		elif arg=='-N':
			i+=1
			N = int(sys.argv[i])
		elif arg=='-W':
			i+=1
			numberOfWumpus = int(sys.argv[i])
		elif arg=='-P':
			i+=1
			numberOfPits = int(sys.argv[i])
		elif arg=='-G':
			i+=1
			numberOfGold = int(sys.argv[i])
		elif arg=='-F':
			i+=1
			filename = str(sys.argv[i])
		i += 1

	# generate world
	s="(define (problem wumpusproblem)\n"

	s+="  (:domain wumpusworldsquare)\n"
	#Objects
	world=dict()
	coordinate=[]
	square=""
	squarelist=[]
	for i in range(1,M+1):
		row=[]
		world[i]=dict()
		for j in range(1,N+1):
			square+="sq-"+str(i)+"-"+str(j)+" "
			row.append("sq-"+str(i)+"-"+str(j))
			world[i][j]=''
			coordinate.append((i,j))
		squarelist.append(row)

	square+="- square "

	wumpus=""
	wumpuslist=[]
	for i in range(1,numberOfWumpus+1):
		wumpuslist.append("wumpus-"+str(i))
		wumpus+="wumpus-"+str(i)+" "
	wumpus+="- wumpus "

	pit=""
	pitlist=[]
	for i in range(1,numberOfPits+1):
		pitlist.append("pit-"+str(i))
		pit+="pit-"+str(i)+" "
	pit+="- pit "

	arrow="the-arrow - arrow "
	agent="agent-1 - player "
	#gold="the-gold - gold "
	gold=""
	goldlist=[]
	for i in range(1,numberOfGold+1):
		goldlist.append("gold-"+str(i))
		gold+="gold-"+str(i)+" "
	gold+="- gold "

	s+="  (:objects " + square + wumpus + pit + arrow + agent + gold +")\n"

	#Init
	initsquare=""
	for row in range(M):
		for col in range(N):
			if (row+1)<M:
				initsquare+="\t(adj "+squarelist[row][col]+" "+squarelist[row+1][col]+ ")\n"
			if (row-1)>=0:
				initsquare+="\t(adj "+squarelist[row][col]+" "+squarelist[row-1][col]+ ")\n"
			if (col+1)<N:
				initsquare+="\t(adj "+squarelist[row][col]+" "+squarelist[row][col+1]+ ")\n"
			if (col-1)>=0:
				initsquare+="\t(adj "+squarelist[row][col]+" "+squarelist[row][col-1]+ ")\n"
	initsquare+="\n"

	# place agent
	initagent="\t(at agent-1 sq-1-1)\n"+"\t(alive agent-1)\n"+"\t(have agent-1 the-arrow)\n"+"\t(not (have agent-1 the-gold))\n\n"
	
	coordinate.remove((1,1))

	# place wumpus
	initwumpus=""
	wumpusposition=sample(coordinate,numberOfWumpus)
	i=0
	while i<len(wumpuslist):
		wumpus=wumpuslist[i]
		position=wumpusposition[i]
		row=position[0]
		col=position[1]
		initwumpus+="\t(at "+wumpus+" "+squarelist[row-1][col-1]+")\n"+"\t(alive "+wumpus+")\n"
		world[row][col] = (wumpusviz + wumpus.split('-')[1] )
		coordinate.remove(position)
		aroundPosition=placeAround(position, (M,N))
		for pos in aroundPosition:
			initwumpus+="\t(stench "+squarelist[pos[0]-1][pos[1]-1]+")\n"
			world[pos[0]][pos[1]] = (stenchviz if world[pos[0]][pos[1]]=='' else world[pos[0]][pos[1]]) 
		i+=1
	initwumpus+="\n"
	# place pits
	initpit=""
	pitposition=sample(coordinate,numberOfPits)
	i=0
	while i<len(pitlist):
		pit=pitlist[i]
		position=pitposition[i]
		row=position[0]
		col=position[1]
		initpit+="\t(pit "+squarelist[row-1][col-1]+")\n"
		world[row][col] = pitviz + pit.split('-')[1] #.append(pit)
		coordinate.remove(position)
		aroundPosition=placeAround(position, (M,N))
		for pos in aroundPosition:
			initpit+="\t(breeze "+squarelist[pos[0]-1][pos[1]-1]+")\n"
			world[pos[0]][pos[1]] = (breezeviz if world[pos[0]][pos[1]]==''  else world[pos[0]][pos[1]])
		i+=1
	initpit+="\n"

	# place gold
	initgold=""
	goldposition=sample(coordinate,numberOfWumpus)
	i=0
	while i<len(goldlist):
		gold=goldlist[i]
		position=goldposition[i]
		row=position[0]
		col=position[1]
		initgold+="\t(at "+gold+" "+squarelist[row-1][col-1]+")\n"
		world[row][col] = goldviz + gold.split('-')[1] #.append(gold)
		coordinate.remove(position)
		i+=1
	initgold+="\n"

	world[1][1] = (angentviz) #("agent-1")

	s+="  (:init \n" + initsquare + initagent + initpit + initgold + initwumpus + "  )\n"
	#Goal
	havegold=""
	for gold in goldlist:
		havegold+="\t\t(have agent-1 "+gold+")\n"
	goal=havegold+"\t\t(at agent-1 sq-1-1)\n"+"\t\t(alive agent-1)\n"
	s+="  (:goal (and\n"+goal+"\t )\n  )\n"
	s+=")"

	# write to file
	fileobj = open(filename, 'w')
	fileobj.write(s)
	fileobj.close()
	print 'Problem file generated and written to ' + filename	
	return world, (M,N)
	#print coordinate
if __name__ == "__main__":
	world, size = generate()
	print visualize_world(size, world)
	#print world