import json
import nlik_utilspypy

with open('ChatBot/Intents.json','r') as file:
    intents = json.load(file)

print(intents)