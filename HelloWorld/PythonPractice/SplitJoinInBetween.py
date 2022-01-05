import requests

res = requests.get("https://thecleverprogrammer.com/2021/01/14/python-projects-with-source-code/")
fullText = res.content
ab = bytes("https", 'utf-8')
split = fullText.split()
newList = []
for data in split:
    if data.startswith(ab):
        newList.append(str(data))

seperator = ';\n'
result = seperator.join(newList)
print(result)