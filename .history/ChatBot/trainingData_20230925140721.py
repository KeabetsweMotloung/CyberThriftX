import json
from nlik_util.py import tokenize,stem,bag_of_words

with open('ChatBot/Intents.json','r') as file:
    intents = json.load(file)

print(intents)

tokenized_pattern = []
tags=[]
tuple_tokens_tag =[]

for request in intents['intents']:
    tags = request