import json
import nlik_util.py fr

with open('ChatBot/Intents.json','r') as file:
    intents = json.load(file)

print(intents)