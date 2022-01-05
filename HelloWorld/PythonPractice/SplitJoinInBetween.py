import requests
"""
Below example first download the conent of the website to a object and then we are searching only the https data in the whole 
string by converting it to bytes as .startswith method doesnot work with string...now we put the result in a new list and then add a 
seperator in each element of that list. put everything  in a result and then print it
"""
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