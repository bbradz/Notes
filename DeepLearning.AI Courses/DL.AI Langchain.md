2023-06-15 @17:05

Status: #idea
Tags: [[𝑪𝑺 📍]] [[Online Courses]]

### Model prompts and parsing Code examples:

```python
# Using langchain

pip install --upgrade langchain

from langchain.chat_models from ChatOpenAI
from langchain.prompts import ChatPromptTemplate

chat = ChatOpenAI(temperature=0.0)
```

```python
# Prompt Template

template_string = """Translate the text \
that is delimited by triple backticks \
into a style that is {style}. \
text: ```{text}```
"""
prompt_template = ChatPromptTemplate.from_template(template_string)

customer_style = """American English \
in a calm and respectful tone
"""

customer_email = """
Arrr, I be fuming that me blender lid \
flew off and splattered me kitchen walls \
with smoothie! And to make matters worse, \
the warranty don't cover the cost of \
cleaning up me kitchen. I need yer help \
right now, matey!
"""

customer_messages = prompt_template.format_messages(
                    style=customer_style,
                    text=customer_email)
```

```python
# Parse the LLM output string into a Python dictionary

from langchain.output_parsers import ResponseSchema
from langchain.output_parsers import StructuredOutputParser

gift_schema = ResponseSchema(name="gift",
                             description="Was the item purchased\
                             as a gift for someone else? \
                             Answer True if yes,\
                             False if not or unknown.")
delivery_days_schema = ResponseSchema(name="delivery_days",
                                      description="How many days\
                                      did it take for the product\
                                      to arrive? If this \
                                      information is not found,\
                                      output -1.")
price_value_schema = ResponseSchema(name="price_value",
                                    description="Extract any\
                                    sentences about the value or \
                                    price, and output them as a \
                                    comma separated Python list.")

response_schemas = [gift_schema, 
                    delivery_days_schema,
                    price_value_schema]

output_parser = StructuredOutputParser.from_response_schemas
format_instructions = output_parser.get_format_instructions()

review_template_2 = """\
For the following text, extract the following information:

gift: Was the item purchased as a gift for someone else? \
Answer True if yes, False if not or unknown.

delivery_days: How many days did it take for the product\
to arrive? If this information is not found, output -1.

price_value: Extract any sentences about the value or price,\
and output them as a comma separated Python list.

text: {text}

{format_instructions}
"""

prompt = ChatPromptTemplate.from_template(template=review_template_2)

messages = prompt.format_messages(text=customer_review, 
                                format_instructions=format_instructions)
response = chat(messages)
output_dict = output_parser.parse(response.content)
output_dict.get('delivery_days')

```


### Memory options:
- ConversationBufferMemory (shown) : Storing messages and extracting the messages in a variable.
- ConversationBufferWindowMemory : List interactions of the conversations over time only using the last K interactions.
- ConversationTokenBufferMemory : Keep buffer of recent interaction using token length rather than number of interactions to decide when to flush interactions.
- ConversationSummaryMemory : Summarize the conversation over time.

```python
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

llm = ChatOpenAI(temperature=0.0)
memory = ConversationBufferMemory()
conversation = ConversationChain(
    llm=llm, 
    memory = memory,
    verbose=True
)

# Input
conversation.predict(input="Hi, my name is Andrew")

# Add to memory
memory.save_context({"input": "AI is what?!"},
                    {"output": "Amazing!"})

# Output memory
memory.load_memory_variables({})

```

##### Additional Memory Types:
- Vector : store the text in a vector database and retrieve the most relevant blocks of text
- Entity memories : use an LLM to remember details about specific entities

### Chain types: 

##### Simple Sequential Chains
![[Screenshot 2023-06-15 at 5.31.19 PM.png| 500]]
#####  Sequential Chain
![[Screenshot 2023-06-15 at 5.32.00 PM.png| 500]]
#####  Router Chain
![[Screenshot 2023-06-15 at 5.32.30 PM.png| 500]]

##### Code Example:
```python
import warnings
import os
from dotenv import load_dotenv, find_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
import pandas as pd

warnings.filterwarnings('ignore')
_ = load_dotenv(find_dotenv())
df = pd.read_csv('Data.csv')
df.head()
llm = ChatOpenAI(temperature=0.9)


# prompt template 1: translate to english
first_prompt = ChatPromptTemplate.from_template(
    "Translate the following review to english:"
    "\n\n{Review}")
# chain 1: input= Review and output= English_Review
chain_one = LLMChain(llm=llm, prompt=first_prompt, 
                     output_key="English_Review")

second_prompt = ChatPromptTemplate.from_template(
    "Can you summarize the following review in 1 sentence:"
    "\n\n{English_Review}")
# chain 2: input= English_Review and output= summary
chain_two = LLMChain(llm=llm, prompt=second_prompt, 
                     output_key="summary")

# prompt template 3: translate to english
third_prompt = ChatPromptTemplate.from_template(
    "What language is the following review:\n\n{Review}")
# chain 3: input= Review and output= language
chain_three = LLMChain(llm=llm, prompt=third_prompt,
                       output_key="language")

# prompt template 4: follow up message
fourth_prompt = ChatPromptTemplate.from_template(
    "Write a follow up response to the following "
    "summary in the specified language:"
    "\n\nSummary: {summary}\n\nLanguage: {language}")
# chain 4: input= summary, language and output= followup_message
chain_four = LLMChain(llm=llm, prompt=fourth_prompt,
                      output_key="followup_message")

# overall_chain: input= Review 
# and output= English_Review,summary, followup_message
overall_chain = SequentialChain(
    chains=[chain_one, chain_two, chain_three, chain_four],
    input_variables=["Review"],
    output_variables=["English_Review", "summary","followup_message"],
    verbose=True)
review = df.Review[5]
overall_chain(review)


product = "Queen Size Sheet Set"
chain.run(product)

# prompt template 1
first_prompt = ChatPromptTemplate.from_template(
    "What is the best name to describe \
    a company that makes {product}?"
)

# Chain 1
chain_one = LLMChain(llm=llm, prompt=first_prompt)

# prompt template 2
second_prompt = ChatPromptTemplate.from_template(
    "Write a 20 words description for the following \
    company:{company_name}"
)
# chain 2
chain_two = LLMChain(llm=llm, prompt=second_prompt)

overall_simple_chain = SimpleSequentialChain(chains=[chain_one, chain_two],
                                             verbose=True)
overall_simple_chain.run(product)
```