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
#Using the email module to send requests
import mail
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
        return 200, {"Set-Cookie": "_SESSION=deleted; path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT"}, msg("Logged out")
    else:
        return 400, {}, msg("Session could not be found")


@handler("profile", "GET")
def profile_get(req: RequestHandler) -> tuple:
    user = logged_in(req)
    if not user:
        return 403, {}, ""
    return 200, {}, json.dumps(user.data)

##the two functions below are my functions to create recovery code ~Shai

@handler("recover_mail","POST")
def recover_mail(req:RequestHandler)->tuple:
    DATA_FILE = "server/database/users/R45mPmkaXXNuZo92qqe3.json"
    # check if user is connected
    user = logged_in(req) 
	if(user not is None):
		return 401,{"WWW-Authentication": "Authenticate POST /login"},msg("User is connected")#TODO : check the return values
	# get request data from post
    data = json_post(req)
	users = login.getUsersValues("username",data["username"])
	#getting client object to send mail from 
    client = mail.login()
	#generate recovery code
    value = random.randint(0,10**16)
	code = hashlib.md5(str(value))
    ##TODO: change code in database (this is what this code is supposed to do) 
    ## Reminder: make database dictionary iteratable (with more than one user)
    file = open(DATA_FILE,"r+")
    dict = json.loads(file.read())
    for i in range dict:
        if i["username"] = data["username"]:
            dict["recovery_code"] = code
            user = True
    if(!user)
        return 401,{"WWW-Authentication": "Authenticate POST /login"},msg("User does not exist") # TODO : check the return values
    file.close()
    file = open(DATA_FILE,"w+")
    file.write(json.dumps(dict))
    file.close()
    ############
    #Send email to user
    details = {}
    details["message"] = code
	details["to"] = users["email"]
	details["client"] = mail.login()
	mail.send(details)


@hanlder("recover_password","GET")
def recover_password(req:RequestHandler)->tuple:
	data = "" #TODO : get 'GET' values
    #get users dictionary
    DATA_FILE = "server/database/users/R45mPmkaXXNuZo92qqe3.json"
    file = open(DATA_FILE,"r+")
    dict = json.loads(file.read(),"r+")
    file.close()
    # find wanted user in dictionary
    user = findUser(users,data["username"])
    if(user==None):
        return 401,{"WWW-Authentication": "Authenticate POST /login"},msg("User does not exist") # TODO : check the return values
    #check recovery code
    if(user["recovery_code"] != data["recovery_code"]):
        return 401,{"WWW-Authentication": "Authenticate POST /login"},msg("code not correct") # TODO : check the return values
    ##TODO : change password in database

def findUser(users,username):
    for i in range(len(users)):
        if(i["username"]==username):
            return i
	return None
		
	
	
