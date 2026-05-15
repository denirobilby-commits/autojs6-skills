# AutoJs6 Skills

Languages: [English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md)

Codex/agent skills for answering AutoJs6 and Auto.js scripting questions from bundled, versioned offline docs.

## Install

Install with the skills.sh CLI:

```bash
npx skills@latest add denirobilby-commits/autojs6-skills
```

Then select the `autojs6` skill in the CLI prompts and restart your agent if required.

## Included Skills

- `autojs6` - AutoJs6 script interfaces, Android automation, accessibility selectors, image matching, OCR, floaty windows, device APIs, engines, files, tasks, and version-specific behavior.

## Repository Layout

```text
skills/
└── autojs6/
    ├── SKILL.md
    ├── agents/
    ├── scripts/
    └── references/
```

The `autojs6` skill includes runtime search helpers and bundled offline docs. Build/import tooling is intentionally not included in this public package.

## Credits

- AutoJs6 documentation source: [SuperMonster003/AutoJs6](https://github.com/SuperMonster003/AutoJs6)
- Skill packaging and documentation assistance: OpenAI Codex

## License

This repository includes documentation derived from AutoJs6, which is licensed under the Mozilla Public License 2.0. See [LICENSE](LICENSE).
