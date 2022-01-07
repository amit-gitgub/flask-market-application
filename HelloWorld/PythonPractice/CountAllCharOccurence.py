"""
This Program  tell the occurence of all the characters in a single row using dictionary

"""

def findoccurence(string):
    print(string)
    dict = {}

    for i in string:
        if i in dict.keys():
            dict[i] +=1

        else:
            dict[i] = 1

    return dict

print(findoccurence("".join("this is good thing".split())))
