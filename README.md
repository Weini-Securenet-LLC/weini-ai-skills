<div align="center">

# 🤖 Weini AI Agent Skills

**告诉 AI，它就能帮你找代理节点**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)

</div>

---

## 💡 这是什么？

一套让 AI 助手（Claude、Cursor、Copilot 等）自动管理代理节点的工具。

**你不需要懂技术，只需要会说话。**

---

## 🚀 怎么用？

### 1️⃣ 告诉 AI 导入这个项目

```
"导入 https://github.com/Weini-Securenet-LLC/weini-ai-skills"
```

### 2️⃣ 用自然语言说出需求

```
"帮我找50个可用的代理节点"
"验证这些节点，生成配置文件"
"自动找节点并配置好"
```

### 3️⃣ AI 自动完成

AI 会自动：
- 🔍 爬取免费节点
- ✅ 测试可用性
- 🔧 生成配置文件
- 📊 返回结果

**就这么简单！**

---

## ✨ 能做什么？

| 功能 | 说什么 |
|------|--------|
| **找节点** | "帮我找一些代理节点" |
| **测试节点** | "验证这些节点哪些能用" |
| **生成配置** | "生成 sing-box 配置" |
| **完整流程** | "自动找节点、测试、生成配置" |

---

## 🤝 支持的 AI 工具

- ✅ Claude Code / Cursor
- ✅ GitHub Copilot
- ✅ OpenAI Codex
- ✅ 其他支持导入 Skills 的 AI 工具

---

## 🛠️ 不想用 AI？也可以手动

```bash
git clone https://github.com/Weini-Securenet-LLC/weini-ai-skills.git
cd weini-ai-skills
pip install -r requirements.txt

python skills/ss_crawler.py          # 爬取节点
python skills/node_validator.py      # 验证节点  
python skills/singbox_config_generator.py  # 生成配置
```

---

## 📖 技能列表

### 🔍 节点发现（3个技能）

| 技能 | 能做什么 |
|------|----------|
| `ss_crawler.py` | 从 GitHub、Telegram 等公开渠道自动抓取免费 SS 节点 |
| `vmess_crawler.py` | 抓取 VMess/VLESS/Trojan 等协议的免费节点 |
| `github_node_aggregator.py` | 汇总 GitHub 上所有免费节点项目的最新节点 |

**用法：** 对 AI 说 *"帮我找一些免费代理节点"*

---

### ✅ 节点验证（2个技能）

| 技能 | 能做什么 |
|------|----------|
| `node_validator.py` | 测试节点能不能连、速度快不快、在哪个国家 |
| `batch_validator.py` | 同时测试几百个节点，找出最快最稳定的 |

**用法：** 对 AI 说 *"验证这些节点哪些能用"*

---

### 🔧 配置生成（3个技能）

| 技能 | 能做什么 |
|------|----------|
| `singbox_config_generator.py` | 生成 sing-box 客户端配置文件，直接导入使用 |
| `clash_config_generator.py` | 生成 Clash 配置文件，适配各种 Clash 客户端 |
| `v2ray_config_generator.py` | 生成 V2Ray 配置文件，支持多种代理协议 |

**用法：** 对 AI 说 *"生成一个 sing-box 配置文件"*

---

### 📊 监控运维（2个技能）

| 技能 | 能做什么 |
|------|----------|
| `node_monitor.py` | 定时检查节点状态，节点挂了自动通知你 |
| `subscription_updater.py` | 自动更新订阅链接，保持节点列表最新 |

**用法：** 对 AI 说 *"帮我监控这些节点的状态"*

---

### 🛠️ 实用工具（3个技能）

| 技能 | 能做什么 |
|------|----------|
| `base64_codec.py` | 解码/编码节点分享链接（ss:// vmess:// 等） |
| `qrcode_generator.py` | 把节点信息生成二维码，手机扫码导入 |
| `subscription_generator.py` | 把你的节点列表生成订阅链接，分享给朋友 |

**用法：** 对 AI 说 *"把这些节点生成二维码"*

---

## 🤝 贡献

欢迎贡献新技能！查看 [CONTRIBUTING.md](CONTRIBUTING.md)

---

## 🔒 安全提醒

- ✅ 所有代码开源可审查
- ✅ 本地运行，不上传数据
- ⚠️ 使用代理节点需自行承担风险
- ⚠️ 了解你的代理服务器来源

---

## 📞 需要帮助？

- 💬 [GitHub Discussions](https://github.com/Weini-Securenet-LLC/weini-ai-skills/discussions)
- 🐛 [报告问题](https://github.com/Weini-Securenet-LLC/weini-ai-skills/issues)
- 📧 Email: contact@weinisecure.net

---

## 📄 许可证

MIT License - 自由使用、修改、分发

---

<div align="center">

**🤖 让 AI 成为互联网自由的工具**

Made with ❤️ by [Weini Securenet LLC](https://weinisecure.net)

</div>