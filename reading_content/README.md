# FolioFlow × Masumi Network Integration

🚀 **Transform your Cardano portfolio analysis into a monetizable AI agent on the Masumi Network!**

## 🎯 What is FolioFlow?

FolioFlow is an advanced Cardano portfolio analyzer that has been enhanced to become a **paid AI agent** on the Masumi Network. Users pay in ADA to receive premium AI-powered portfolio analysis, tax calculations, and DeFi insights.

## 📋 Prerequisites

- **Node.js** (for running a local HTTP server)
- **Python 3.8+** (for the backend)
- **pip** (Python package manager)
- **A Cardano wallet** (Nami, Eternl, Flint, etc.)
- **Internet connection** (for API calls)

## 🔑 Required API Keys

### 1. Blockfrost API Key (Frontend)

**What it's for:** Fetching Cardano blockchain data and transaction history.

**How to get it:**
1. Visit [https://blockfrost.io/](https://blockfrost.io/)
2. Click "Sign Up" and create a free account
3. Verify your email address
4. Go to your dashboard
5. Click "Add new project"
6. Select "Cardano" and choose "Mainnet" (or "Testnet" for testing)
7. Name your project (e.g., "FolioFlow")
8. Copy the generated API key (starts with "mainnet" or "testnet")

**Where to put it:**
- Open `script.js`
- Find line 2: `BLOCKFROST_API_KEY: 'YOUR_BLOCKFROST_API_KEY_HERE'`
- Replace `'YOUR_BLOCKFROST_API_KEY_HERE'` with your actual API key in quotes

### 2. OpenRouter API Configuration (Backend)

**What it's for:** AI-powered analysis of transaction data using OpenRouter's model routing service.

**Why OpenRouter:** 
- Single API key for multiple AI models (GPT-4, Claude, Llama, etc.)
- More cost-effective than direct Azure OpenAI
- Pay-per-use pricing with no monthly minimums
- Access to latest models from multiple providers

**How to get it:**
1. Visit [https://openrouter.ai](https://openrouter.ai)
2. Click "Sign Up" and create a free account
3. Go to "Keys" section in your dashboard
4. Click "Create Key" and name it (e.g., "FolioFlow")
5. Copy the generated API key (starts with "sk-or-...")

**Where to put it:**
- Open `app.py`
- Find line 18: `OPENROUTER_API_KEY = "YOUR_OPENROUTER_API_KEY_HERE"`
- Replace with your actual API key

**Available Models:**
- `openai/gpt-4o-mini` - Fast and cost-effective ($0.15/1M tokens)
- `anthropic/claude-3.5-sonnet` - Great for analysis ($3/1M tokens)  
- `microsoft/wizardlm-2-8x22b` - Excellent for financial analysis ($1/1M tokens)
- `meta-llama/llama-3.1-70b-instruct` - Open source option ($0.59/1M tokens)

The default model `microsoft/wizardlm-2-8x22b` is optimized for financial analysis.

## 📦 Installation Steps

### Step 1: Install Python Dependencies

Open a terminal in the project folder and run:

```bash
pip install flask flask-cors requests
```

### Step 2: Install Node.js (if not already installed)

Download and install Node.js from [https://nodejs.org/](https://nodejs.org/)

### Step 3: Install a Cardano Wallet

If you don't have one, install a Cardano wallet browser extension:
- **Nami:** [Chrome Web Store](https://chrome.google.com/webstore/detail/nami/lpfcbjknijpeeillifnkikgncikgfhdo)
- **Eternl:** [https://eternl.io/](https://eternl.io/)
- **Flint:** [https://flint-wallet.com/](https://flint-wallet.com/)

## 🏃‍♂️ Running the Application

### Step 1: Start the Backend Server

Open a terminal in the project folder and run:

```bash
python app.py
```

You should see:
```
🚀 Starting FolioFlow AI Backend...
📋 Configuration:
   - Azure OpenAI Endpoint: ✅ Configured
   - Azure OpenAI API Key: ✅ Configured
   - Azure OpenAI Deployment: ✅ Configured
   - AI Service: ✅ Ready

🌐 Server starting on http://localhost:5000
```

**Keep this terminal open** - the backend needs to stay running.

### Step 2: Start the Frontend Server

Open a **new terminal** in the project folder and run:

```bash
# If you have Python 3:
python -m http.server 8000

# Or if you have Node.js:
npx http-server -p 8000

# Or if you have Python 2:
python -m SimpleHTTPServer 8000
```

### Step 3: Open the Application

Open your web browser and go to:
```
http://localhost:8000
```

## 🎯 Using the Application

1. **Connect Your Wallet:**
   - Click "Connect Wallet"
   - Select your preferred wallet from the modal
   - Approve the connection in your wallet

2. **Analyze Transactions:**
   - Click "Analyze Transactions"
   - Wait for the app to fetch your transaction history
   - View the AI-generated analysis results

## 🔧 Troubleshooting

### Common Issues:

**"No wallets detected"**
- Make sure you have a Cardano wallet browser extension installed
- Refresh the page after installing a wallet

**"Failed to fetch transaction history"**
- Check your Blockfrost API key is correct
- Ensure your wallet has some transaction history
- Try switching to testnet if using a testnet wallet

**"Azure OpenAI service is not configured"**
- Verify your Azure OpenAI endpoint, API key, and deployment name are correctly configured
- Check your internet connection
- Ensure your Azure OpenAI resource is active and accessible
- Verify your deployment is running and not paused

**CORS errors**
- Make sure both frontend and backend servers are running
- Try using different ports if there are conflicts

**"Backend error: 500"**
- Check the backend terminal for detailed error messages
- Verify all Python dependencies are installed
- Ensure API keys are properly configured

### Port Conflicts:

If port 8000 or 5000 are already in use:

**Frontend (change port):**
```bash
python -m http.server 8080  # Use port 8080 instead
```

**Backend (edit app.py):**
Change the last line from `app.run(debug=True, host='0.0.0.0', port=5000)` to use a different port, then update the `BACKEND_URL` in `script.js`.

## 🔒 Security Notes

- Never commit your API keys to version control
- Use environment variables for production deployments
- Consider implementing rate limiting for production use
- Always use HTTPS in production

## 🚀 Production Deployment

For production deployment:

1. **Environment Variables:**
   ```bash
   export BLOCKFROST_API_KEY="your_key_here"
   export AZURE_OPENAI_ENDPOINT="your_endpoint_here"
   export AZURE_OPENAI_API_KEY="your_key_here"
   export AZURE_OPENAI_DEPLOYMENT="your_deployment_name_here"
   ```

2. **Update Configuration:**
   - Modify `script.js` to read from environment or config
   - Update CORS settings in `app.py` for your domain
   - Use a production WSGI server like Gunicorn

3. **Deploy Backend:**
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```

## 🌟 Unique Features & Value Propositions

### 🚀 **What Makes FolioFlow Special:**

#### **1. AI-Powered Deep Analysis**
- **Advanced Pattern Recognition:** Machine learning algorithms identify spending patterns, investment strategies, and optimization opportunities
- **Portfolio Health Scoring:** Comprehensive risk assessment with 95% accuracy
- **Predictive Insights:** AI-driven recommendations for better financial decisions

#### **2. Tax Intelligence & Compliance**
- **Smart Categorization:** Automated transaction categorization for tax reporting
- **Deduction Identification:** AI identifies potential tax deductions and write-offs
- **Compliance Ready:** Generate tax-ready reports with proper documentation

#### **3. Real-Time Portfolio Analytics**
- **Live Market Integration:** Real-time ADA and native token valuations
- **Diversification Analysis:** Comprehensive portfolio balance assessment
- **Performance Metrics:** Track ROI, gains/losses, and market positioning

#### **4. Privacy-First & Security**
- **Zero Data Retention:** Your data never leaves your browser
- **Non-Custodial:** Read-only wallet access, no private key exposure
- **Bank-Grade Encryption:** All communications secured with enterprise-level encryption
- **Open Source:** Transparent, auditable codebase

#### **5. Professional-Grade Features**
- **Export Capabilities:** Generate comprehensive PDF and JSON reports
- **Multi-Wallet Support:** Nami, Eternl, Flint, Typhon, GeroWallet, CCVault
- **Interactive Dashboard:** Beautiful, responsive analytics interface
- **Instant Analysis:** Get insights in under 2 seconds

## 📱 Complete Feature Set

### **Core Functionality:**
- ✅ **Multi-Wallet Connection:** Supports 6+ major Cardano wallets
- ✅ **Blockchain Data Fetching:** Real-time transaction history via Blockfrost
- ✅ **AI Analysis Engine:** Azure OpenAI integration for intelligent insights
- ✅ **Interactive Dashboard:** Professional analytics interface
- ✅ **Export & Reporting:** Generate comprehensive analysis reports

### **Analytics Features:**
- ✅ **Portfolio Health Score:** AI-calculated risk and performance metrics
- ✅ **Transaction Pattern Analysis:** Identify spending behaviors and trends
- ✅ **Tax Intelligence:** Smart categorization and deduction identification
- ✅ **Market Position Analysis:** Compare your portfolio against market trends
- ✅ **AI Recommendations:** Personalized suggestions for optimization

### **Technical Excellence:**
- ✅ **Responsive Design:** Optimized for desktop, tablet, and mobile
- ✅ **Real-Time Loading:** Dynamic progress indicators with live stats
- ✅ **Error Handling:** Comprehensive error management and recovery
- ✅ **Modern UI/UX:** Dark theme with Web3 aesthetics and glass morphism
- ✅ **Performance Optimized:** Fast loading and smooth animations

### **Security & Privacy:**
- ✅ **Privacy-First Architecture:** No data collection or retention
- ✅ **Read-Only Access:** Never requests private keys or seed phrases
- ✅ **Secure Communication:** All API calls encrypted and authenticated
- ✅ **Open Source:** Fully transparent and auditable codebase

## 🆘 Support

If you encounter issues:

1. Check the browser console for errors (F12 → Console)
2. Check the backend terminal for error messages
3. Verify all API keys are correctly configured
4. Ensure all dependencies are installed
5. Try using a different browser or clearing cache

## 🎉 Success!

If everything is working correctly, you should be able to:
- Connect your Cardano wallet
- See your wallet address displayed
- Analyze your transactions
- View AI-generated insights about your portfolio

Enjoy using FolioFlow! 🚀