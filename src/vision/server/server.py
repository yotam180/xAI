#
#   Communication module
#   Author: Yotam Salmon
#   Last Edited: 29/12/17
# 
 
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

import static_files
 
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
            if "Access-Control-Allow-Origin" not in headers.keys():
                self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()

            self.wfile.write(bytes(content, "utf8"))

        else:
            page, mime = static_files.get(self.path)

            if page is None:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(bytes("404 - Not Found", "utf8"))

            else:
                self.send_response(200)
                self.send_header("Conten-Type", mime)
                self.end_headers()
                self.wfile.write(bytes(page, "utf-8") if type(page) == str else page)
        return

    def do_POST(self):
        global _get_handlers, _post_handlers

        handler = self.path.split("/")[1].split("#")[0].split("?")[0]

        if handler in _post_handlers.keys():
            response, headers, content = _post_handlers[handler](self)
            
            self.send_response(response)
            for h, v in headers.items():
                self.send_header(h, v)
            if "Access-Control-Allow-Origin" not in headers.keys():
                self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()

            self.wfile.write(bytes(content, "utf8"))

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(bytes("404 - Not Found", "utf8"))
        return
    
    def parse_get(self):
        """
        Returns the GET parameters of a request. Same as the querystring method in http_helper,
        but less reliable.
        """
        path = self.path
        path = path.split("?")
        args = path[1]
        args = args.split("&")
        get_dict = {}
        for i in args:
            part = i.split("=")
            get_dict[part[0]] = part[1]
        return get_dict

def run() -> None:
    print('Running server...')
    server_address = ('', 80)
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
