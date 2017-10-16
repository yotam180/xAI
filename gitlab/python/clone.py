import settings
import logit
from os import system
import os
import time

log = logit.getlogger()

system("git clone --mirror " + settings._from)
os.chdir(settings._from.split("/")[-1] + ".git")
system("git remote set-url --push " + settings._to)
log.log("Cloned github repo from " + settings._from + " to " + settings._to + " at " + time.strftime("%H:%M:%S"))
log.file.close()

import update