# Import the Llama class
from llama_cpp import Llama


# Initialize the Llama model
llm = Llama(model_path=llama_path)

prompt = "Give me four short steps to troubleshoot my internet connection."

conv = [
	# Complete the user message
	{
        "role": "user",
	    "content": prompt
    }
]

# Pass the conversation to the model
result = llm.create_chat_completion(messages=conv, max_tokens=20)
print(result)



# Add a system message to the conversation list
conv = [
	{
        "role": "system",
        "content": "You are a helpful and professional customer support assistant for an internet service provider. If the question or instruction doesn't relate to internet service, quote the response: 'Sorry, I can't answer that.'"},
	{
        "role": "user",
	    "content": "Help me decide which stocks to invest in."
    }
]

result = llm.create_chat_completion(messages=conv, max_tokens=15)
# Extract the model response from the result object
assistant_content = result["choices"][0]["message"]["content"]
print(assistant_content)
