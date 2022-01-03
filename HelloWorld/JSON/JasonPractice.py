import json

with open('sample.json', 'r') as file:
    data = json.load(file)
    print(data)
    print(type(data['people']))
    print(len(data['people'][0]))

    for i in range(0, len(data['people'])):
        print(f"{data['people'][i]['firstName']} ----> {data['people'][i]['number']}")

dict1 = {}
list1 = []
print(data["people"])
#newlist = [item.get("firstName") for item in data]
#print(newlist)


for item in data["people"]:
    dict1 = dict(item)
    for k,v in dict1.items():
        if k == "firstName":
            list1.append(v)
            #print(f" Print all names of the document: {v}" )

print(list1.count("James"))










