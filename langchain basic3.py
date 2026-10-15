
from langchain_ollama import ChatOllama

model = ChatOllama(
    model="tinyllama:latest"
)

# invoke() sends the input to the model and asks it to generate a response.
response = model.invoke(
    "What is artificial intelligence?"
)
print(response)
##print(response.content)
