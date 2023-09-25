import json
from nlik_util.py import tokenize,stem,bag_of_words

with open('ChatBot/Intents.json','r') as file:
    intents = json.load(file)

print(intents)

tokenized_pattern = []
tags=[]
tuple_tokens_tag =[]

for request in intents['intents']:
    tag = request['tag']
    tags.append(tag)

    for pattern in request['patterns']:
        token_pattern = tokenize(pattern)
        tokenized_pattern.extend(token_pattern)
        tuple_tokens_tag.append((token_pattern,tag))


pun