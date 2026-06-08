<div align="center">

# 🧰 DevToolbox-CLI

**Lightweight Terminal Developer Utility Engine**

*轻量级终端开发者工具箱引擎 | 輕量級終端開發者工具箱引擎*

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey)]()
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Zero-brightgreen)]()

[English](#english) · [简体中文](#简体中文) · [繁體中文](#繁體中文)

</div>

---

<a id="english"></a>
## 🎉 Introduction

**DevToolbox-CLI** is a unified, lightweight terminal utility engine designed for developers who need quick, reliable format conversions, encoding/decoding, and data manipulation — all without leaving the command line.

Inspired by the popularity of tools like **DevToys** (GUI) and **jq** (JSON), DevToolbox-CLI brings **12+ essential developer utilities** into a single, zero-dependency Python CLI. No more switching between browser tabs, online converters, or installing dozens of separate tools.

### ✨ Key Differentiators
- **🚀 Zero Dependencies** — Pure Python 3.8+, no pip install hell
- **🖥️ Cross-Platform** — Works identically on Linux, macOS, and Windows
- **⚡ Blazing Fast** — Native Python performance, no overhead
- **🎨 Beautiful Output** — Colorized terminal output with intuitive icons
- **📦 Single Binary** — One command, 12+ tools
- **🔒 Safe & Local** — All processing happens locally, no data leaves your machine

---

## ✨ Core Features

| Command | Emoji | Description |
|---------|-------|-------------|
| `json` | 📋 | Format, validate, minify, sort keys |
| `base64` | 🔐 | Encode / decode Base64 |
| `url` | 🌐 | URL encode / decode |
| `hash` | 🔑 | MD5 / SHA1 / SHA256 / SHA512 |
| `uuid` | 🆔 | Generate UUID v1 / v4 |
| `jwt` | 🎫 | Decode JWT payload (no verification) |
| `regex` | 🔍 | Test regex patterns with groups |
| `time` | ⏰ | Timestamp ↔ ISO8601 conversion |
| `color` | 🎨 | HEX ↔ RGB conversion |
| `password` | 🔒 | Secure random password generator |
| `qr` | 📱 | ASCII QR code generator |
| `html` | 📝 | HTML escape / unescape |
| `diff` | 📊 | Simple line diff |

---

## 🚀 Quick Start

### Requirements
- Python 3.8 or higher

### Installation

```bash
# Clone the repository
git clone https://github.com/gitstq/DevToolbox-CLI.git
cd DevToolbox-CLI

# Install (optional, creates 'devtoolbox' command)
pip install -e .

# Or run directly without installation
python3 main.py
```

### Usage Examples

```bash
# Pretty-print JSON
echo '{"b":1,"a":2}' | devtoolbox json --format

# Base64 encode
devtoolbox base64 --input "hello world"

# Generate SHA256 hash
devtoolbox hash --algo sha256 --input "secret"

# Generate 5 UUIDs
devtoolbox uuid --count 5

# Decode JWT
devtoolbox jwt --input "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."

# Test regex
devtoolbox regex --pattern "\d+" --input "abc123def456"

# Convert timestamp to ISO8601
devtoolbox time --to-iso 1717776000

# Generate secure password
devtoolbox password --length 20

# HTML escape
devtoolbox html --input "<div>hello</div>"

# Show current time
devtoolbox time --now
```

---

## 📖 Detailed Usage Guide

### JSON Processing
```bash
# Format with custom indent
cat data.json | devtoolbox json --format --indent 4

# Minify for production
devtoolbox json --minify --input '{"a": 1, "b": 2}'

# Sort keys alphabetically
devtoolbox json --format --sort < config.json
```

### Hash Generation
```bash
# Supported algorithms: md5, sha1, sha256, sha512
devtoolbox hash --algo md5 --input "file content"
devtoolbox hash --algo sha512 --input "sensitive data"
```

### Regex Testing
```bash
# Case-insensitive matching with group extraction
devtoolbox regex --pattern "(\w+)@(\w+\.\w+)" --input "contact@example.com"
```

### Color Conversion
```bash
# HEX to RGB
devtoolbox color --hex-to-rgb "#FF8000"
# → RGB: (255, 128, 0)

# RGB to HEX
devtoolbox color --rgb-to-hex "255,128,0"
# → HEX: #ff8000
```

---

## 💡 Design Philosophy & Roadmap

### Why DevToolbox-CLI?
Developers constantly need small utility conversions — formatting JSON, encoding strings, generating hashes. Most solutions require either:
- Opening browser-based tools (privacy risk, slow)
- Installing multiple separate CLI tools (dependency hell)
- Using heavy GUI apps like DevToys (not terminal-friendly)

DevToolbox-CLI solves this by providing **one lightweight, zero-dependency tool** that covers 90% of daily developer utility needs.

### Technical Choices
- **Pure Python**: Maximum compatibility, no compilation needed
- **argparse**: Standard library, no external CLI frameworks
- **stdin-first design**: Pipe-friendly, Unix philosophy compliant

### Roadmap
- [ ] CSV ↔ JSON conversion
- [ ] Lorem ipsum generator
- [ ] Cron expression parser
- [ ] JSONPath query support
- [ ] TOML / YAML format support
- [ ] Plugin system for custom commands

---

## 📦 Packaging & Deployment

### PyPI Package (Coming Soon)
```bash
pip install devtoolbox-cli
```

### Standalone Executable
Using PyInstaller:
```bash
pip install pyinstaller
pyinstaller --onefile main.py --name devtoolbox
```

### Docker
```dockerfile
FROM python:3.11-slim
COPY main.py /app/main.py
ENTRYPOINT ["python3", "/app/main.py"]
```

---

## 🤝 Contributing

We welcome contributions! Please follow these guidelines:

1. **Fork** the repository
2. Create a **feature branch** (`git checkout -b feat/amazing-feature`)
3. **Commit** with clear messages (`feat: add CSV converter`)
4. **Push** to your fork
5. Open a **Pull Request**

### Commit Convention
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation update
- `refactor:` Code refactoring
- `test:` Test additions/changes

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

<a id="简体中文"></a>
## 🎉 项目介绍

**DevToolbox-CLI** 是一款统一的轻量级终端开发者工具箱引擎，专为需要在命令行中快速、可靠地进行格式转换、编解码和数据处理的开发者设计。

受 **DevToys**（GUI）和 **jq**（JSON）等工具流行的启发，DevToolbox-CLI 将 **12+ 核心开发者工具** 整合到一个零依赖的 Python CLI 中。无需再切换浏览器标签页、使用在线转换器或安装数十个独立工具。

### ✨ 自研差异化亮点
- **🚀 零依赖** — 纯 Python 3.8+，无需 pip 安装地狱
- **🖥️ 跨平台** — 在 Linux、macOS 和 Windows 上表现一致
- **⚡ 极速响应** — 原生 Python 性能，无额外开销
- **🎨 精美输出** — 彩色终端输出，搭配直观图标
- **📦 单一入口** — 一个命令，12+ 工具
- **🔒 安全本地** — 所有处理均在本地完成，数据绝不上传

---

## ✨ 核心特性

| 命令 | 图标 | 功能描述 |
|------|------|----------|
| `json` | 📋 | JSON 格式化、校验、压缩、按键排序 |
| `base64` | 🔐 | Base64 编码 / 解码 |
| `url` | 🌐 | URL 编码 / 解码 |
| `hash` | 🔑 | MD5 / SHA1 / SHA256 / SHA512 哈希 |
| `uuid` | 🆔 | 生成 UUID v1 / v4 |
| `jwt` | 🎫 | 解码 JWT 载荷（不验证签名）|
| `regex` | 🔍 | 正则表达式测试，支持分组提取 |
| `time` | ⏰ | 时间戳 ↔ ISO8601 互转 |
| `color` | 🎨 | HEX ↔ RGB 颜色转换 |
| `password` | 🔒 | 安全随机密码生成器 |
| `qr` | 📱 | ASCII 二维码生成 |
| `html` | 📝 | HTML 转义 / 反转义 |
| `diff` | 📊 | 简易行级文本对比 |

---

## 🚀 快速开始

### 环境要求
- Python 3.8 或更高版本

### 安装步骤

```bash
# 克隆仓库
git clone https://github.com/gitstq/DevToolbox-CLI.git
cd DevToolbox-CLI

# 安装（可选，创建 'devtoolbox' 命令）
pip install -e .

# 或直接运行，无需安装
python3 main.py
```

### 使用示例

```bash
# 美化 JSON
echo '{"b":1,"a":2}' | devtoolbox json --format

# Base64 编码
devtoolbox base64 --input "hello world"

# 生成 SHA256 哈希
devtoolbox hash --algo sha256 --input "secret"

# 生成 5 个 UUID
devtoolbox uuid --count 5

# 解码 JWT
devtoolbox jwt --input "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."

# 测试正则
devtoolbox regex --pattern "\d+" --input "abc123def456"

# 时间戳转 ISO8601
devtoolbox time --to-iso 1717776000

# 生成安全密码
devtoolbox password --length 20

# HTML 转义
devtoolbox html --input "<div>hello</div>"

# 显示当前时间
devtoolbox time --now
```

---

## 📖 详细使用指南

### JSON 处理
```bash
# 自定义缩进格式化
cat data.json | devtoolbox json --format --indent 4

# 生产环境压缩
devtoolbox json --minify --input '{"a": 1, "b": 2}'

# 按键名排序
devtoolbox json --format --sort < config.json
```

### 哈希生成
```bash
# 支持算法：md5、sha1、sha256、sha512
devtoolbox hash --algo md5 --input "文件内容"
devtoolbox hash --algo sha512 --input "敏感数据"
```

### 正则测试
```bash
# 忽略大小写，提取分组
devtoolbox regex --pattern "(\w+)@(\w+\.\w+)" --input "contact@example.com"
```

### 颜色转换
```bash
# HEX 转 RGB
devtoolbox color --hex-to-rgb "#FF8000"
# → RGB: (255, 128, 0)

# RGB 转 HEX
devtoolbox color --rgb-to-hex "255,128,0"
# → HEX: #ff8000
```

---

## 💡 设计思路与迭代规划

### 为什么做 DevToolbox-CLI？
开发者日常频繁需要小型工具转换 —— 格式化 JSON、编码字符串、生成哈希。现有方案要么：
- 打开浏览器工具（隐私风险、速度慢）
- 安装多个独立 CLI 工具（依赖地狱）
- 使用 DevToys 等重型 GUI（不适合终端场景）

DevToolbox-CLI 通过 **一个轻量、零依赖的工具** 覆盖 90% 的日常开发者实用需求。

### 技术选型原因
- **纯 Python**：最大兼容性，无需编译
- **argparse**：标准库内置，无外部 CLI 框架依赖
- **stdin 优先设计**：支持管道，符合 Unix 哲学

### 后续迭代计划
- [ ] CSV ↔ JSON 转换
- [ ] Lorem ipsum 文本生成器
- [ ] Cron 表达式解析器
- [ ] JSONPath 查询支持
- [ ] TOML / YAML 格式支持
- [ ] 自定义命令插件系统

---

## 📦 打包与部署指南

### PyPI 包（即将发布）
```bash
pip install devtoolbox-cli
```

### 独立可执行文件
使用 PyInstaller：
```bash
pip install pyinstaller
pyinstaller --onefile main.py --name devtoolbox
```

### Docker 部署
```dockerfile
FROM python:3.11-slim
COPY main.py /app/main.py
ENTRYPOINT ["python3", "/app/main.py"]
```

---

## 🤝 贡献指南

欢迎贡献！请遵循以下规范：

1. **Fork** 本仓库
2. 创建**功能分支**（`git checkout -b feat/awesome-feature`）
3. **提交**清晰的提交信息（`feat: 添加 CSV 转换器`）
4. **推送**到你的 Fork
5. 发起 **Pull Request**

### 提交规范
- `feat:` 新功能
- `fix:` 修复问题
- `docs:` 文档更新
- `refactor:` 代码重构
- `test:` 测试相关

---

## 📄 开源协议

本项目采用 [MIT 协议](LICENSE) 开源。

---

<a id="繁體中文"></a>
## 🎉 專案介紹

**DevToolbox-CLI** 是一款統一的輕量級終端開發者工具箱引擎，專為需要在命令列中快速、可靠地進行格式轉換、編解碼和資料處理的開發者設計。

受 **DevToys**（GUI）和 **jq**（JSON）等工具流行的啟發，DevToolbox-CLI 將 **12+ 核心開發者工具** 整合到一個零依賴的 Python CLI 中。無需再切換瀏覽器分頁、使用線上轉換器或安裝數十個獨立工具。

### ✨ 自研差異化亮點
- **🚀 零依賴** — 純 Python 3.8+，無需 pip 安裝地獄
- **🖥️ 跨平台** — 在 Linux、macOS 和 Windows 上表現一致
- **⚡ 極速響應** — 原生 Python 效能，無額外開銷
- **🎨 精美輸出** — 彩色終端輸出，搭配直觀圖示
- **📦 單一入口** — 一個命令，12+ 工具
- **🔒 安全本地** — 所有處理均在本地完成，資料絕不上傳

---

## ✨ 核心特性

| 命令 | 圖示 | 功能描述 |
|------|------|----------|
| `json` | 📋 | JSON 格式化、校驗、壓縮、按鍵排序 |
| `base64` | 🔐 | Base64 編碼 / 解碼 |
| `url` | 🌐 | URL 編碼 / 解碼 |
| `hash` | 🔑 | MD5 / SHA1 / SHA256 / SHA512 雜湊 |
| `uuid` | 🆔 | 生成 UUID v1 / v4 |
| `jwt` | 🎫 | 解碼 JWT 載荷（不驗證簽章）|
| `regex` | 🔍 | 正規表示式測試，支援分群擷取 |
| `time` | ⏰ | 時間戳記 ↔ ISO8601 互轉 |
| `color` | 🎨 | HEX ↔ RGB 顏色轉換 |
| `password` | 🔒 | 安全隨機密碼產生器 |
| `qr` | 📱 | ASCII 二維碼產生 |
| `html` | 📝 | HTML 跳脫 / 反跳脫 |
| `diff` | 📊 | 簡易行級文字比對 |

---

## 🚀 快速開始

### 環境要求
- Python 3.8 或更高版本

### 安裝步驟

```bash
# 克隆倉庫
git clone https://github.com/gitstq/DevToolbox-CLI.git
cd DevToolbox-CLI

# 安裝（可選，建立 'devtoolbox' 命令）
pip install -e .

# 或直接執行，無需安裝
python3 main.py
```

### 使用範例

```bash
# 美化 JSON
echo '{"b":1,"a":2}' | devtoolbox json --format

# Base64 編碼
devtoolbox base64 --input "hello world"

# 產生 SHA256 雜湊
devtoolbox hash --algo sha256 --input "secret"

# 產生 5 個 UUID
devtoolbox uuid --count 5

# 解碼 JWT
devtoolbox jwt --input "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."

# 測試正規表示式
devtoolbox regex --pattern "\d+" --input "abc123def456"

# 時間戳記轉 ISO8601
devtoolbox time --to-iso 1717776000

# 產生安全密碼
devtoolbox password --length 20

# HTML 跳脫
devtoolbox html --input "<div>hello</div>"

# 顯示目前時間
devtoolbox time --now
```

---

## 📖 詳細使用指南

### JSON 處理
```bash
# 自訂縮排格式化
cat data.json | devtoolbox json --format --indent 4

# 生產環境壓縮
devtoolbox json --minify --input '{"a": 1, "b": 2}'

# 按鍵名排序
devtoolbox json --format --sort < config.json
```

### 雜湊產生
```bash
# 支援演算法：md5、sha1、sha256、sha512
devtoolbox hash --algo md5 --input "檔案內容"
devtoolbox hash --algo sha512 --input "敏感資料"
```

### 正規表示式測試
```bash
# 忽略大小寫，擷取分群
devtoolbox regex --pattern "(\w+)@(\w+\.\w+)" --input "contact@example.com"
```

### 顏色轉換
```bash
# HEX 轉 RGB
devtoolbox color --hex-to-rgb "#FF8000"
# → RGB: (255, 128, 0)

# RGB 轉 HEX
devtoolbox color --rgb-to-hex "255,128,0"
# → HEX: #ff8000
```

---

## 💡 設計理念與迭代規劃

### 為什麼做 DevToolbox-CLI？
開發者日常頻繁需要小型工具轉換 —— 格式化 JSON、編碼字串、產生雜湊。現有方案要么：
- 開啟瀏覽器工具（隱私風險、速度慢）
- 安裝多個獨立 CLI 工具（依賴地獄）
- 使用 DevToys 等重型 GUI（不適合終端場景）

DevToolbox-CLI 透過 **一個輕量、零依賴的工具** 覆蓋 90% 的日常開發者實用需求。

### 技術選型原因
- **純 Python**：最大相容性，無需編譯
- **argparse**：標準庫內建，無外部 CLI 框架依賴
- **stdin 優先設計**：支援管線，符合 Unix 哲學

### 後續迭代計畫
- [ ] CSV ↔ JSON 轉換
- [ ] Lorem ipsum 文字產生器
- [ ] Cron 表示式解析器
- [ ] JSONPath 查詢支援
- [ ] TOML / YAML 格式支援
- [ ] 自訂命令外掛系統

---

## 📦 打包與部署指南

### PyPI 套件（即將發布）
```bash
pip install devtoolbox-cli
```

### 獨立可執行檔
使用 PyInstaller：
```bash
pip install pyinstaller
pyinstaller --onefile main.py --name devtoolbox
```

### Docker 部署
```dockerfile
FROM python:3.11-slim
COPY main.py /app/main.py
ENTRYPOINT ["python3", "/app/main.py"]
```

---

## 🤝 貢獻指南

歡迎貢獻！請遵循以下規範：

1. **Fork** 本倉庫
2. 建立**功能分支**（`git checkout -b feat/awesome-feature`）
3. **提交**清晰的提交資訊（`feat: 新增 CSV 轉換器`）
4. **推送**到你的 Fork
5. 發起 **Pull Request**

### 提交規範
- `feat:` 新功能
- `fix:` 修復問題
- `docs:` 文件更新
- `refactor:` 程式碼重構
- `test:` 測試相關

---

## 📄 開源協議

本專案採用 [MIT 協議](LICENSE) 開源。

---

<div align="center">

Made with 💙 by **gitstq** | If you find this useful, please consider giving it a ⭐

</div>
