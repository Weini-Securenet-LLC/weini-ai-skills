# Weini AI Agent Skills

AI-compatible skills for proxy node management and internet freedom.

## Skills Manifest

This directory contains AI-ready skills that can be invoked by AI assistants through natural language or function calling.

### Skill Format

Each skill follows this standard structure:

```python
"""
Skill Name: [Name]
Description: [What it does]
Author: Weini Securenet LLC
Date: YYYY-MM-DD
Dependencies: [list]

Usage:
    [command line examples]
    
Examples:
    [usage examples]
"""

# Standard function interface
def main(args):
    """
    Main entry point for AI agents
    
    Args:
        args: Dictionary or argparse namespace
    
    Returns:
        Dict with 'success', 'data', and 'message' keys
    """
    pass
```

### AI Integration

Skills can be invoked by:

1. **Natural Language** (Recommended)
   ```
   "Find me some free proxy nodes"
   → AI calls ss_crawler skill
   ```

2. **Function Calling**
   ```json
   {
     "skill": "ss_crawler",
     "args": {
       "output": "nodes.json",
       "sources": ["github"]
     }
   }
   ```

3. **Direct Execution**
   ```bash
   python skills/ss_crawler.py --output nodes.json
   ```

### Standard Output Format

All skills return:

```python
{
    "success": bool,
    "data": any,
    "message": str,
    "metadata": {
        "skill": str,
        "duration": float,
        "timestamp": str
    }
}
```

### Adding New Skills

See [CONTRIBUTING.md](../CONTRIBUTING.md) for skill development guidelines.

### Compatibility

- ✅ Claude Code / Cursor
- ✅ GitHub Copilot  
- ✅ OpenAI Function Calling
- ✅ MCP (Model Context Protocol)
- ✅ LangChain Tools
- ✅ Command Line

---

**For detailed skill documentation, see [skills.json](../skills.json)**