import os
from threading import Thread
import time


#thread function to get changes and save them on cloud or server
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
        update_changes(additions,deletions)


#returns differences between two lists
#returns two lists
#first list is additions
#second list is deletions
def get_changes(list1, list2):
    return [i for i in list1 if i not in list2],[i for i in list2 if i not in list1]

#responsible for saving directory changes
def update_changes(additions, deletions):
    for file in deletions:
        delete_from_server(file)
    for file in additions:
        save_to_server(file)

#saves the given file to remote server
def save_to_server(file):
    no = None
def delete_from_server(file)
    no = None
    
listDir = os.listdir(os.getcwd())
#thread = Thread(target = sync_changes())




