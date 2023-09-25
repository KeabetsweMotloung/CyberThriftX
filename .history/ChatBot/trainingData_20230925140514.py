import json
from nlik_util.py import tokenize,

with open('ChatBot/Intents.json','r') as file:
    intents = json.load(file)

print(intents)