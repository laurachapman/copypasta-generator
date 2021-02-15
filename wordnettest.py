import nltk

from nltk.corpus import wordnet as wn

myword = 'sofa'

synonyms = wn.synset(myword + '.n.01').lemma_names()

print("synonyms:", synonyms)