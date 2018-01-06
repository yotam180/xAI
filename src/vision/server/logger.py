import socket
import json
from time import time
#this function checks wheather client address reqeust was recieved in the last 3 seconds(could be changed)
# if request was recieved return true, otherwise return false
MINIMAL_TIME = 3
def log(clientAddr):
    valid =False
    file = open("server/database/logs/logs.txt","r+")
    logs = json.loads(file.read())
    if(logs[clientAddr]-time()<MINIMAL_TIME):
        valid = True
    logs[clientAddr] = time()
    file.write(json.dumps(logs))
    file.close()
    return valid
