# 
#   Authentication handlers
#   Author: Yotam Salmon
#   Last Edited: 30/12/17
#
"""
This file contains HTTP handlers related to authentication (login, logout, password recovery, etc.)
It uses the @handler decorator from the server module to handle requests
"""

# Using the handler decorator to handle HTTP requests
from server import handler, RequestHandler

# Trivial utility imports 
import sys
import json

# Importing some helper functions from http_helper to parse requests
from http_helper import msg, get_session, post, json_post, logged_in

# Using the login module to interface with the user database
import login
import nets
#Using the email module to send requests
#import mail
#Using hashlib and random to create hash recovery code
import hashlib
import random

@handler("login", "GET")
def login_get(req: RequestHandler) -> tuple:
    """
    Handles a GET request to /login
    Returns a 405 response specifying that a POST should be made to the endpoint to login.
    """
    return 405, {}, msg("Please use POST for authenticating")

@handler("login", "POST")
def login_post(req: RequestHandler) -> tuple:
    """
    Logs a user into the web server. 
    """

    # Parsing the request body
    data = json_post(req)

    # Trying to get the user's authentication session
    session = get_session(req)

    # If there's a session (user is already authenticated) we don't wish to create
    # a new one, but to inform the client that they are already logged in.
    if session:
        return 200, {}, msg("Already authenticated")

    # If the data is malformatted or is an incorrect data structure, we should inform
    # the client that the data must be reorganised to be accepted by the server.
    if data is None or type(data) != type({}):
        return 400, {}, msg("Content is not in the correct format")

    # Making sure that the JSON body contains a username and a password.
    if "username" not in data.keys() or "password" not in data.keys():
        return 400, {}, msg("Must specify username and password to log in")

    # Querying the user object and forcing the creation of a new session object in the
    # database.
    user, session = login.login(data["username"], data["password"], True)

    # If the login procedure did not find a matching user to the request, we announce defeat
    # and cancel the login.
    if not user:
        return 200, {}, json.dumps({"login": False, "message": "Incorrect Credentials"})
    
    # Otherwise, we know that everything has worked, we signal a cookie update to the client and
    # return a success message with the new session id.
    return 200, {"Set-Cookie": "_SESSION=" + session.item_id + ";"}, json.dumps({"login": True, "session": session.item_id})

@handler("register", "GET")
def register_get(req: RequestHandler) -> tuple:
    return 405, {}, msg("Please use POST for authenticating")

@handler("register", "POST")
def register_post(req: RequestHandler) -> tuple:
    data = json_post(req)
    session = get_session(req)

    if session:
        return 200, {}, msg("Already Authenticated")

    err = login.register(data)

    if not err:
        return 200, {}, msg("Registration Successful")

    return 200, {}, json.dumps({"error": err})

@handler("logout", "GET")
@handler("logout", "POST")
def logout(req: RequestHandler) -> tuple:
    """
    This logs the user out of the web server.
    """

    # Trying to query the session from the user's request
    session = get_session(req)

    # If there is no session (or no matching session object in the database was found) we should
    # tell the user that they were not authenticated prior to the request, and thus they will not
    # be logged out.
    # We return a 401 response with a WWW-Authentication hint that points developers/hackers to the /login
    # endpoint to login first.
    if not session:
        return 401, {"WWW-Authentication": "Authenticate POST /login"}, msg("Not authenticated")
    
    # Logging out the user from the database
    res = login.logout(session.item_id)

    # If the logout worked, deleting the session cookie at the client side. Otherwise, informing that
    # something wrong happened in the database.
    if res:
        return 303, {"Location": "/login.php","Set-Cookie": "_SESSION=deleted; path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT"}, msg("Logged out")
    else:
        return 400, {}, msg("Session could not be found")


@handler("profile", "GET")
def profile_get(req: RequestHandler) -> tuple:
    user = logged_in(req)
    if not user:
        return 403, {}, ""
    obj = user.data
    obj["datasets"] = {i.item_id: i.data for i in nets.get_datasets(user.item_id)}
    obj["classifiers"] = {i.item_id: i.data for i in nets.get_classifiers(user.item_id)}
    return 200, {}, json.dumps(obj)

@handler("recover","GET")
def recvoer(req:RequestHandler)->tuple:
    val  = random.randint(0,16**16)
    m = hashlib.md5()
    m.update(str(val))
    code = m.hexdigest()
    details = {}
    details["message"] = code
    #TODO: change mail to mail in GET request
    details["to"] = "shaikimhi221199@gmail.com"
    details["subject"] = "recovery_mail"
    mail.send(details)
    return 200,msg("Recovery mail sent")

@handler("login_test")
def login_test(req):
    user = logged_in(req)
    return 200, {}, user.get("username") if user else "-"