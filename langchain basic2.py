
from langchain_ollama import ChatOllama

# Create a connection to the llama3.2 model
model = ChatOllama(
    model="tinyllama:latest"
)

# Create a conversation using different message roles
messages = [
    (
        "system",
        "You are a friendly Python teacher."
    ),
    (
        "human",
        "Explain Python variables with a simple example."
    )
]

response = model.invoke(messages)

print(response.content)
