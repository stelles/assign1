from nltk import *
from nltk.corpus import PlaintextCorpusReader


words = PlaintextCorpusReader('./', "sample.txt")

word_list = words.words()

print "Number of total tokens: %d" % len(word_list)
print "Number of distinct tokens: %d" % len(set(word_list))

freq_word_list = {}

for word in word_list:
	if word in freq_word_list:
		freq_word_list[word] = freq_word_list[word] + 1
	else:
		freq_word_list[word] = 1


sorted_list = []

for i in freq_word_list:
	if i.isalpha():
		sorted_list.append((i, freq_word_list.get(i)))

single_words = 0
sorted_list.sort(key=lambda x: x[1])
for i in sorted_list:
	if i[1] == 1:
		single_words += 1
	print i 

print "Number of distinct words : %d" % len(sorted_list)
print "Number of single words : %d" % single_words
percent_of_single_words = float(single_words)/float(len(sorted_list))
print "Percentage of singlying used words : %f" % percent_of_single_words



