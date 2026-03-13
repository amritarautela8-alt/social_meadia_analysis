import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"C:\Users\hp\social_media\Tweets.csv")

print(df.head())

# Sentiment function
def analyze_sentiment(text):

    analysis = TextBlob(str(text))

    if analysis.sentiment.polarity > 0:
        return "Positive"

    elif analysis.sentiment.polarity == 0:
        return "Neutral"

    else:
        return "Negative"

# Apply sentiment analysis
df["Sentiment"] = df["text"].apply(analyze_sentiment)

print(df.head())

# Count sentiments
sentiment_count = df["Sentiment"].value_counts()

print(sentiment_count)

# Plot graph
plt.bar(sentiment_count.index, sentiment_count.values)

plt.title("Sentiment Analysis Result")
plt.xlabel("Sentiment")
plt.ylabel("Count")

import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"C:\Users\hp\social_media\Tweets.csv")

print(df.head())

# Sentiment function
def analyze_sentiment(text):

    analysis = TextBlob(str(text))

    if analysis.sentiment.polarity > 0:
        return "Positive"

    elif analysis.sentiment.polarity == 0:
        return "Neutral"

    else:
        return "Negative"

# Apply sentiment analysis
df["Sentiment"] = df["text"].apply(analyze_sentiment)

print(df.head())

# Count sentiments
sentiment_count = df["Sentiment"].value_counts()

print(sentiment_count)

# Plot graph
plt.bar(sentiment_count.index, sentiment_count.values)

plt.title("Sentiment Analysis Result")
plt.xlabel("Sentiment")
plt.ylabel("Count")

plt.show()