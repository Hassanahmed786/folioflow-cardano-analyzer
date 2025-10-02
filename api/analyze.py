from http.server import BaseHTTPRequestHandler
import json
import os
import urllib.request
from datetime import datetime

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
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
                self.send_header('Access-Control-Allow-Origin', '*')
                self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
                self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
                self.end_headers()
                response = {"error": "Invalid JSON data"}
                self.wfile.write(json.dumps(response).encode())
                return
            
            # Extract data
            wallet_address = data.get('walletAddress', 'Unknown')
            transactions = data.get('transactions', [])
            portfolio_data = data.get('portfolioData', {})
            
            # Get Azure OpenAI configuration from environment variables
            azure_api_key = os.getenv('AZURE_OPENAI_API_KEY')
            azure_endpoint = os.getenv('AZURE_OPENAI_ENDPOINT') 
            azure_deployment = os.getenv('AZURE_OPENAI_DEPLOYMENT_NAME', 'model-router')
            azure_api_version = os.getenv('AZURE_OPENAI_API_VERSION', '2024-08-01-preview')
            
            # Check if Azure OpenAI is configured
            if azure_api_key and azure_endpoint:
                # Call Azure OpenAI for real analysis
                analysis_result = self.call_azure_openai(
                    wallet_address, transactions, portfolio_data,
                    azure_api_key, azure_endpoint, azure_deployment, azure_api_version
                )
            else:
                # Return mock analysis
                analysis_result = self.create_mock_analysis(wallet_address, transactions, portfolio_data)
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
            self.end_headers()
            self.wfile.write(json.dumps(analysis_result).encode())
            
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
            self.end_headers()
            response = {
                "error": "Internal server error",
                "details": str(e),
                "timestamp": datetime.now().isoformat()
            }
            self.wfile.write(json.dumps(response).encode())
    
    def call_azure_openai(self, wallet_address, transactions, portfolio_data, api_key, endpoint, deployment, api_version):
        """Call Azure OpenAI for real analysis"""
        try:
            prompt = f"""
You are a professional Cardano blockchain analyst. Analyze this portfolio data and provide insights.

WALLET: {wallet_address}
TRANSACTIONS: {len(transactions)} analyzed
PORTFOLIO DATA: {json.dumps(portfolio_data) if portfolio_data else "No portfolio data"}

Provide a professional analysis covering:
1. Portfolio Overview
2. Transaction Patterns  
3. Risk Assessment
4. Recommendations

Format as markdown for readability.
"""
            
            # Prepare request data
            request_data = {
                "messages": [
                    {"role": "system", "content": "You are an expert Cardano blockchain analyst."},
                    {"role": "user", "content": prompt}
                ],
                "max_tokens": 3000,
                "temperature": 0.7
            }
            
            # Make request to Azure OpenAI
            url = f"{endpoint}/openai/deployments/{deployment}/chat/completions?api-version={api_version}"
            headers = {
                "Content-Type": "application/json",
                "api-key": api_key
            }
            
            req = urllib.request.Request(url, json.dumps(request_data).encode(), headers)
            with urllib.request.urlopen(req, timeout=30) as response:
                result = json.loads(response.read().decode())
                
                if 'choices' in result and result['choices']:
                    analysis_text = result['choices'][0]['message']['content']
                    return {
                        "success": True,
                        "analysis": analysis_text,
                        "wallet_address": wallet_address,
                        "transactions_analyzed": len(transactions),
                        "timestamp": datetime.now().isoformat(),
                        "ai_service": "Azure OpenAI",
                        "status": "ai_analysis_complete"
                    }
                else:
                    return self.create_mock_analysis(wallet_address, transactions, portfolio_data, "Azure OpenAI response error")
                    
        except Exception as e:
            return self.create_mock_analysis(wallet_address, transactions, portfolio_data, f"Azure OpenAI error: {str(e)}")
    
    def create_mock_analysis(self, wallet_address, transactions, portfolio_data, error_note=None):
        """Create mock analysis when Azure OpenAI is not available"""
        return {
            "success": True,
            "analysis": f"""
# Portfolio Analysis for {wallet_address}

## 📊 Portfolio Overview
- **Total Transactions Analyzed**: {len(transactions)}
- **Portfolio Status**: Active Cardano wallet
- **Analysis Date**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## 📈 Transaction Patterns
- Your wallet shows {'regular' if len(transactions) > 5 else 'moderate'} transaction activity
- Portfolio demonstrates active engagement with the Cardano ecosystem
- Transaction volume suggests {'high' if len(transactions) > 20 else 'moderate'} usage

## ⚠️ Risk Assessment
- **Activity Level**: {'High' if len(transactions) > 20 else 'Moderate' if len(transactions) > 5 else 'Low'}
- **Diversification**: Analysis based on transaction patterns
- **Security**: Regular monitoring recommended

## 💡 Recommendations
1. **Continue Monitoring**: Regular portfolio reviews recommended
2. **Diversification**: Consider spreading across different assets
3. **Security**: Maintain strong wallet security practices
4. **DeFi Exploration**: Consider Cardano DeFi opportunities

## 🔧 Technical Note
{error_note or 'This is a demo analysis. For full AI-powered insights, ensure Azure OpenAI environment variables are configured in your Vercel deployment.'}

---
*Powered by FolioFlow AI Portfolio Analyzer*
            """,
            "wallet_address": wallet_address,
            "transactions_analyzed": len(transactions),
            "timestamp": datetime.now().isoformat(),
            "status": "demo_analysis",
            "ai_service": "Demo Mode"
        }
    
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
        
        # Check if Azure OpenAI is configured
        azure_configured = bool(os.getenv('AZURE_OPENAI_API_KEY') and os.getenv('AZURE_OPENAI_ENDPOINT'))
        
        response = {
            "endpoint": "/api/analyze-full",
            "method": "POST",
            "description": "Complete portfolio analysis with Azure OpenAI integration",
            "azure_openai_configured": azure_configured,
            "status": "ready",
            "timestamp": datetime.now().isoformat()
        }
        
        self.wfile.write(json.dumps(response).encode())