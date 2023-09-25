import json
from nlik_util.py import 

with open('ChatBot/Intents.json','r') as file:
    intents = json.load(file)

print(intents)