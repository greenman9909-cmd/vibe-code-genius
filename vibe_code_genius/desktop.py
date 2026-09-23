from __future__ import annotations
import json,threading,webbrowser
from pathlib import Path
import tkinter as tk
from tkinter import filedialog,messagebox,ttk
from .project_engine import inspect_project
from .project_graph import build_graph
from .git_engine import status,diff
from .agent_gateway import discovery_payload
from .mission_engine import create_mission

BG="#101113";PANEL="#17181b";TEXT="#f3f4f6";MUTED="#9ca3af";ACCENT="#7c8cff"

class GodTree(tk.Tk):
 def __init__(self):
  super().__init__();self.title("GodTree OS");self.geometry("1280x780");self.minsize(1000,650)
  self.configure(bg=BG);self.repo=None;self._style();self._shell()
 def _style(self):
  s=ttk.Style(self);s.theme_use("clam")
  s.configure("TFrame",background=BG);s.configure("TLabel",background=BG,foreground=TEXT,font=("Segoe UI",10))
  s.configure("Nav.TButton",background=BG,foreground=TEXT,padding=(14,10),relief="flat")
  s.configure("Primary.TButton",background=ACCENT,foreground="white",padding=(14,9),relief="flat")
 def _shell(self):
  top=ttk.Frame(self);top.pack(fill="x",padx=18,pady=(14,8))
  ttk.Label(top,text="GodTree",font=("Segoe UI Semibold",17)).pack(side="left")
  ttk.Button(top,text="Open Project",style="Primary.TButton",command=self.open_project).pack(side="right")
  body=ttk.Frame(self);body.pack(fill="both",expand=True,padx=18,pady=(0,14))
  nav=ttk.Frame(body,width=190);nav.pack(side="left",fill="y",padx=(0,14));nav.pack_propagate(False)
  for name in ("Projects","Work","Git","Activity"):
   ttk.Button(nav,text=name,style="Nav.TButton",command=lambda n=name:self.show(n)).pack(fill="x",pady=2)
  self.canvas=tk.Text(body,bg=PANEL,fg=TEXT,insertbackground=TEXT,relief="flat",font=("Cascadia Mono",10),padx=22,pady=20,wrap="word")
  self.canvas.pack(side="left",fill="both",expand=True);self.show("Projects")
 def write(self,obj):
  self.canvas.config(state="normal");self.canvas.delete("1.0","end")
  self.canvas.insert("end",obj if isinstance(obj,str) else json.dumps(obj,indent=2));self.canvas.config(state="disabled")
 def open_project(self):
  p=filedialog.askdirectory(title="Open project")
  if p:self.repo=Path(p);self.show("Projects")
 def show(self,name):
  if not self.repo:return self.write("Open a project to begin.\n\nGodTree keeps repository facts, missions, validation receipts and Git state local.")
  try:
   if name=="Projects":self.write(inspect_project(self.repo))
   elif name=="Git":self.write({"status":status(self.repo),"diff":diff(self.repo)})
   elif name=="Work":
    g=build_graph(self.repo);self.write({"project":self.repo.name,"graph_nodes":len(g["nodes"]),"relationships":len(g["edges"]),"god_nodes":g["god_nodes"],"agents":discovery_payload()["agents"]})
   else:self.write("Activity receipts live under .godtree/ in this project.\n\nNo fabricated activity is shown.")
  except Exception as e:self.write({"error":str(e)})
 def new_mission(self):
  if self.repo:create_mission("New mission",self.repo,self.repo/".godtree/missions")

def main():GodTree().mainloop()
if __name__=="__main__":main()
