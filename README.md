# 🚀 FolioFlow - Advanced Cardano Portfolio Analyzer

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Cardano](https://img.shields.io/badge/Cardano-Portfolio%20Analysis-blue)](https://cardano.org/)

> **AI-powered portfolio analysis for Cardano wallets with advanced insights, tax intelligence, and DeFi analytics**

## ✨ **What is FolioFlow?**

FolioFlow is the first AI-powered Cardano portfolio analyzer that provides:
- **🧠 AI-Driven Insights** - Advanced pattern recognition powered by Azure OpenAI
- **📊 Real-Time Analysis** - Live blockchain data via Blockfrost API
- **💼 Tax Intelligence** - Smart categorization for tax reporting
- **🔍 Risk Assessment** - Portfolio health scoring and recommendations
- **💰 Monetizable** - Masumi Network integration for revenue generation

## 🚀 **Quick Start**

### **Prerequisites**
- Python 3.8+
- Azure OpenAI API access
- Blockfrost API key
- Cardano wallet (Lace, Eternl, Nami)

### **Installation**
```bash
git clone https://github.com/Hassanahmed786/folioflow-cardano-analyzer.git
cd folioflow-cardano-analyzer
pip install -r requirements.txt
```

### **Configuration**
```bash
# Copy template and add your API keys
cp config/masumi_config_template.py config/masumi_config.py
# Edit config/masumi_config.py with your actual keys
```

### **Run the Application**
```bash
# Terminal 1: Backend
python backend/app.py

# Terminal 2: Frontend  
cd frontend
python -m http.server 8000
```

### **Access the App**
Open `http://localhost:8000` in your browser

## 🎯 **Features**

### **🔬 AI Analysis Engine**
- Real-time transaction pattern recognition
- Spending behavior analysis
- Investment strategy identification
- Risk assessment and scoring

### **💼 Tax Intelligence**
- Automatic transaction categorization
- Tax event identification
- Compliance reporting
- Deduction optimization

### **🎨 Professional UI**
- Interactive dashboard with animated cards
- Read more/less functionality for better UX
- Responsive design for all devices
- Professional styling and smooth animations

### **🔒 Security First**
- CIP-30 wallet standard compliance
- No private key storage
- Client-side wallet interactions
- Secure API key management

## 💰 **Masumi Network Integration**

FolioFlow is designed to be monetized through the Masumi Network:

- **Pay-per-Analysis**: Users pay 5 ADA for comprehensive analysis
- **Agent Economy**: Other AI agents can purchase portfolio insights
- **Subscription Model**: Monthly monitoring and alerts
- **B2B Services**: White-label solutions for institutions

## 📁 **Project Structure**

```
folioflow-cardano-analyzer/
├── 🎨 frontend/              # Web interface
├── 🤖 backend/               # Flask API server
├── ⚙️ config/                # Configuration management
├── 🛠️ scripts/              # Deployment scripts
├── 📚 reading_content/       # 📖 All documentation & guides
└── 📄 Core project files
```

## 📚 **Documentation**

All documentation is organized in the **[reading_content/](reading_content/)** folder:

### **📋 Quick Links:**
- **[Setup Guide](reading_content/SETUP_REQUIREMENTS.md)** - Installation and configuration
- **[Demo Guide](reading_content/LOCAL_DEMO_CHECKLIST.md)** - Hackathon presentation ready
- **[Masumi Integration](reading_content/MASUMI_INTEGRATION_COMPLETE_GUIDE.md)** - Monetization strategy
- **[GitHub Guide](reading_content/GITHUB_UPLOAD_GUIDE.md)** - Repository management
- **[Full Index](reading_content/INDEX.md)** - Complete documentation index

## 🏆 **Hackathon Ready**

FolioFlow is **presentation-ready** with:
- ✅ Working prototype with live demo
- ✅ Professional UI/UX design
- ✅ Real blockchain integration
- ✅ AI-powered analysis
- ✅ Clear business model
- ✅ Comprehensive documentation

**Demo Flow**: Connect wallet → Analyze portfolio → View AI insights → Show monetization potential

## 🛠️ **Technology Stack**

### **Backend**
- **Flask** - Python web framework
- **Azure OpenAI** - AI analysis engine
- **Blockfrost API** - Cardano blockchain data
- **CORS** - Cross-origin resource sharing

### **Frontend**
- **Vanilla JavaScript** - Modern ES6+
- **CIP-30** - Cardano wallet integration
- **Professional CSS** - Custom design system
- **Responsive Design** - Mobile-first approach

## 🤝 **Contributing**

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 **Contact & Support**

- **GitHub**: [Hassanahmed786](https://github.com/Hassanahmed786)
- **Repository**: [folioflow-cardano-analyzer](https://github.com/Hassanahmed786/folioflow-cardano-analyzer)
- **Issues**: [GitHub Issues](https://github.com/Hassanahmed786/folioflow-cardano-analyzer/issues)

---

**🎯 Built for the Cardano ecosystem with ❤️**

*Transforming portfolio analysis through AI and blockchain technology*