"""
Skill Name: Node Validator
Description: Validate proxy nodes' connectivity and measure latency
Author: Weini Securenet LLC
Date: 2026-04-30
Dependencies: requests, socket, concurrent.futures

Usage:
    python node_validator.py [--input INPUT] [--output OUTPUT] [--timeout TIMEOUT]
    
Examples:
    # Validate nodes from JSON file
    python node_validator.py --input nodes.json --output valid_nodes.json
    
    # Custom timeout and concurrency
    python node_validator.py --input nodes.json --timeout 10 --concurrency 20
    
    # Filter fast nodes only (latency < 300ms)
    python node_validator.py --input nodes.json --max-latency 300
"""

import argparse
import json
import socket
import time
from typing import List, Dict, Optional
from concurrent.futures import ThreadPoolExecutor, as_completed


class NodeValidator:
    """Proxy Node Validator"""
    
    def __init__(self, timeout: int = 5, concurrency: int = 10):
        self.timeout = timeout
        self.concurrency = concurrency
        
    def validate_tcp_connection(self, server: str, port: int) -> tuple[bool, float]:
        """
        Test TCP connection to server:port
        Returns: (success, latency_ms)
        """
        try:
            start_time = time.time()
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            result = sock.connect_ex((server, port))
            latency = (time.time() - start_time) * 1000  # Convert to ms
            sock.close()
            
            return result == 0, latency
        except Exception as e:
            return False, -1
    
    def validate_node(self, node: Dict) -> Dict:
        """
        Validate a single node
        Returns node dict with validation results
        """
        server = node.get('server')
        port = node.get('port')
        
        if not server or not port:
            return {**node, 'valid': False, 'latency': -1, 'error': 'Invalid node data'}
        
        print(f"Testing {server}:{port}...", end=' ')
        
        success, latency = self.validate_tcp_connection(server, port)
        
        result = {
            **node,
            'valid': success,
            'latency': round(latency, 2) if success else -1,
            'tested_at': time.strftime('%Y-%m-%d %H:%M:%S')
        }
        
        if success:
            print(f"✅ {latency:.0f}ms")
        else:
            print(f"❌ Failed")
            
        return result
    
    def validate_batch(self, nodes: List[Dict]) -> List[Dict]:
        """
        Validate multiple nodes concurrently
        """
        print(f"🔍 Validating {len(nodes)} nodes (concurrency: {self.concurrency})...\n")
        
        results = []
        with ThreadPoolExecutor(max_workers=self.concurrency) as executor:
            future_to_node = {executor.submit(self.validate_node, node): node for node in nodes}
            
            for future in as_completed(future_to_node):
                try:
                    result = future.result()
                    results.append(result)
                except Exception as e:
                    node = future_to_node[future]
                    print(f"❌ Error validating {node.get('server')}: {e}")
                    results.append({**node, 'valid': False, 'error': str(e)})
        
        return results
    
    def get_valid_nodes(self, results: List[Dict]) -> List[Dict]:
        """Filter only valid nodes"""
        return [r for r in results if r.get('valid', False)]
    
    def get_fast_nodes(self, results: List[Dict], max_latency: int = 500) -> List[Dict]:
        """Filter nodes with latency under threshold"""
        valid = self.get_valid_nodes(results)
        return [r for r in valid if r.get('latency', float('inf')) <= max_latency]
    
    def sort_by_latency(self, results: List[Dict]) -> List[Dict]:
        """Sort nodes by latency (fastest first)"""
        valid = self.get_valid_nodes(results)
        return sorted(valid, key=lambda x: x.get('latency', float('inf')))
    
    def print_summary(self, results: List[Dict]):
        """Print validation summary"""
        total = len(results)
        valid = len(self.get_valid_nodes(results))
        fast = len(self.get_fast_nodes(results, max_latency=300))
        
        print(f"\n{'='*50}")
        print(f"Validation Summary")
        print(f"{'='*50}")
        print(f"Total nodes tested: {total}")
        print(f"Valid nodes: {valid} ({valid/total*100:.1f}%)")
        print(f"Fast nodes (<300ms): {fast} ({fast/total*100:.1f}%)")
        
        if valid > 0:
            latencies = [r['latency'] for r in results if r.get('valid')]
            avg_latency = sum(latencies) / len(latencies)
            min_latency = min(latencies)
            max_latency = max(latencies)
            
            print(f"\nLatency Stats:")
            print(f"  Min: {min_latency:.0f}ms")
            print(f"  Max: {max_latency:.0f}ms")
            print(f"  Avg: {avg_latency:.0f}ms")
        
        print(f"{'='*50}\n")


def main():
    parser = argparse.ArgumentParser(
        description='Validate proxy nodes connectivity and latency',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python node_validator.py --input nodes.json --output valid_nodes.json
  python node_validator.py --input nodes.json --max-latency 300
  python node_validator.py --input nodes.json --timeout 10 --concurrency 20
        """
    )
    
    parser.add_argument('--input', '-i', required=True,
                      help='Input JSON file with nodes')
    parser.add_argument('--output', '-o',
                      help='Output JSON file for validation results')
    parser.add_argument('--timeout', '-t', type=int, default=5,
                      help='Timeout in seconds (default: 5)')
    parser.add_argument('--concurrency', '-c', type=int, default=10,
                      help='Number of concurrent tests (default: 10)')
    parser.add_argument('--max-latency', '-m', type=int,
                      help='Filter nodes with latency under threshold (ms)')
    parser.add_argument('--sort', action='store_true',
                      help='Sort results by latency')
    
    args = parser.parse_args()
    
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
        print("⚠️  No nodes to validate!")
        return
    
    # Create validator
    validator = NodeValidator(timeout=args.timeout, concurrency=args.concurrency)
    
    # Validate nodes
    results = validator.validate_batch(nodes)
    
    # Filter/sort results
    if args.max_latency:
        results = validator.get_fast_nodes(results, max_latency=args.max_latency)
        print(f"\n🎯 Filtered to {len(results)} nodes with latency < {args.max_latency}ms")
    
    if args.sort:
        results = validator.sort_by_latency(results)
        print("\n📊 Results sorted by latency")
    
    # Print summary
    validator.print_summary(results)
    
    # Save results
    if args.output:
        output_data = {
            "validated_at": time.strftime('%Y-%m-%d %H:%M:%S'),
            "total": len(results),
            "valid": len(validator.get_valid_nodes(results)),
            "nodes": results
        }
        
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)
            
        print(f"💾 Results saved to {args.output}")
    
    print(f"\n✅ Done!")


if __name__ == '__main__':
    main()
