import os
from threading import Thread
import time

listDir = os.listdir(os.getcwd())

def sync_changes():
    global listDir
    while(True):
        time.sleep(1)
        tempDir = os.listdir(os.getcwd())
        changes = get_changes(tempDir, listDir)
        #reorganizing the array into listDir and changes to additions and deletions
        listDir = tempDir
        additions = changes[0]
        deletions =  changes[1]
    
def get_changes(list1, list2):
    return [i for i in list1 if i not in list2],[i for i in list2 if i not in list1]
