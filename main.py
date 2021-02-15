import emoji
import nltk
import random

from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords

file = open("emoji-test.txt", "r")

count = 0

keywords = []
word_to_description = dict()

stopwords = stopwords.words('english')

for line in file:
	if "qualified" in line and ";" in line and "E0.6" in line:
		words = line.split("E0.6 ")

		keyword_without_newline = words[1][0:-1]
		remove_colon = keyword_without_newline.replace(':', "")
		replace_space = remove_colon.replace(' ', '_')

		all_words = keyword_without_newline.split(' ')
		for word in all_words:
			if word not in stopwords:

				syns = wn.synsets(word)
				parts_of_speech = list(set([x.pos() for x in syns]))

				for pos in parts_of_speech:
					try:
						wordsyns = wn.synset(word + '.' + pos + '.01').lemma_names()
						for w in wordsyns:
							if w not in word_to_description:
								word_to_description[w] = {replace_space}
							else:
								word_to_description[w].add(replace_space)							
					except:
						pass

				word = word.lower()
				word = word.replace('"', "")

				if word not in word_to_description:
					word_to_description[word] = {replace_space}
				else:
					word_to_description[word].add(replace_space)

				count += 1

		keywords.append(replace_space)

file.close()

def print_emoji(keyword):
	print(emoji.emojize(":" + keyword + ":"), end=" ")


def print_all_emojis(keyword):
	for item in list(word_to_description[keyword]):
		print_emoji(item)

text_file = open("sample_text.txt", "r")

for line in text_file:
	words = line.split(" ")
	for word in words:

		if word in stopwords or word.lower() in stopwords:
			print(word, end=" ")

		elif word in word_to_description.keys():
			print(word, end="")
			print_all_emojis(word)

		else:
			print(word, end=" ")

print()

text_file.close()