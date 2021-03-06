#
#   Login system
#   Author: Yotam Salmon
#   Last Edited: 30/12/17
#

import database
import db_entities

import json
import hashlib
import time

from email.utils import parseaddr

db = db_entities.db_instance

def register(params: dict):
    username = params["username"]
    password = params["password"]
    confirmation = params["confirmation"]
    first_name = params["first_name"]
    last_name = params["last_name"]
    email = params["email"]
    country = params["country"]
    phone = params["phone"]

    if len(username) < 6:
        return "Username must be at least 6 characters long"

    if len(username) > 30:
        return "Username must be at most 30 characters long"

    if len(password) < 6:
        return "Password must be at least 6 characters long"

    if len(password) > 30:
        return "Password must be at most 30 characters long"

    if password != confirmation:
        return "The password confirmation is not the same as the password"
    
    if not any(x.isupper() for x in password):
        return "Password must contain at least one upper-case character"

    if not any(x.islower() for x in password):
        return "Password must contain at least one lower-case character"

    if not any(x.isdigit() for x in password):
        return "Password must contain at least one digit"

    if "".join(parseaddr(email)) == "":
        return "The email entered is not in the correct format"

    if len(first_name) < 2:
        return "You must enter a first name"

    if len(last_name) < 2:
        return "You must enter a last name"

    with open("static/countries.json", "r") as f:
        if not country in json.loads(f.read()).keys():
            return "The country code is invalid"

    users = db.table("users", db_entities.USER)

    same_username = len(list(users.query(lambda c: c.get("username") == username)))

    if same_username > 0:
        return "Username is already taken"

    user = users.new()
    user.set("username", username) \
        .set("password_hash", md5(password)) \
        .set("first_name", first_name) \
        .set("last_name", last_name) \
        .set("phone_num", phone) \
        .set("country", country) \
        .set("email", email)
    
    users.update(user)
    return None

def login(username: str, password: str, create_session: bool = True):
    hash = md5(password)
    users = db.table("users", db_entities.USER)
    results = [x for x in users.query(lambda c: c.get("username") == username and c.get("password_hash") == hash)]
    if len(results) == 0:
        return None, None
    else:
        if create_session:
            sessions = db.table("sessions", db_entities.SESSION)
            ses = sessions.new()
            ses.set("username", username) \
                .set("expiery", 31536000 + time.time())
            sessions.update(ses)
            return results[0], ses
        else:
            return results[0], None

def logout(session_id: str) -> bool:
    sessions = db.table("sessions", db_entities.SESSION)
    ses = sessions.load_item(session_id)
    if ses:
        sessions.delete(ses)
        return True
    else:
        return False

def verify_session(session_id: str) -> bool:
    sessions = db.table("sessions", db_entities.SESSION)
    ses = sessions.load_item(session_id)
    if ses is None:
        return None
    if ses.get("expiery") <= time.time():
        sessions.delete(ses)
        return None
    return ses

def get_logged_user(session: database.db_item) -> database.db_item:
    users = db.table("users", db_entities.USER)
    a = list(users.query(lambda c: session.get("username") == c.get("username")))
    if len(a) < 1:
        return None
    else:
        return a[0]

def create_api_key(username: str, password: str) -> database.db_item:
    user, _ = login(username, password, False)
    if user is None:
        return None
    else:
        keys = db.table("keys", db_entities.API_KEY)
        key = keys.new() \
            .set("username", username) \
            .set("creation_date", time.time())
        keys.update(key)
        return key

def remove_api_key(token: str, password: str) -> bool:
    users = db.table("users", db_entities.USER)
    keys = db.table("keys", db_entities.API_KEY)

    key = keys.load_item(token)
    if key is None:
        print("Error finding key")
        return False

    matching_users = list(users.query(lambda c: c.get("username") == key.get("username")))
    if len(matching_users) < 1:
        print("Error finding user " + key.get("username"))
        return False
    user = matching_users[0]

    if user.get("password_hash") != md5(password):
        print("Error comparing password")
        return False

    keys.delete(key)
    return True

def md5(string: str) -> str:
    return hashlib.md5(string.encode("utf-8")).hexdigest()

def get_tokens(user: database.db_item) -> list:
    token_tbl = db.table("keys", db_entities.API_KEY)
    tokens = token_tbl.query(lambda c: c.get("username") == user.get("username"))
    return list(tokens)
def getUsersValues(filed,filter):
	users = db.table("user",db_entities.USER)
	af = [x for x in users.query(lambda c:c.get(field)==filter)]
	return af