#
#   Communication module
#   Author: Yotam Salmon
#   Last Edited: 29/12/17
# 
 
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
 
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):

        if self.path.split("/")[1] in handlers.keys():
            response, headers, content = handlers[self.path.split("/")[1]](self)
            
            self.send_response(response)
            for h, v in headers.items():
                self.send_header(h, v)
            self.end_headers()

            self.wfile.write(bytes(content, "utf8"))

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(bytes("404 - Not Found", "utf8"))
        return

handlers = {}

def run():
    print('Running server...')
    server_address = ('', 9090)
    httpd = HTTPServer(server_address, RequestHandler)
    thread = threading.Thread(target=httpd.serve_forever)
    thread.start()
    return httpd


def handler(url):
    global handlers
    def handler_decorator(func):
        global handlers
        handlers[url] = func
        return func
    return handler_decorator