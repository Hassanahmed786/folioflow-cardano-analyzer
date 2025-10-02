# Masumi Network Configuration
# Copy this to masumi_config.py and update with your actual values

# API Configuration
MASUMI_API_KEY = "your_masumi_api_key_here"
MASUMI_PAYMENT_SERVICE_URL = "https://api.masumi.network"
OPENROUTER_API_KEY = "your_openrouter_api_key_here"

# Agent Configuration
AGENT_IDENTIFIER = "folioflow-portfolio-analyzer"
AGENT_NAME = "FolioFlow AI Portfolio Analyzer"
AGENT_VERSION = "1.0.0"
AGENT_DESCRIPTION = "Advanced Cardano portfolio analysis with tax intelligence and DeFi insights"

# Pricing Configuration (in lovelace)
BASIC_ANALYSIS_PRICE = 2000000      # 2 ADA
PREMIUM_ANALYSIS_PRICE = 5000000    # 5 ADA
TAX_REPORT_PRICE = 10000000         # 10 ADA

# Network Configuration
DEFAULT_NETWORK = "Preprod"  # Change to "Mainnet" for production
SMART_CONTRACT_ADDRESSES = {
    "Mainnet": "addr1wx7j4kmg2cs7yf92uat3ed4a3u97kr7axxr4avaz0lhwdsq87ujx7",
    "Preprod": "addr_test1wz7j4kmg2cs7yf92uat3ed4a3u97kr7axxr4avaz0lhwdsqukgwfm"
}

# AI Model Configuration
DEFAULT_AI_MODEL = "microsoft/wizardlm-2-8x22b"
BACKUP_AI_MODELS = [
    "meta-llama/llama-3.1-70b-instruct",
    "anthropic/claude-3.5-sonnet",
    "openai/gpt-4o"
]

# Blockfrost Configuration
BLOCKFROST_PROJECT_ID_MAINNET = "your_mainnet_project_id"
BLOCKFROST_PROJECT_ID_PREPROD = "your_preprod_project_id"

# Service URLs
FRONTEND_URL = "http://localhost:8000"
BACKEND_URL = "http://localhost:5000"
MASUMI_AGENT_URL = "http://localhost:5000/agent"

# Payment Configuration
PAYMENT_TIMEOUT_MINUTES = 60
RESULT_DELIVERY_TIMEOUT_MINUTES = 120
DISPUTE_RESOLUTION_TIMEOUT_HOURS = 24

# Features Configuration
FEATURES = {
    "basic_portfolio_analysis": True,
    "tax_calculations": True,
    "defi_insights": True,
    "nft_analysis": True,
    "staking_rewards_tracking": True,
    "yield_farming_analysis": True,
    "regulatory_compliance": True,
    "multi_wallet_support": True
}

# Registration Data for Masumi Network
AGENT_REGISTRATION_DATA = {
    "name": AGENT_NAME,
    "version": AGENT_VERSION,
    "description": AGENT_DESCRIPTION,
    "identifier": AGENT_IDENTIFIER,
    "capabilities": [
        "portfolio_analysis",
        "tax_calculation",
        "defi_insights",
        "transaction_categorization",
        "yield_tracking",
        "compliance_reporting"
    ],
    "pricing": {
        "basic_analysis": BASIC_ANALYSIS_PRICE,
        "premium_analysis": PREMIUM_ANALYSIS_PRICE,
        "tax_report": TAX_REPORT_PRICE
    },
    "supported_networks": ["Mainnet", "Preprod"],
    "response_time_sla": "< 30 seconds",
    "availability_sla": "99.9%"
}