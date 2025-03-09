"""
Module to interact with the GPT-2 model from Hugging Face.
"""

from transformers import GPT2LMHeadModel, GPT2Tokenizer


def ask_gpt2(query: str) -> str:
    """
    Ask a question to the GPT-2 model and get a response.

    Args:
        query (str): The question to ask the GPT-2 model.

    Returns:
        str: The response from the GPT-2 model.
    """
    model_name = "openai-community/gpt2"
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPT2LMHeadModel.from_pretrained(model_name)

    inputs = tokenizer.encode(query, return_tensors="pt")
    outputs = model.generate(inputs, max_length=50, num_return_sequences=1)
    model_answer = str(tokenizer.decode(outputs[0], skip_special_tokens=True))
    return model_answer


if __name__ == "__main__":
    question = "How many eggs are there in a dozen eggs?"
    answer = ask_gpt2(question)
    print(answer)
