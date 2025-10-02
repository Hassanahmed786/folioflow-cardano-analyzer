from http.server import BaseHTTPRequestHandler
import json
import urllib.parse
import os
from datetime import datetime

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Enable CORS
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        
        try:
            # Read the request body
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            
            # Parse JSON data
            try:
                data = json.loads(post_data.decode('utf-8'))
            except json.JSONDecodeError:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = {"error": "Invalid JSON data"}
                self.wfile.write(json.dumps(response).encode())
                return
            
            # Extract data
            wallet_address = data.get('walletAddress', 'Unknown')
            transactions = data.get('transactions', [])
            portfolio_data = data.get('portfolioData', {})
            
            # For now, return a mock analysis since we're testing deployment
            mock_analysis = {
                "success": True,
                "analysis": f"""
# Portfolio Analysis for {wallet_address}

## Portfolio Overview
- **Total Transactions Analyzed**: {len(transactions)}
- **Portfolio Status**: Active Cardano wallet
- **Analysis Date**: {datetime.now().isoformat()}

## Key Insights
- Your wallet shows regular transaction activity
- Portfolio demonstrates active engagement with the Cardano ecosystem
- Transaction patterns suggest diversified usage

## Recommendations
1. **Continue Regular Monitoring**: Keep tracking your portfolio performance
2. **Diversification**: Consider spreading investments across different assets
3. **Security**: Ensure your wallet security practices remain up to date

*Note: This is a simplified analysis. Full AI-powered insights will be available once Azure OpenAI is configured.*
                """,
                "wallet_address": wallet_address,
                "transactions_analyzed": len(transactions),
                "timestamp": datetime.now().isoformat(),
                "status": "mock_analysis",
                "note": "Demo version - Azure OpenAI integration pending environment variables"
            }
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(mock_analysis).encode())
            
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {
                "error": "Internal server error",
                "details": str(e),
                "timestamp": datetime.now().isoformat()
            }
            self.wfile.write(json.dumps(response).encode())
    
    def do_OPTIONS(self):
        # Handle preflight requests
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        self.end_headers()
    
    def do_GET(self):
        # Return info about the analyze endpoint
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        response = {
            "endpoint": "/api/analyze",
            "method": "POST",
            "description": "Portfolio analysis endpoint",
            "status": "ready",
            "timestamp": datetime.now().isoformat()
        }
        
        self.wfile.write(json.dumps(response).encode())