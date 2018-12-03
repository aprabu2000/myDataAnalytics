#from textblob import TextBlob

#b = TextBlob("Simple is better than complex.")

#b.sentiment

#TextBlob("not a very great calculation").sentiment


#print ("Hello myFirst")


from textblob import TextBlob

a = TextBlob(" very very awesome calculation")
b = TextBlob(" very very aweful calculation")

print(dir(a))

print ('##############word_counts')
print(a.word_counts)
print(b.word_counts)
print ('##############words')
print(a.words)
print(b.words)
print('##############sentiment_assessments')
print(a.sentiment_assessments)
print(b.sentiment_assessments)
print('##############sentiment')
print(a.sentiment)
print(b.sentiment)
#print('##############noun_phrases')
#print (a.noun_phrases)
#print('##############json')
#print(a.json)
print('##############classify')
print(a.classify)
print('##############classifier')
print(a.classifier)
print('##############analyzer')
print(a.analyzer)
print('##############detect_language')
print(a.detect_language)
print('##############parser')
print(a.parser)
print('##############parse')
print(a.parse)
print('##############sentences')
print(a.sentences)
# print('##############serialized')
#print(a.serialized)
# print('##############tags')
#print (a.tags)
print('##############title')
print(a.title)
print('##############to_json')
print(a.to_json)
print('##############tokenize')
print(a.tokenize)
print('##############tokens')
print(a.tokenizer)
print('##############')
print(a.tokens)
print('##############translate')
print(a.translate(to='es'))
print('##############upper')
print(a.upper)

