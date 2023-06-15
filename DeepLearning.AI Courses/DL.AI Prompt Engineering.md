2023-06-15 @10:06

Status: #idea
Tags: [[𝑪𝑺 📍]] [[Online Courses]]

```python
import os
import openai
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key  = os.getenv('OPENAI_API_KEY')

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, 
    )
    return response.choices[0].message["content"]

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message["content"]

response = get_completion_from_messages(messages, temperature=1)
print(response)

response = get_completion(prompt)
print(response)


```

### Principles of Prompting

##### 1. Write clear and specific instructions
- Tactic 1: Use Delimiters
	- Triple Quotes """
	- Triple Backticks 
	- Triple Dashes ---
	- Angle Brackets < >
	- XML tags
- Tactic 2: Ask for structured output (HTML, JSON)
- Tactic 3: Check whether conditions are satisfied. Check assumptions required to do the task
- Tactic 4: Few-shot prompting (Providing successful examples of what you want the prompt to do)

##### 2. Give the Model time to think
- Tactic 1: Specify the steps required to complete a task + Ask for output in a specified format
- Tactic 2: Instruct the model to work out its own solution before rushing to a conclusion

##### Model Limitations: Hallucinations
- Will make statement that sound plausible but are not true
- Reducing Hallucinations:
	- 1st find relevant information,
	- then answer the question based on the relevant information

### Iterative Prompt Development

- Try something
- Analyze where the result does not give what you want
- Clarify instructions, give more time to think
- Refine prompts with a batch of examples

- **Issue 1**: The Text is too Long -> Limit # of words/sentences/characters
- **Issue 2**: Text focuses on wrong details -> Ask it to focus on aspects relevant to the target audience
- **Issue 3**: Description needs a table of dimensions -> - Ask it to extract information and organize it in a table.

##### Load Python libraries to view HTML
```python
from IPython.display import display, HTML
display(HTML(response))
```

### Summarizing

- w/ a word/sentence/character limit
- w/ a focus on shipping and delivery
- w/ a focus on price and value
- Try "extract" instead of "summarize"

### Inferring

- Sentiment (positive/negative)
- Identify types of emotions
- Extract product and company name from customer reviews
- Doing multiple tasks at once
- Inferring topics
- Make a news alert for certain topics

### Transforming 
Language translation, spelling and grammar checking, tone adjustment, and format conversion.

- Translation
- Tone transformation
- Formate conversion
- Spellcheck/Grammar check

### Expanding

- Customize the automated reply to a customer email
- Remind the model to use details from the customer's email



