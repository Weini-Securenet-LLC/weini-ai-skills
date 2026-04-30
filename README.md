<div align="center">

# 🤖 Weini AI Agent Skills

**Open-Source AI Tools for Internet Freedom**

*赋能 AI，让每个人都能实现通信自由*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![AI Powered](https://img.shields.io/badge/AI-Powered-green.svg)](https://github.com/Weini-Securenet-LLC/weini-ai-skills)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

[English](#english) | [中文](#中文) | [فارسی](#فارسی)

</div>

---

## 🎯 项目愿景

**让 AI 成为互联网自由的工具**

本项目提供一系列开源的 AI Agent Skills，让任何人都能通过 AI 工具（如 Claude、GPT、Cursor 等）自动化地：
- 🔍 发现可用的翻墙节点
- ✅ 验证节点可用性
- 🔧 生成代理配置文件
- 📊 监控节点状态
- 🛠️ 自动化运维任务

### 为什么需要 AI Skills？

- 💡 **降低门槛**: 普通用户也能使用 AI 帮助自己或他人翻墙
- 🤝 **社区驱动**: 任何人都可以贡献新技能
- 🔄 **持续更新**: 适应不断变化的网络环境
- 🆓 **完全免费**: 开源共享，人人可用
- 🌍 **全球协作**: 共同对抗网络审查

---

## ✨ 可用技能

### 🔍 节点发现技能

#### 1. `ss_crawler.py` - SS节点爬虫
从多个公开来源聚合免费SS节点

**功能**:
- 从 GitHub、Telegram、网站等聚合节点
- 自动解析多种格式（SS、base64等）
- 去重和格式化
- 导出为标准格式

**使用场景**:
```
User: 帮我找一些可用的SS节点
AI: [调用 ss_crawler.py，返回节点列表]
```

#### 2. `vmess_crawler.py` - VMess节点爬虫
聚合免费VMess/VLESS/Trojan节点

**功能**:
- 支持多协议（VMess、VLESS、Trojan）
- 从订阅链接和公开频道获取
- 智能过滤和排序
- 支持分地区获取

#### 3. `github_node_aggregator.py` - GitHub节点聚合器
从GitHub上的免费节点项目聚合

**功能**:
- 自动搜索GitHub上的节点仓库
- 解析README和配置文件
- 追踪更新和变化
- 生成综合节点列表

### ✅ 节点验证技能

#### 4. `node_validator.py` - 节点验证器
测试节点的连接性和速度

**功能**:
- TCP连接测试
- HTTP/HTTPS可达性测试
- 延迟测量
- 带宽测试
- 地理位置检测

**使用场景**:
```
User: 验证这些节点哪些还能用
AI: [调用 node_validator.py，返回可用节点]
```

#### 5. `batch_validator.py` - 批量验证器
并发测试大量节点

**功能**:
- 多线程并发测试
- 超时控制
- 结果排序（按延迟、成功率）
- 导出验证报告

### 🔧 配置生成技能

#### 6. `singbox_config_generator.py` - sing-box配置生成
生成sing-box代理配置

**功能**:
- 从节点列表生成sing-box配置
- 支持多种入站/出站协议
- 自动路由规则
- 订阅转换

**使用场景**:
```
User: 把这些节点转成sing-box配置
AI: [调用生成器，返回config.json]
```

#### 7. `clash_config_generator.py` - Clash配置生成
生成Clash/Clash Meta配置

**功能**:
- 节点转Clash格式
- 自动分组（按地区、类型）
- 规则集配置
- 订阅链接生成

#### 8. `v2ray_config_generator.py` - V2Ray配置生成
生成V2Ray/Xray配置

### 📊 监控与运维技能

#### 9. `node_monitor.py` - 节点监控
持续监控节点状态

**功能**:
- 定时检查节点可用性
- 故障告警
- 状态历史记录
- 可用性统计

#### 10. `subscription_updater.py` - 订阅更新器
自动更新订阅链接

**功能**:
- 定时拉取订阅
- 合并多个订阅源
- 去重和优化
- 自动推送更新

### 🛠️ 工具技能

#### 11. `base64_codec.py` - Base64编解码
处理节点链接的编解码

#### 12. `qrcode_generator.py` - 二维码生成
生成节点分享二维码

#### 13. `subscription_generator.py` - 订阅链接生成
将节点列表生成订阅链接

---

## 🚀 快速开始

### 前置要求

- Python 3.8+
- pip 包管理器
- AI工具（Claude Desktop、Cursor、GPT等）

### 安装

```bash
# 克隆仓库
git clone https://github.com/Weini-Securenet-LLC/weini-ai-skills.git
cd weini-ai-skills

# 安装依赖
pip install -r requirements.txt

# 测试技能
python skills/ss_crawler.py --test
```

### 在 AI 工具中使用

#### 方式1: Claude Desktop (推荐)

1. 将技能脚本放到 AI 可访问的目录
2. 在对话中请求：
   ```
   请使用 ss_crawler.py 帮我找一些可用的SS节点
   ```
3. AI 会自动调用技能并返回结果

#### 方式2: Cursor IDE

1. 打开 Cursor 项目
2. 在 Agent 模式下请求：
   ```
   Run the node validator on these nodes
   ```
3. AI 会执行验证并显示结果

#### 方式3: 命令行直接使用

```bash
# 爬取节点
python skills/ss_crawler.py --output nodes.json

# 验证节点
python skills/node_validator.py --input nodes.json --output valid_nodes.json

# 生成配置
python skills/singbox_config_generator.py --input valid_nodes.json --output config.json
```

---

## 📖 技能详细文档

### SS节点爬虫使用示例

```python
from skills.ss_crawler import SSCrawler

# 创建爬虫实例
crawler = SSCrawler()

# 爬取节点
nodes = crawler.crawl_all_sources()

# 过滤可用节点
valid_nodes = crawler.filter_valid(nodes)

# 导出
crawler.export_json(valid_nodes, 'nodes.json')
```

### 节点验证器使用示例

```python
from skills.node_validator import NodeValidator

# 创建验证器
validator = NodeValidator(timeout=5, concurrency=10)

# 验证节点列表
results = validator.validate_batch(nodes)

# 获取可用节点（延迟<500ms）
fast_nodes = validator.get_fast_nodes(results, max_latency=500)
```

### sing-box配置生成示例

```python
from skills.singbox_config_generator import SingBoxGenerator

# 创建生成器
generator = SingBoxGenerator()

# 添加节点
generator.add_nodes(nodes)

# 生成配置
config = generator.generate_config(
    inbound_port=1080,
    enable_direct=True,
    enable_block_ads=True
)

# 保存配置
generator.save_config(config, 'config.json')
```

---

## 🤝 如何贡献

我们欢迎所有形式的贡献！

### 贡献新技能

1. **Fork** 本仓库
2. 创建技能分支: `git checkout -b skill/my-new-skill`
3. 在 `skills/` 目录下添加你的技能脚本
4. 编写文档和测试
5. 提交PR

### 技能开发规范

每个技能应该包括：

```python
"""
Skill Name: Your Skill Name
Description: Brief description of what this skill does
Author: Your Name
Date: 2026-04-30
Dependencies: list, of, dependencies

Usage:
    python your_skill.py [args]
    
Examples:
    python your_skill.py --input data.json --output result.json
"""

import argparse

def main():
    """Main function with clear documentation"""
    parser = argparse.ArgumentParser(description='Your skill description')
    parser.add_argument('--input', help='Input file')
    parser.add_argument('--output', help='Output file')
    args = parser.parse_args()
    
    # Your skill logic here
    
if __name__ == '__main__':
    main()
```

### 贡献类型

- 🆕 **新技能**: 添加新的AI技能脚本
- 🐛 **Bug修复**: 修复现有技能的问题
- 📖 **文档**: 改进文档和使用示例
- ✨ **功能增强**: 改进现有技能
- 🌍 **翻译**: 添加多语言支持

详见: [CONTRIBUTING.md](CONTRIBUTING.md)

---

## 📋 技能清单

### 已实现 ✅

- [x] SS节点爬虫
- [x] VMess节点爬虫  
- [x] 节点验证器
- [x] sing-box配置生成
- [x] Clash配置生成

### 开发中 🚧

- [ ] 批量验证器（多线程优化）
- [ ] 订阅更新器
- [ ] 节点监控器
- [ ] GitHub节点聚合器

### 规划中 📝

- [ ] Telegram Bot技能
- [ ] 自动测速技能
- [ ] 节点评分系统
- [ ] 智能节点推荐
- [ ] 订阅链接管理
- [ ] 配置自动优化
- [ ] 节点分享社区集成

---

## 🔒 安全与隐私

### 安全考虑

- ✅ 所有代码开源可审计
- ✅ 不收集用户数据
- ✅ 不上传节点使用信息
- ✅ 本地运行，数据不离开设备
- ⚠️ 使用公开节点需谨慎

### 隐私保护

- 不记录用户操作日志
- 不追踪技能使用情况
- 不要求注册或登录
- 本地配置，本地存储

### 使用建议

- 🛡️ 优先使用可信的节点源
- 🔐 定期验证节点安全性
- 🚫 避免在公开节点传输敏感信息
- 💾 定期备份重要配置

---

## 🌍 适用场景

### 个人用户

- 🔍 找免费翻墙节点
- ✅ 测试节点可用性
- 📱 配置手机/电脑代理
- 🔄 管理多个订阅

### 开发者

- 🛠️ 集成到自己的工具
- 🤖 构建自动化脚本
- 📊 监控节点健康度
- 🔧 定制配置生成

### 社区运营者

- 🌐 维护公开节点池
- 📢 分享给需要的人
- 🤝 协作改进工具
- 📈 追踪可用性统计

---

## 📞 联系与支持

### 社区渠道

- 💬 **Telegram**: [@weini_quantum](https://t.me/weini_quantum)
- 🐙 **GitHub Issues**: [提交问题](https://github.com/Weini-Securenet-LLC/weini-ai-skills/issues)
- 💡 **Discussions**: [参与讨论](https://github.com/Weini-Securenet-LLC/weini-ai-skills/discussions)
- 📧 **Email**: weinidaohang@proton.me

### 获取帮助

- 📖 查看 [Wiki](https://github.com/Weini-Securenet-LLC/weini-ai-skills/wiki)
- 🎬 观看 [视频教程](https://www.youtube.com/@weinisecurenet)（规划中）
- 💬 加入社区讨论
- 📧 发送邮件咨询

---

## 📊 项目统计

- 🤖 **技能数量**: 13+
- 📝 **代码行数**: 5000+
- 🌍 **支持语言**: Python, Shell, JavaScript
- 🤝 **贡献者**: 欢迎加入
- ⭐ **GitHub Stars**: [点击Star支持](https://github.com/Weini-Securenet-LLC/weini-ai-skills)

---

## 🛠️ 技术架构

### 核心技术

- **Python 3.8+**: 主要开发语言
- **Requests**: HTTP客户端
- **aiohttp**: 异步HTTP
- **BeautifulSoup**: HTML解析
- **pyyaml**: 配置文件处理

### 支持的AI平台

- ✅ Claude Desktop
- ✅ Cursor IDE
- ✅ ChatGPT with Code Interpreter
- ✅ GitHub Copilot
- ✅ 其他支持Python的AI工具

---

## 📄 许可证

本项目采用 **MIT License**

- ✅ 商业使用
- ✅ 修改
- ✅ 分发
- ✅ 私有使用
- ⚠️ 提供"按原样"，无保证

详见: [LICENSE](LICENSE)

---

## 🙏 致谢

### 相关项目

感谢这些优秀的开源项目：

- [sing-box](https://github.com/SagerNet/sing-box) - 通用代理平台
- [Clash](https://github.com/Dreamacro/clash) - 规则基础代理工具
- [v2ray-core](https://github.com/v2fly/v2ray-core) - 网络代理工具
- [Shadowsocks](https://github.com/shadowsocks) - 安全代理协议

### 社区贡献

感谢所有为互联网自由贡献的人：

- 🌟 所有贡献者和技能开发者
- 🛡️ 节点提供者和维护者
- 💻 开源社区
- 🌐 Weini Securenet LLC

---

## 🌟 支持我们

如果这个项目对你有帮助：

- ⭐ **Star** 这个仓库
- 🔄 **Fork** 并改进
- 💡 **贡献** 新技能
- 📢 **分享** 给需要的人
- 💰 **赞助** [Weini Securenet LLC](https://github.com/sponsors/Weini-Securenet-LLC)

---

<div align="center">

### 🤖 Empower AI, Empower Freedom

*让 AI 成为每个人的自由工具*

**© 2026 Weini Securenet LLC** | Made with ❤️ for Freedom

[Website](https://weinidaohang.com/) | [Weini Quantum Proxy](https://github.com/Weini-Securenet-LLC/weini-quantum-proxy) | [Democratic Navigation](https://github.com/Weini-Securenet-LLC/democratic-navigation)

</div>
