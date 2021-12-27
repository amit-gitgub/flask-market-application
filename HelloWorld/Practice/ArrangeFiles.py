import os
import stat


if __name__ == "__main__":
    os.chdir("C:\Amit\code\python")
    print(os.getcwd())
    Dir_list = os.listdir()
    set1 = set()
    doc_list = ['.txt','.csv','.docx']
    image_list = ['.png','.PNG','.jpg']
    presentation_list = ['.pptx','pdf','.potx']
    os.mkdir('docer', 0o777)
    for file in Dir_list:

        split_tup = os.path.splitext(file)
        #print(split_tup)
        if split_tup[1] in doc_list:
            #os.chmod('C:\Ami', 0o777)
            os.chmod(file, 0o777)
            os.replace(file, f'C:/Amit/code/python/docer/{file}')
        #print(split_tup[1])
            set1.add(split_tup[1])



    print("printing set")
    print(set1)

