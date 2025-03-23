import torch
#import sentencepiece
from transformers import AutoModelForCausalLM, AutoTokenizer, GPT2Tokenizer, GPT2LMHeadModel, LlamaTokenizer, LlamaForCausalLM, LlamaModel

# Use GPT-2 model
MODEL_NAME = "gpt2"
MODEL_NAME ="meta-llama/Llama-2-7b-hf"
MODEL_NAME = "bert-base-uncased"


# Load the tokenizer and model
print("Downloading and loading GPT-2 model...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

#tokenizer= GPT2Tokenizer.from_pretrained(MODEL_NAME)
#model=GPT2LMHeadModel.from_pretrained(MODEL_NAME)

#tokenizer = LlamaTokenizer.from_pretrained(MODEL_NAME)
#model = LlamaForCausalLM.from_pretrained(MODEL_NAME)

# Detect if running on Apple Silicon (M1/M2/M3) and use Metal for acceleration
#device = "mps" if torch.backends.mps.is_available() else "cpu"
#model.to(device)

def generate_story(prompt, max_length=200):
    #inputs = tokenizer(prompt, return_tensors="pt").to(device)
    inputs = tokenizer(prompt, return_tensors="pt")
    with torch.no_grad():
        output = model.generate(**inputs, max_length=max_length, temperature=0.7, top_k=50, top_p=0.9)
    return tokenizer.decode(output[0], skip_special_tokens=True)

# Get user input for the story prompt
prompt = input("Enter a story prompt: ")

# Generate and print the story
story = generate_story(prompt)
print("\nGenerated Story:\n")
print(story)
