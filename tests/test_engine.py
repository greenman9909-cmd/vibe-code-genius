import json, tempfile, unittest
from pathlib import Path
from vibe_code_genius.engine import load_tree, topo_order, plan
class EngineTests(unittest.TestCase):
    def test_tree_order(self):
        root=Path(__file__).resolve().parents[1]; tree=load_tree(root); order=topo_order(tree); self.assertEqual(len(order),61); self.assertLess(order.index('01'),order.index('01a'))
    def test_plan(self):
        root=Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as d:
            result=plan('Build a dashboard',Path(d),root); self.assertEqual(result['nodes'],61); self.assertTrue((Path(d)/'plan.md').exists())
if __name__=='__main__': unittest.main()
