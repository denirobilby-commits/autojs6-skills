---
name: autojs6
description: Use when writing, reviewing, debugging, or answering questions about AutoJs6 or Auto.js scripts, including 安卓自动化, 无障碍, 控件选择器, 找图, 找色, 截图, OCR, 悬浮窗, device, engines, files, tasks, plugins, automator actions, UI selectors/objects, images, and version-specific AutoJs6 script APIs such as functions, modules, objects, methods, options, and return values. Always prefer the matching versioned offline documentation bundled with this skill over model memory.
---

# AutoJs6 Docs Skill v0.2

## Overview

This skill answers AutoJs6 questions from bundled, versioned offline docs. It keeps the original HTML for traceability, but the default AI reading path is cleaned Markdown plus JSONL chunks and SQLite search.

## Workflow

1. Determine the target AutoJs6 version. If the user does not specify one, use the latest available local docs version and mention that choice when the answer depends on script API availability or signatures.
2. Resolve the best available docs version with `scripts/resolve_version.py`.
3. Search the matching docs with `scripts/search_docs.py`. Start with exact function, module, object, method, or option names, then retry with nearby domain terms if results are weak.
4. Read only the relevant `clean/chunks.jsonl` entries or `clean/pages/*.md` files.
5. Open `raw/` HTML only when checking original links, page structure, images, or formatting.

When the exact requested version is unavailable, use the nearest lower available version and explicitly say which version was used. If every available version is higher than the requested version, say that no compatible local docs are available instead of guessing.

## Versioned Docs

Version metadata lives in `references/versions.json`.

Each imported version uses this layout:

```text
references/versions/<version>/
├── raw/                 # original offline docs copied from AutoJs6
├── clean/
│   ├── pages/*.md       # cleaned Markdown, one file per HTML page
│   └── chunks.jsonl     # AI-oriented searchable chunks
├── docs.sqlite          # SQLite FTS5 search index
└── manifest.json        # import metadata and path mapping
```

## Commands

Run these commands from the skill root directory.

Resolve the latest available docs version:

```bash
python3 scripts/resolve_version.py
```

Resolve a requested version:

```bash
python3 scripts/resolve_version.py --version 6.7.0
```

Search the latest available docs:

```bash
python3 scripts/search_docs.py --query "autojs.versionName"
```

Search a requested version:

```bash
python3 scripts/search_docs.py --version 6.6.4 --query "images.findImage"
```

## Answering Rules

- For script API availability, signatures, return values, and examples, check the versioned docs first.
- Mention the docs version used when the user asks a version-sensitive question, or when using the latest local docs because no version was specified.
- Prefer selectors and documented AutoJs6 functions/modules/objects over invented helper functions.
- Do not read `all.html` unless a broad full-document search is explicitly needed; it duplicates many pages.
- If search results are weak, search again with nearby terms from the AutoJs6 domain, such as `automator`, `UiSelector`, `UiObject`, `images`, `colors`, `captureScreen`, `ocr`, `engines`, `floaty`, `device`, or `requiresAutojsVersion`.
- If local docs do not confirm a function, module, object, method, option, signature, or return value, say that the bundled docs did not confirm it instead of inventing details.
- Do not mix AutoJs6 script APIs with Auto.js Pro, AutoX.js, or other forks unless the user explicitly asks for a comparison and the source distinction is clear.

## Search Tactics

- For exact script interfaces, search the symbol first, for example `images.findImage`, `textContains`, or `floaty.window`.
- For Chinese requests, map the user's term to likely docs terms before searching, for example `找图` -> `images`, `找色` -> `colors` or `captureScreen`, `控件` -> `UiSelector` or `UiObject`, `悬浮窗` -> `floaty`.
- Prefer reading the matching `clean/pages/*.md` file after search results identify the relevant page; use `chunks.jsonl` for narrow snippets and ranking.
