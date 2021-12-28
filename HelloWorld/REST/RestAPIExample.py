import json

import requests
myresp = {}
response = requests.get("http://api.open-notify.org/astros.json")
myresp = dict(response.json())
print(myresp)
print(myresp['people'][0]['name'])
list1 = []
dict1 = {}
for i in range(0,len(myresp['people'])):
    dict1 = {}
    #print(f"name --> {myresp['people'][i]['name']} \n craft -----> {myresp['people'][i]['craft']}")
    dict1['craft'] = myresp['people'][i]['craft']
    dict1['name'] = myresp['people'][i]['name']
    print(dict1)
    list1.append(dict1)


print(list1)






#print(myresp)
#print(response.raise_for_status())