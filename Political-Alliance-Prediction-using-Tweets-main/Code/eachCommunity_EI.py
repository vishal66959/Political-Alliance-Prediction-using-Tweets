
#### EI index for each community

import csv
import numpy
from sklearn.metrics import confusion_matrix
reader = csv.reader(open("covid_retweet_polvpol_mapped.csv", "rt",encoding = "ISO-8859-1"), delimiter=",")
x = list(reader)
x = numpy.array(x)
r,c = x.shape


z = []
zz = []
zzz = []
for i in range(r):
	z.append(x[i][0])
	zz.append(x[i][1])

unique_words = set(z)
unique_words1 = set(zz)
unique_words.union(unique_words1)
zzz = list(unique_words)
print(zzz)
############### Edge Matrix (Source, Target) ############
k=(confusion_matrix(z, zz,labels=zzz))
print(k)
r,c = k.shape
internal = external = ei_index = 0

########### EI_index Community ########################
for i in range(r):
	for j in range(c):
		if i==j:
			internal = k[i][j]
		else:
			external += k[i][j]
	if external + internal == 0:
		ei_index = 0
	else:
		ei_index = (external - internal)/(internal + external)
	internal = external = 0
	print(zzz[i],':', ei_index)