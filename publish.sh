#!/bin/bash

# Weini AI Agent Skills - Publisher Script
# AI 技能开源项目 - 发布脚本

set -e

echo "🤖 准备发布 Weini AI Agent Skills..."
echo ""

# 检查是否在正确的目录
if [ ! -f "README.md" ] || [ ! -d "skills" ]; then
    echo "❌ 错误: 找不到必要的文件或目录"
    echo "请在 weini-ai-skills 目录中运行此脚本"
    exit 1
fi

# 初始化 Git 仓库
if [ ! -d ".git" ]; then
    echo "📦 初始化 Git 仓库..."
    git init
    echo "✅ Git 仓库已初始化"
else
    echo "✅ Git 仓库已存在"
fi

# 添加所有文件
echo ""
echo "📝 添加文件..."
git add .

# 创建提交
echo ""
echo "💾 创建提交..."
git commit -m "Initial commit: Weini AI Agent Skills

🤖 开源 AI 工具技能库，让 AI 成为互联网自由的工具

Features:
- SS节点爬虫
- 节点验证器
- sing-box配置生成器
- 批量处理工具
- 自动化工作流

Skills:
- ss_crawler.py - SS节点爬取
- node_validator.py - 节点验证
- singbox_config_generator.py - 配置生成

Usage:
- 与 Claude、Cursor 等 AI 工具集成
- 命令行直接使用
- 自动化脚本

Documentation:
- 完整使用文档
- 贡献指南
- 快速开始指南
- 示例工作流

© 2026 Weini Securenet LLC"

# 设置主分支
echo ""
echo "🌿 设置主分支..."
git branch -M main

# 添加远程仓库
REMOTE_URL="git@github.com-weini:Weini-Securenet-LLC/weini-ai-skills.git"
if git remote | grep -q "origin"; then
    echo "🔗 更新远程仓库地址..."
    git remote set-url origin "$REMOTE_URL"
else
    echo "🔗 添加远程仓库..."
    git remote add origin "$REMOTE_URL"
fi

echo ""
echo "✅ 准备完成！"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📋 下一步操作："
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "1️⃣  在 GitHub 创建仓库："
echo "   名称: weini-ai-skills"
echo "   组织: Weini-Securenet-LLC"
echo "   可见性: Public"
echo "   描述: Open-source AI tools for internet freedom"
echo "   不要添加 README、.gitignore 或 LICENSE"
echo ""
echo "   快速创建链接："
echo "   https://github.com/organizations/Weini-Securenet-LLC/repositories/new"
echo ""
echo "2️⃣  创建后，运行以下命令推送："
echo "   git push -u origin main"
echo ""
echo "3️⃣  配置仓库设置："
echo "   - Topics: ai, proxy, vpn, freedom, python, skills, automation"
echo "   - Enable Issues and Discussions"
echo "   - Add description and website"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "🎯 项目亮点:"
echo "   - 13+ AI 技能脚本"
echo "   - 支持多种 AI 工具（Claude、Cursor、GPT）"
echo "   - 完整文档和示例"
echo "   - 自动化工作流"
echo "   - 社区驱动开发"
echo ""
echo "🤖 Empower AI, Empower Freedom!"
echo ""
