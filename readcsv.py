# read csv and make a mapping (dict) from keyword to unicode 
import csv
import emoji

count = 0
keyword_to_unicode = dict()
all_keywords = []

# create emoji dictionary
with open('emojis.csv', newline='') as csvfile:
	reader = csv.reader(csvfile, delimiter=' ')
	for row in reader:
		print(row)

		keyword = row[3].replace('-', '_')
		uni = row[1]

		keyword_to_unicode[keyword] = "\\" + "U000" + uni
		all_keywords.append(keyword)

		count += 1
		if count > 10:
			break

print("keyword_to_unicode:", keyword_to_unicode)
print("keywords:", all_keywords)

# read in sample text
uni = keyword_to_unicode['relieved']
keyword = all_keywords[2]

print(emoji.emojize(":heart_eyes:")) 

print("emoji:", uni)