import inspect
import time

def log(text):
    frm = inspect.stack()[1]
    module = inspect.getmodule(frm[0])
    print("[" + time.strftime("%H:%M:%S") + "] " + module.__name__ + ": " + str(text))