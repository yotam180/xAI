# 
#   HTTP helpers
#   Author: Yotam Salmon
#   Last Edited: 30/12/17
# 

import sys
import json
import base64
from http.cookies import SimpleCookie

from server import RequestHandler

import login

def msg(txt : str) -> str:
    """
    Encodes a simple string message in a json response format
    """
    return json.dumps({"message": txt})

def post(req: RequestHandler):
    """
    Extract the POST body from a request.
    """
    print(type(req))
    if not "Content-Length" in req.headers.keys():
        return None
    try:
        content_length = int(req.headers["Content-Length"])
    except:
        return None
    return req.rfile.read(content_length)

def json_post(req: RequestHandler):
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

def get_session_id_from_cookie(req: RequestHandler) -> str:
    """
    Gets a session id from a request and validates it against the database.
    """
    if "Cookie" in req.headers.keys():
        cookies = SimpleCookie()
        cookies.load(req.headers["Cookie"])
        if "_SESSION" in cookies:
            ses = cookies["_SESSION"].value
            return ses or False
        else:
            return False
    else:
        return False

def get_session_id_from_header(req: RequestHandler) -> str:
    if "Authorization" in req.headers:
        auth = req.headers["Authorization"].split(" ")
        if len(auth) < 2:
            return False
        if auth[0] == "Session":
            try:
                return base64.b64decode(auth[1]).decode("utf-8")
            except:
                return False
        return False
    return False

def get_session(req: RequestHandler):
    """
    Gets the session object from a connection.
    """
    session = get_session_id_from_header(req) or get_session_id_from_cookie(req)
    if not session:
        return False
    return login.verify_session(session) or False

def logged_in(req: RequestHandler):
    """
    Gets the currently logged in user.
    """
    ses = get_session(req)
    if not ses:
        return None
    user = login.get_logged_user(ses)
    if not user:
        return None
    return user