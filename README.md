# FolioFlow × Masumi Network Integration

🚀 **Advanced Cardano Portfolio Analyzer transformed into a monetizable AI agent on the Masumi Network**

## 📁 Project Structure

```
folioflow-masumi/
├── 🌐 frontend/                 # Frontend Application
│   ├── index.html              # Main application interface
│   ├── style.css               # Professional styling
│   ├── script.js               # Wallet integration (CIP-30)
│   └── masumi-integration.js   # Masumi payment handling
│
├── 🤖 backend/                  # Backend Services
│   ├── masumi_agent.py         # MIP-003 compliant AI agent
│   └── app.py                  # Legacy backend (free tier)
│
├── ⚙️ config/                   # Configuration Files
│   ├── masumi_config.py        # Active configuration
│   ├── masumi_config_template.py # Configuration template
│   └── .env                    # Environment variables
│
├── 📜 scripts/                  # Deployment & Automation
│   ├── deploy_masumi.py        # Deployment automation
│   └── start_folioflow.bat     # Launch script
│
├── 📚 docs/                     # Documentation
│   ├── README.md               # Complete setup guide
│   ├── MASUMI_INTEGRATION_PLAN.md # Integration strategy
│   └── DEPLOYMENT_SUCCESS.md    # Deployment summary
│
└── 🔧 Development Files
    ├── .venv/                  # Python virtual environment
    ├── __pycache__/           # Python cache files
    └── test.html              # Test files
```

## 🚀 Quick Start

### 1. **Start the Application**
```bash
# Navigate to project root
cd "e:\MY CERTIFICATES\Masumi Hackathon"

# Run the startup script
.\scripts\start_folioflow.bat
```

### 2. **Access Your App**
- 🌐 **Frontend:** http://localhost:8000
- 🤖 **Agent API:** http://localhost:5000/agent/capabilities
- 📊 **Health Check:** http://localhost:5000/health

## 💰 **Revenue Model**

| Service Tier | Price | Features |
|-------------|-------|----------|
| **Basic** | 2 ADA | Portfolio overview, transaction categorization |
| **Premium** | 5 ADA | AI insights, tax calculations, DeFi analysis |
| **Tax Report** | 10 ADA | Comprehensive tax documentation |

## 🔧 **Configuration**

Update API keys in `config/masumi_config.py`:
- Masumi Network API key
- OpenRouter API key  
- Blockfrost API key

## 📖 **Documentation**

- **Setup Guide:** [docs/README.md](docs/README.md)
- **Integration Plan:** [docs/MASUMI_INTEGRATION_PLAN.md](docs/MASUMI_INTEGRATION_PLAN.md)
- **Deployment Status:** [docs/DEPLOYMENT_SUCCESS.md](docs/DEPLOYMENT_SUCCESS.md)

## 🎯 **Key Features**

- ✅ **Multi-wallet support** (Lace, Nami, Eternl, Flint, Typhon, GeroWallet, CCVault)
- ✅ **AI-powered analysis** via OpenRouter
- ✅ **Monetized services** through Masumi Network
- ✅ **MIP-003 compliance** for agent standards
- ✅ **Payment verification** before service delivery
- ✅ **Professional UI** with payment modals

## 🛠️ **Architecture**

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Frontend      │    │   Masumi Agent   │    │  Masumi Network │
│   (port 8000)   │◄──►│   (port 5000)    │◄──►│   (Payments)    │
└─────────────────┘    └──────────────────┘    └─────────────────┘
        │                       │                       │
        │              ┌─────────────────┐              │
        │              │   OpenRouter    │              │
        └──────────────►│   (AI Models)   │◄─────────────┘
                       └─────────────────┘
```

## 🌟 **Status**

- ✅ **Development:** Complete
- ✅ **Integration:** Masumi Network ready
- ✅ **Testing:** Local deployment successful
- 🔄 **Production:** Ready for API key configuration

---

**🚀 Your Cardano dApp is now a monetizable AI agent on the Masumi Network!**

*Built with ❤️ for the Cardano ecosystem*