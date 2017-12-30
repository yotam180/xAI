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
    return json.dumps({"message": txt})

def post(req):
    if not "Content-Length" in req.headers.keys():
        return None
    try:
        content_length = int(req.headers["Content-Length"])
    except:
        return None
    return req.rfile.read(content_length)

def json_post(req):
    content = post(req)
    if content is None:
        return None
    try:
        return json.loads(content.decode("utf-8"))
    except:
        return None

def get_session(req):
    if "Cookie" in req.headers.keys():
        cookies = SimpleCookie()
        cookies.load(req.headers["Cookie"])
        if "_SESSION" in cookies:
            ses = cookies["_SESSION"].value
            is_ok = login.verify_session(ses)
            return ses if is_ok else False
        else:
            return False
    else:
        return False
