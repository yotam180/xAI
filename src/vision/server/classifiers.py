#
#   The network interface for training classifiers
#   Author: Yotam Salmon   
#   Last Edited: 28/02/18
#

# HTTP imports
from server import handler
from http_helper import msg, json_post, querystring, logged_in

# The task scheduler, to communicate with the trainer process
import task_scheduler as ts

# Nets, for interacting with dataset and classifier database entries
import nets

# Utilities
import json

# TODO: write the interface

pending = {}

@handler("create_classifier", "POST")
def create_classifier_handler(req):
    """
    Handler for creating and traning classifiers
    """
    global pending

    user = logged_in(req)
    if user is None:
        return 403, {}, msg("Not Authenticated")

    data = json_post(req)
    #try:
    classifier_id = data["classifier_id"]
    owner_id = user.item_id
    dataset_id = data["dataset_id"]

    # Trying to create the database entry
    success, obj = nets.create_classifier(
        classifier_id,
        owner_id,
        dataset_id
    )

    # Returning error message upon failure
    if not success:
        return 200, {}, msg(obj)

    task_id = ts.train(
        dataset_id,
        classifier_id
    )

    pending[task_id] = obj

    return 200, {}, json.dumps({"classifier_id": obj})

    #except:
    #    return 400, {}, msg("Content is not in the correct format")

@handler("classifier_status", "GET")
def classifier_status_handler(req):
    qs = querystring(req)

    if not "classifier_id" in qs:
        return 400, {}, msg("querystring is missing classifier_id")

    return 200, {}, json.dumps(ts.get_training_status("".join(qs["classifier_id"])))

def done_training(el):
    nets.mark_trained(pending[el["task_id"]], el["best_val_acc"] * 100)

@handler("stop_training")
def stop_training(req):
    user = logged_in(req)
    if not user:
        return 403, {}, msg("Unauthorized")

    qs = querystring(req)

    s = ts._current_training

    if not s:
        return 403, {}, msg("Unauthorized 1")

    c = nets.get_dataset(s["dataset_id"])

    if not c:
        return 403, {}, msg("Unauthorized 2")

    if c.get("owner_id") != user.item_id:
        return 403, {}, msg("Unauthorized 3")

    ts.stop_training()
    return 200, {}, msg("Training Stopped")


@handler("classifier")
def classifier_info_handler(req):
    qs = querystring(req)

    if not "id" in qs:
        return 404, {}, ""

    cl = nets.get_classifier("".join(qs["id"]))

    if not cl:
        return 404, {}, ""
    
    cl.data["dataset"] = nets.get_dataset(cl.get("dataset_trained")).data
    return 200, {}, json.dumps(cl.data)


ts.on_net_created = done_training