import tempfile,unittest
from pathlib import Path
from vibe_code_genius.capability_router import route
from vibe_code_genius.validator_engine import run_command
class RuntimeTests(unittest.TestCase):
 def test_deterministic_route(self):self.assertEqual(route("test")["executor"],"godtree-local")
 def test_validator_receipt(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d);r=run_command(p,["python","-c","print('ok')"],p/"r.json")
   self.assertEqual(r["status"],"passed");self.assertTrue((p/"r.json").exists())
if __name__=="__main__":unittest.main()
