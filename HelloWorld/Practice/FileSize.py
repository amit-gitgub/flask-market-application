import os

print(os.getcwd())
os.chdir('C:\Amit\code\python')
path = os.path.abspath('C:\Amit\code\python')

#print(os.listdir())

temp_dict = {}

for folder, subfolders, files in os.walk(path):

    # checking the size of each file
    for file in files:
        size = os.stat(os.path.join(folder, file)).st_size
        file = os.path.join(folder, file)
        temp_dict[file] = size/1000



#print(temp_dict)
sorted(temp_dict.values())
sorted(temp_dict.items(), key =
             lambda kv:(kv[1], kv[0]))

list1 = list(sorted(temp_dict.items(), key =
             lambda kv:(kv[1], kv[0])))
print(list1[-5:])
print("=================")
for file, size in reversed(list1[-int(input("Enter how many files: ")):]):
    print(f"{file} ------> {size/1000} mb")
#print(temp_dict)