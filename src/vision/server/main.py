from server import handler, run
import login

# Importing our request handlers
import authentication
import tokenizer

# Running our server
serv = run()

# Waiting for a keyboard press to shut the server down
input()
serv.shutdown()