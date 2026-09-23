import json,tempfile,unittest
from pathlib import Path
from vibe_code_genius.project_graph import build_graph,query_graph
from vibe_code_genius.mission_engine import create_mission,record_receipt

class GraphMissionTests(unittest.TestCase):
 def test_graph_imports_and_god_nodes(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d);(p/"core.py").write_text("VALUE=1\n");(p/"a.py").write_text("import core\n");(p/"b.py").write_text("import core\n")
   g=build_graph(p)
   self.assertEqual(len(g["edges"]),2);self.assertEqual(g["god_nodes"][0]["id"],"core.py")
   self.assertTrue(query_graph(g,"core")["edges"])
 def test_mission_receipts_own_status(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d);m=create_mission("ship it",p,p/"missions")
   r=record_receipt(m,"inspect","repo_graph","passed",{"nodes":3})
   self.assertEqual(r["status"],"passed")
   data=json.loads(m.read_text());self.assertEqual(data["status"],"running")
   record_receipt(m,"verify","tests","failed",{"exit_code":1})
   self.assertEqual(json.loads(m.read_text())["status"],"failed")

if __name__=="__main__":unittest.main()
