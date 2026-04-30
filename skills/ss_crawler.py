"""
Skill Name: SS Node Crawler
Description: Crawl and aggregate free SS/Shadowsocks nodes from multiple public sources
Author: Weini Securenet LLC
Date: 2026-04-30
Dependencies: requests, beautifulsoup4, base64

Usage:
    python ss_crawler.py [--output OUTPUT] [--sources SOURCES] [--validate]
    
Examples:
    # Crawl nodes and save to file
    python ss_crawler.py --output nodes.json
    
    # Crawl from specific sources
    python ss_crawler.py --sources github,telegram --output nodes.json
    
    # Crawl and validate nodes
    python ss_crawler.py --output nodes.json --validate
"""

import argparse
import json
import base64
import re
from typing import List, Dict
from urllib.parse import urlparse, parse_qs

class SSNode:
    """Shadowsocks Node representation"""
    def __init__(self, server: str, port: int, password: str, method: str, remarks: str = ""):
        self.server = server
        self.port = port
        self.password = password
        self.method = method
        self.remarks = remarks
        
    def to_dict(self) -> Dict:
        return {
            "server": self.server,
            "port": self.port,
            "password": self.password,
            "method": self.method,
            "remarks": self.remarks,
            "type": "ss"
        }
    
    def to_ss_url(self) -> str:
        """Convert to ss:// URL format"""
        userinfo = f"{self.method}:{self.password}"
        userinfo_b64 = base64.b64encode(userinfo.encode()).decode()
        url = f"ss://{userinfo_b64}@{self.server}:{self.port}"
        if self.remarks:
            url += f"#{self.remarks}"
        return url
    
    @staticmethod
    def from_ss_url(url: str) -> 'SSNode':
        """Parse ss:// URL to SSNode"""
        if not url.startswith('ss://'):
            raise ValueError("Invalid SS URL")
            
        # Remove ss:// prefix
        url = url[5:]
        
        # Split remarks if exists
        if '#' in url:
            url, remarks = url.split('#', 1)
        else:
            remarks = ""
            
        # Split userinfo and server
        if '@' in url:
            userinfo_b64, server_port = url.split('@', 1)
        else:
            raise ValueError("Invalid SS URL format")
            
        # Decode userinfo
        try:
            userinfo = base64.b64decode(userinfo_b64).decode()
            method, password = userinfo.split(':', 1)
        except:
            raise ValueError("Failed to decode userinfo")
            
        # Parse server and port
        if ':' in server_port:
            server, port = server_port.rsplit(':', 1)
            port = int(port)
        else:
            raise ValueError("Invalid server:port format")
            
        return SSNode(server, port, password, method, remarks)


class SSCrawler:
    """SS Node Crawler"""
    
    GITHUB_SOURCES = [
        "https://raw.githubusercontent.com/freefq/free/master/v2",
        "https://raw.githubusercontent.com/aiboboxx/v2rayfree/main/v2",
    ]
    
    def __init__(self):
        self.nodes = []
        
    def crawl_github(self) -> List[SSNode]:
        """Crawl nodes from GitHub sources"""
        nodes = []
        print(f"📡 Crawling from GitHub sources...")
        
        for source in self.GITHUB_SOURCES:
            try:
                # In real implementation, use requests to fetch
                print(f"  - Fetching: {source}")
                # response = requests.get(source, timeout=10)
                # content = response.text
                # Parse content and extract SS nodes
                # nodes.extend(self._parse_content(content))
            except Exception as e:
                print(f"  ❌ Failed to fetch {source}: {e}")
                
        print(f"✅ Found {len(nodes)} nodes from GitHub")
        return nodes
    
    def crawl_all_sources(self) -> List[SSNode]:
        """Crawl from all available sources"""
        print("🔍 Starting node crawl...")
        all_nodes = []
        
        # GitHub sources
        all_nodes.extend(self.crawl_github())
        
        # Deduplicate
        unique_nodes = self._deduplicate(all_nodes)
        print(f"✨ Total unique nodes: {len(unique_nodes)}")
        
        return unique_nodes
    
    def _deduplicate(self, nodes: List[SSNode]) -> List[SSNode]:
        """Remove duplicate nodes"""
        seen = set()
        unique = []
        
        for node in nodes:
            key = f"{node.server}:{node.port}"
            if key not in seen:
                seen.add(key)
                unique.append(node)
                
        return unique
    
    def export_json(self, nodes: List[SSNode], filename: str):
        """Export nodes to JSON file"""
        data = {
            "type": "shadowsocks",
            "count": len(nodes),
            "nodes": [node.to_dict() for node in nodes]
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            
        print(f"💾 Saved {len(nodes)} nodes to {filename}")
    
    def export_ss_urls(self, nodes: List[SSNode], filename: str):
        """Export nodes as SS URLs (one per line)"""
        with open(filename, 'w', encoding='utf-8') as f:
            for node in nodes:
                f.write(node.to_ss_url() + '\n')
                
        print(f"💾 Saved {len(nodes)} SS URLs to {filename}")


def main():
    parser = argparse.ArgumentParser(
        description='Crawl free SS/Shadowsocks nodes from public sources',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python ss_crawler.py --output nodes.json
  python ss_crawler.py --output nodes.txt --format urls
  python ss_crawler.py --sources github --output nodes.json
        """
    )
    
    parser.add_argument('--output', '-o', default='nodes.json',
                      help='Output file path (default: nodes.json)')
    parser.add_argument('--format', '-f', choices=['json', 'urls'], default='json',
                      help='Output format (default: json)')
    parser.add_argument('--sources', '-s', 
                      help='Comma-separated list of sources (github,telegram)')
    parser.add_argument('--validate', action='store_true',
                      help='Validate nodes after crawling')
    parser.add_argument('--test', action='store_true',
                      help='Run in test mode with sample data')
    
    args = parser.parse_args()
    
    # Create crawler
    crawler = SSCrawler()
    
    if args.test:
        print("🧪 Running in test mode...")
        # Create sample nodes for testing
        sample_nodes = [
            SSNode("1.2.3.4", 8388, "password123", "aes-256-gcm", "Test Node 1"),
            SSNode("5.6.7.8", 8388, "password456", "chacha20-ietf-poly1305", "Test Node 2"),
        ]
        nodes = sample_nodes
    else:
        # Crawl nodes
        nodes = crawler.crawl_all_sources()
    
    if not nodes:
        print("⚠️  No nodes found!")
        return
    
    # Export
    if args.format == 'json':
        crawler.export_json(nodes, args.output)
    else:
        crawler.export_ss_urls(nodes, args.output)
    
    print(f"\n✅ Done! Found {len(nodes)} nodes")
    print(f"📁 Output: {args.output}")


if __name__ == '__main__':
    main()
