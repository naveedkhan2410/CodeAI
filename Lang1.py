from transformers import GPT2LMHeadModel, GPT2Tokenizer, BartForConditionalGeneration, BartTokenizer
import torch

def connect_to_llm():
    # Load pre-trained GPT-2 model and tokenizer from Hugging Face
    model_name = "facebook/bart-large-cnn"  # You can change this to another open-source model
    #tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    tokenizer = BartTokenizer.from_pretrained(model_name)
    #model = GPT2LMHeadModel.from_pretrained(model_name)
    model = BartForConditionalGeneration.from_pretrained(model_name)
    

    # Set the model to evaluation mode (disable dropout layers)
    model.eval()

    # Prompt to feed the model
    prompt = "Aligarh Muslim University"

    # Tokenize the prompt text
    #inputs = tokenizer.encode(prompt, return_tensors="pt")
    inputs = tokenizer.encode(prompt, return_tensors="pt",truncation=True, max_length=1024)

    # Generate text with the model
    #with torch.no_grad():
     #   outputs = model.generate(inputs, max_length=100, num_return_sequences=1, no_repeat_ngram_size=2)
    with torch.no_grad():
        outputs = model.generate(inputs, max_length=150, num_beams=4, early_stopping=True)
        

    print (outputs)
    # Decode and print the generated text
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print("Generated Text:")
    print(generated_text)

if __name__ == "__main__":

    print (" The control start here ")
    connect_to_llm()

