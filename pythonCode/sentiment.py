from transformers import pipeline
#import torch


#specify the model 

model_path="C:\\Users\\naveed.khan\\.cache\\huggingface\\hub\\models--gpt2"

# Load sentiment analysis pipeline

#sentiment_analysis = pipeline("sentiment-analysis")
sentiment_analysis = pipeline("sentiment-analysis", model=model_path, tokenizer=model_path)

# Analyze sentiment of a sentence
result = sentiment_analysis("I love using the transformers library!")
print(result)

#if __name_ == "__main__
#    main()
