from __future__ import annotations
import json
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs,urlparse
from .project_engine import inspect_project
from .project_graph import build_graph,query_graph
from .git_engine import status,diff
from .agent_gateway import discovery_payload

class Handler(BaseHTTPRequestHandler):
 root=Path(".")
 def _send(self,data,code=200):
  raw=json.dumps(data).encode();self.send_response(code);self.send_header("Content-Type","application/json")
  self.send_header("Content-Length",str(len(raw)));self.end_headers();self.wfile.write(raw)
 def do_GET(self):
  u=urlparse(self.path);q=parse_qs(u.query);root=self.root.resolve()
  try:
   if u.path=="/health":return self._send({"ok":True,"service":"godtree"})
   if u.path=="/project":return self._send(inspect_project(root))
   if u.path=="/graph":
    g=build_graph(root);needle=q.get("q",[None])[0]
    return self._send(query_graph(g,needle) if needle else g)
   if u.path=="/git/status":return self._send(status(root))
   if u.path=="/git/diff":return self._send({"diff":diff(root,q.get("staged",["0"])[0]=="1")})
   if u.path=="/agents":return self._send(discovery_payload())
   return self._send({"error":"not found"},404)
  except Exception as e:return self._send({"error":str(e)},500)
 def log_message(self,*_):pass

def serve(root:Path,host:str="127.0.0.1",port:int=7331):
 Handler.root=root.resolve();server=ThreadingHTTPServer((host,port),Handler);server.serve_forever()
