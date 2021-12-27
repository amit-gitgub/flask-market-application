import os


def checkFileExt(filer, extlist):
    print(extlist)
    filelist = []
    for f in filer:
        print(f)
        if os.path.splitext(f)[1].lower() in extlist:
            filelist.append(f)
            print("000000000")
            print(filelist)

    return filelist


files = os.listdir()
# print(f" this are total files {files}\n")
#print(len(files))
print("--------------------------------")
dontTouch = [".py", "venv"]
num = 0
for file in files:

    if os.path.splitext(file)[1].lower() == ".py":
        #print(file)
       # files.remove(file)
        num = num + 1

        # print(str(num)+ "-"+file)

#print(len(files))
# print(f" this are total files {files}\n")
images = []
imageExt = [".png", ".jpg", ".jpeg"]
images = checkFileExt(files, imageExt)
print("===========")
print(images)
print("===========")
images = [file for file in files if os.path.splitext(file)[1].lower() in imageExt ]
print(images)
for file in files:
    if os.path.splitext(file)[1].lower() in imageExt:
        images = file
        print("from loop " +images)
        # print(images)

docExt = [".doc", ".pdf", ".xls", ".docx"]
docs = checkFileExt(files, docExt)
