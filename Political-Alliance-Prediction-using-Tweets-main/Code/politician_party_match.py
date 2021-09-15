import pandas as pd
import numpy as np

df = pd.read_csv("edge_farm_mention_with_polvpol.csv",encoding = "ISO-8859-1")
df['Source']=df['Source'].str.lower()
df['Target']=df['Target'].str.lower()
df1 = pd.read_csv("PartyPolUNIQUE.csv",encoding = "ISO-8859-1")
df.to_csv('edge_farm_mention_with_polvpol1.csv', index=False)

import csv
import numpy
reader = csv.reader(open("edge_farm_mention_with_polvpol1.csv", "rt",encoding = "ISO-8859-1"), delimiter=",")
x = list(reader)
x = numpy.array(x)
r,c = x.shape

reader1 = csv.reader(open("PartyPolUNIQUE.csv", "rt",encoding = "ISO-8859-1"), delimiter=",")
y = list(reader1)
y = numpy.array(y)
r1,c1 = y.shape
z = []
counter = 0
for i in range(r):
	l = x[i][0]
	for j in range(r1):
		if (x[i][0] == y[j][0]):
			k = y[j][0]
			m = y[j][1]
			n= l+","+m
			z.append(n)
			#print(l,k,m)
			break
		else:
			counter = counter + 1
			if counter==r1:
				o = l+","+"nan"
				z.append(o)
				counter = 0
	
print(z)
print(r,r1,len(z))


#df['Source'] = df['Source'].replace(['Blue'],'Green')

#df['Source'] = df['Source'].replace(['Blue'],'Green')

#df1['pricesMatch?'] = np.where(df['Source'] == df1['politician'], 'True', 'False')

'''    if ix < len(df)-1:
        if df.loc[ix, 'num'] == df.loc[ix+1, 'num']:
            df.loc[ix, 'matches?'] = True
        else:
            df.loc[ix, 'matches?'] = False
    else: #last observation
        df.loc[ix, 'matches?'] = False'''