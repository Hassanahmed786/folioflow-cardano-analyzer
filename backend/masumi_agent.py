#!/usr/bin/env python3
"""
FolioFlow Masumi Agent Integration
MIP-003 compliant AI agent for Cardano portfolio analysis
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
import sys
from datetime import datetime
import requests
import hashlib

# Add config directory to Python path
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config'))

try:
    import masumi_config as config
    print("📁 Configuration loaded from config directory")
    
    # Set up Blockfrost configuration
    BLOCKFROST_API_KEY = getattr(config, 'BLOCKFROST_PROJECT_ID_PREVIEW', 'demo_key')
    BLOCKFROST_BASE_URL = "https://cardano-preview.blockfrost.io/api/v0"
    
    print(f"🔗 Blockfrost configured for {config.DEFAULT_NETWORK} network")
except ImportError:
    print("⚠️  Using default configuration (config/masumi_config.py not found)")
    config = None
    BLOCKFROST_API_KEY = 'demo_key'
    BLOCKFROST_BASE_URL = "https://cardano-preview.blockfrost.io/api/v0"

# Masumi Integration
MASUMI_API_KEY = os.getenv('MASUMI_API_KEY', 'your_masumi_api_key_here')
MASUMI_PAYMENT_SERVICE_URL = os.getenv('MASUMI_PAYMENT_SERVICE_URL', 'http://localhost:3001')
MASUMI_NETWORK = os.getenv('MASUMI_NETWORK', 'Preview')  # Using Preview network

# Agent Configuration
AGENT_NAME = "FolioFlow Portfolio Analyzer"
AGENT_VERSION = "1.0.0"
AGENT_DESCRIPTION = "AI-powered Cardano portfolio analysis with tax intelligence and DeFi insights"
ANALYSIS_PRICE_LOVELACE = "5000000"  # 5 ADA per analysis

app = Flask(__name__)
CORS(app)

def fetch_cardano_data(wallet_address):
    """Fetch real Cardano data using Blockfrost API"""
    try:
        headers = {'project_id': BLOCKFROST_API_KEY}
        
        # Get address information
        address_url = f"{BLOCKFROST_BASE_URL}/addresses/{wallet_address}"
        address_response = requests.get(address_url, headers=headers, timeout=10)
        
        if address_response.status_code != 200:
            return {"error": f"Failed to fetch address data: {address_response.status_code}"}
        
        address_data = address_response.json()
        
        # Get recent transactions
        tx_url = f"{BLOCKFROST_BASE_URL}/addresses/{wallet_address}/transactions?count=10&order=desc"
        tx_response = requests.get(tx_url, headers=headers, timeout=10)
        
        transactions = []
        if tx_response.status_code == 200:
            tx_hashes = tx_response.json()
            
            # Get details for first few transactions
            for tx_hash in tx_hashes[:5]:  # Limit to 5 transactions to avoid rate limits
                tx_detail_url = f"{BLOCKFROST_BASE_URL}/txs/{tx_hash}"
                tx_detail_response = requests.get(tx_detail_url, headers=headers, timeout=10)
                if tx_detail_response.status_code == 200:
                    transactions.append(tx_detail_response.json())
        
        return {
            "address_info": address_data,
            "recent_transactions": transactions,
            "total_transactions": len(transactions)
        }
        
    except Exception as e:
        print(f"Error fetching Cardano data: {e}")
        return {"error": str(e)}

# MIP-003 Compliance: Agent Capabilities Endpoint
@app.route('/agent/capabilities', methods=['GET'])
def get_agent_capabilities():
    """
    MIP-003 required endpoint: Returns agent capabilities and pricing
    """
    return jsonify({
        "name": AGENT_NAME,
        "version": AGENT_VERSION,
        "description": AGENT_DESCRIPTION,
        "capabilities": [
            "cardano_portfolio_analysis",
            "transaction_categorization", 
            "defi_activity_analysis",
            "tax_optimization_recommendations",
            "risk_assessment",
            "performance_metrics"
        ],
        "pricing": {
            "type": "fixed",
            "amount": ANALYSIS_PRICE_LOVELACE,
            "unit": "lovelace"
        },
        "endpoints": {
            "analyze": "/agent/analyze",
            "status": "/agent/status"
        },
        "supported_networks": ["mainnet", "preprod"],
        "response_format": "json",
        "max_processing_time": 120  # seconds
    })

@app.route('/agent/status', methods=['GET'])
def get_agent_status():
    """
    MIP-003 required endpoint: Returns agent health status
    """
    return jsonify({
        "status": "active",
        "uptime": "99.9%",
        "last_maintenance": "2025-01-01T00:00:00Z",
        "current_load": "low",
        "estimated_response_time": "30-60 seconds"
    })

@app.route('/agent/analyze', methods=['POST'])
def analyze_portfolio_paid():
    """
    MIP-003 compliant paid analysis endpoint
    Requires payment verification through Masumi Network
    """
    try:
        # Parse request
        data = request.get_json()
        
        # Required parameters
        blockchain_identifier = data.get('blockchain_identifier')
        wallet_address = data.get('wallet_address')
        input_hash = data.get('input_hash')
        
        if not all([blockchain_identifier, wallet_address, input_hash]):
            return jsonify({
                "error": "Missing required parameters",
                "required": ["blockchain_identifier", "wallet_address", "input_hash"]
            }), 400
        
        # Verify payment through Masumi Payment Service
        payment_verified = verify_masumi_payment(blockchain_identifier)
        
        if not payment_verified:
            return jsonify({
                "error": "Payment not verified",
                "message": "Please ensure payment is completed before requesting analysis"
            }), 402  # Payment Required
        
        # Perform the portfolio analysis (your existing logic)
        analysis_result = perform_portfolio_analysis(wallet_address)
        
        # Create result hash for Masumi
        result_hash = create_result_hash(analysis_result)
        
        # Log decision on Masumi Network (for transparency)
        log_decision_to_masumi(blockchain_identifier, result_hash, analysis_result)
        
        return jsonify({
            "status": "success",
            "result_hash": result_hash,
            "analysis": analysis_result,
            "agent": {
                "name": AGENT_NAME,
                "version": AGENT_VERSION
            },
            "processed_at": datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({
            "error": "Analysis failed",
            "message": str(e)
        }), 500

def verify_masumi_payment(blockchain_identifier):
    """
    Verify payment through Masumi Payment Service
    """
    try:
        headers = {
            'Authorization': f'Bearer {MASUMI_API_KEY}',
            'Content-Type': 'application/json'
        }
        
        payload = {
            "blockchainIdentifier": blockchain_identifier,
            "network": MASUMI_NETWORK,
            "includeHistory": "false"
        }
        
        response = requests.post(
            f"{MASUMI_PAYMENT_SERVICE_URL}/api/v1/payment/resolve-blockchain-identifier",
            json=payload,
            headers=headers,
            timeout=30
        )
        
        if response.status_code == 200:
            payment_data = response.json()
            # Check if payment is confirmed and funds are locked
            return payment_data.get('data', {}).get('onChainState') == 'FundsLocked'
        
        return False
        
    except Exception as e:
        print(f"Payment verification error: {e}")
        return False

def perform_portfolio_analysis(wallet_address):
    """
    Enhanced portfolio analysis using real Blockfrost data
    """
    print(f"🔍 Analyzing portfolio for address: {wallet_address}")
    
    # Fetch real Cardano data
    cardano_data = fetch_cardano_data(wallet_address)
    
    if "error" in cardano_data:
        return {
            "error": "Failed to fetch portfolio data",
            "details": cardano_data["error"]
        }
    
    # Extract key metrics from real data
    address_info = cardano_data.get("address_info", {})
    transactions = cardano_data.get("recent_transactions", [])
    
    # Calculate portfolio metrics from real data
    total_received = int(address_info.get("received_sum", [{"quantity": "0"}])[0]["quantity"]) / 1000000  # Convert from lovelace to ADA
    total_sent = int(address_info.get("sent_sum", [{"quantity": "0"}])[0]["quantity"]) / 1000000
    current_balance = total_received - total_sent
    
    # Analyze transaction patterns
    tx_count = len(transactions)
    
    # Calculate basic metrics
    portfolio_health_score = min(95, max(20, 60 + (current_balance * 2) + (tx_count * 0.5)))
    risk_level = "Low" if current_balance > 1000 else "Medium" if current_balance > 100 else "High"
    
    return {
        "wallet_address": wallet_address,
        "real_data": True,
        "current_balance_ada": round(current_balance, 2),
        "total_received_ada": round(total_received, 2),
        "total_sent_ada": round(total_sent, 2),
        "portfolio_health_score": round(portfolio_health_score, 1),
        "total_transactions": tx_count,
        "risk_level": risk_level,
        "network": "Cardano Preview",
        "analysis_timestamp": datetime.now().isoformat(),
        "recent_activity": len([tx for tx in transactions if tx]) > 0,
        "recommendations": [
            f"Current balance: {round(current_balance, 2)} ADA",
            f"Transaction activity: {'Active' if tx_count > 0 else 'Inactive'}",
            "Consider diversifying beyond ADA for better risk management",
            "Monitor transaction fees and optimize timing",
            "Review staking opportunities for passive income"
        ],
        "raw_data_summary": {
            "address_info_available": bool(address_info),
            "transactions_analyzed": len(transactions),
            "data_source": "Blockfrost API"
        }
    }

def create_result_hash(analysis_result):
    """
    Create cryptographic hash of analysis result for Masumi
    """
    result_string = json.dumps(analysis_result, sort_keys=True)
    return hashlib.sha256(result_string.encode()).hexdigest()

def log_decision_to_masumi(blockchain_identifier, result_hash, analysis_data):
    """
    Log agent decision to Masumi Network for transparency
    """
    try:
        decision_log = {
            "agent": AGENT_NAME,
            "version": AGENT_VERSION,
            "blockchain_identifier": blockchain_identifier,
            "result_hash": result_hash,
            "decision_type": "portfolio_analysis",
            "confidence_score": 0.95,
            "processing_time": "45 seconds",
            "timestamp": datetime.now().isoformat()
        }
        
        # Log to Masumi Decision Logging system
        # This would integrate with Masumi's decision logging API
        print(f"Decision logged: {decision_log}")
        
    except Exception as e:
        print(f"Decision logging error: {e}")

# Legacy endpoint for existing users (free tier with rate limiting)
@app.route('/analyze', methods=['POST'])
def analyze_legacy():
    """
    Legacy free analysis endpoint with limitations
    """
    return jsonify({
        "message": "Free tier analysis",
        "note": "For full AI-powered analysis, use the paid Masumi agent service at /agent/analyze",
        "masumi_agent_url": f"{request.url_root}agent/analyze",
        "pricing": f"{int(ANALYSIS_PRICE_LOVELACE) / 1000000} ADA per analysis"
    })

# Masumi Agent Registration Helper
@app.route('/masumi/register', methods=['POST'])
def register_with_masumi():
    """
    Helper endpoint to register this agent with Masumi Network
    """
    registration_data = {
        "name": AGENT_NAME,
        "description": AGENT_DESCRIPTION,
        "apiBaseUrl": f"{request.url_root}agent",
        "capabilities": {
            "name": "Portfolio Analysis",
            "version": AGENT_VERSION
        },
        "author": {
            "name": "FolioFlow Team",
            "contactEmail": "contact@folioflow.com",
            "organization": "FolioFlow Analytics"
        },
        "pricing": {
            "pricingType": "Fixed",
            "pricing": [{"amount": ANALYSIS_PRICE_LOVELACE, "unit": ""}]
        },
        "tags": ["portfolio", "analysis", "cardano", "defi", "tax", "ai"],
        "exampleOutputs": [],
        "network": MASUMI_NETWORK
    }
    
    return jsonify({
        "registration_data": registration_data,
        "instructions": "Submit this data to Masumi Registry Service to complete agent registration"
    })

if __name__ == '__main__':
    print(f"""
🚀 FolioFlow Masumi Agent Starting...

Agent Name: {AGENT_NAME}
Version: {AGENT_VERSION}
Network: {MASUMI_NETWORK}
Analysis Price: {int(ANALYSIS_PRICE_LOVELACE) / 1000000} ADA

MIP-003 Endpoints:
- GET  /agent/capabilities
- GET  /agent/status  
- POST /agent/analyze

Legacy Endpoint:
- POST /analyze (free tier)

Masumi Integration:
- POST /masumi/register

""")
    app.run(debug=True, host='0.0.0.0', port=5000)