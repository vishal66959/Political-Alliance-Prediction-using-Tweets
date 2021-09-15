#import pandas as pd

'''df = pd.read_csv("farmbilldocuments.csv",encoding = "ISO-8859-1")

df = df[df.lang.str.contains("en")]
df['author_screen_name']=df['author_screen_name'].str.lower()
df['tweet_text']=df['tweet_text'].str.lower()
df = df[['author_screen_name','tweet_text']]
df.to_csv('farmbill_english_document_lower.csv',index = False)'''

import csv
import numpy
from sklearn.metrics import confusion_matrix
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from scipy.spatial import distance
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import euclidean_distances
import math
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.metrics.pairwise import manhattan_distances
from sklearn.metrics import jaccard_similarity_score
#covid_English_PartyAuthorTweet
#farmbill_english_document_party
reader = csv.reader(open("farmbill_english_document_party.csv", "rt",encoding = "ISO-8859-1"), delimiter=",")
x = list(reader)
x = numpy.array(x)
r,c = x.shape
bjp = []
inc = []
akali = []
rjd = []
cpimspeaks = []
jmmjharkhand = []
goaforwardparty = [] 
aamaadmiparty = []
aitcofficial = []
samajwadiparty = []
for i in range(1,r):
	if(x[i][0] == 'bjp4india'):
		bjp.append(x[i][2])
	if(x[i][0] == 'incindia'):
		inc.append(x[i][2])
	if(x[i][0] == 'akali_dal_'):
		akali.append(x[i][2])
	if(x[i][0] == 'rjdforindia'):
		rjd.append(x[i][2])
	if(x[i][0] == 'cpimspeaks'):
		cpimspeaks.append(x[i][2])
	if(x[i][0] == 'jmmjharkhand'):
		jmmjharkhand.append(x[i][2])
	if(x[i][0] == 'goaforwardparty'):
		goaforwardparty.append(x[i][2])
	if(x[i][0] == 'aamaadmiparty'):
		aamaadmiparty.append(x[i][2])
	if(x[i][0] == 'aitcofficial'):
		aitcofficial.append(x[i][2])
	if(x[i][0] == 'samajwadiparty'):
		samajwadiparty.append(x[i][2])
#print(len(inc), len(bjp))
# Python program to convert a list
# to string using list comprehension
#cpimspeaks , jmmjharkhand , goaforwardparty , aamaadmiparty , officeofrsp , jduonline , rlpindiaorg , arivalayam
#aitcofficial , samajwadiparty , ysrcparty , aimim_national , cpimspeak

def jaccard_similarity(list1, list2):
    intersection = len(list(set(list1).intersection(list2)))
    union = (len(list1) + len(list2)) - intersection
    return float(intersection) / union


# using list comprehension
bjp = ' '.join(map(str, bjp))
inc = ' '.join(map(str, inc))
aamaadmiparty = ' '.join(map(str, aamaadmiparty))
goaforwardparty = ' '.join(map(str, goaforwardparty))
rjd = ' '.join(map(str, rjd))

X_list = word_tokenize(inc) 
Y_list = word_tokenize(rjd)

sw = stopwords.words('english') 
l1 =[];l2 =[]
  
# remove stop words from the string
X_set = {w for w in X_list if not w in sw} 
Y_set = {w for w in Y_list if not w in sw}

# form a set containing keywords of both strings 
rvector = X_set.union(Y_set) 
for w in rvector:
    if w in X_set: l1.append(1) # create a vector
    else: l1.append(0)
    if w in Y_set: l2.append(1)
    else: l2.append(0)
c = 0

# cosine formula 
for i in range(len(rvector)):
        c+= l1[i]*l2[i]
cosine = c / float((sum(l1)*sum(l2))**0.5)
print("Cosine_similarity: ", cosine)
sim = jaccard_similarity(X_set,Y_set)
print("Jaccard_sim: ", sim)

#eucledian Distance
t = numpy.array(l1).reshape(1,-1)
n = numpy.array(l2).reshape(1,-1)
x=euclidean_distances(t, n)[0][0]
print("Eucledian Distance:",x)

y=manhattan_distances(t,n)[0][0]
print("Manhattan Distance:",y)
