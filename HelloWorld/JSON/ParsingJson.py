import json
dict1 = {}
with open("file.json", encoding="utf8") as file:
    data = json.load(file)
set1 = set()
list1 = ['USA', 'INDI', 'Germany', 'Estonia', 'India', 'Chile','noida', 'Hungary', 'UK', 'Turkey', 'In', 'Australia', 'Brazil','ind']

for i in range(0, len(data['feeds'])):
    #print(data['feeds'][i]['location'])
    location = str(data['feeds'][i]['location'])
    #print(location.split()[-1])
    abc = location.split()[-1]
    if abc in list1:
        set1.add(abc)

print(set1)






