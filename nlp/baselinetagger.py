
from utils import *
'''
function baseline_tagger(sentence, wordtag_frequency_dictionary) 
return list of tags for words, using only frequency of words from corpus (dictionary) - Trond
sentence - the sentence to get tags for 
wordtag_freq_dict - 
'''
def baseline_tagger(sentence, wordtag_freq_dict):
	# a list to contain tags for each of the words in the given sentence
	retval = []

	sentencelst = sentence.split(' ')
	# for each word look it up in the dictionary, get the tags and frequency for those tags
	# and choose the one with highest frequency
	for word in sentencelst:
		# get all word-tag pairs
		wordtaglist = [(tag, freq) for (wrd, tag), freq in wordtag_freq_dict.items() if wrd==word]
		hifreqtag = argmax(wordtaglist, lambda x: x[1])[0]
		retval.append(hifreqtag)

	return retval


#
# test
#
if __name__=='__main__':
	test_dict = {
		('that', 'dt') : 438,
		('that', 'in') : 5,
		('that', 'wdt') : 3,
		('round', 'jj') : 5,
		('round', 'nn') : 23,
		('round', 'vb') : 2,
		('round', 'vbp') : 1,
		('table', 'nn') : 35,
		('might', 'md') : 328,
		('might', 'nn') : 4,
		('collapse', 'nn') : 57,
		('collapse', 'nnp') : 1,
		('collapse', 'vb') : 5}

	sentence = 'that round table might collapse'
	print baseline_tagger(sentence, test_dict)