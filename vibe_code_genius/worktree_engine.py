from __future__ import annotations
import re,subprocess
from pathlib import Path

SAFE=re.compile(r"[^a-zA-Z0-9._/-]+")
def _run(repo:Path,*args:str):
 p=subprocess.run(["git","-C",str(repo),*args],capture_output=True,text=True,check=False)
 if p.returncode:raise RuntimeError(p.stderr.strip() or p.stdout.strip())
 return p.stdout.strip()
def mission_worktree(repo:Path,mission_id:str,root:Path)->dict:
 slug=SAFE.sub("-",mission_id).strip("-/") or "mission"
 branch=f"godtree/{slug}"; target=(root/slug).resolve();target.parent.mkdir(parents=True,exist_ok=True)
 _run(repo,"worktree","add","-b",branch,str(target),"HEAD")
 return {"branch":branch,"workspace":str(target)}
def remove_worktree(repo:Path,path:Path):
 _run(repo,"worktree","remove",str(path.resolve()))
