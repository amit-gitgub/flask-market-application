import os
import time

path = r'C:\Amit\code\python'
files = os.listdir(path)
print(files)
for file in files:
    print(f"{file} ---> "+time.ctime(os.path.getmtime(f"{path}/{file}")))
    t = time.ctime(os.path.getmtime(f"{path}/{file}"))
    split = os.path.splitext(str(t))
    print(split[0].split()[:])
#print(time.ctime(os.path.getmtime()))
