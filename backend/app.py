#!/usr/bin/env python3
"""
FolioFlow Backend - AI-Powered Cardano Transaction Analysis
A Flask backend service that receives Cardano transaction data and provides AI-powered accounting insights.
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
    # Fallback to environment variables or defaults
    AZURE_OPENAI_API_KEY = os.getenv('AZURE_OPENAI_API_KEY', 'YOUR_AZURE_OPENAI_API_KEY_HERE')
    AZURE_OPENAI_ENDPOINT = os.getenv('AZURE_OPENAI_ENDPOINT', 'YOUR_AZURE_OPENAI_ENDPOINT_HERE')
    AZURE_OPENAI_API_VERSION = os.getenv('AZURE_OPENAI_API_VERSION', '2024-02-15-preview')
    AZURE_OPENAI_DEPLOYMENT_NAME = os.getenv('AZURE_OPENAI_DEPLOYMENT_NAME', 'YOUR_DEPLOYMENT_NAME_HERE')

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# Azure OpenAI Configuration validation
azure_openai_configured = (
    AZURE_OPENAI_API_KEY != "YOUR_AZURE_OPENAI_API_KEY_HERE" and 
    AZURE_OPENAI_ENDPOINT != "YOUR_AZURE_OPENAI_ENDPOINT_HERE" and
    AZURE_OPENAI_DEPLOYMENT_NAME != "YOUR_DEPLOYMENT_NAME_HERE"
)

if azure_openai_configured:
    print("✅ Azure OpenAI configuration detected")
else:
    print("❌ Azure OpenAI not configured - please update the configuration variables")

@app.route('/')
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "service": "FolioFlow AI Backend",
        "version": "1.0.0",
        "timestamp": datetime.now().isoformat()
    })

@app.route('/analyze', methods=['POST'])
def analyze_transactions():
    """
    Main analysis endpoint that receives transaction data and returns AI-powered insights
    
    Expected input:
    {
        "transactions": [...],  # Array of transaction objects from Blockfrost
        "wallet_address": "addr1..."  # Wallet address (optional)
    }
    
    Returns:
    {
        "portfolio_summary": {...},
        "transaction_analysis": [...],
        "insights": {...}
    }
    """
    try:
        # Validate request
        if not request.is_json:
            return jsonify({"error": "Request must be JSON"}), 400
        
        data = request.get_json()
        
        if not data or 'transactions' not in data:
            return jsonify({"error": "Missing 'transactions' field in request"}), 400
        
        transactions = data.get('transactions', [])
        wallet_address = data.get('wallet_address', 'Unknown')
        
        if not transactions:
            return jsonify({"error": "No transactions provided"}), 400
        
        print(f"📊 Analyzing {len(transactions)} transactions for wallet: {wallet_address[:20]}...")
        
        # Check if Azure OpenAI is configured
        if not azure_openai_configured:
            return jsonify({"error": "Azure OpenAI service is not configured. Please check your API key configuration."}), 503
        
        # Generate AI analysis
        analysis_result = generate_ai_analysis(transactions, wallet_address)
        
        if not analysis_result:
            return jsonify({"error": "Failed to generate AI analysis"}), 500
        
        print("✅ Analysis completed successfully")
        return jsonify(analysis_result)
        
    except Exception as e:
        print(f"❌ Analysis error: {str(e)}")
        return jsonify({"error": f"Analysis failed: {str(e)}"}), 500

def generate_ai_analysis(transactions, wallet_address):
    """
    Generate AI-powered analysis using Azure OpenAI
    """
    try:
        # Prepare transaction data for AI analysis
        transaction_summary = prepare_transaction_data(transactions)
        
        # Create prompt for Azure OpenAI
        prompt = create_analysis_prompt(transaction_summary, wallet_address)
        
        # Generate AI response using Azure OpenAI
        response_text = call_azure_openai(prompt)
        print(f"🔍 Response text type: {type(response_text)}")
        print(f"🔍 Response text value: {repr(response_text)}")
        
        if not response_text:
            raise Exception("Empty response from Azure OpenAI")
        
        # Parse AI response
        ai_analysis = parse_ai_response(response_text)
        
        return ai_analysis
        
    except Exception as e:
        print(f"❌ AI analysis error: {str(e)}")
        return None

def call_azure_openai(prompt):
    """
    Make API call to Azure OpenAI with improved error handling
    """
    try:
        # Validate prompt length to prevent token overflow
        if len(prompt) > 100000:  # Approximately 25k tokens
            print(f"⚠️ Prompt too long ({len(prompt)} chars), truncating...")
            prompt = prompt[:100000] + "\n\n[Content truncated due to length]"
        
        # Construct Azure OpenAI endpoint URL
        endpoint_url = f"{AZURE_OPENAI_ENDPOINT}/openai/deployments/{AZURE_OPENAI_DEPLOYMENT_NAME}/chat/completions?api-version={AZURE_OPENAI_API_VERSION}"
        print(f"🔗 Azure OpenAI URL: {endpoint_url}")
        
        headers = {
            "Content-Type": "application/json",
            "api-key": AZURE_OPENAI_API_KEY
        }
        
        data = {
            "messages": [
                {
                    "role": "system",
                    "content": "You are an expert Cardano blockchain analyst. Provide concise, structured financial insights."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "max_tokens": 4000,
            "temperature": 0.3,
            "top_p": 0.9,
            "frequency_penalty": 0.1,
            "presence_penalty": 0.1
        }
        
        print(f"📤 Sending request to Azure OpenAI... (timeout: 120s)")
        response = requests.post(endpoint_url, headers=headers, json=data, timeout=120)
        print(f"📨 Response status: {response.status_code}")
        
        if response.status_code != 200:
            print(f"❌ Azure OpenAI error response: {response.text}")
            raise Exception(f"Azure OpenAI API error: {response.status_code} - {response.text}")
        
        response_json = response.json()
        print(f"📋 Full Azure OpenAI response: {response_json}")
        
        if 'choices' not in response_json or not response_json['choices']:
            print(f"❌ No choices in response: {response_json}")
            raise Exception("No response choices from Azure OpenAI")
        
        content = response_json['choices'][0]['message']['content']
        print(f"📝 AI response content length: {len(content) if content else 0}")
        print(f"📝 AI response preview: {content[:200] if content else 'None'}...")
        
        return content
        
    except requests.exceptions.Timeout:
        print("⏰ Azure OpenAI request timed out after 120 seconds")
        raise Exception("Azure OpenAI request timed out - the request took too long to complete")
    except requests.exceptions.ConnectionError:
        print("🔌 Azure OpenAI connection error")
        raise Exception("Azure OpenAI connection error - please check your internet connection")
    except requests.exceptions.RequestException as e:
        print(f"🌐 Azure OpenAI request failed: {str(e)}")
        raise Exception(f"Azure OpenAI request failed: {str(e)}")
    except json.JSONDecodeError as e:
        print(f"📄 JSON decode error: {str(e)}")
        raise Exception(f"Invalid JSON response from Azure OpenAI: {str(e)}")
    except KeyError as e:
        print(f"🔑 Missing key in response: {str(e)}")
        raise Exception(f"Unexpected response format from Azure OpenAI: missing {str(e)}")
    except Exception as e:
        print(f"❌ Unexpected Azure OpenAI error: {str(e)}")
        raise Exception(f"Azure OpenAI error: {str(e)}")

def prepare_transaction_data(transactions):
    """
    Prepare and summarize transaction data for AI analysis
    """
    try:
        summary = {
            "total_transactions": len(transactions),
            "transaction_details": []
        }
        
        for i, tx in enumerate(transactions[:20]):  # Limit to 20 transactions for analysis
            tx_summary = {
                "transaction_number": i + 1,
                "hash": tx.get('hash', 'Unknown')[:16] + '...' if tx.get('hash') else 'Unknown',
                "block": tx.get('block', 'Unknown'),
                "block_time": tx.get('block_time', 'Unknown'),
                "fees": tx.get('fees', 'Unknown'),
                "size": tx.get('size', 'Unknown'),
                "input_count": len(tx.get('inputs', [])),
                "output_count": len(tx.get('outputs', [])),
                "total_output": tx.get('output_amount', 'Unknown')
            }
            summary["transaction_details"].append(tx_summary)
        
        return summary
        
    except Exception as e:
        print(f"❌ Error preparing transaction data: {str(e)}")
        return {"total_transactions": len(transactions), "error": "Failed to process transaction details"}

def create_analysis_prompt(transaction_data, wallet_address):
    """
    Create a detailed prompt for AI analysis
    """
    prompt = f"""
You are an expert blockchain accountant analyzing Cardano wallet transactions. Please provide a comprehensive analysis of the following transaction data.

Wallet Address: {wallet_address}
Transaction Data: {json.dumps(transaction_data, indent=2)}

Please analyze this data and provide your response in JSON format with the following structure. Be sure to make it valid JSON:

{{
    "portfolio_summary": {{
        "total_transactions": "number",
        "total_fees_paid": "estimated amount in ADA",
        "transaction_frequency": "analysis of spending patterns",
        "account_type_assessment": "likely use case (personal, business, trading, etc.)"
    }},
    "transaction_analysis": [
        {{
            "category": "Transaction Type Category",
            "count": "number of transactions",
            "total_value": "estimated total value",
            "description": "brief description"
        }}
    ],
    "insights": {{
        "spending_patterns": "analysis of spending behavior",
        "tax_considerations": "potential tax implications",
        "recommendations": "actionable recommendations for the user",
        "risk_assessment": "any notable patterns or risks"
    }}
}}

Focus on:
1. Transaction patterns and frequency
2. Fee analysis and optimization suggestions
3. Portfolio activity assessment
4. Potential accounting categories
5. Tax-relevant insights
6. Security and best practices recommendations

Provide concrete, actionable insights based on the actual transaction data. If certain data is not available or unclear, mention this in your analysis.
"""
    
    return prompt

def parse_ai_response(ai_text):
    """
    Parse AI response and ensure it's valid JSON
    """
    try:
        # Try to find JSON in the response
        start_idx = ai_text.find('{')
        end_idx = ai_text.rfind('}') + 1
        
        if start_idx == -1 or end_idx == 0:
            # If no JSON found, create a structured response
            return create_fallback_response(ai_text)
        
        json_str = ai_text[start_idx:end_idx]
        parsed_response = json.loads(json_str)
        
        # Validate required fields
        required_fields = ['portfolio_summary', 'transaction_analysis', 'insights']
        for field in required_fields:
            if field not in parsed_response:
                parsed_response[field] = f"Analysis for {field} not available"
        
        return parsed_response
        
    except json.JSONDecodeError as e:
        print(f"❌ JSON parsing error: {str(e)}")
        return create_fallback_response(ai_text)
    except Exception as e:
        print(f"❌ Response parsing error: {str(e)}")
        return create_fallback_response(ai_text)

def create_fallback_response(ai_text):
    """
    Create a fallback response when JSON parsing fails
    """
    return {
        "portfolio_summary": {
            "analysis_status": "Generated with fallback parser",
            "raw_analysis": ai_text[:500] + "..." if len(ai_text) > 500 else ai_text
        },
        "transaction_analysis": [
            {
                "category": "General Analysis",
                "description": "AI analysis completed but response format needs adjustment"
            }
        ],
        "insights": {
            "note": "Full analysis available in portfolio summary",
            "recommendation": "Try running the analysis again for improved formatting"
        }
    }

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    print("🚀 Starting FolioFlow AI Backend...")
    print("📋 Configuration:")
    print(f"   - Azure OpenAI API Key: {'✅ Configured' if azure_openai_configured else '❌ Not configured'}")
    print(f"   - Azure OpenAI Endpoint: {AZURE_OPENAI_ENDPOINT if azure_openai_configured else '❌ Not configured'}")
    print(f"   - Azure OpenAI Deployment: {AZURE_OPENAI_DEPLOYMENT_NAME if azure_openai_configured else '❌ Not configured'}")
    print(f"   - AI Service: {'✅ Azure OpenAI Ready' if azure_openai_configured else '❌ Not configured'}")
    print("\n🌐 Server starting on http://localhost:5000")
    print("📡 Ready to receive transaction analysis requests at /analyze")
    print("\n⚠️  Remember to:")
    print("   1. Get an API key from Azure OpenAI service")
    print("   2. Replace YOUR_AZURE_OPENAI_API_KEY_HERE with your Azure OpenAI API key")
    print("   3. Replace YOUR_AZURE_OPENAI_ENDPOINT_HERE with your Azure OpenAI endpoint")
    print("   4. Replace YOUR_DEPLOYMENT_NAME_HERE with your deployment name")
    print("   5. Install required dependencies: pip install flask flask-cors requests")
    print("   6. Configure CORS settings for production deployment")
    
    # Run the Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)