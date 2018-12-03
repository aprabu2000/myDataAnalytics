# infile = '/Users/prabahar/Desktop/Machine Learning Data sciences/s1.txt'
# # readline=open(infile,'r+').readlines()
# # print(readline)
# read1=open(infile,'r+').read()
# print (read1)
# # readline1=open(infile,'r+').readline()
# # print(readline1)
#
# file= open('/Users/prabahar/Desktop/Machine Learning Data sciences/s1.txt','r+').readlines()
# # print (file)
# # # print (type(file))
# # #
# fileFor = open('/Users/prabahar/Desktop/Machine Learning Data sciences/s1.txt')
# # print(fileFor)
# for line in fileFor:
#     print (line)
# fileFor.close()
#
# mylist1=["Arun","karthy",'prabu',"nandhu"]
# mylist1[2]='Prabu'
# print(mylist1)
# for line in mylist1:
#     print(line)
# while True:
#     line = mylist1
#     print(line)
#     if not line:
#         break
#         mylist1.close()

from textblob import TextBlob

import nltk
import numpy
import pandas
from nltk.corpus import stopwords
import re
# import counter


infile = '/Users/prabahar/Desktop/sample_data.rtf'
sentences = open(infile,'r+').readlines()
print('##########Sentences')
print(sentences)
# print(type(sentences))
stop=set (stopwords.words('english'))
print('##########Stopwords')
print (stopwords.words())

my_list = []
for s in sentences[:]:
    sa=TextBlob(s)
    value=sa.sentiment.polarity
    print('##########Sentiment')
    print(value)
    #Word_list
    wordList=s.split()
    print('##########Wordlist')
    print(wordList)
    print('##########Stopwords')
    # print([i for i in wordList if i not in stop])
    # print(for i in wordList if i not in stop)
    for word in wordList:
        word=word.lower()
        print('#########Lowerword')
        print(word)

        if word not in stop:
            word = re.sub('[^A-Za-z0-9]+','',word)
            my_list.append(word)
print('#########my_list after regex')
print(my_list)
# print('#########newList')
# print(newList)
# # wc=TextBlob(my_list)
# # wordCount=wc.word_counts
# # print('######Word_counts')
# # print(wordCount)


unique,counts = numpy.unique(my_list,return_counts=True)
d=dict(zip(unique,counts))
df= pandas.DataFrame.from_dict(d,orient='index')
df['Word']=df.index
df = df.rename(columns={0: 'Count'})
df=df[['Word','Count']]
df=df.sort_values('Count',ascending=False)
print('##########DF')
print(df)




