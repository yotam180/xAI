# 
#   Email sending module
#   Author: Shai Kimhi
#   Last Edited: 13/01/18
#

import os
import sys
import smtplib
import mimetypes

from argparse import ArgumentParser

from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# Constants to declare our username and password for the email account
# As the project is open source, it's a mere mistake to put them here.
# But it's alright for now... I guess...
# Gotta fix that later using ENV variables.
SENDER = "xaivision123@gmail.com"
PASSWORD = "rig123456"

def login():
    """
    Creates SMTP connection to our GMAIL servers and returns the SMTP mailer object.
    """
    smtp = smtplib.SMTP("smtp.gmail.com",587)
    smtp.starttls()
    smtp.login(SENDER,PASSWORD)
    return smtp

# Logging into Gmail when the module is imported
_client = login()

def send(details):
    """
    Sends a mail message.
    Parameters: 
        - details - dictionary with all arguments:
            * message - the message text
            * to - the recipient we are sending the mail to. 
    """
    outer = MIMEText(details["message"])
    outer["To"] = details["to"]
    outer["From"] = "xAI No-Reply"
    outer.preamble = "You will not see this in a MIME-aware mail reader.\n"
    msg = outer.as_string()

    _client.sendmail(SENDER, details["to"], msg)

def parameterize(msg, src):
    """
    To embed data in a parameterized message.
    Parameters:
        - msg - the parameterized message with {{variable}} fields.
        - src - the dictionary contains the variable names and values to embed.
    """
    for i, t in src.items():
        msg = msg.replace("{{" + i + "}}", t)
    
    return msg
