from read_corpus import *

def viterbi(sentence):
	dicOfWordTag,dicOfTag,dicOfTags=read_corpus("corpus/CoNLL2009-ST-English-train-pos.txt")
	tags=dicOfTag.keys()
	words=sentence.split()
	table=[{}]
	path={}
	# init
	for tag in tags:
		if dicOfWordTag.has_key((words[0],tag)) and dicOfTags.has_key(('BOS',tag)):
			table[0][tag]=tag1_tag2_prob('BOS',tag,dicOfTag, dicOfTags)*word_tag_prob(tag, words[0], dicOfWordTag, dicOfTag)
		else:
			table[0][tag]=0
		path[tag]=[tag]

	# Run Viterbi for t > 0
	for t in range(1,len(words)):
		table.append({})
		newpath={}

		for y in tags:
			if dicOfWordTag.has_key((words[t],y)):
				m=[0,'']
				for y0 in tags:
					if table[t-1][y0]>0 and dicOfTags.has_key((y0,y)):
						value=table[t-1][y0]*tag1_tag2_prob(y0,y,dicOfTag, dicOfTags)#dicOfTags[(y0,y)]
						if value>m[0]:
							m[0]=value
							m[1]=y0
					else:
						None
				if m[0]>0:
					table[t][y]=m[0]*word_tag_prob(y,words[t], dicOfWordTag, dicOfTag)#dicOfWordTag[(words[t],y)]
					newpath[y]=path[m[1]]+[y]
				else:
					table[t][y]=0

			else:
				table[t][y]=0

		path = newpath

	m=[0,'']
	for y in tags:
		#print table[t][y]
		if table[t][y]>m[0]:
			m[0]=table[t][y]
			m[1]=y
	prob=m[0]
	state=m[1]
	return (prob,path[state])

if __name__=='__main__':
	t=viterbi("That round table might collapse")
	print t[0],t[1]