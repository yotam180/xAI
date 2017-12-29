import server
import sys

shutdown = False

# Examples for using the server module

@server.handler("hello")
def hello_handler(req):
    return 200, {}, "Hello World"

@server.handler("exit")
def exit_handler(req):
    global shutdown
    shutdown = True
    return 200, {}, "Shutting down"
    
serv = server.run()

while not shutdown:
    pass
serv.shutdown()