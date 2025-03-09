"""
Module to interact with the LLaMA model from Hugging Face.
"""

from transformers import AutoModelForCausalLM, AutoTokenizer

def ask_llama(query: str) -> str:
    """
    Ask a question to the LLaMA model and get a response.

    Args:
        query (str): The question to ask the LLaMA model.

    Returns:
        str: The response from the LLaMA model.
    """
    model_name = "huggingface/llama"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    inputs = tokenizer(query, return_tensors="pt")
    outputs = model.generate(**inputs)
    model_answer = str(tokenizer.decode(outputs[0], skip_special_tokens=True))
    return model_answer

if __name__ == "__main__":
    question = "How many are there in a dozen?"
    answer = ask_llama(question)
    print(answer)
