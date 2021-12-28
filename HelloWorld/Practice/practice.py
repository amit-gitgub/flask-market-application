import json

def findwordmeaning(wordlist):
    with open('EnglishDictionary2.json') as file:
       data =  json.load(file)
    newword = []
    for word in wordlist:
        if word in data:
            newword.append(f"{word} ----> {data[word]}")
        else:
            newword.append(f"{word} ---> not in dictionary")
    return newword

list1 = []
for i in range(0,int(input("How many words you want to search: "))):
    list1.append(input("Enter the words: "))
meaninglist = []
meaninglist.append(findwordmeaning(list1))
for meaning in meaninglist:
    print('\n'.join(map(str, meaning)))

#meaning = findwordmeaning("joint")
#print(meaning)


