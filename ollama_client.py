from ollama import Client
import json

client = Client(host='http://localhost:11434')
response = client.chat(model='llama3.2', messages=[
    {
        'role': 'user',
        'content': 'Porque o ceu é azul?',
    },
])

formatted_output = json.dumps(response, indent=5)

print(formatted_output)
