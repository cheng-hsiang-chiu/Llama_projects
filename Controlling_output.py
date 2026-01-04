# Import the Llama class
from llama_cpp import Llama



# Add formatting to the prompt
prompt="""
Instruction: Explain the concept of gravity in simple terms.
Question: What is gravity?
Answer:
"""

# Send the prompt to the model
output = llm(prompt, max_tokens=15, stop=["Question:"]) 
print(output['choices'][0]['text'])



# Complete the few-shot prompt
prompt="""Review 1: I ordered from this place last night, and I'm impressed! 
Sentiment 1: Positive,
Review 2: My order was delayed by over an hour without any updates. Disappointing!  
Sentiment 2: Negative,
Review 3: The food quality is top-notch. Highly recommend! 
Sentiment 3: Positive,
Review 4: Delicious food, and excellent customer service! 
Sentiment 4:"""

# Send the prompt to the model with a stop word
output = llm(prompt, max_tokens=2, stop=["Review"]) 
print(output['choices'][0]['text'])





#### Structured output
output = llm.create_chat_completion(
        messages=[
            {"role": "system", "content": "You convert inventory lists from text to JSON, extracting item counts and names from the text as keys and values in the form: item: count; for example, 'banana': 32.",},
            {"role": "user", "content": "Fifteen apples, thirty-three oranges, and five thousand fifty-two potatoes."},
        ],
		    # Specify output format to JSON
        response_format={
            "type": "json_object",
        }
)

print(output['choices'][0]['message']['content'])



output = llm.create_chat_completion(
    messages=messages,
    response_format={
        "type": "json_object",
        "schema": {
            "type": "object",
            # Set the properties of the JSON fields and their data types
            "properties": {"Question": {"type": "string"}, "Answer": {"type": "string"}}
        }
    }
)

print(output['choices'][0]['message']['content'])
