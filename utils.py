import openai
from tenacity import retry, wait_random_exponential, stop_after_attempt


@retry(wait=wait_random_exponential(min=1, max=20), stop=stop_after_attempt(6))
def get_embedding(text, model):
    text = text.replace("\n", " ")
    response = openai.Embedding.create(input=[text], model=model)
    usage = response["usage"]
    print(f"""
    Input: {text}
    OpenAI API tokens usage:
    - Prompt tokens: {usage["prompt_tokens"]}
    - Total tokens: {usage["total_tokens"]}
    """)
    return response["data"][0]["embedding"]
