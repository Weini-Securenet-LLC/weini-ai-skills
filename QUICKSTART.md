# Quick Start Guide

## Installation

```bash
# Clone the repository
git clone https://github.com/Weini-Securenet-LLC/weini-ai-skills.git
cd weini-ai-skills

# Install dependencies
pip install -r requirements.txt
```

## Basic Usage

### 1. Crawl Free Nodes

```bash
python skills/ss_crawler.py --output nodes.json
```

### 2. Validate Nodes

```bash
python skills/node_validator.py --input nodes.json --output valid_nodes.json
```

### 3. Generate Configuration

```bash
python skills/singbox_config_generator.py --input valid_nodes.json --output config.json
```

### 4. Use with sing-box

```bash
sing-box run -c config.json
```

## Use with AI Tools

### Claude Desktop

Simply ask:
```
Please use ss_crawler.py to find some free SS nodes
```

Claude will automatically run the skill and return results.

### Cursor IDE

In Agent mode, request:
```
Run the node validator on nodes.json and show me the fast ones
```

Cursor will execute and display results.

## Common Workflows

### Find and Use Nodes Quickly

```bash
# 1. Crawl nodes
python skills/ss_crawler.py --output nodes.json

# 2. Validate and get fast nodes
python skills/node_validator.py --input nodes.json --max-latency 300 --output fast_nodes.json

# 3. Generate sing-box config
python skills/singbox_config_generator.py --input fast_nodes.json --output config.json --enable-all

# 4. Run sing-box
sing-box run -c config.json
```

### Automated Script

Create `update_nodes.sh`:

```bash
#!/bin/bash

echo "🔍 Crawling nodes..."
python skills/ss_crawler.py --output nodes.json

echo "✅ Validating nodes..."
python skills/node_validator.py --input nodes.json --output valid_nodes.json

echo "⚡ Generating config..."
python skills/singbox_config_generator.py --input valid_nodes.json --output config.json --enable-all

echo "✅ Done! Use: sing-box run -c config.json"
```

Make it executable:
```bash
chmod +x update_nodes.sh
./update_nodes.sh
```

## Tips

- Run validation regularly as nodes may go offline
- Use `--max-latency` to filter fast nodes
- Enable DNS and routing for better performance
- Backup working configs

## Troubleshooting

**No nodes found?**
- Check your internet connection
- Try running again later (sources may be temporarily down)

**Validation fails?**
- Increase timeout: `--timeout 10`
- Reduce concurrency: `--concurrency 5`
- Some nodes may be offline, that's normal

**Config doesn't work?**
- Ensure sing-box is installed
- Check config syntax: `sing-box check -c config.json`
- Try different nodes

## Next Steps

- Read [full documentation](docs/)
- Explore [all available skills](skills/)
- [Contribute](CONTRIBUTING.md) your own skills
- Join our [community](https://t.me/weini_quantum)

---

**© 2026 Weini Securenet LLC**
