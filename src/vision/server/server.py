#
#   Communication module
#   Author: Yotam Salmon
#   Last Edited: 29/12/17
# 
 
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
 
_get_handlers = {}
_post_handlers = {}

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global _get_handlers, _post_handlers

        handler = self.path.split("/")[1].split("#")[0].split("?")[0]

        if handler in _get_handlers.keys():
            response, headers, content = _get_handlers[handler](self)
            
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

    def do_POST(self):
        global _get_handlers, _post_handlers

        handler = self.path.split("/")[1].split("#")[0].split("?")[0]

        if handler in _post_handlers.keys():
            response, headers, content = _post_handlers[handler](self)
            
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
    
    def parseGet(self):
        path = self.path
        path = path.split("?")
        args = path[1]
        args = args.split("&")
        GetDict = {}
        for i in args:
            part = i.split("=")
            GetDict[part[0]] = part[1]
        return GetDict

def run() -> None:
    print('Running server...')
    server_address = ('', 9090)
    httpd = HTTPServer(server_address, RequestHandler)
    thread = threading.Thread(target=httpd.serve_forever)
    thread.start()
    return httpd


def handler(url: str, method: str = "GET"):
    global _get_handlers, _post_handlers
    def handler_decorator(func):
        global handlers
        (_get_handlers if method.upper() == "GET" else _post_handlers)[url] = func
        return func
    return handler_decorator
