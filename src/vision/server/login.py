#
#   Login system
#   Author: Yotam Salmon
#   Last Edited: 29/12/17
#

import database
import db_entities

import json
import hashlib
import time

from email.utils import parseaddr

db = db_entities.db_instance

def register(params):
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

def login(username, password):
    hash = md5(password)
    users = db.table("users", db_entities.USER)
    results = [x for x in users.query(lambda c: c.get("username") == username and c.get("password_hash") == hash)]
    if len(results) == 0:
        return False
    else:
        sessions = db.table("sessions", db_entities.SESSION)
        ses = sessions.new()
        ses.set("username", username) \
            .set("expiery", 31536000 + time.time())
        sessions.update(ses)
        return results[0]

def md5(str):
    return hashlib.md5(str.encode("utf-8")).hexdigest()