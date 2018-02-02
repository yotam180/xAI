import server
import login

import downloader

# Importing our request handlers
import authentication
import tokenizer

# Running our server
serv = server.run()
downloader.run()

# Waiting for a keyboard press to shut the server down
input()

# And closing everything
serv.shutdown()
downloader.shutdown()