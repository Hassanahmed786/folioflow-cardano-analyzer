# 🔑 FolioFlow API Keys & Endpoints Requirements

## 📋 **What You Need to Get Your App Running**

### 🚨 **Critical API Keys Required:**

#### 1. **OpenRouter API Key** (Essential for AI Analysis)
- **Purpose:** Powers the AI portfolio analysis engine
- **Where to get:** https://openrouter.ai/
- **Cost:** Pay-per-use (starts ~$0.01 per analysis)
- **Current Status:** `sk-or-v1-demo-key` (Demo - needs replacement)
- **Priority:** 🔴 **HIGH** - Required for premium analysis

```python
# In config/masumi_config.py
OPENROUTER_API_KEY = "sk-or-v1-YOUR_ACTUAL_KEY_HERE"
```

#### 2. **Blockfrost API Key** (Essential for Cardano Data)
- **Purpose:** Fetches Cardano blockchain data (transactions, addresses, etc.)
- **Where to get:** https://blockfrost.io/
- **Cost:** Free tier available (up to 10k requests/day)
- **Current Status:** `preprod_demo_key` (Demo - needs replacement)
- **Priority:** 🔴 **HIGH** - Required for portfolio analysis

```python
# In config/masumi_config.py
BLOCKFROST_PROJECT_ID_PREPROD = "preprodYOUR_PROJECT_ID_HERE"
BLOCKFROST_PROJECT_ID_MAINNET = "mainnetYOUR_PROJECT_ID_HERE"  # For production
```

#### 3. **Masumi Network API Key** (Optional for Testing)
- **Purpose:** Integrates with Masumi Network for payments
- **Where to get:** https://masumi.network/ (when available)
- **Cost:** TBD (Network integration fees)
- **Current Status:** `demo_masumi_key_for_testing` (Demo)
- **Priority:** 🟡 **MEDIUM** - Can run without for testing

```python
# In config/masumi_config.py
MASUMI_API_KEY = "your_actual_masumi_api_key_here"
```

---

## 🛠️ **API Endpoints & Services**

### 🤖 **Your App's Endpoints (After Starting):**

#### **Frontend Application:**
- **URL:** http://localhost:8000
- **Purpose:** Main user interface
- **Status:** ✅ Ready to run
- **Files:** `frontend/index.html`, `frontend/style.css`, `frontend/script.js`

#### **AI Agent API:**
- **Base URL:** http://localhost:5000
- **Endpoints:**
  - `GET /agent/capabilities` - Agent info and pricing
  - `GET /agent/status` - Health check
  - `POST /agent/analyze` - Premium AI analysis (requires payment)
  - `POST /analyze` - Free basic analysis
  - `GET /health` - Service health check

### 🌐 **External API Endpoints Used:**

#### **OpenRouter API:**
- **Base URL:** https://openrouter.ai/api/v1/
- **Endpoints Used:**
  - `POST /chat/completions` - AI analysis requests
  - `GET /models` - Available AI models
- **Models Available:**
  - `microsoft/wizardlm-2-8x22b` (Default)
  - `meta-llama/llama-3.1-70b-instruct`
  - `anthropic/claude-3.5-sonnet`
  - `openai/gpt-4o`

#### **Blockfrost API:**
- **Base URL:** https://cardano-preprod.blockfrost.io/api/v0/ (Testnet)
- **Base URL:** https://cardano-mainnet.blockfrost.io/api/v0/ (Mainnet)
- **Endpoints Used:**
  - `GET /addresses/{address}` - Address information
  - `GET /addresses/{address}/transactions` - Transaction history
  - `GET /transactions/{hash}` - Transaction details
  - `GET /network` - Network information

#### **Masumi Network APIs:**
- **Payment Service:** https://api.masumi.network (Future)
- **Registry:** TBD (For agent registration)

---

## 🚀 **Getting Started - Step by Step:**

### **Phase 1: Basic Testing (Free Tier)**
1. **Get Blockfrost API Key:**
   - Go to https://blockfrost.io/
   - Sign up for free account
   - Create project for "Preprod" network
   - Copy your project ID

2. **Update Configuration:**
   ```python
   # In config/masumi_config.py
   BLOCKFROST_PROJECT_ID_PREPROD = "preprod_YOUR_PROJECT_ID_HERE"
   ```

3. **Start the App:**
   ```bash
   .\scripts\start_folioflow.bat
   ```

4. **Test Basic Features:**
   - Connect wallet at http://localhost:8000
   - Try basic (free) portfolio analysis

### **Phase 2: Premium AI Features**
1. **Get OpenRouter API Key:**
   - Go to https://openrouter.ai/
   - Sign up and add payment method
   - Generate API key
   - Add $5-10 credit for testing

2. **Update Configuration:**
   ```python
   # In config/masumi_config.py
   OPENROUTER_API_KEY = "sk-or-v1-YOUR_ACTUAL_KEY_HERE"
   ```

3. **Test Premium Analysis:**
   - Restart the app
   - Try premium AI analysis (5 ADA)

### **Phase 3: Masumi Integration (Future)**
1. **Register with Masumi Network**
2. **Get Masumi API credentials**
3. **Update configuration**
4. **Deploy agent to network**

---

## 💰 **Cost Breakdown:**

### **Required Costs:**
- **Blockfrost:** FREE (up to 10k requests/day)
- **OpenRouter:** ~$0.01-0.05 per AI analysis
- **Hosting:** $0 (local testing) or ~$10-50/month (cloud)

### **Optional Costs:**
- **Masumi Network:** TBD (network fees)
- **Domain & SSL:** ~$10-20/year
- **Premium Blockfrost:** $10-50/month (for higher limits)

---

## 🔧 **Configuration Files to Update:**

### **1. Main Config File:**
```bash
# Edit this file with your API keys
notepad config\masumi_config.py
```

### **2. Environment File:**
```bash  
# Also update the .env file
notepad config\.env
```

### **3. Test Configuration:**
```bash
# Run this to test your setup
python scripts\deploy_masumi.py
```

---

## ✅ **Quick Checklist:**

### **To Run Basic App:**
- [ ] Get Blockfrost API key (FREE)
- [ ] Update `config/masumi_config.py`
- [ ] Run `.\scripts\start_folioflow.bat`
- [ ] Access http://localhost:8000

### **To Enable Premium AI:**
- [ ] Get OpenRouter API key (~$5 minimum)
- [ ] Update `config/masumi_config.py`
- [ ] Restart the app
- [ ] Test premium analysis

### **For Production Deployment:**
- [ ] Get production Blockfrost key (Mainnet)
- [ ] Set up cloud hosting (AWS/Azure/GCP)
- [ ] Configure domain and SSL
- [ ] Register with Masumi Network

---

## 🆘 **Troubleshooting:**

### **Common Issues:**
1. **"API key not configured"** → Update `config/masumi_config.py`
2. **"Connection failed"** → Check internet and API key validity
3. **"Agent not starting"** → Check Python dependencies and config path
4. **"Payment not working"** → Masumi integration is for future deployment

### **Test Commands:**
```bash
# Test configuration
python scripts\deploy_masumi.py

# Test API endpoints
curl http://localhost:5000/health
curl http://localhost:5000/agent/capabilities
```

---

## 🎯 **Priority Action Items:**

### **🔴 Immediate (Required to run):**
1. Get Blockfrost API key
2. Update configuration file
3. Test basic functionality

### **🟡 Short-term (For full features):**
1. Get OpenRouter API key
2. Test premium AI analysis
3. Optimize prompts and responses

### **🟢 Long-term (For production):**
1. Production API keys
2. Cloud deployment
3. Masumi Network integration

**Your app is 90% ready - just needs the API keys to unlock its full potential! 🚀**