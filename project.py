from ollama import chat

messages = [
    {
        "role": "system",
        "content": """
        You are a friendly AI teacher.
        Explain technical concepts to complete beginners.
        Use simple English.
        Give practical examples.
        Avoid unnecessary technical jargon.
        """
    },
    {
        "role": "user",
        "content": "What is deep learning?"
    }
]

response = chat(
    model="tinyllama:latest",
    messages=messages
)

print("\nAI:")
print(response["message"]["content"])