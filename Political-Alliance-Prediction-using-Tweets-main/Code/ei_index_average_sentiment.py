
#### EI index for whole network
#### Average sentiment for topic wise
#### Avergae Sentiment for each community for each topic

import pandas as pd
from sklearn.metrics import confusion_matrix
'''
df = pd.read_csv("farm_retweet_with_polVpol_ei.csv",encoding = "ISO-8859-1")

ds = df[['Source_Party', 'Target_Party', 'sentiment']]
#print(ds)
ds.to_csv('farm_retweet_with_polVpol_ei_2.csv',index=False)
'''
import csv
import numpy
reader = csv.reader(open("covid_retweet_polvpol_mapped.csv", "rt",encoding = "ISO-8859-1"), delimiter=",")
x = list(reader)
x = numpy.array(x)
r,c = x.shape

print(r)

################### EI_index Network ##############
internal = 0
external = 0
for i in range(r):
		if x[i][0] == x[i][1]:
			internal = internal + 1
		else:
			external = external + 1
print(internal,external)

ei_index = (external - internal)/(external + internal)
print(ei_index)

sen = 0
for i in range(r):
	sen = sen + float(x[i][2])
print("Sentiment:",sen/r)

c0 = c1 = c2 = 0

z = []
zz = []
for i in range(r):
	z.append(x[i][0])
	zz.append(x[i][2])
unique_words = set(z)
unique_words1 = set(zz)
xy = unique_words.union(unique_words1)
#zzz = list(unique_words)
#zzzz = list(unique_words1)
xy = list(xy)
print(xy)
########### Edge Matrix (sentiment) ############################
k=(confusion_matrix(z, zz,labels=xy))
print(k)
r,c = k.shape
value = 0
value1 = 0
################## Average Sentiment ###############
for i in range(r):
	for j in range(c):
		value1 += k[i][j] 
		if xy[j] == '0':
			value += (0*k[i][j])
		elif xy[j] == '1':
			value += (1*k[i][j])
		elif xy[j] == '2':
			value += (2*k[i][j])
	if value1 == 0:
		value2 = 0
	else:
		value2 = value/value1
	if xy[i] == '0' or xy[i] == '1' or xy[i] == '2':
		continue
	else: 
		print(xy[i],':',value2)
	value = 0
	value1 = 0
