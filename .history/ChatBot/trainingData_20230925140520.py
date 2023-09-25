import json
from nlik_util.py import tokenize,stem,ba

with open('ChatBot/Intents.json','r') as file:
    intents = json.load(file)

print(intents)