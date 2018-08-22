import sys,os
import time, json
from threading import Thread


sourceDir = "\songs"
listDir = os.listdir(os.getcwd())
if(len(sys.argv) > 1):
    sourceDir = sys.argv[1]

#thread function to get changes and save them on cloud or server
def sync_changes():
    global listDir
    while(True):
        time.sleep(2)
        tempDir = os.listdir(os.getcwd()+ sourceDir)
        changes = get_changes(tempDir, listDir)
        #reorganizing the array into listDir and changes to additions and deletions
        listDir = tempDir
        additions = changes[0]
        deletions =  changes[1]
        update_changes(additions,deletions)
        #debug print line
        print(json.dumps(listDir) + "->" + json.dumps(additions) + ";" + json.dumps(deletions))


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
#deletes the given file from the remote server
def delete_from_server(file):
    no = None

    
thread = Thread(target = sync_changes())




