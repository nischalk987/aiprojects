from textblob import TextBlob

with open('combination.txt', 'r') as f:
    text = f.read()

blob = TextBlob(text)
sentiment = blob.sentiment.polarity # -1 to 1
print(sentiment)
