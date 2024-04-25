from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

text = 'Today is a beautiful day. Tomorrow looks like bad weather.'

blob = TextBlob(text)
try:
    print("Blob lang:")
    print(blob.detect_language())
except Exception as e:
    print("Could not detect language due to the following error:")
    print(str(e))
    
print("Sentences:")
print(blob.sentences)
print("=" * 30)
print("Words:")
print(blob.words)
print("=" * 30)
print("Tags: ")
print(blob.tags)
print("Sentiment property:")
print(f"{blob.sentiment}")
print("scale of -1 to 1 (-1 being negative)")
print("=" * 30)
print("Polarity and subjectivity")
sent_blob = blob.sentiment 
print(sent_blob.polarity)
print(sent_blob.subjectivity)




print("=" * 30)
print("For loop through blob:")
# loop to get sentences in a blob 
for sentence in blob.sentences:
    print(sentence.sentiment)

print("=" * 30)
print("blob with analyzer set to nativebayes")
blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())
print(blob)
print(blob.sentiment)


print("=" * 30)
print("sentiment for each sentence")
for sentence in blob.sentences:
    print(sentence.sentiment)


print("=" * 30)
exercise_blob = TextBlob('This is a TextBlob')
print(exercise_blob)


print("=" * 30)
tst_blob = TextBlob('The red brick factory is for sale.').noun_phrases
# only printing noun phrases with the .noun_phrases modifier 
print(tst_blob)
