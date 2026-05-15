# AutoJs6 Skills

<p align="center">
  <img src="https://s1.imagehub.cc/images/2023/03/07/af8ed087c9d354b9ab6142aae7bbafb6.png" alt="AutoJs6" width="704">
</p>

语言：[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md)

用于 Codex/Agent 的 AutoJs6 技能包，可基于内置的分版本离线文档回答 AutoJs6 与 Auto.js 脚本相关问题。

## 安装

使用 skills.sh CLI 安装：

```bash
npx skills@latest add denirobilby-commits/autojs6-skills
```

然后在 CLI 提示中选择 `autojs6` skill。如工具要求重启 Agent，请重启后再使用。

## 包含的 Skill

- `autojs6` - 用于查询 AutoJs6 脚本接口、Android 自动化、无障碍选择器、找图、OCR、悬浮窗、device、engines、files、tasks 以及版本相关行为。

## 仓库结构

```text
skills/
└── autojs6/
    ├── SKILL.md
    ├── agents/
    ├── scripts/
    └── references/
```

`autojs6` skill 包含运行时文档搜索辅助脚本和离线文档资源。构建/导入工具不会包含在公开发布包中。

## 致谢

- AutoJs6 文档来源：[SuperMonster003/AutoJs6](https://github.com/SuperMonster003/AutoJs6)
- Skill 打包与文档整理协助：OpenAI Codex

## 许可证

本仓库包含由 AutoJs6 文档派生的资料，AutoJs6 使用 Mozilla Public License 2.0。详见 [LICENSE](LICENSE)。
