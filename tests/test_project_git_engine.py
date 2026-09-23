import subprocess,tempfile,unittest
from pathlib import Path
from vibe_code_genius.project_engine import register_project,inspect_project
from vibe_code_genius.git_engine import create_branch,stage,commit,status,push_command

class ProjectGitEngineTests(unittest.TestCase):
 def _repo(self):
  t=tempfile.TemporaryDirectory(); p=Path(t.name)
  subprocess.run(["git","init",str(p)],capture_output=True,check=True)
  subprocess.run(["git","-C",str(p),"config","user.email","test@example.com"],check=True)
  subprocess.run(["git","-C",str(p),"config","user.name","Test"],check=True)
  (p/"README.md").write_text("hi\n")
  subprocess.run(["git","-C",str(p),"add","README.md"],check=True)
  subprocess.run(["git","-C",str(p),"commit","-m","init"],capture_output=True,check=True)
  return t,p
 def test_register_and_inspect(self):
  t,p=self._repo()
  try:
   pr=register_project(p,p/".godtree/projects")
   self.assertTrue(pr.git["enabled"]); self.assertIn("git",inspect_project(p))
  finally:t.cleanup()
 def test_safe_git_flow(self):
  t,p=self._repo()
  try:
   create_branch(p,"mission/test"); (p/"x.txt").write_text("x")
   stage(p,["x.txt"]); result=commit(p,"test: add x")
   self.assertTrue(result["commit"]); self.assertEqual(status(p)["changes"],[])
   self.assertEqual(push_command(p)[-1],"mission/test")
  finally:t.cleanup()
 def test_stage_rejects_escape(self):
  t,p=self._repo()
  try:
   with self.assertRaises(ValueError): stage(p,["../escape.txt"])
  finally:t.cleanup()

if __name__=="__main__": unittest.main()
