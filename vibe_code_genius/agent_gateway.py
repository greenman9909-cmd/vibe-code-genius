from __future__ import annotations
import json, os, shutil, subprocess
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

@dataclass(frozen=True)
class AgentStatus:
    id: str
    kind: str
    available: bool
    resolved: str | None
    mode: str
    note: str = ""

CLI_CANDIDATES = {
    "codex": ["codex"],
    "claude": ["claude"],
    "gemini": ["gemini"],
    "aider": ["aider"],
}
ENV_COMMANDS = {
    "antigravity": "GODTREE_ANTIGRAVITY_COMMAND",
    "manus": "GODTREE_MANUS_COMMAND",
}

def discover_agents() -> list[AgentStatus]:
    out=[]
    for name,candidates in CLI_CANDIDATES.items():
        resolved=next((shutil.which(c) for c in candidates if shutil.which(c)),None)
        out.append(AgentStatus(name,"cli",resolved is not None,resolved,"automatic" if resolved else "unavailable"))
    for name,env in ENV_COMMANDS.items():
        command=os.getenv(env)
        resolved=shutil.which(command) if command and " " not in command else command
        out.append(AgentStatus(name,"external",bool(command),resolved,"automatic" if command else "manual",
            f"Set {env} only to a supported local CLI/adapter command; GodTree does not infer private interfaces."))
    out.append(AgentStatus("chatgpt-bridge","human",True,None,"human-bridge",
        "Exports a compact task packet for use in the ChatGPT app; no API key required."))
    return out

def discovery_payload() -> dict[str,Any]:
    agents=discover_agents()
    return {"policy":"zero-cost-first","agents":[asdict(a) for a in agents]}

def create_task_packet(objective:str, repo:Path, out:Path, *, allowed:list[str]|None=None,
                       forbidden:list[str]|None=None, acceptance:list[str]|None=None) -> Path:
    repo=repo.resolve()
    if not repo.exists(): raise FileNotFoundError(repo)
    out.parent.mkdir(parents=True,exist_ok=True)
    changed=[]
    if (repo/".git").exists():
        p=subprocess.run(["git","-C",str(repo),"status","--porcelain"],capture_output=True,text=True,check=False)
        changed=[line[3:] for line in p.stdout.splitlines() if len(line)>3][:100]
    packet={
      "version":"1.0.0","objective":objective,"workspace":str(repo),
      "policy":{"cost":"zero-cost-first","write_scope":"explicit","success_claims":"validator-owned"},
      "allowed_paths":allowed or [],"forbidden_paths":forbidden or [],
      "acceptance":acceptance or [],"working_tree_changes":changed,
      "instructions":[
        "Return an implementation or patch that satisfies the acceptance criteria.",
        "Do not claim tests passed unless their output is provided.",
        "Do not modify forbidden paths.",
        "Prefer deterministic local checks over additional AI calls."
      ]}
    out.write_text(json.dumps(packet,indent=2)+"\n",encoding="utf-8")
    return out
