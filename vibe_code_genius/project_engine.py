from __future__ import annotations
import hashlib, json, subprocess
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

@dataclass(frozen=True)
class Project:
    version:str
    id:str
    name:str
    workspace:str
    git:dict[str,Any]
    policy:dict[str,Any]

def _git(repo:Path,*args:str)->subprocess.CompletedProcess[str]:
    return subprocess.run(["git","-C",str(repo),*args],capture_output=True,text=True,check=False)

def inspect_git(repo:Path)->dict[str,Any]:
    if not (repo/".git").exists():
        return {"enabled":False,"remote":None,"default_branch":None,"branch":None,"dirty":[]}
    branch=_git(repo,"branch","--show-current").stdout.strip() or None
    remote=_git(repo,"remote","get-url","origin").stdout.strip() or None
    dirty=[x[3:] for x in _git(repo,"status","--porcelain").stdout.splitlines() if len(x)>3]
    return {"enabled":True,"remote":remote,"default_branch":None,"branch":branch,"dirty":dirty}

def register_project(workspace:Path, store:Path)->Project:
    workspace=workspace.resolve()
    if not workspace.is_dir(): raise FileNotFoundError(workspace)
    pid=hashlib.sha256(str(workspace).encode()).hexdigest()[:12]
    git=inspect_git(workspace)
    project=Project("1.0.0",pid,workspace.name,str(workspace),
        {"enabled":git["enabled"],"remote":git["remote"],"default_branch":git["default_branch"]},
        {"zero_cost_first":True,"require_confirmation_for_push":True,"require_confirmation_for_deploy":True})
    store.mkdir(parents=True,exist_ok=True)
    (store/f"{pid}.json").write_text(json.dumps(asdict(project),indent=2)+"\n",encoding="utf-8")
    return project

def inspect_project(workspace:Path)->dict[str,Any]:
    workspace=workspace.resolve()
    git=inspect_git(workspace)
    markers={
      "python":(workspace/"pyproject.toml").exists() or (workspace/"requirements.txt").exists(),
      "node":(workspace/"package.json").exists(),
      "nextjs":(workspace/"next.config.js").exists() or (workspace/"next.config.mjs").exists() or (workspace/"next.config.ts").exists(),
      "supabase":(workspace/"supabase").is_dir(),
    }
    return {"workspace":str(workspace),"name":workspace.name,"stack":[k for k,v in markers.items() if v],"git":git}
