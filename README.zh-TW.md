# AutoJs6 Skills

語言：[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md)

用於 Codex/Agent 的 AutoJs6 技能包，可基於內建的分版本離線文件回答 AutoJs6 與 Auto.js 腳本相關問題。

## 安裝

使用 skills.sh CLI 安裝：

```bash
npx skills@latest add <owner>/autojs6-skills
```

然後在 CLI 提示中選擇 `autojs6` skill。如工具要求重新啟動 Agent，請重新啟動後再使用。

## 包含的 Skill

- `autojs6` - 用於查詢 AutoJs6 腳本介面、Android 自動化、無障礙選擇器、找圖、OCR、懸浮窗、device、engines、files、tasks 以及版本相關行為。

## 倉庫結構

```text
skills/
└── autojs6/
    ├── SKILL.md
    ├── agents/
    ├── scripts/
    └── references/
```

`autojs6` skill 包含執行時文件搜尋輔助腳本和離線文件資源。建置/匯入工具不會包含在公開發布包中。

## 致謝

- AutoJs6 文件來源：[SuperMonster003/AutoJs6](https://github.com/SuperMonster003/AutoJs6)
- Skill 打包與文件整理協助：OpenAI Codex

## 授權

本倉庫包含由 AutoJs6 文件衍生的資料，AutoJs6 使用 Mozilla Public License 2.0。詳見 [LICENSE](LICENSE)。
