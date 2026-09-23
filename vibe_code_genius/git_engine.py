from __future__ import annotations
import subprocess
from pathlib import Path
from typing import Any

class GitError(RuntimeError): pass

def _run(repo:Path,args:list[str])->subprocess.CompletedProcess[str]:
    p=subprocess.run(["git","-C",str(repo),*args],capture_output=True,text=True,check=False)
    if p.returncode: raise GitError(p.stderr.strip() or p.stdout.strip() or "git command failed")
    return p

def status(repo:Path)->dict[str,Any]:
    branch=_run(repo,["branch","--show-current"]).stdout.strip()
    rows=_run(repo,["status","--porcelain"]).stdout.splitlines()
    return {"branch":branch,"changes":[{"code":r[:2],"path":r[3:]} for r in rows if len(r)>3]}

def diff(repo:Path,staged:bool=False)->str:
    args=["diff"]
    if staged: args.append("--cached")
    return _run(repo,args).stdout

def create_branch(repo:Path,name:str)->dict[str,str]:
    if not name or name.startswith("-") or any(c.isspace() for c in name):
        raise ValueError("invalid branch name")
    _run(repo,["check-ref-format","--branch",name])
    _run(repo,["switch","-c",name])
    return {"branch":name}

def stage(repo:Path,paths:list[str])->dict[str,Any]:
    if not paths: raise ValueError("explicit paths are required")
    root=repo.resolve()
    safe=[]
    for raw in paths:
        p=(root/raw).resolve()
        try:p.relative_to(root)
        except ValueError: raise ValueError(f"path escapes workspace: {raw}")
        safe.append(raw)
    _run(repo,["add","--",*safe])
    return {"staged":safe}

def commit(repo:Path,message:str)->dict[str,str]:
    if not message.strip(): raise ValueError("commit message required")
    _run(repo,["commit","-m",message])
    sha=_run(repo,["rev-parse","HEAD"]).stdout.strip()
    return {"commit":sha,"message":message}

def push_command(repo:Path,remote:str="origin")->list[str]:
    branch=_run(repo,["branch","--show-current"]).stdout.strip()
    if not branch: raise GitError("detached HEAD cannot be pushed by GodTree")
    return ["git","-C",str(repo.resolve()),"push","-u",remote,branch]
