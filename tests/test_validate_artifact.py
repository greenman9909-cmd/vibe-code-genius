import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


class ValidateArtifactTests(unittest.TestCase):
    def test_tsx_declared_artifact_is_validated_as_text(self):
        repo = Path(__file__).resolve().parents[1]
        validator = repo / "scripts" / "validate-artifact.py"
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            artifact = tmp_path / "pages.tsx"
            schema = tmp_path / "pages.schema.json"
            artifact.write_text(
                "/** pages */\n" + ("export const pages = [];\n" * 30),
                encoding="utf-8",
            )
            schema.write_text(
                json.dumps({"required_headings": ["pages"]}),
                encoding="utf-8",
            )
            result = subprocess.run(
                [
                    sys.executable,
                    str(validator),
                    "--node",
                    "13",
                    "--artifact",
                    str(artifact),
                    "--schema",
                    str(schema),
                ],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("PASS: node 13", result.stdout)


if __name__ == "__main__":
    unittest.main()
