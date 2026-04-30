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

<details>
<summary>🔍 <b>节点发现</b> - 3个技能</summary>

- `ss_crawler.py` - SS节点爬虫
- `vmess_crawler.py` - VMess节点爬虫  
- `github_node_aggregator.py` - GitHub节点聚合

</details>

<details>
<summary>✅ <b>节点验证</b> - 2个技能</summary>

- `node_validator.py` - 节点验证器
- `batch_validator.py` - 批量验证器

</details>

<details>
<summary>🔧 <b>配置生成</b> - 3个技能</summary>

- `singbox_config_generator.py` - sing-box配置
- `clash_config_generator.py` - Clash配置
- `v2ray_config_generator.py` - V2Ray配置

</details>

<details>
<summary>📊 <b>监控运维</b> - 2个技能</summary>

- `node_monitor.py` - 节点监控
- `subscription_updater.py` - 订阅更新

</details>

<details>
<summary>🛠️ <b>实用工具</b> - 3个技能</summary>

- `base64_codec.py` - Base64编解码
- `qrcode_generator.py` - 二维码生成
- `subscription_generator.py` - 订阅生成

</details>

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