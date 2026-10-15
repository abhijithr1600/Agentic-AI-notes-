
from ollama import chat

recipient = input("Recipient: ")
purpose = input("Purpose: ")
tone = input("Tone: ")
points = input("Important points: ")

prompt = f"""
Write a professional email.

Recipient:
{recipient}

Purpose:
{purpose}

Tone:
{tone}

Important points:
{points}

Requirements:
- Write a clear subject line.
- Keep sentences reasonably short.
- Be polite and professional.
- Do not invent information.
- Include a clear closing.
"""

response = chat(
    model="tinyllama:latest",
    messages=[
        {
            "role": "system",
            "content": "You are a professional email writing assistant."
        },
        {
            "role": "user",
            "content": prompt
        }
    ]
)
print(response)
3#print("\nGenerated Email\n")
##print(response["message"]["content"])
