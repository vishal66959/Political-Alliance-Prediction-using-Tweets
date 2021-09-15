Political Alliance Prediction using Twitter Data

Drive link: (all the code, datasets, gephi files, output images are present)
https://drive.google.com/drive/folders/1-24xgwjI6lMP4cKL08SIF_cIsBUpC_YT?usp=sharing

Tools:
1) Python
2) Excel
3) Gephi

Python Library:
numpy, sklearn, csv, pandas, math, scipy, nltk, word2vec, textblob

Code:
1.codeHash.py 
	creating different csv file based on the hashtag which are related to COVID, FarmBill, and Indo-China.
2. filter_lower_multipleRow.py
	a) converts all the letter into the lowercase
	b) if two names are present in a single cell then convert into two rows (for example, a->b,c --- a->b and a->c).
	c) Also filter out data based on political vs political, political vs party and party vs party.
3. poltician_party_match.py
	replacing the politician with their party which is required to calculate the EI_index.
4. ei_index_average_sentiment.py 
	Computing EI_index for whole network
	Calculating average sentiment for topic wise (covid, farmbill, indo-china)
	computing average sentiment for each community like bjp, inc etc for each topic
5. eachCommunity_EI.py
	calculating the EI_index for each community.
6. document.py
	measuring the similarity between two documents.
		a) Cosine Similarity
		b) Jaccard Similarity
		c) Euclidean Distance
		d) Manhatten Distance
7. senti_text.py
	finding the sentiment of the tweet text using textblob.