from server import handler, run
import sys

shutdown = False

# Examples for using the server module

@handler("hello")
def hello_handler(req):
    return 200, {}, "Hello World"

@handler("exit")
def exit_handler(req):
    global shutdown
    shutdown = True
    return 200, {}, "Shutting down"
    
serv = run()

while not shutdown:
    pass
serv.shutdown()