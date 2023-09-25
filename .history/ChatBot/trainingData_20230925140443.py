import json
import nlik_utilsp

with open('ChatBot/Intents.json','r') as file:
    intents = json.load(file)

print(intents)