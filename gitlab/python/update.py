import time
import logit
import settings
from os import system
import os

if __name__ == "__main__":
    os.chdir(settings._from.split("/")[-1] + ".git")

log = logit.getlogger()

system("git fetch -p origin")
system("git push --mirror")

log.log("Updated github repo from " + settings._from + " to " + settings._to + " on " + time.strftime("%b %d, %Y at %H:%M:%S"))
log.file.close()