from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from pathlib import Path

class GodTreeHandler(BaseHTTPRequestHandler):
    project = Path('.')

    def respond(self, payload):
        data=json.dumps(payload).encode()
        self.send_response(200)
        self.send_header('Content-Type','application/json')
        self.send_header('Content-Length',str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        if self.path == '/health':
            self.respond({'status':'online','service':'godtree-daemon'})
        elif self.path == '/project':
            self.respond({'workspace':str(self.project.resolve())})
        else:
            self.respond({'error':'unknown endpoint'})

    def log_message(self,*args):
        pass

def start_daemon(port=7331):
    server=HTTPServer(('127.0.0.1',port),GodTreeHandler)
    server.serve_forever()
