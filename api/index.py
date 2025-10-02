#!/usr/bin/env python3
"""
FolioFlow Backend - Vercel Serverless Function
AI-Powered Cardano Transaction Analysis API
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
import sys
from datetime import datetime
import requests

# Add the parent directory to Python path to import config
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

try:
    from config.masumi_config import (
        AZURE_OPENAI_API_KEY, 
        AZURE_OPENAI_ENDPOINT, 
        AZURE_OPENAI_API_VERSION,
        AZURE_OPENAI_DEPLOYMENT_NAME
    )
    print("✅ Successfully imported Azure OpenAI configuration from config file")
except ImportError as e:
    print(f"⚠️ Could not import config: {e}")
    # Fallback to environment variables
    AZURE_OPENAI_API_KEY = os.getenv('AZURE_OPENAI_API_KEY', 'YOUR_AZURE_OPENAI_API_KEY_HERE')
    AZURE_OPENAI_ENDPOINT = os.getenv('AZURE_OPENAI_ENDPOINT', 'YOUR_AZURE_OPENAI_ENDPOINT_HERE')
    AZURE_OPENAI_API_VERSION = os.getenv('AZURE_OPENAI_API_VERSION', '2024-02-15-preview')
    AZURE_OPENAI_DEPLOYMENT_NAME = os.getenv('AZURE_OPENAI_DEPLOYMENT_NAME', 'YOUR_DEPLOYMENT_NAME_HERE')

# Initialize Flask app
app = Flask(__name__)
CORS(app, origins=["*"])  # Enable CORS for all origins in production

# Azure OpenAI Configuration validation
azure_openai_configured = (
    AZURE_OPENAI_API_KEY != "YOUR_AZURE_OPENAI_API_KEY_HERE" and 
    AZURE_OPENAI_ENDPOINT != "YOUR_AZURE_OPENAI_ENDPOINT_HERE" and
    AZURE_OPENAI_DEPLOYMENT_NAME != "YOUR_DEPLOYMENT_NAME_HERE"
)

def call_azure_openai(messages, max_tokens=4000, temperature=0.7):
    """Call Azure OpenAI API with enhanced timeout and error handling"""
    if not azure_openai_configured:
        return {
            "error": "Azure OpenAI not configured",
            "message": "Please configure Azure OpenAI credentials in environment variables"
        }
    
    headers = {
        "Content-Type": "application/json",
        "api-key": AZURE_OPENAI_API_KEY
    }
    
    data = {
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "top_p": 0.95,
        "frequency_penalty": 0,
        "presence_penalty": 0
    }
    
    url = f"{AZURE_OPENAI_ENDPOINT}/openai/deployments/{AZURE_OPENAI_DEPLOYMENT_NAME}/chat/completions?api-version={AZURE_OPENAI_API_VERSION}"
    
    try:
        print(f"🚀 Calling Azure OpenAI API...")
        print(f"📡 Endpoint: {AZURE_OPENAI_ENDPOINT}")
        print(f"🎯 Deployment: {AZURE_OPENAI_DEPLOYMENT_NAME}")
        print(f"📊 Request size: {len(str(data))} characters")
        
        # Extended timeout for complex analysis (120 seconds)
        response = requests.post(url, headers=headers, json=data, timeout=120)
        
        print(f"📈 Response status: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            if 'choices' in result and len(result['choices']) > 0:
                content = result['choices'][0]['message']['content']
                print(f"✅ Successful response: {len(content)} characters")
                return {"content": content}
            else:
                print("❌ No choices in response")
                return {"error": "No response content", "details": result}
        else:
            error_details = f"Status: {response.status_code}, Text: {response.text}"
            print(f"❌ API Error: {error_details}")
            return {"error": f"Azure OpenAI API error: {error_details}"}
            
    except requests.exceptions.Timeout:
        error_msg = "Request timed out after 120 seconds - try with shorter transaction data"
        print(f"⏰ Timeout Error: {error_msg}")
        return {"error": error_msg}
    except requests.exceptions.RequestException as e:
        error_msg = f"Request failed: {str(e)}"
        print(f"🔌 Connection Error: {error_msg}")
        return {"error": error_msg}
    except Exception as e:
        error_msg = f"Unexpected error: {str(e)}"
        print(f"💥 Unexpected Error: {error_msg}")
        return {"error": error_msg}

@app.route('/')
def home():
    return jsonify({
        "service": "FolioFlow AI Backend",
        "version": "2.0.0",
        "status": "running",
        "ai_service": "Azure OpenAI" if azure_openai_configured else "Not configured",
        "endpoints": ["/analyze"],
        "timestamp": datetime.now().isoformat()
    })

@app.route('/analyze', methods=['POST', 'OPTIONS'])
def analyze_transactions():
    """Enhanced transaction analysis with better error handling"""
    if request.method == 'OPTIONS':
        return '', 200
    
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400
        
        print(f"📥 Received analysis request: {len(str(data))} characters")
        
        # Extract wallet address and transactions
        wallet_address = data.get('walletAddress', 'Unknown')
        transactions = data.get('transactions', [])
        portfolio_data = data.get('portfolioData', {})
        
        print(f"🏦 Wallet: {wallet_address}")
        print(f"📊 Transactions: {len(transactions)}")
        print(f"💼 Portfolio data keys: {list(portfolio_data.keys()) if portfolio_data else 'None'}")
        
        if not transactions and not portfolio_data:
            return jsonify({"error": "No transaction or portfolio data provided"}), 400
        
        # Create enhanced prompt for AI analysis
        prompt = f"""
You are a professional Cardano blockchain analyst and financial advisor. Analyze the following portfolio data and provide comprehensive insights.

WALLET ADDRESS: {wallet_address}

PORTFOLIO DATA:
{json.dumps(portfolio_data, indent=2) if portfolio_data else "No portfolio data available"}

RECENT TRANSACTIONS:
{json.dumps(transactions[:20], indent=2) if transactions else "No transaction data available"}

Please provide a detailed analysis covering:

1. **Portfolio Overview**
   - Total ADA holdings and USD value
   - Asset distribution and diversification
   - Native tokens and their significance

2. **Transaction Analysis**
   - Transaction patterns and frequency
   - Spending vs receiving behavior
   - Notable large transactions or patterns

3. **Risk Assessment**
   - Portfolio concentration risks
   - Volatility exposure
   - Liquidity considerations

4. **Investment Insights**
   - Asset allocation recommendations
   - Potential optimization strategies
   - Market positioning analysis

5. **Security & Best Practices**
   - Wallet security observations
   - Transaction pattern security
   - Recommended improvements

6. **Future Outlook**
   - Growth potential analysis
   - Strategic recommendations
   - Risk mitigation strategies

Format your response in clear, professional sections with actionable insights. Use bullet points and clear headings for readability.
"""

        # Prepare messages for Azure OpenAI
        messages = [
            {
                "role": "system",
                "content": "You are an expert Cardano blockchain analyst and financial advisor specializing in portfolio analysis and investment strategy."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
        
        # Call Azure OpenAI with enhanced error handling
        ai_response = call_azure_openai(messages, max_tokens=4000, temperature=0.7)
        
        if "error" in ai_response:
            print(f"❌ AI Analysis failed: {ai_response['error']}")
            return jsonify({
                "error": "AI analysis failed",
                "details": ai_response.get("error", "Unknown error"),
                "timestamp": datetime.now().isoformat()
            }), 500
        
        analysis_result = ai_response.get("content", "No analysis content received")
        print(f"✅ Analysis completed: {len(analysis_result)} characters")
        
        return jsonify({
            "success": True,
            "analysis": analysis_result,
            "wallet_address": wallet_address,
            "transactions_analyzed": len(transactions),
            "timestamp": datetime.now().isoformat(),
            "ai_service": "Azure OpenAI"
        })
        
    except Exception as e:
        error_msg = f"Server error during analysis: {str(e)}"
        print(f"💥 Server Error: {error_msg}")
        return jsonify({
            "error": "Internal server error",
            "details": error_msg,
            "timestamp": datetime.now().isoformat()
        }), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Export the Flask app for Vercel
def handler(request, response):
    """Vercel serverless function handler"""
    return app

# Default export for Vercel (this is critical)
application = app

# For local development
if __name__ == '__main__':
    print("🚀 Starting FolioFlow AI Backend (Local Development)...")
    print("📋 Configuration:")
    print(f"   - Azure OpenAI API Key: {'✅ Configured' if azure_openai_configured else '❌ Not configured'}")
    print(f"   - Azure OpenAI Endpoint: {AZURE_OPENAI_ENDPOINT if azure_openai_configured else '❌ Not configured'}")
    print(f"   - Azure OpenAI Deployment: {AZURE_OPENAI_DEPLOYMENT_NAME if azure_openai_configured else '❌ Not configured'}")
    print(f"   - AI Service: {'✅ Azure OpenAI Ready' if azure_openai_configured else '❌ Not configured'}")
    
    app.run(debug=True, host='0.0.0.0', port=5000)