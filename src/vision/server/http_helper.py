# 
#   HTTP helpers
#   Author: Yotam Salmon
#   Last Edited: 30/12/17
# 

import sys
import json
from http.cookies import SimpleCookie

import login

def msg(txt):
    """
    Encodes a simple string message in a json response format
    """
    return json.dumps({"message": txt})

def post(req):
    """
    Extract the POST body from a request.
    """
    if not "Content-Length" in req.headers.keys():
        return None
    try:
        content_length = int(req.headers["Content-Length"])
    except:
        return None
    return req.rfile.read(content_length)

def json_post(req):
    """
    Extracts and parses a json POST data.
    """
    content = post(req)
    if content is None:
        return None
    try:
        return json.loads(content.decode("utf-8"))
    except:
        return None

def get_session(req):
    """
    Gets a session id from a request and validates it against the database.
    """
    if "Cookie" in req.headers.keys():
        cookies = SimpleCookie()
        cookies.load(req.headers["Cookie"])
        if "_SESSION" in cookies:
            ses = cookies["_SESSION"].value
            session = login.verify_session(ses)
            return session or False
        else:
            return False
    else:
        return False
