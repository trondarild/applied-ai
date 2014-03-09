from viterbi import *
def evaluate(testFile,n):
	dicOfWordTag,dicOfTag,dicOfTags=read_corpus("corpus/CoNLL2009-ST-English-train-pos.txt")
	f=open(testFile,'r')
	rightNumber=0
	denominator=0
	totalNumber=0
	noSolution=0
	words=[]
	right=[]
	for line in f:
		line=line.strip()
		if line=='':
			
			if len(words)>n:
				#print "length> ",n
				words=[]
				right=[]
				continue

			prob,path=viterbi(words,dicOfWordTag,dicOfTag,dicOfTags)
			
			if prob==0:
				words=[]
				right=[]
				noSolution+=1
				continue
			
			i=0
			while i<len(path):
				if path[i]==right[i]:
					rightNumber+=1
				denominator+=1
				i+=1
			words=[]
			right=[]

		else:
			line=line.split()
			words.append(line[1])
			right.append(line[4])
			#print 'deal with '+line[1]+'\t'+str(totalNumber)
			totalNumber+=1
			

	precision=float(rightNumber)/denominator
	recall=1-float(denominator)/totalNumber
	return precision,recall
if __name__ == '__main__':
	precision,recall=evaluate('corpus/CoNLL2009-ST-English-development-pos.txt',16)
	print precision,recall