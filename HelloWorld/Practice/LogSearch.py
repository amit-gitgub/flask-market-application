import re
import os


myFile = r"C:\Amit\code\python\logs\apache_logs.log"

def RegEx(file):
    openFile = open(myFile, 'r')
    myResList = []
    myList = openFile.readlines()
    myReg = re.compile(r'error')
    for i in (myList):
            #print(i, end='')
            result = myReg.search(i)
            if result != None:
                    #print(i, end='')
                    myResList.append(i.rstrip())
                    print("++++++++++++++++")
                    print(i.split())
    final = '\n'.join(myResList[:])
    return final

print()
print('Results:')
print(RegEx(myFile))
print()


