from collections import deque
from copy import deepcopy
#
# do exhaustive search of trellis table for a given sentence/tags list, 
# and corresponding result list
#

def processlist(reclist, sentenceprobpair):
	# take the first in the list
	currentlist = reclist.popleft()
	retval = []
	if not reclist:
		for (tag, prob) in currentlist:
			newsentence = deepcopy(sentenceprobpair[0])
			newsentence.append(tag)
			retval.append((newsentence, prob*sentenceprobpair[1]))
	else:
		for (tag, prob) in currentlist:
			newsentence = deepcopy(sentenceprobpair[0])
			newsentence.append(tag)
			retval += processlist(deepcopy(reclist), (newsentence, prob*sentenceprobpair[1]))

	return retval

# sentencetaglist - [('<s>', [('BOS', 1.0)]), [('DT', 0.0011), ('IN', 6.440e-06), ('WDT', ...)]),...]
def exhaustive_search(sentencetaglist):
	# calculate all permutations of path through sentence, and return
	# list with pair of tags, probability
	retval = []
	sentenceprobpairs = sentencetaglist.popleft()
	for pair in sentenceprobpairs:
		retval += processlist(sentencetaglist, ([pair[0]], pair[1]))
	return retval 


# read resultlist
f = open('manualresults.txt')
results = eval(f.read())

trellislist = [
	('<s>',['BOS']),
	('That',['DT', 'IN', 'WDT']),
	('round',['JJ', 'NN', 'VB', 'VBP' ]),
	('table',['NN']),
	('might',['MD', 'NN']),
	('collapse', ['NN', 'NNP', 'VB'])
]

# combine the two
sentencetaglist = deque()
resultcnt = 0
for pair in trellislist:
	tagproblist = []
	tags = pair[1]
	for tag in tags:
		# join probs and tags
		tagproblist.append((tag, results[resultcnt]))
		resultcnt+=1
	sentencetaglist.append(tagproblist)
#print sentencetaglist

paths = exhaustive_search(sentencetaglist)
#print paths

paths = sorted(paths, key = lambda pair: -pair[1] )
print len(paths)
for path in paths: 
	print path
