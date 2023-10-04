import openai
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key  = os.getenv('OPENAI_API_KEY')

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

input = """
I woke up so angry and I feel like it's going to be a shitty day
"""

prompt = f"""
What is the sentiment of the following text, 
which is delimited with triple backticks?

Review text: '''{input}'''
"""
response = get_completion(prompt)
print(response)