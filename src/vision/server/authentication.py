# 
#   Authentication handlers
#   Author: Yotam Salmon
#   Last Edited: 30/12/17
#

from server import handler

import sys
import json

from http_helper import msg, get_session, post, json_post

import login

@handler("login", "GET")
def login_get(req):
    return 405, {}, msg("Please use POST for authenticating")

@handler("login", "POST")
def login_post(req):
    data = json_post(req)

    session = get_session(req)

    if session:
        return 400, {}, msg("Already authenticated")

    if data is None or type(data) != type({}):
        return 400, {}, msg("Content is not in the correct format")

    if "username" not in data.keys() or "password" not in data.keys():
        return 400, {}, msg("Must specify username and password to log in")

    user, session = login.login(data["username"], data["password"], True)

    if not user:
        return 200, {}, json.dumps({"login": False, "message": "Incorrect Credentials"})
    
    return 200, {"Set-Cookie": "_SESSION=" + session.item_id + ";"}, json.dumps({"login": True, "session": session.item_id})

@handler("logout", "GET")
@handler("logout", "POST")
def logout(req):
    session = get_session(req)

    if not session:
        return 401, {"WWW-Authentication": "Authenticate POST /login"}, msg("Not authenticated")
    
    res = login.logout(session)

    if res:
        return 200, {"Set-Cookie": "_SESSION=deleted; path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT"}, msg("Logged out")
    else:
        return 400, {}, msg("Session could not be found")
