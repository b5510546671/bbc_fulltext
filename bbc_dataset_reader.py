import os
import nltk
import re

def preprocess(line):

	stop_words = nltk.corpus.stopwords.words('english')
	
	preprocessed_line_list = []
	for w in line.split():
		if w.lower() not in stop_words and len(w) > 1:
			# w = re.sub('[^a-zA-Z]', '', w)
			# preprocessed_line_list.append(stemmer.stem(w).lower())
			
			preprocessed_line_list.append((re.sub('[^a-zA-Z]', '', w)).lower())
	preprocess_line = " ".join(preprocessed_line_list)

	return preprocess_line

bbc_headlines = open("bbc-dataset-headlines.txt", 'w')

for dirname in ['business', 'entertainment', 'politics', 'sport', 'tech']:
	for filename in os.listdir(dirname):
		f = open("dataset/"+dirname+"/"+filename)

		lines = f.readlines()

		if lines[0].endswith("\n"):
			line = lines[0][:-1]
		else:
			line = lines[0]

		try:
			# PREPROCESS DATA
			# line = unicodedata.normalize('NFKD', preprocess(line)).encode('ascii', 'ignore')
			line = preprocess(line)
		except:
			pass

		print line

		line += (" " + dirname)
		print ">>>>>" + line
		if len(line) > 3:
			bbc_headlines.write(line + "\n")

		f.close()
