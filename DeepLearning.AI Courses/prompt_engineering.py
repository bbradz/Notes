import openai
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key  = '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'

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

text = f"""
"""
prompt = f"""
```{text}```
"""
response = get_completion(prompt)
print(response)



