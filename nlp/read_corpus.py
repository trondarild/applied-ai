
def tag1_tag2_prob(tag1, tag2,dicOfTag, dicOfTags):
	if dicOfTag.has_key(tag1):
		denominator=dicOfTag[tag1]
	else:
		denominator=0
		print "no answer"
		return
	if dicOfTags.has_key((tag1,tag2)):
		numerator=dicOfTags[(tag1,tag2)]
	else:
		numerator=0
	return float(numerator)/denominator

def word_tag_prob(tag, word, dicOfWordTag, dicOfTag):
	if dicOfWordTag.has_key((word,tag)):
		numerator=dicOfWordTag[(word,tag)]
	else:
		numerator=0
	if dicOfTag.has_key(tag):
		denominator=dicOfTag[tag]
	else:
		denominator=0
		print "no answer"
		return
	return float(numerator)/denominator

def read_corpus(fileName):
	dicOfWordTag=dict()
	dicOfTag=dict()
	dicOfTags=dict()
	f=open(fileName,"r")
	prevTag='BOS'
	dicOfTag['BOS']=1
	for line in f:
		line=line.strip()
		if line=='':
			prevTag='BOS'
			dicOfTag['BOS']+=1
		else:
			line=line.split()
			word=line[1].strip()
			tag=line[4].strip()
			wordtag=(word,tag)
			if dicOfWordTag.has_key(wordtag):
				dicOfWordTag[wordtag]+=1
			else:
				dicOfWordTag[wordtag]=1
			if dicOfTag.has_key(tag):
				dicOfTag[tag]+=1
			else:
				dicOfTag[tag]=1
			if prevTag:
				tags=(prevTag,tag)
				if dicOfTags.has_key(tags):
					dicOfTags[tags]+=1
				else:
					dicOfTags[tags]=1
			prevTag=tag

	return dicOfWordTag,dicOfTag,dicOfTags

if __name__ == '__main__':
	dicOfWordTag,dicOfTag,dicOfTags=read_corpus("corpus/CoNLL2009-ST-English-train-pos.txt")
	t=tag1_tag2_prob('BOS', 'DT', dicOfTag, dicOfTags)
	w=word_tag_prob('DT', 'That', dicOfWordTag, dicOfTag)
	print t*w