# 🌟 FolioFlow - AI-Powered Cardano Portfolio Analyzer

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Vercel](https://img.shields.io/badge/Deployed%20on-Vercel-black)](https://vercel.com)

> **Professional AI-powered portfolio analysis for Cardano wallets**

## 🚀 **Live Demo**
**[Try FolioFlow Live](https://folioflow-cardano-analyzer-2-7gmdozeyd.vercel.app/)** - Deployed on Vercel

---

## ✨ **Features**

- 🧠 **AI Analysis** - Azure OpenAI powered insights
- 💼 **Portfolio Overview** - Complete asset and transaction analysis
- 🔗 **Multi-Wallet Support** - Lace, Nami, Eternl, Flint, Typhon, GeroWallet, CCVault
- 📊 **Real-time Data** - Blockfrost API integration
- 📱 **Responsive Design** - Works on all devices
- 🔒 **Secure** - No private keys stored, read-only access

---

## 🏗️ **Project Structure**

```
folioflow-cardano-analyzer/
├── api/                    # Vercel Serverless Functions
│   ├── analyze.py         # Portfolio analysis endpoint  
│   └── index.py           # API health check
├── public/                # Static frontend files
│   ├── index.html         # Main application
│   ├── script.js          # Core functionality
│   ├── style.css          # Styling
│   └── masumi-integration.js # Wallet integration
├── config/                # Configuration
├── vercel.json           # Deployment config
└── README.md             # This file
```

---

## 🚀 **Deployment**

### **Option 1: One-Click Deploy**
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/Hassanahmed786/folioflow-cardano-analyzer)

### **Option 2: Local Development**
```bash
# Clone and setup
git clone https://github.com/Hassanahmed786/folioflow-cardano-analyzer.git
cd folioflow-cardano-analyzer
pip install -r requirements.txt

# Configure API keys (optional for demo)
cp config/masumi_config_template.py config/masumi_config.py

# Run locally  
python -m http.server 8000 --directory public
# Visit http://localhost:8000
```

---

## ⚙️ **Configuration**

### **Required for Full AI Analysis**
Add these environment variables in Vercel dashboard:

| Variable | Purpose |
|----------|---------|
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API key |
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI endpoint URL |
| `AZURE_OPENAI_API_VERSION` | API version (e.g. `2024-08-01-preview`) |
| `AZURE_OPENAI_DEPLOYMENT_NAME` | Deployment name |

**Note**: App works in demo mode without configuration.

---

## 📖 **How to Use**

1. **Visit the app** - Live demo or deploy your own
2. **Connect wallet** - Choose from supported Cardano wallets
3. **Analyze portfolio** - Click "Analyze Portfolio" button
4. **Review insights** - Get AI-powered recommendations

---

## 🛠️ **Technology**

- **Frontend**: Vanilla JavaScript, CSS3, HTML5
- **Backend**: Python serverless functions
- **AI**: Azure OpenAI (GPT models)
- **Blockchain**: Blockfrost API
- **Deployment**: Vercel platform
- **Wallets**: CIP-30 standard

---

## 🤝 **Contributing**

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

---

## 📄 **License**

MIT License - see [LICENSE](LICENSE) file for details.

---

## 🙏 **Acknowledgments**

- **Azure OpenAI** - AI analysis engine
- **Blockfrost** - Cardano blockchain API  
- **Vercel** - Deployment platform
- **Cardano Community** - Wallet standards

---

**Made with ❤️ for the Cardano Community**

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
