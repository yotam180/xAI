import socket
import json
from time import time

MINIMAL_TIME = 3

def log(clientAddr):
    """
    This function checks whether a client address reqeust was recieved in the last 3 seconds (parameterized).
    If a request was recieved, returns true. Otherwise, returns false.
    """
    valid = False

    with open("server/logs/log.txt","r") as file:
        logs = json.loads(file.read())
        if(logs[clientAddr] - time() < MINIMAL_TIME):
            valid = True
    
    logs[clientAddr] = time()

    with open("server/logs/log.txt","w") as file:
        file.write(json.dumps(logs))

    return valid
