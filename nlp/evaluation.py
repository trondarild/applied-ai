from viterbi import *
def evaluate(testFile):
	dicOfWordTag,dicOfTag,dicOfTags=read_corpus("corpus/CoNLL2009-ST-English-train-pos.txt")
	f=open(testFile,'r')
	rightNumber=0
	totalNumber=0
	words=[]
	right=[]
	for line in f:
		line=line.strip()
		if line=='':
			prob,path=viterbi(words,dicOfWordTag,dicOfTag,dicOfTags)
			if prob==0:
				words=[]
				right=[]
				continue
			i=0
			while i<len(path):
				if path[i]==right[i]:
					rightNumber+=1
				i+=1
			words=[]
			right=[]
		else:
			line=line.split()
			words.append(line[1])
			right.append(line[4])
			print 'deal with '+line[1]+'\t'+str(totalNumber)
			totalNumber+=1

	precision=float(rightNumber)/totalNumber
	return precision
if __name__ == '__main__':
	precision=evaluate('corpus/CoNLL2009-ST-English-train-pos.txt')
	print precision