#
#   Dataset creation module HTTP handlers
#   Author: Yotam Salmon
#   Last Edited: 02/02/2018
#

import keywords as kw
import nets

# For communicating with the downloader thread we will use the message queue
import task_scheduler as ts

# Helper utilities to work with HTTP requests
from http_helper import json_post, logged_in, msg, post

# Using the handler decorator to handle HTTP requests.
from server import RequestHandler, handler

pending = {}

@handler("create_dataset", "POST")
def create_dataset_handler(req):
    """
    Handler for creating a dataset on the server side.
    """
    global pending

    user = logged_in(req)
    if user is None:
        return 403, {}, msg("Not Authenticated")
    
    data = json_post(req)
    try:
        subject = data["subject"]
        description = data["description"]
        positive = data["positive"]
        negative = data["negative"]
        identifier = data["identifier"] if "identifier" in data else user.get("username") + "_" + subject

        obj = {
            "tasks": [],
            "done": [],
            "ready": []
        }
        for w in positive:
            if not kw.exists(w):
                obj["tasks"].append(
                    ts.download(w)
                )
            else:
                obj["ready"].append(w)

        for w in negative:
            if not kw.exists(w):
                obj["tasks"].append(
                    ts.download(w)
                )
            else:
                obj["ready"].append(w)

        obj_name = nets.create_dataset(
            identifier,
            positive,
            negative,
            user.item_id,
            subject,
            description
        )

        if len(obj["tasks"]) > 0:
            pending[obj_name] = obj
            return 200, {}, msg("Dataset Creating")
        else:
            nets.set_working(obj_name)
            return 200, {}, msg("Dataset Created")
    except:
        return 400, {}, msg("Content is not in the correct format or a parameter is missing")


def done_task(task):
    """
    Handles a downloaded keyword
    """
    global pending
    print(task)
    print("---")
    for _id, p in pending.items():
        if task["task_id"] in p["tasks"]:
            p["done"].append(task["keyword"])
            p["tasks"].remove(task["task_id"])
            if len(p["tasks"]):
                nets.set_working(_id)


# Registering the event handler
ts.on_keyword_downloaded = done_task
