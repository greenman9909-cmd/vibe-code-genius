from __future__ import annotations
import json,subprocess,time
from pathlib import Path
def run_command(workspace:Path,command:list[str],receipt:Path,timeout:int=900)->dict:
 if not command:raise ValueError("command required")
 started=time.time()
 try:
  p=subprocess.run(command,cwd=workspace,capture_output=True,text=True,timeout=timeout,check=False)
  status="passed" if p.returncode==0 else "failed"; code=p.returncode
  stdout=p.stdout[-12000:];stderr=p.stderr[-12000:]
 except subprocess.TimeoutExpired as e:
  status="failed";code=124;stdout=(e.stdout or "")[-12000:];stderr="validator timeout"
 data={"kind":"command","command":command,"workspace":str(workspace.resolve()),"status":status,"exit_code":code,
 "duration_ms":round((time.time()-started)*1000),"stdout":stdout,"stderr":stderr}
 receipt.parent.mkdir(parents=True,exist_ok=True);receipt.write_text(json.dumps(data,indent=2)+"\n",encoding="utf-8");return data
