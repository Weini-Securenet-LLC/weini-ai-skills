"""
Skill Name: sing-box Config Generator
Description: Generate sing-box proxy configuration from node list
Author: Weini Securenet LLC
Date: 2026-04-30
Dependencies: json

Usage:
    python singbox_config_generator.py [--input INPUT] [--output OUTPUT]
    
Examples:
    # Generate config from nodes
    python singbox_config_generator.py --input nodes.json --output config.json
    
    # Custom inbound port
    python singbox_config_generator.py --input nodes.json --port 7890
    
    # Enable advanced features
    python singbox_config_generator.py --input nodes.json --enable-dns --enable-routing
"""

import argparse
import json
from typing import List, Dict


class SingBoxGenerator:
    """sing-box Configuration Generator"""
    
    def __init__(self):
        self.config = {
            "log": {
                "disabled": False,
                "level": "info",
                "timestamp": True
            },
            "dns": {},
            "inbounds": [],
            "outbounds": [],
            "route": {}
        }
    
    def add_mixed_inbound(self, port: int = 1080):
        """Add mixed (SOCKS5 + HTTP) inbound"""
        inbound = {
            "type": "mixed",
            "tag": "mixed-in",
            "listen": "127.0.0.1",
            "listen_port": port,
            "sniff": True,
            "sniff_override_destination": True
        }
        self.config["inbounds"].append(inbound)
        return self
    
    def add_ss_outbound(self, node: Dict, tag: str = None) -> Dict:
        """Convert SS node to sing-box outbound"""
        if not tag:
            tag = f"ss-{node.get('server')}"
        
        outbound = {
            "type": "shadowsocks",
            "tag": tag,
            "server": node.get("server"),
            "server_port": node.get("port"),
            "method": node.get("method"),
            "password": node.get("password")
        }
        
        return outbound
    
    def add_nodes(self, nodes: List[Dict]):
        """Add multiple nodes as outbounds"""
        for i, node in enumerate(nodes):
            node_type = node.get("type", "ss")
            tag = f"{node_type}-{i}"
            
            if node_type == "ss":
                outbound = self.add_ss_outbound(node, tag)
                self.config["outbounds"].append(outbound)
        
        return self
    
    def add_direct_outbound(self):
        """Add direct outbound"""
        self.config["outbounds"].append({
            "type": "direct",
            "tag": "direct"
        })
        return self
    
    def add_block_outbound(self):
        """Add block outbound"""
        self.config["outbounds"].append({
            "type": "block",
            "tag": "block"
        })
        return self
    
    def add_urltest_selector(self, outbound_tags: List[str]):
        """Add automatic URL test selector"""
        selector = {
            "type": "urltest",
            "tag": "auto",
            "outbounds": outbound_tags,
            "url": "https://www.gstatic.com/generate_204",
            "interval": "10m",
            "tolerance": 50
        }
        self.config["outbounds"].insert(0, selector)
        return self
    
    def add_dns(self):
        """Add DNS configuration"""
        self.config["dns"] = {
            "servers": [
                {
                    "tag": "cloudflare",
                    "address": "https://1.1.1.1/dns-query"
                },
                {
                    "tag": "google",
                    "address": "https://8.8.8.8/dns-query"
                },
                {
                    "tag": "local",
                    "address": "local",
                    "detour": "direct"
                }
            ],
            "rules": [
                {
                    "outbound": "any",
                    "server": "local"
                },
                {
                    "clash_mode": "Direct",
                    "server": "local"
                },
                {
                    "clash_mode": "Global",
                    "server": "google"
                }
            ]
        }
        return self
    
    def add_routing_rules(self):
        """Add basic routing rules"""
        self.config["route"] = {
            "rules": [
                {
                    "protocol": "dns",
                    "outbound": "dns-out"
                },
                {
                    "geoip": "cn",
                    "outbound": "direct"
                },
                {
                    "geosite": "cn",
                    "outbound": "direct"
                },
                {
                    "geosite": "category-ads-all",
                    "outbound": "block"
                }
            ],
            "auto_detect_interface": True
        }
        return self
    
    def generate(self) -> Dict:
        """Generate final configuration"""
        return self.config
    
    def save(self, filename: str):
        """Save configuration to file"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, indent=2, ensure_ascii=False)
        print(f"💾 Configuration saved to {filename}")


def main():
    parser = argparse.ArgumentParser(
        description='Generate sing-box proxy configuration from node list',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python singbox_config_generator.py --input nodes.json --output config.json
  python singbox_config_generator.py --input nodes.json --port 7890 --enable-all
  python singbox_config_generator.py --input nodes.json --no-direct
        """
    )
    
    parser.add_argument('--input', '-i', required=True,
                      help='Input JSON file with nodes')
    parser.add_argument('--output', '-o', default='config.json',
                      help='Output configuration file (default: config.json)')
    parser.add_argument('--port', '-p', type=int, default=1080,
                      help='Inbound port (default: 1080)')
    parser.add_argument('--enable-dns', action='store_true',
                      help='Enable DNS configuration')
    parser.add_argument('--enable-routing', action='store_true',
                      help='Enable routing rules')
    parser.add_argument('--enable-all', action='store_true',
                      help='Enable all features')
    parser.add_argument('--no-direct', action='store_true',
                      help='Do not add direct outbound')
    parser.add_argument('--no-block', action='store_true',
                      help='Do not add block outbound')
    parser.add_argument('--auto-select', action='store_true',
                      help='Add URL test selector for automatic node selection')
    
    args = parser.parse_args()
    
    # Enable all features if requested
    if args.enable_all:
        args.enable_dns = True
        args.enable_routing = True
        args.auto_select = True
    
    # Load nodes
    try:
        with open(args.input, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, dict) and 'nodes' in data:
                nodes = data['nodes']
            elif isinstance(data, list):
                nodes = data
            else:
                raise ValueError("Invalid input format")
    except Exception as e:
        print(f"❌ Error loading input file: {e}")
        return
    
    if not nodes:
        print("⚠️  No nodes found!")
        return
    
    # Filter valid nodes
    valid_nodes = [n for n in nodes if n.get('valid', True)]
    print(f"📊 Loaded {len(valid_nodes)} nodes")
    
    # Create generator
    generator = SingBoxGenerator()
    
    # Add inbound
    generator.add_mixed_inbound(port=args.port)
    print(f"✅ Inbound: mixed (SOCKS5+HTTP) on port {args.port}")
    
    # Add nodes as outbounds
    generator.add_nodes(valid_nodes)
    print(f"✅ Added {len(valid_nodes)} node outbounds")
    
    # Add URL test selector
    if args.auto_select:
        outbound_tags = [f"ss-{i}" for i in range(len(valid_nodes))]
        generator.add_urltest_selector(outbound_tags)
        print(f"✅ Added automatic node selector")
    
    # Add direct/block outbounds
    if not args.no_direct:
        generator.add_direct_outbound()
        print(f"✅ Added direct outbound")
    
    if not args.no_block:
        generator.add_block_outbound()
        print(f"✅ Added block outbound")
    
    # Add DNS
    if args.enable_dns:
        generator.add_dns()
        print(f"✅ Added DNS configuration")
    
    # Add routing
    if args.enable_routing:
        generator.add_routing_rules()
        print(f"✅ Added routing rules")
    
    # Save configuration
    generator.save(args.output)
    
    print(f"\n🎉 Done! Configuration generated successfully")
    print(f"📁 Output: {args.output}")
    print(f"\n💡 To use this config with sing-box:")
    print(f"   sing-box run -c {args.output}")


if __name__ == '__main__':
    main()
