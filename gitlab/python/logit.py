class logger(object):
    def __init__(self, filename):
        self.file = open(filename, "a")
    def log(self, txt):
        self.file.write(txt + "\n")
		
def getlogger():
    return logger("C:\Users\Intel-Makers\Desktop\elections\web_docs\gitlog.txt")