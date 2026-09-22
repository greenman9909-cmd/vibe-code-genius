from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit


@dataclass(frozen=True)
class ToolStatus:
    name: str
    available: bool
    resolved: str | None
    install: str
    note: str = ""


INSTALL_COMMANDS = {
    "spa-ripper": "git clone https://github.com/greenman9909-cmd/spa-ripper.git && cd spa-ripper && python -m pip install -e .",
    "sitemapx": "git clone https://github.com/greenman9909-cmd/SiteMap-X_Owais.git && cd SiteMap-X_Owais && python -m pip install -e .",
    "apiresearch": "git clone https://github.com/greenman9909-cmd/api-researcher.git && cd api-researcher && python -m pip install -e .",
    "slopmonster": "git clone https://github.com/ItsssssJack/SlopMonster.git && set SLOPMONSTER_HOME to that directory",
}


def _now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _slopmonster_home() -> Path | None:
    candidates: list[Path] = []
    if os.getenv("SLOPMONSTER_HOME"):
        candidates.append(Path(os.environ["SLOPMONSTER_HOME"]))
    candidates.extend([
        Path.cwd() / "SlopMonster",
        Path.cwd().parent / "SlopMonster",
    ])
    for candidate in candidates:
        if (candidate / "tools" / "deslop.py").is_file():
            return candidate.resolve()
    return None


def check_tools(include_slopmonster: bool = False) -> list[ToolStatus]:
    statuses = [
        ToolStatus("spa-ripper", bool(shutil.which("spa-ripper")), shutil.which("spa-ripper"), INSTALL_COMMANDS["spa-ripper"]),
        ToolStatus("sitemapx", bool(shutil.which("sitemapx")), shutil.which("sitemapx"), INSTALL_COMMANDS["sitemapx"]),
        ToolStatus("apiresearch", bool(shutil.which("apiresearch")), shutil.which("apiresearch"), INSTALL_COMMANDS["apiresearch"]),
    ]
    if include_slopmonster:
        home = _slopmonster_home()
        statuses.append(ToolStatus(
            "slopmonster",
            home is not None,
            str(home / "tools" / "deslop.py") if home else None,
            INSTALL_COMMANDS["slopmonster"],
            "SlopMonster is a repository script, not a pip console entry point.",
        ))
    return statuses


def preflight_payload(include_slopmonster: bool = False) -> dict[str, Any]:
    statuses = check_tools(include_slopmonster=include_slopmonster)
    return {
        "status": "ready" if all(s.available for s in statuses) else "missing-tools",
        "tools": [asdict(s) for s in statuses],
    }


def _validate_reference_url(url: str) -> None:
    parts = urlsplit(url)
    if parts.scheme not in {"http", "https"} or not parts.netloc:
        raise ValueError("reference URL must be an absolute http:// or https:// URL")


def _run_command(
    command: list[str],
    *,
    timeout_seconds: int,
    display_command: list[str] | None = None,
) -> dict[str, Any]:
    started = _now()
    proc = subprocess.run(
        command,
        capture_output=True,
        text=True,
        timeout=timeout_seconds,
        check=False,
    )
    return {
        "status": "complete" if proc.returncode == 0 else "failed",
        "command": display_command or command,
        "exit_code": proc.returncode,
        "started_at": started,
        "finished_at": _now(),
        "stdout_tail": proc.stdout[-4000:],
        "stderr_tail": proc.stderr[-4000:],
    }


def _status_map() -> dict[str, ToolStatus]:
    return {s.name: s for s in check_tools(include_slopmonster=False)}


def _read_endpoint_lines(path: Path | None) -> list[str]:
    if not path or not path.is_file():
        return []
    lines = []
    for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
        value = raw.strip()
        if value and not value.startswith("#"):
            lines.append(value)
    return sorted(set(lines))


def acquire_reference(
    reference_url: str,
    out: Path,
    *,
    with_api: bool = True,
    strict_tools: bool = False,
    auth_header: str | None = None,
    timeout_seconds: int = 300,
) -> dict[str, Any]:
    """Run real reference acquisition tools and persist evidence/provenance.

    This function never fabricates tool output. Missing tools are recorded. At least
    one of SPA-Ripper or SiteMap-X must complete successfully.
    """
    _validate_reference_url(reference_url)
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    acquisition_root = out / "acquisition"
    acquisition_root.mkdir(parents=True, exist_ok=True)

    statuses = _status_map()
    runs: dict[str, dict[str, Any]] = {}

    spa_dir = acquisition_root / "spa-ripper"
    spa = statuses["spa-ripper"]
    if spa.available and spa.resolved:
        spa_dir.mkdir(parents=True, exist_ok=True)
        runs["spa-ripper"] = _run_command(
            [spa.resolved, "clone", reference_url, "-o", str(spa_dir), "-t", "20"],
            timeout_seconds=timeout_seconds,
        )
    else:
        runs["spa-ripper"] = {"status": "missing", "install": spa.install}

    sitemap_dir = acquisition_root / "sitemapx"
    sx = statuses["sitemapx"]
    if sx.available and sx.resolved:
        sitemap_dir.mkdir(parents=True, exist_ok=True)
        runs["sitemapx"] = _run_command(
            [
                sx.resolved,
                reference_url,
                "--out",
                str(sitemap_dir),
                "--depth",
                "3",
                "--output-format",
                "html,json,md,txt",
            ],
            timeout_seconds=timeout_seconds,
        )
    else:
        runs["sitemapx"] = {"status": "missing", "install": sx.install}

    acquisition_success = [
        name for name in ("spa-ripper", "sitemapx")
        if runs[name].get("status") == "complete"
    ]
    if not acquisition_success:
        installs = "\n".join(
            f"- {name}: {statuses[name].install}" for name in ("spa-ripper", "sitemapx")
        )
        raise RuntimeError(
            "reference acquisition failed: neither SPA-Ripper nor SiteMap-X completed.\n"
            + installs
        )

    endpoints_path: Path | None = None
    for candidate in (
        sitemap_dir / "endpoints.txt",
        spa_dir / "endpoints.txt",
    ):
        if candidate.is_file():
            endpoints_path = candidate
            break

    api_dir = acquisition_root / "api-research"
    if with_api and endpoints_path is not None:
        ar = statuses["apiresearch"]
        if ar.available and ar.resolved:
            api_dir.mkdir(parents=True, exist_ok=True)
            command = [
                ar.resolved,
                "--endpoints",
                str(endpoints_path),
                "--out",
                str(api_dir),
            ]
            display = list(command)
            if auth_header is not None:
                command.extend(["--auth-header", auth_header])
                display.extend(["--auth-header", "<redacted>"])
            runs["apiresearch"] = _run_command(
                command,
                timeout_seconds=timeout_seconds,
                display_command=display,
            )
        else:
            runs["apiresearch"] = {"status": "missing", "install": ar.install}
    elif with_api:
        runs["apiresearch"] = {
            "status": "skipped",
            "reason": "no endpoints.txt was produced by acquisition",
        }
    else:
        runs["apiresearch"] = {"status": "skipped", "reason": "API research disabled"}

    if strict_tools:
        required_failures = [
            name for name, run in runs.items()
            if name in {"spa-ripper", "sitemapx"}
            and run.get("status") != "complete"
        ]
        if with_api and endpoints_path is not None and runs["apiresearch"].get("status") != "complete":
            required_failures.append("apiresearch")
        if required_failures:
            raise RuntimeError("strict tool mode failed: " + ", ".join(sorted(set(required_failures))))

    endpoint_lines = _read_endpoint_lines(endpoints_path)
    evidence = []
    if runs["spa-ripper"].get("status") == "complete":
        evidence.append(f"SPA-Ripper clone: {spa_dir}")
    if runs["sitemapx"].get("status") == "complete":
        evidence.append(f"SiteMap-X report: {sitemap_dir / 'report.json'}")
    if runs["apiresearch"].get("status") == "complete":
        evidence.append(f"api-researcher profile: {api_dir / 'api_research.json'}")

    reference = {
        "version": "1.0.0",
        "status": "complete",
        "reference_url": reference_url,
        "acquired_at": _now(),
        "acquirer": "+".join(
            name for name in ("spa-ripper", "sitemapx", "apiresearch")
            if runs.get(name, {}).get("status") == "complete"
        ),
        "stack": {},
        "routes": endpoint_lines,
        "sections": {},
        "components": [],
        "design_tokens": {},
        "api_surface": endpoint_lines,
        "external_hosts": [],
        "evidence": evidence,
    }
    reference_path = out / "reference.json"
    _write_json(reference_path, reference)

    manifest = {
        "version": "1.0.0",
        "status": "complete" if all(
            run.get("status") in {"complete", "skipped"} for run in runs.values()
        ) else "degraded",
        "reference_url": reference_url,
        "generated_at": _now(),
        "runs": runs,
    }
    manifest_path = out / "acquisition-manifest.json"
    _write_json(manifest_path, manifest)

    source: dict[str, Any] = {
        "mode": "cached",
        "reference_url": reference_url,
        "report_path": str(reference_path.resolve()),
        "acquisition_manifest_path": str(manifest_path.resolve()),
        "note": "Generated by vibe-tree acquire from commands that actually executed; see acquisition-manifest.json.",
    }
    if runs["spa-ripper"].get("status") == "complete":
        source["mirror_path"] = str(spa_dir.resolve())
    elif (sitemap_dir / "mirror").is_dir():
        source["mirror_path"] = str((sitemap_dir / "mirror").resolve())
    if endpoints_path is not None:
        source["endpoints_path"] = str(endpoints_path.resolve())
    api_research_path = api_dir / "api_research.json"
    if api_research_path.is_file():
        source["api_research_path"] = str(api_research_path.resolve())

    source_path = out / "reference-source.json"
    _write_json(source_path, source)
    return {
        "status": manifest["status"],
        "reference_source": str(source_path),
        "reference": str(reference_path),
        "acquisition_manifest": str(manifest_path),
        "runs": runs,
    }


def run_slop_check(path: Path, *, allow_proof: bool = False, timeout_seconds: int = 60) -> dict[str, Any]:
    home = _slopmonster_home()
    if home is None:
        raise RuntimeError("SlopMonster is not installed. " + INSTALL_COMMANDS["slopmonster"])
    target = Path(path)
    if not target.exists():
        raise FileNotFoundError(target)
    command = [sys.executable, str(home / "tools" / "deslop.py"), str(target)]
    if allow_proof:
        command.append("--allow-proof")
    return _run_command(command, timeout_seconds=timeout_seconds)
