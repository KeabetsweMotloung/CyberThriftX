import json
import n

with open('ChatBot/Intents.json','r') as file:
    intents = json.load(file)

print(intents)