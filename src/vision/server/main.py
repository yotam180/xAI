import server
import login

import downloader

# Importing our request handlers
import authentication
import tokenizer
import dataset

# Running our server
serv = server.run()
#downloader.run()

# Waiting for a keyboard press to shut the server down
input()

# And closing everything
print("Killing server")
serv.shutdown()
print("Killed server")

print("Killing downloader")
#downloader.shutdown()
print("Killed downloader")