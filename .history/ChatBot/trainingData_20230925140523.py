import json
from nlik_util.py import tokenize,stem,bag_of_words

with open('ChatBot/Intents.json','r') as file:
    intents = json.load(file)

print(intents)