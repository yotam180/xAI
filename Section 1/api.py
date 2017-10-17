import os
def findFilesFormat(formatter):
    list = []
    l = os.listdir(os.getcwd())
    for file in l:
        parts = file.split(".")
        if(len(parts)>1):
            if(parts[len(parts)-1].lower()==formatter.lower()):
                list.append(file)
    return list
def formatPng():
    
l = findFilesFormat("png")
for i in l:
    print i
                
    