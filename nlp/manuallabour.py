from read_corpus import *

#dicOfWordTag,dicOfTag,dicOfTags=read_corpus("corpus/CoNLL2009-ST-English-train-pos.txt")
f = open("dictofwordtag.txt", 'r')
dicOfWordTag = eval(f.read())
f.close()

f= open('dictoftag.txt', 'r')
dicOfTag = eval(f.read())
f.close()

f= open('dictoftags.txt', 'r')
dicOfTags = eval(f.read())
f.close()


#print dicOfWordTag
def calc_base_result(tag1, tag2, word):
	t=tag1_tag2_prob(tag1, tag2, dicOfTag, dicOfTags)
	w=word_tag_prob(tag2, word, dicOfWordTag, dicOfTag)
	return t*w

def calc_result(tag, word, prevtaglist, prevresults, dicofwordtag, dicoftag, dicoftags):
	# calculate intermediates
	intermed = []
	for i in range(len(prevtaglist)):
		prevtag = prevtaglist[i]
		prevresult = prevresults[i]
		term = tag1_tag2_prob(prevtag, tag, dicoftag, dicoftags) * prevresult
		intermed.append(term)
	wordprob = word_tag_prob(tag, word, dicofwordtag, dicoftag)
	return max(intermed) * wordprob

results = [1.0]
# results.append(calc_base_result('BOS', 'DT', 'That'))
# results.append(calc_base_result('BOS', 'IN', 'That'))
# results.append(calc_base_result('BOS', 'WDT', 'That'))

# word = 'round'
# prevtags = ['DT', 'IN', 'WDT']
# tags = ['JJ', 'NN', 'VB', 'VBP' ]

trellislist = [
	('<s>',['BOS']),
	('That',['DT', 'IN', 'WDT']),
	('round',['JJ', 'NN', 'VB', 'VBP' ]),
	('table',['NN']),
	('might',['MD', 'NN']),
	('collapse', ['NN', 'NNP', 'VB'])
]

for i in range(1,len(trellislist)):
	pair = trellislist[i]
	word = pair[0]
	tags = pair[1]
	prevtags = trellislist[i-1][1]
	prevresults = results[-len(prevtags):]
	for tag in tags:
		results.append(calc_result(tag, word, prevtags, prevresults, dicOfWordTag, dicOfTag, dicOfTags))
	
for res in results: print res

f = open('manualresults.txt', 'w')
f.write(str(results))
f.close()


	
