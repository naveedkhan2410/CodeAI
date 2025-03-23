from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Step 1: Load the pre-trained GPT-2 model and tokenizer
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Step 2: Create a small dataset of documents (you can replace it with your own data)
# For simplicity, we will use a few example paragraphs
dataset = [
    "The Eiffel Tower is a famous landmark in Paris, France. It was built in 1887 and stands 324 meters tall.", "Paris is the capital of France",
    "The capital of the United States is Washington, D.C. It is known for its historical monuments, including the Lincoln Memorial.",
    "The Great Wall of China is a massive structure built to protect China from invaders. It stretches over 13,000 miles."
]

# Step 3: Simple retrieval of relevant documents (for demonstration, we just pick the top document based on a query)
def retrieve_documents(query):
    # For simplicity, we just return the first document that matches a keyword from the query
    for doc in dataset:
        if query.lower() in doc.lower():
            return doc
    return dataset[0]  # If no match is found, return the first document

# Step 4: Generate a response based on the query and the retrieved document
def generate_response(query):
    # Step 4.1: Retrieve relevant document (this would usually be more sophisticated, like using FAISS or other methods)
    retrieved_doc = retrieve_documents(query)

    # Step 4.2: Create a prompt by combining the retrieved document with the query
    prompt = f"Query: {query}\nContext: {retrieved_doc}\nAnswer:"

    # Step 4.3: Tokenize the prompt and generate a response using the GPT-2 model
    inputs = tokenizer.encode(prompt, return_tensors="pt", max_length=512, truncation=True)
    outputs = model.generate(inputs, max_length=100, num_return_sequences=1, no_repeat_ngram_size=2)
    #input_ids = inputs['input_ids']
    #attention_mask = inputs['attention_mask']

    #print("Attention Mask:", attention_mask)
    #print("Pad Token ID:", tokenizer.pad_token_id)
    #outputs = model.generate(input_ids, attention_mask=attention_mask, max_length=100, num_return_sequences=1, no_repeat_ngram_size=2)

    # Decode and print the response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

# Step 5: Test the RAG system
query = "What is the capital of France?"
response = generate_response(query)
print("Query:", query)
print("Response:", response)
