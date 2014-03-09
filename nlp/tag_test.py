from viterbi import *
def tagger(testFile,taggedFile,n):
	dicOfWordTag,dicOfTag,dicOfTags=read_corpus("corpus/CoNLL2009-ST-English-train-pos.txt")
	f=open(testFile,'r')
	fw=open(taggedFile,'w')
	totalNumber=0
	noSolution=0
	words=[]
	lines=[]
	for line in f:
		line=line.strip()
		if line=='':
			if len(words)>n:
				for row in lines:
					for item in row:
						print >> fw,item,
				words=[]
				lines=[]
				continue

			prob,path=viterbi(words,dicOfWordTag,dicOfTag,dicOfTags)
			
			if prob==0:
				#print >>fw,"no solution"
				noSolution+=1
				for row in lines:
					for item in row:
						print >> fw,item,
					print >> fw
				print >>fw
				words=[]
				lines=[]
				continue
			
			i=0
			while i<len(path):
				for item in lines[i]:
					print >> fw,item,
				print >> fw,path[i],path[i]
				i+=1
			print >> fw
			words=[]
			lines=[]

		else:
			line=line.split()
			words.append(line[1])
			lines.append(line)
			totalNumber+=1
	
	print 1-float(noSolution)/totalNumber

if __name__ == '__main__':
	tagger('corpus/CoNLL2009-ST-test-words.txt','corpus/CoNLL2009-ST-tagged-test-words.txt',150)