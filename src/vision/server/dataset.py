#
#   Dataset creation module HTTP handlers
#   Author: Yotam Salmon
#   Last Edited: 02/02/2018
#

# Using the handler decorator to handle HTTP requests.
from server import handler, RequestHandler

# Helper utilities to work with HTTP requests
from http_helper import msg, post, json_post, logged_in

# For communicating with the downloader thread we will use the message queue
import task_scheduler as ts

import keywords as kw

pending = {}

@handler("create_dataset", "POST")
def create_dataset_handler(req):
    """
    Handler for creating a dataset on the server side.
    """

    user = logged_in(req)
    if user is None:
        return 403, {}, msg("Not Authenticated")
    
    data = json_post(req)
    try:
        subject = data["subject"]
        description = data["description"]
        positive = data["positive"]
        negative = data["negative"]
        identifier = user.get("username") + "_" + subject

        tasks = []
        for w in positive:
            if not kw.exists(w):
                tasks.append(
                    ts.download(w)
                )

        for w in negative:
            if not kw.exists(w):
                tasks.append(
                    ts.download(w)
                )

        pending[identifier] = tasks

        print tasks
    except:
        return 400, {}, msg("Content is not in the correct format or a parameter is missing")