import ollama

response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": "Quais as principais capitais do Brasil?",
        },
    ],
)
print(response["message"]["content"])
