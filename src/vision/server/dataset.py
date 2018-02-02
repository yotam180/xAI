#
#   Dataset creation module HTTP handlers
#   Author: Yotam Salmon
#   Last Edited: 02/02/2018
#

# Using the handler decorator to handle HTTP requests.
from server import handler, RequestHandler

# Helper utilities to work with HTTP requests
from http_helper import msg, get_session, post, json_post

# For communicating with the downloader thread we will use the message queue
import task_scheduler

@handler("create_dataset", "POST")
def create_dataset_handler(req):
    """
    Handler for creating a dataset on the server side.
    """
    pass