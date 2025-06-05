from textblob import TextBlob
import nltk
nltk.download('punkt')

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "😊 Positive"
    elif polarity < 0:
        return "😠 Negative"
    else:
        return "😐 Neutral"

if __name__ == "__main__":
    user_input = input("Enter a sentence to analyze: ")
    result = analyze_sentiment(user_input)
    print("Sentiment:", result)
