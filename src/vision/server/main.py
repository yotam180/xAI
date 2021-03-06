import server
import login

import constants

import downloader
import trainer

# Importing our request handlers

import authentication
import tokenizer
import dataset
import classifiers
import evaluator

# Running our server
serv = server.run()
downloader.run()
trainer.run()

# Waiting for a keyboard press to shut the server down
input()

# And closing everything
print("Killing server")
serv.shutdown()
print("Killed server")

print("Killing downloader")
downloader.shutdown()
print("Killed downloader")

print("Killing trainer")
trainer.shutdown()
print("Killed trainer")