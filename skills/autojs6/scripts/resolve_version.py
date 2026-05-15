#!/usr/bin/env python3
"""Resolve the best available AutoJs6 docs version for this skill."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
VERSIONS_PATH = SKILL_ROOT / "references" / "versions.json"


def version_key(version: str) -> tuple[int, ...]:
    parts = [int(part) for part in re.findall(r"\d+", version)]
    return tuple(parts or [0])


def load_versions(path: Path = VERSIONS_PATH) -> dict:
    if not path.exists():
        return {"latest": None, "versions": {}}
    return json.loads(path.read_text(encoding="utf-8"))


def resolve_version(requested: str | None, data: dict) -> tuple[str | None, str]:
    versions = sorted(data.get("versions", {}).keys(), key=version_key)
    if not versions:
        return None, "no-docs"

    if not requested:
        latest = data.get("latest") or versions[-1]
        if latest in versions:
            return latest, "latest"
        return versions[-1], "latest-fallback"

    if requested in versions:
        return requested, "exact"

    lower = [version for version in versions if version_key(version) <= version_key(requested)]
    if lower:
        return lower[-1], "nearest-lower"

    return None, "no-compatible-lower"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", help="Requested AutoJs6 version")
    parser.add_argument("--versions-json", type=Path, default=VERSIONS_PATH)
    args = parser.parse_args()

    data = load_versions(args.versions_json)
    resolved, status = resolve_version(args.version, data)
    print(json.dumps({"requested": args.version, "resolved": resolved, "status": status}, ensure_ascii=False))
    return 0 if resolved else 1


if __name__ == "__main__":
    raise SystemExit(main())
