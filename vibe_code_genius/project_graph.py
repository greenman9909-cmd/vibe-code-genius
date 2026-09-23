from __future__ import annotations
import ast, json, re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

IGNORED={".git",".godtree","node_modules",".next","dist","build",".venv","venv","__pycache__"}
TEXT_EXT={".py",".js",".jsx",".ts",".tsx",".json",".md",".css",".html",".sql",".toml",".yaml",".yml"}

@dataclass(frozen=True)
class Node:
 id:str; kind:str; path:str; label:str
@dataclass(frozen=True)
class Edge:
 source:str; target:str; kind:str; evidence:str

def _files(root:Path)->Iterable[Path]:
 for p in root.rglob("*"):
  if not p.is_file() or any(x in IGNORED for x in p.parts): continue
  if p.suffix.lower() in TEXT_EXT: yield p

def _id(root:Path,p:Path)->str: return p.relative_to(root).as_posix()

def _python_edges(root:Path,p:Path,text:str)->list[Edge]:
 out=[]; src=_id(root,p)
 try: tree=ast.parse(text)
 except SyntaxError:return out
 for n in ast.walk(tree):
  name=None
  if isinstance(n,ast.ImportFrom): name=n.module
  elif isinstance(n,ast.Import) and n.names:name=n.names[0].name
  if not name:continue
  candidate=root.joinpath(*name.split("."))
  choices=[candidate.with_suffix(".py"),candidate/"__init__.py"]
  for q in choices:
   if q.exists():
    out.append(Edge(src,_id(root,q),"imports",f"line {getattr(n,'lineno','?')}: {name}"));break
 return out

_JS_IMPORT=re.compile(r"""(?:from\s+|import\s*\(\s*)['"]([^'"]+)['"]""")
def _js_edges(root:Path,p:Path,text:str)->list[Edge]:
 out=[]; src=_id(root,p)
 for m in _JS_IMPORT.finditer(text):
  raw=m.group(1)
  if not raw.startswith("."):continue
  base=(p.parent/raw).resolve()
  for q in [base,base.with_suffix(".ts"),base.with_suffix(".tsx"),base.with_suffix(".js"),base.with_suffix(".jsx"),base/"index.ts",base/"index.tsx",base/"index.js"]:
   if q.is_file():
    try: target=_id(root,q)
    except ValueError:continue
    out.append(Edge(src,target,"imports",raw));break
 return out

def build_graph(workspace:Path)->dict:
 root=workspace.resolve(); nodes=[]; edges=[]
 for p in _files(root):
  rel=_id(root,p); nodes.append(Node(rel,"file",rel,p.name))
  try:text=p.read_text(encoding="utf-8")
  except UnicodeDecodeError:continue
  if p.suffix==".py":edges.extend(_python_edges(root,p,text))
  elif p.suffix in {".js",".jsx",".ts",".tsx"}:edges.extend(_js_edges(root,p,text))
 inbound={n.id:0 for n in nodes}
 outbound={n.id:0 for n in nodes}
 for e in edges:
  inbound[e.target]=inbound.get(e.target,0)+1;outbound[e.source]=outbound.get(e.source,0)+1
 ranked=sorted(nodes,key=lambda n:(inbound.get(n.id,0),outbound.get(n.id,0)),reverse=True)
 return {"version":"1.0.0","workspace":str(root),"nodes":[asdict(n) for n in nodes],"edges":[asdict(e) for e in edges],
 "god_nodes":[{"id":n.id,"inbound":inbound.get(n.id,0),"outbound":outbound.get(n.id,0)} for n in ranked[:12] if inbound.get(n.id,0)>0]}

def save_graph(workspace:Path,out:Path)->Path:
 payload=build_graph(workspace);out.parent.mkdir(parents=True,exist_ok=True)
 out.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8");return out

def query_graph(payload:dict,needle:str,limit:int=20)->dict:
 q=needle.lower();hits=[n for n in payload["nodes"] if q in n["id"].lower() or q in n["label"].lower()]
 ids={n["id"] for n in hits}; edges=[e for e in payload["edges"] if e["source"] in ids or e["target"] in ids]
 return {"query":needle,"nodes":hits[:limit],"edges":edges[:limit*3]}
