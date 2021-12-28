import os
import time

path = r'C:\Users\91964\PycharmProjects\HelloWorld'
files = os.listdir(path)
print(files)
for folder, subfolders, files in os.walk(path):
    print(files)
    for file in files:
        print(f"{file} ---> "+time.ctime(os.path.getmtime(f"{path}/{file}")))
        t = time.ctime(os.path.getmtime(f"{path}/{file}"))
        split = os.path.splitext(str(t))
        print(split[0].split()[:])
    #print(time.ctime(os.path.getmtime()))
