from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

def ask_llama(question):
    model_name = "huggingface/llama"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    inputs = tokenizer(question, return_tensors="pt")
    outputs = model.generate(**inputs)
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return answer

if __name__ == "__main__":
    question = "How many are there in a dozen?"
    answer = ask_llama(question)
    print(answer)