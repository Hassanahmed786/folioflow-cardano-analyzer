# 🚀 Deploy FolioFlow to Vercel - Quick Guide

## ✅ Your App is Ready for Vercel Deployment!

I've configured your FolioFlow application for Vercel deployment with the following setup:

### 📁 Files Created for Deployment:
- `vercel.json` - Vercel configuration
- `api/index.py` - Serverless function for backend
- `package.json` - Project metadata
- `VERCEL_DEPLOYMENT.md` - Detailed deployment guide
- `scripts/deploy_vercel.py` - Deployment helper script

### 🎯 Three Ways to Deploy:

## Option 1: One-Click Deploy (Easiest)
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/Hassanahmed786/folioflow-cardano-analyzer)

## Option 2: GitHub Integration
1. Go to [vercel.com](https://vercel.com)
2. Sign up/Login with GitHub
3. Click "Import Project"
4. Select your `folioflow-cardano-analyzer` repository
5. Click "Deploy"

## Option 3: Manual with Vercel CLI
```bash
# Install Node.js from https://nodejs.org
# Then install Vercel CLI
npm install -g vercel

# In your project directory
vercel login
vercel --prod
```

## 🔐 Environment Variables Setup

**CRITICAL**: After deployment, add these environment variables in Vercel dashboard:

1. **AZURE_OPENAI_API_KEY** = `your_azure_openai_api_key`
2. **AZURE_OPENAI_ENDPOINT** = `your_azure_endpoint_url`
3. **AZURE_OPENAI_API_VERSION** = `2024-02-15-preview`
4. **AZURE_OPENAI_DEPLOYMENT_NAME** = `your_deployment_name`

### How to Add Environment Variables:
1. Go to your Vercel project dashboard
2. Click **Settings** → **Environment Variables**
3. Add each variable above
4. **Important**: Redeploy after adding variables

## 🎉 What You Get:

✅ **Global CDN**: Fast loading worldwide  
✅ **Auto-scaling**: Handles traffic spikes  
✅ **HTTPS**: Secure by default  
✅ **Custom Domain**: Add your own domain  
✅ **Serverless**: No server management  

## 📊 Your App Structure:
```
https://your-app.vercel.app/          → Frontend
https://your-app.vercel.app/api/      → API Health Check  
https://your-app.vercel.app/api/analyze → Portfolio Analysis
```

## 🚀 Ready to Deploy!

Your FolioFlow app is fully configured for Vercel. Choose any deployment option above and you'll have a live app in minutes!

Need help? Check `VERCEL_DEPLOYMENT.md` for detailed instructions.