import json
import requests
# Below is the example of best practice while working with json. i.e to tackle all the possible exception
# also it also shows json data extraction with list and dictionary....
# for more info on json extration technique visit https://towardsdatascience.com/how-do-i-extract-nested-data-in-python-4e7bed37566a
try:
    response = requests.get("https://restcountries.com/v3.1/currency/dollar", timeout=10)
    response.raise_for_status()
    # Code here will only run if the request is successful
except requests.exceptions.HTTPError as errh:
    print(errh)
except requests.exceptions.ConnectionError as errc:
    print(errc)
except requests.exceptions.Timeout as errt:
    print(errt)
except requests.exceptions.RequestException as err:
    print(err)
#print(response.json())
# Most important while working with Rest APi with Json...always work with Json object as below...response.json() give json object
data = response.json()
print(type(data))
print(data)
for i in range(0,len(data)):
    print(data[i]['name']['official'])

for i in range(0,3):
    #print(data[i]['name']['nativeName'])
    #print(data[i]['name']['official'])
    if 'spa' in data[i]['name']['nativeName']:
        print(f"Spanish officials ---> {data[i]['name']['nativeName']['spa']['official']}")
    elif 'eng' in data[i]['name']['nativeName']:
        print(f"English officials ---> {data[i]['name']['nativeName']['eng']['official']}")


