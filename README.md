# 🚀 FolioFlow - AI-Powered Cardano Portfolio Analyzer

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Cardano](https://img.shields.io/badge/Cardano-Portfolio%20Analysis-blue)](https://cardano.org/)

> **The most advanced AI-powered portfolio analysis tool for Cardano wallets**

## ✨ Key Features

### 🧠 **AI-Powered Analysis**
- **Azure OpenAI Integration** - GPT-powered transaction analysis
- **Smart Pattern Recognition** - Identifies spending habits and investment strategies
- **Portfolio Health Scoring** - Real-time risk assessment with visual indicators
- **Tax Intelligence** - Automated tax event detection and optimization suggestions

### 🔗 **Wallet Integration**
- **CIP-30 Compatible** - Works with Lace, Eternl, Nami, and other Cardano wallets
- **Real-time Data** - Live blockchain integration via Blockfrost API
- **Secure Connection** - No private keys stored, zero data retention
- **Multi-Network Support** - Mainnet, Preview, and Preprod testnets

### 🎨 **Modern Interface**
- **Interactive Dashboard** - Beautiful cards with expandable content
- **Read More/Less** - Smart text truncation for better readability
- **Responsive Design** - Perfect on desktop and mobile
- **Smooth Animations** - Professional transitions and visual feedback

## 🚀 Quick Start

### 1. **Clone & Setup**
```bash
git clone https://github.com/Hassanahmed786/folioflow-cardano-analyzer.git
cd folioflow-cardano-analyzer
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### 2. **Configure API Keys**
```bash
# Copy template and add your keys
copy config\masumi_config_template.py config\masumi_config.py
# Edit config/masumi_config.py with your actual API keys
```

### 3. **Run the Application**
```bash
# Terminal 1: Start Backend
python backend/app.py

# Terminal 2: Start Frontend  
cd frontend
python -m http.server 8000
```

### 4. **Access the App**
Open `http://localhost:8000` in your browser

## 🔧 Required Configuration

### **Azure OpenAI** (Primary AI Engine)
```python
AZURE_OPENAI_API_KEY = "your_api_key_here"
AZURE_OPENAI_ENDPOINT = "your_endpoint_here" 
AZURE_OPENAI_DEPLOYMENT_NAME = "your_deployment_name"
```

### **Blockfrost API** (Cardano Data)
```python
BLOCKFROST_PROJECT_ID = "your_blockfrost_project_id"
```
Get your free API key at: https://blockfrost.io

## 🎯 How It Works

1. **Connect Wallet** - Use any CIP-30 compatible Cardano wallet
2. **Fetch Transactions** - Real-time data from Cardano blockchain
3. **AI Analysis** - Azure OpenAI processes transaction patterns
4. **Get Insights** - Comprehensive portfolio analysis with recommendations

## 📊 Analysis Features

### **Portfolio Health Score**
- Risk assessment with visual indicators
- Diversification analysis
- Transaction frequency patterns

### **Transaction Categorization**
- Automatic classification (spending, trading, staking)
- Fee analysis and optimization
- Pattern recognition for investment strategies

### **Tax Intelligence**
- Taxable event identification
- Potential deduction suggestions
- Compliance-ready categorization

### **AI Insights**
- Spending pattern analysis
- Investment recommendations
- Risk assessment warnings
- Portfolio optimization tips

## 🏗️ Project Structure

```
folioflow-cardano-analyzer/
├── backend/                 # Flask API Server
│   ├── app.py              # Main application with Azure OpenAI
│   └── masumi_agent.py     # AI agent integration
├── frontend/               # Web Interface
│   ├── index.html          # Main UI with modern design
│   ├── script.js           # Wallet integration & API calls
│   ├── style.css           # Professional styling
│   └── masumi-integration.js # Payment integration
├── config/                 # Configuration
│   ├── masumi_config_template.py # Template (copy this)
│   └── masumi_config.py    # Your actual config (gitignored)
├── scripts/                # Deployment utilities
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## 🔒 Security Features

- ✅ **No Private Key Storage** - Uses CIP-30 standard
- ✅ **API Key Protection** - Configuration files gitignored  
- ✅ **CORS Enabled** - Secure cross-origin requests
- ✅ **Rate Limiting** - Prevents API abuse

## 🌐 Supported Networks

- **Cardano Mainnet** ✅
- **Cardano Preview Testnet** ✅  
- **Cardano Preprod Testnet** ✅

## 🚀 Deployment

### **Environment Variables**
```bash
AZURE_OPENAI_API_KEY=your_key
BLOCKFROST_PROJECT_ID=your_project_id
FLASK_ENV=production
```

### **Deployment Platforms**
- **Heroku** - Use included Procfile
- **Railway** - Auto-deploy from GitHub
- **Render** - Connect repository
- **GitHub Pages** - Frontend only

## 📞 Support & Contributing

- **Issues**: [GitHub Issues](https://github.com/Hassanahmed786/folioflow-cardano-analyzer/issues)
- **Discussions**: [GitHub Discussions](https://github.com/Hassanahmed786/folioflow-cardano-analyzer/discussions)

## 📝 License

MIT License - see [LICENSE](LICENSE) file for details.

---

**Built with ❤️ for the Cardano community**

*Transform your Cardano portfolio analysis with the power of AI*
