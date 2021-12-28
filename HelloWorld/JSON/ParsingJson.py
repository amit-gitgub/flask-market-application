import json
dict1 = {}
with open("file.json", 'r') as file:
    dict1 = {}
    dict1 = dict(json.load(file))
    print(dict1)
    print(dict1['items'][0]['links']['self'])



