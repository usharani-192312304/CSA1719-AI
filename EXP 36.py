
from textblob import TextBlob

# Input text
text = input("Enter a sentence: ")

# Perform sentiment analysis
blob = TextBlob(text)
sentiment = blob.sentiment.polarity

# Display result
print("Sentiment Analysis Result")

if sentiment > 0:
    print("Sentiment: Positive")
elif sentiment < 0:
    print("Sentiment: Negative")
else:
    print("Sentiment: Neutral")

print("Polarity Score:", sentiment)
