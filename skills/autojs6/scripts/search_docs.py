#!/usr/bin/env python3
"""Search versioned AutoJs6 docs imported by this skill."""

from __future__ import annotations

import argparse
import json
import sqlite3
import subprocess
import sys
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
VERSIONS_ROOT = SKILL_ROOT / "references" / "versions"
RESOLVE_SCRIPT = SKILL_ROOT / "scripts" / "resolve_version.py"


def resolve_version(requested: str | None) -> tuple[str, str]:
    cmd = [sys.executable, str(RESOLVE_SCRIPT)]
    if requested:
        cmd.extend(["--version", requested])
    proc = subprocess.run(cmd, check=False, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode != 0:
        raise SystemExit(proc.stdout.strip() or proc.stderr.strip() or "no compatible docs version")
    payload = json.loads(proc.stdout)
    return payload["resolved"], payload["status"]


def search(version: str, query: str, limit: int) -> list[dict]:
    sqlite_path = VERSIONS_ROOT / version / "docs.sqlite"
    if not sqlite_path.exists():
        raise SystemExit(f"docs index not found: {sqlite_path}")

    conn = sqlite3.connect(sqlite_path)
    conn.row_factory = sqlite3.Row
    try:
        try:
            rows = conn.execute(
                """
                SELECT c.id, c.title, c.source_html, c.source_md, c.heading_path, c.anchor,
                       snippet(chunks_fts, 3, '[', ']', ' ... ', 24) AS snippet
                FROM chunks_fts
                JOIN chunks c ON c.id = chunks_fts.id
                WHERE chunks_fts MATCH ?
                ORDER BY bm25(chunks_fts, 8.0, 4.0, 1.0)
                LIMIT ?
                """,
                (query, limit),
            ).fetchall()
        except sqlite3.OperationalError:
            rows = []
        if not rows:
            like_query = f"%{query}%"
            rows = conn.execute(
                """
                SELECT id, title, source_html, source_md, heading_path, anchor,
                       substr(content, 1, 360) AS snippet
                FROM chunks
                WHERE title LIKE ? OR heading_path LIKE ? OR content LIKE ?
                LIMIT ?
                """,
                (like_query, like_query, like_query, limit),
            ).fetchall()
    finally:
        conn.close()

    return [dict(row) for row in rows]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--query", required=True)
    parser.add_argument("--version", help="Requested AutoJs6 docs version")
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--json", action="store_true", help="Print JSON instead of readable text")
    args = parser.parse_args()

    version, status = resolve_version(args.version)
    results = search(version, args.query, args.limit)
    payload = {"requested_version": args.version, "resolved_version": version, "status": status, "results": results}

    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 0

    print(f"AutoJs6 docs version: {version} ({status})")
    for index, row in enumerate(results, start=1):
        print(f"\n{index}. {row['title']} :: {row['heading_path']}")
        print(f"   id: {row['id']}")
        print(f"   md: {row['source_md']} | html: {row['source_html']}#{row['anchor']}")
        print(f"   {row['snippet']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
