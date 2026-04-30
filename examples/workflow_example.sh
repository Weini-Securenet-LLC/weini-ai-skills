#!/bin/bash

# Example: Automated Node Update Workflow
# 自动化节点更新工作流示例

set -e

echo "🤖 Weini AI Skills - Automated Workflow"
echo "========================================"
echo ""

# Step 1: Crawl nodes
echo "📡 Step 1: Crawling free nodes..."
python skills/ss_crawler.py --output nodes.json --test
echo "✅ Crawling complete"
echo ""

# Step 2: Validate nodes
echo "🔍 Step 2: Validating nodes..."
python skills/node_validator.py --input nodes.json --output validated_nodes.json --timeout 5 --concurrency 10
echo "✅ Validation complete"
echo ""

# Step 3: Filter fast nodes
echo "⚡ Step 3: Filtering fast nodes (< 300ms)..."
python skills/node_validator.py --input validated_nodes.json --output fast_nodes.json --max-latency 300
echo "✅ Filtering complete"
echo ""

# Step 4: Generate sing-box config
echo "🔧 Step 4: Generating sing-box configuration..."
python skills/singbox_config_generator.py --input fast_nodes.json --output config.json --enable-all --port 1080
echo "✅ Configuration generated"
echo ""

echo "========================================"
echo "🎉 Workflow complete!"
echo ""
echo "📁 Generated files:"
echo "  - nodes.json (all crawled nodes)"
echo "  - validated_nodes.json (validated nodes)"
echo "  - fast_nodes.json (fast nodes < 300ms)"
echo "  - config.json (sing-box config)"
echo ""
echo "💡 To use the proxy:"
echo "   sing-box run -c config.json"
echo ""
echo "🔄 To update nodes again, simply run:"
echo "   ./examples/workflow_example.sh"
echo ""
