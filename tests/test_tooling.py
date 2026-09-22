import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from vibe_code_genius.tooling import ToolStatus, acquire_reference, check_tools


class ToolingTests(unittest.TestCase):
    def test_preflight_uses_path(self):
        with patch("vibe_code_genius.tooling.shutil.which", side_effect=lambda name: f"/mock/{name}"):
            statuses=check_tools()
        self.assertTrue(all(s.available for s in statuses))
        self.assertEqual({s.name for s in statuses},{"spa-ripper","sitemapx","apiresearch"})

    def test_acquisition_writes_cached_reference_source(self):
        statuses={
            "spa-ripper":ToolStatus("spa-ripper",True,"/mock/spa-ripper","install spa"),
            "sitemapx":ToolStatus("sitemapx",True,"/mock/sitemapx","install sx"),
            "apiresearch":ToolStatus("apiresearch",True,"/mock/apiresearch","install api"),
        }
        def fake_run(command, *, timeout_seconds, display_command=None):
            out=None
            if "spa-ripper" in command[0]:
                out=Path(command[command.index("-o")+1])
                out.mkdir(parents=True,exist_ok=True)
                (out/"index.html").write_text("<html></html>")
            elif "sitemapx" in command[0]:
                out=Path(command[command.index("--out")+1])
                out.mkdir(parents=True,exist_ok=True)
                (out/"endpoints.txt").write_text("https://example.com/api/health\n")
                (out/"report.json").write_text("{}")
            elif "apiresearch" in command[0]:
                out=Path(command[command.index("--out")+1])
                out.mkdir(parents=True,exist_ok=True)
                (out/"api_research.json").write_text('{"status":"complete"}')
            return {"status":"complete","command":display_command or command,"exit_code":0,"stdout_tail":"","stderr_tail":""}

        with tempfile.TemporaryDirectory() as d, \
             patch("vibe_code_genius.tooling._status_map", return_value=statuses), \
             patch("vibe_code_genius.tooling._run_command", side_effect=fake_run):
            result=acquire_reference("https://example.com",Path(d),strict_tools=True)
            source=json.loads((Path(d)/"reference-source.json").read_text())
            reference=json.loads((Path(d)/"reference.json").read_text())
            self.assertEqual(result["status"],"complete")
            self.assertEqual(source["mode"],"cached")
            self.assertTrue(Path(source["report_path"]).exists())
            self.assertEqual(reference["api_surface"],["https://example.com/api/health"])

if __name__=="__main__":
    unittest.main()
