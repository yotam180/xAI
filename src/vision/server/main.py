from server import handler, run
import login

# Importing our request handlers
import authentication

# Running our server
serv = run()

# Waiting for a request to shut the server down
input()
serv.shutdown()