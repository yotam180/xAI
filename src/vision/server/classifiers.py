#
#   The network interface for training classifiers
#   Author: Yotam Salmon   
#   Last Edited: 18/02/18
#

# HTTP imports
from server import handler
from http_helper import json_post, querystring

# The task scheduler, to communicate with the trainer process
import task_scheduler as ts

# Nets, for interacting with dataset and classifier database entries
import nets

# TODO: write the interface