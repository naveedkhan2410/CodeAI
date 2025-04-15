from transformers import pipeline

# Load summarization pipeline
summarizer = pipeline("summarization")

# Summarize the text
text = """Transformers are a type of deep learning model that have revolutionized the field of NLP. 
They work by processing input data in parallel, unlike previous architectures like RNNs and LSTMs."""
summary = summarizer(text, max_length=50, min_length=25, do_sample=False)

print(summary)
