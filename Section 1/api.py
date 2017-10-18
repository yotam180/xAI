import os
import photosDownload as Pdownload
import shutil
def findFilesFormat(formatter):
    list = []
    l = os.listdir(os.getcwd())
    for file in l:
        parts = file.split(".")
        if(len(parts)>1):
            if(parts[len(parts)-1].lower()==formatter.lower()):
                list.append(file)
    return list
def formatPng(file):
    input()#to be changed
def deleteFD(name):
    l = name.split(".")
    if(len(l)>1):
        os.remove(name)
    else:
        shutil.rmtree(name)
def iterateDownload(search,keyWords):
    if("output" in os.listdir(os.getcwd())):
        deleteFD("output")
    Pdownload.download(search,keyWords)
l = ["one","two","three"]
for i in l:
    iterateDownload([str(i)],[""])
                
    