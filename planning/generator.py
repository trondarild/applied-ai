import sys
from random import *
M=2
N=3
numberOfWumpus=2
numberOfPits=1

if not sys.argv[1:]:
	print "Usage: python generator.py [OPTIONS]"
	print "Options are:"
	print "-M, the number of the rows in the world"
	print "-N, the number of colomns in the world"
	print "-W, the number of Wumpus"
	print "-P, the number of Pits"
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
	i += 1

# generate world
s="(define (problem wumpusproblem)\n"

s+="  (:domain wumpusworldsquare)\n"
#Objects
square=""
squarelist=[]
for i in range(1,M+1):
	row=[]
	for j in range(1,N+1):
		square+="sq-"+str(i)+"-"+str(j)+" "
		row.append("sq-"+str(i)+"-"+str(j))
	squarelist.append(row)

square+="- square "

wumpus=""
wumpuslist=[]
for i in range(1,numberOfWumpus+1):
	wumpuslist.append("wumpus-"+str(i))
	wumpus+="wumpus-"+str(i)+" "
wumpus+="- wumpus "

pit=""
for i in range(1,numberOfPits+1):
	pit+="pit-"+str(i)+" "
pit+="- pit "

arrow="the-arrow - arrow "
agent="agent-1 - player "
gold="the-gold - gold "

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

initagent="\t(at agent-1 sq-1-1)\n"+"\t(alive agent-1)\n"+"\t(have agent-1 the-arrow)\n"+"\t(not (have agent-1 the-gold))\n\n"
initwumpus=""
for wumpus in wumpuslist:
	row=randint(1,M)
	col=randint(1,N)
	initwumpus+="\t(at "+wumpus+" "+squarelist[row-1][col-1]+")\n"+"\t(alive "+wumpus+")\n"
initwumpus+="\n"

initgold="\t(at the-gold "+ squarelist[randint(1,M)-1][randint(1,N)-1]+")\n\n"

s+="  (:init \n" + initsquare + initagent + initwumpus + initgold + "  )\n"
#Goal
goal="\t\t(have agent-1 the-gold)\n"+"\t\t(at agent-1 sq-1-1)\n"+"\t\t(alive agent-1)\n"
s+="  (:goal (and\n"+goal+"\t )\n  )\n"
print s+")"