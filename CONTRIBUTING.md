# Contributing to Weini AI Agent Skills

感谢你对本项目的关注！我们欢迎所有形式的贡献。

## 🤝 行为准则

本项目遵循 [Contributor Covenant](CODE_OF_CONDUCT.md) 行为准则。参与即表示您同意遵守其条款。

## 💡 贡献类型

### 1. 贡献新技能 ⭐

这是最有价值的贡献！

**步骤**:
1. Fork 本仓库
2. 创建技能分支: `git checkout -b skill/your-skill-name`
3. 在 `skills/` 目录创建你的技能脚本
4. 添加文档和使用示例
5. 提交 Pull Request

**技能要求**:
- 清晰的文档头部（功能、作者、依赖、使用方法）
- 命令行参数支持
- 错误处理
- 示例用法
- 测试数据

**技能模板**:
```python
"""
Skill Name: Your Skill Name
Description: What this skill does
Author: Your Name
Date: 2026-04-30
Dependencies: list, dependencies

Usage:
    python your_skill.py [args]
    
Examples:
    python your_skill.py --input data.json
"""

import argparse

def main():
    parser = argparse.ArgumentParser(description='Your skill')
    parser.add_argument('--input', help='Input file')
    args = parser.parse_args()
    
    # Your code here
    
if __name__ == '__main__':
    main()
```

### 2. Bug 修复 🐛

发现 Bug？请：
1. 创建 Issue 描述问题
2. Fork 并创建修复分支
3. 提交 PR 引用 Issue

### 3. 文档改进 📖

帮助改进文档：
- README 增强
- 技能使用指南
- 常见问题解答
- 多语言翻译

### 4. 功能增强 ✨

改进现有技能：
- 性能优化
- 新增参数选项
- 更好的错误处理
- 输出格式改进

## 📋 开发指南

### 环境设置

```bash
# 克隆仓库
git clone https://github.com/Weini-Securenet-LLC/weini-ai-skills.git
cd weini-ai-skills

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows

# 安装依赖
pip install -r requirements.txt
```

### 代码规范

- 使用 Python 3.8+ 特性
- 遵循 PEP 8 风格指南
- 使用类型提示（Type Hints）
- 添加文档字符串（Docstrings）
- 变量命名清晰有意义

### 提交信息格式

使用语义化提交信息：

```
<类型>: <简短描述>

<详细描述>（可选）

<相关Issue>（可选）
```

**类型**:
- `Skill`: 新增技能
- `Fix`: Bug修复
- `Docs`: 文档更新
- `Feat`: 功能增强
- `Refactor`: 代码重构
- `Test`: 测试相关
- `Chore`: 构建/工具相关

**示例**:
```
Skill: 添加 Clash 配置生成器

- 支持多种节点类型
- 自动分组功能
- 规则集配置

Closes #42
```

## 🧪 测试

在提交 PR 前，请确保：

```bash
# 测试你的技能
python skills/your_skill.py --test

# 确保没有语法错误
python -m py_compile skills/your_skill.py

# 测试所有依赖已列出
pip install -r requirements.txt
```

## 📤 Pull Request 流程

1. **更新你的 Fork**
   ```bash
   git remote add upstream https://github.com/Weini-Securenet-LLC/weini-ai-skills.git
   git fetch upstream
   git merge upstream/main
   ```

2. **创建分支**
   ```bash
   git checkout -b skill/my-new-skill
   ```

3. **提交更改**
   ```bash
   git add .
   git commit -m "Skill: 添加新技能"
   git push origin skill/my-new-skill
   ```

4. **创建 PR**
   - 访问 GitHub 仓库
   - 点击 "New Pull Request"
   - 选择你的分支
   - 填写 PR 模板
   - 提交

### PR 检查清单

- [ ] 代码遵循项目规范
- [ ] 添加了清晰的文档
- [ ] 包含使用示例
- [ ] 更新了 README（如需要）
- [ ] 测试通过
- [ ] 提交信息清晰

## 🎯 贡献想法

不确定贡献什么？这里有一些想法：

### 新技能想法

- [ ] Telegram Bot 节点发布器
- [ ] 订阅链接转换器
- [ ] 节点评分系统
- [ ] 自动测速工具
- [ ] 配置备份/恢复
- [ ] 节点分享二维码生成
- [ ] 批量订阅管理
- [ ] 节点健康监控
- [ ] 智能节点推荐

### 改进想法

- [ ] 添加更多数据源
- [ ] 改进错误处理
- [ ] 增加并发性能
- [ ] 支持更多代理协议
- [ ] 添加配置预设
- [ ] 改进CLI体验
- [ ] 添加进度条显示
- [ ] 支持配置文件

## 🔒 安全问题

如果发现安全漏洞，请**不要**创建公开 Issue。

请发送邮件至: weinidaohang@proton.me
主题: [SECURITY] Weini AI Skills

## 📞 获取帮助

需要帮助？

- 💬 [GitHub Discussions](https://github.com/Weini-Securenet-LLC/weini-ai-skills/discussions)
- 📧 Email: weinidaohang@proton.me
- 💬 Telegram: [@weini_quantum](https://t.me/weini_quantum)

## 🙏 致谢

感谢所有贡献者！你的名字将出现在 [CONTRIBUTORS.md](CONTRIBUTORS.md)

---

**© 2026 Weini Securenet LLC** | Together, we make AI tools for freedom!
