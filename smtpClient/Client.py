import os
import sys
import smtplib
# For guessing MIME type based on file name extension
import mimetypes

from argparse import ArgumentParser

from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
SENDER = "xaivision123@gmail.com"
PASSWORD = "rig123456"
def login():
    smtp = smtplib.SMTP("smtp.gmail.com",587)
    smtp.starttls()
    smtp.login(SENDER,PASSWORD)
    return smtp
def main(mail,reciever,title,message):
    outer = MIMEText(message)
    outer['Subject'] = title
    outer['To'] = reciever
    outer['From'] = 'xaivision123@gmail.com'
    outer.preamble = 'You will not see this in a MIME-aware mail reader.\n'
    messageInstance = outer.as_string()
    '''with smtplib.SMTP('smtp.gmail.com',587) as s:
            s.starttls()
            s.login("xaivision123","rig123456")
            s.sendmail(args.sender, args.recipients, composed)
            print (composed)'''
    mail.sendmail(SENDER,reciever,messageInstance)
smtp = login()
main(smtp,"yotam.salmon@gmail.com","test","hello")