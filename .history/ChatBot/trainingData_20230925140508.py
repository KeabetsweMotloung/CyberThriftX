import json
from nlik_util.py import t

with open('ChatBot/Intents.json','r') as file:
    intents = json.load(file)

print(intents)