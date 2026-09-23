from __future__ import annotations

import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


class GodTreeHandler(BaseHTTPRequestHandler):
    project = Path('.')

    def respond(self, payload, code=200):
        data = json.dumps(payload, indent=2).encode('utf-8')
        self.send_response(code)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        if self.path == '/health':
            return self.respond({'status': 'online', 'service': 'godtree-daemon'})
        if self.path == '/project':
            return self.respond({'workspace': str(self.project.resolve())})
        return self.respond({'error': 'unknown endpoint'}, 404)

    def log_message(self, *_args):
        pass


def start_daemon(port=7331, workspace='.'):
    GodTreeHandler.project = Path(workspace)
    server = ThreadingHTTPServer(('127.0.0.1', port), GodTreeHandler)
    server.serve_forever()
