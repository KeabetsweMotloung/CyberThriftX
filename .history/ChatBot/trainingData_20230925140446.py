import json
import nlik_util.

with open('ChatBot/Intents.json','r') as file:
    intents = json.load(file)

print(intents)