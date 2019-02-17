'''

IMPORTING THE NEEDED LIBRARIES


'''

import nltk 



# OPENING THE FILE FOR GETTING THE INPUT TEXT
f = open('sample.txt' ,'r')
text = f.read()
f.close()

#print(text)


sentences = nltk.sent_tokenize(text)
print(sentences)


words= nltk.word_tokenize(text)
print(words)

words_with_pos = nltk.pos_tag(words)
print(words_with_pos)


word_dictionary = {}
NOUN_TAGS = [ 'NN' ,'NNS','NNP' ,'NNPS']

for word ,tag in words_with_pos:
    if tag in NOUN_TAGS :
        if word not in word_dictionary:
            word_dictionary[word] = 1
        else:
            word_dictionary[word] +=1
print(word_dictionary)

sorted_dict = sorted(word_dictionary, key =word_dictionary.get ,reverse=True)
print("Frequently occuring nouns")
print(sorted_dict[:5])


