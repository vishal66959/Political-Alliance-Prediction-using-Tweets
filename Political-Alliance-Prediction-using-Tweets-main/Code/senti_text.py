#predictin the sentiment of a string

from textblob import TextBlob
import csv
import numpy

reader = csv.reader(open("farmbill_english_document_party.csv", "rt",encoding = "ISO-8859-1"), delimiter=",")
x = list(reader)
x = numpy.array(x)
r,c = x.shape
# Preparing an input sentence
for i in range(1,r):
	sentence = x[i][2]

	# Creating a textblob object and assigning the sentiment property
	analysis = TextBlob(sentence).sentiment
	print(analysis.polarity)