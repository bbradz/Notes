2023-06-15 @16:18

Status: #idea
Tags:  [[𝑪𝑺 📍]] [[Online Courses]]

##### Tokens
Because some words will be broken up by tokenization into multiple tokens, word units can break down unless properly handled and specified to the API.

##### Roles
- System: Sets behavior of assistant... Sets tone / behavior of assistant
- Assistant: Chat model.... LLM response
- User: You... does the prompting

```python
messages = {
	{'role': 'system', 'content': 'You are an assistant who responds to me'},
	{'role': 'user', 'content': 'write me a poem'}
}
```

##### Useful for:
- Classification into categories
- Moderation using OpenAI moderation [categories](https://platform.openai.com/docs/guides/moderation/overview)
	- Avoiding Prompt Injections

**Chain-of-Thought prompting**: Have the LLM separate its reasoning steps by a delimiter (####) and then use the delimiter to only display to the user that final output after the delimiters.

**Using multiple Prompts**: Sometimes it's better for the LLM to focus on one part of the task at once for quality to be maximized. It is also sometimes easier to break up a prompt into multiple steps.

##### Testing best Practices
- Evaluate on some queries
- Harder test cases
- Regression testing: verify that the model still works on previous test cases
- Gather development set for testing
- Compare to the ideal answers
- Run through the end-to-end system to answer the user query
- Evaluate answer on a rubric, based on the extracted product information
- Check for agreement or disagreement with an expert answer






