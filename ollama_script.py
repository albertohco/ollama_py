import ollama
import json

# Supondo que `ollama.list()` retorne o dicionário JSON
output1 = ollama.ps()
output2 = ollama.list()

# Exibir o JSON formatado
formatted_output1 = json.dumps(output1, indent=5)
formatted_output2 = json.dumps(output2, indent=5)
print(formatted_output1)
print(formatted_output2)
