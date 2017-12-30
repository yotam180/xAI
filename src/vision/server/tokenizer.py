#
#   API tokens handlers
#   Author: Yotam Salmon
#   Last Edited: 30/12/17
#

# For handling requests
from server import handler

# Utility imports
import json

# Importing some basic http helpers to help us with processing requests
from http_helper import msg, json_post, get_session, logged_in

# Importing the login module to interface indirectly with the users database
import login

@handler("delete_key", "GET")
@handler("create_key", "GET")
def key_operation_get(req):
    return 405, {}, msg("Please use POST to create and delete API keys")

@handler("create_key", "POST")
def create_key_post(req):

    session = get_session(req)
    if not session:
        return 401, {"WWW-Authentication": "Authenticate with _SESSION cookie"}, msg("Not authenticated")

    data = json_post(req)
    if not data or type(data) != type({}):
        return 400, {}, msg("Request body could not be parsed")
    
    if "password" not in data.keys() or "username" not in data.keys():
        return 400, {}, msg("Must specify username and password")

    if data["username"] != session.get("username"):
        return 403, {}, msg("Session username did not match the request credential")

    key = login.create_api_key(data["username"], data["password"])
    if not key:
        return 403, {}, msg("Invalid credentials")

    return 200, {}, json.dumps({"api_key": key.item_id})

@handler("delete_key", "POST")
def delete_key_post(req):

    session = get_session(req)
    if not session:
        return 401, {"WWW-Authentication": "Authenticate with _SESSION cookie"}, msg("Not authenticated")

    data = json_post(req)
    if not data or type(data) != type({}):
        return 400, {}, msg("Request body could not be parsed")
    
    if "password" not in data.keys() or "username" not in data.keys() or "api_key" not in data.keys():
        return 400, {}, msg("Must specify username, password and API key.")

    if data["username"] != session.get("username"):
        return 403, {}, msg("Session username did not match the request credential")

    res = login.remove_api_key(data["api_key"], data["password"])
    if res:
        return 200, {}, msg("API key deleted")
    else:
        return 200, {}, msg("Error deleting API key")

@handler("tokens", "GET")
def tokens_list_get(req):
    user = logged_in(req)

    if not user:
        return 401, {}, ""
    
    tokens = [{"id": x.item_id, "creation_date": x.get("creation_date")} for x in login.get_tokens(user)]

    return 200, {}, json.dumps(tokens)