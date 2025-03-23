import transformers
from transformers import pipeline
import torch

# Load pre-trained sentiment-analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

# Function to perform sentiment analysis
def analyze_sentiment(text):
    result = sentiment_pipeline(text)
    #return result
    return text

# Example usage
text = "I love sunny days!"
result = analyze_sentiment(text)
print("Sentiment Analysis Result:", result)
