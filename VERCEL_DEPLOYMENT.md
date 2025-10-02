# 🚀 Vercel Deployment Guide for FolioFlow

## Quick Deploy to Vercel

### Option 1: One-Click Deploy
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/Hassanahmed786/folioflow-cardano-analyzer)

### Option 2: Manual Deployment

1. **Fork or Clone this repository**
   ```bash
   git clone https://github.com/Hassanahmed786/folioflow-cardano-analyzer.git
   cd folioflow-cardano-analyzer
   ```

2. **Install Vercel CLI** (if not already installed)
   ```bash
   npm install -g vercel
   ```

3. **Login to Vercel**
   ```bash
   vercel login
   ```

4. **Deploy to Vercel**
   ```bash
   vercel
   ```

## Environment Variables Setup

After deployment, you need to configure these environment variables in your Vercel dashboard:

### Required Environment Variables:
1. `AZURE_OPENAI_API_KEY` - Your Azure OpenAI API key
2. `AZURE_OPENAI_ENDPOINT` - Your Azure OpenAI endpoint URL
3. `AZURE_OPENAI_API_VERSION` - API version (default: `2024-02-15-preview`)
4. `AZURE_OPENAI_DEPLOYMENT_NAME` - Your deployment name

### How to Add Environment Variables:
1. Go to your Vercel dashboard
2. Select your deployed project
3. Go to **Settings** → **Environment Variables**
4. Add each variable with its value
5. Redeploy the project for changes to take effect

## Project Structure for Vercel

```
folioflow-cardano-analyzer/
├── api/                    # Serverless functions
│   └── index.py           # Main Flask API
├── frontend/              # Static frontend files
│   ├── index.html
│   ├── script.js
│   ├── style.css
│   └── masumi-integration.js
├── config/                # Configuration files
├── vercel.json           # Vercel configuration
├── requirements.txt      # Python dependencies
└── package.json         # Node.js metadata
```

## Features

✅ **Serverless Backend**: Python Flask API deployed as Vercel serverless function  
✅ **Static Frontend**: Optimized HTML/CSS/JS served from CDN  
✅ **Auto-scaling**: Automatically scales based on traffic  
✅ **Global CDN**: Fast loading worldwide  
✅ **Environment Variables**: Secure configuration management  
✅ **Custom Domain**: Support for custom domains  

## API Endpoints

- **Frontend**: `https://your-deployment.vercel.app/`
- **API Health**: `https://your-deployment.vercel.app/api/`
- **Portfolio Analysis**: `https://your-deployment.vercel.app/api/analyze`

## Local Development

```bash
# Start backend
python backend/app.py

# Start frontend (in new terminal)
python -m http.server 8000 --directory frontend

# Access app
open http://localhost:8000
```

## Troubleshooting

### Common Issues:

1. **API Key Not Found**
   - Ensure environment variables are set in Vercel dashboard
   - Redeploy after adding environment variables

2. **CORS Issues**
   - The app is configured for cross-origin requests
   - Check browser console for specific errors

3. **Timeout Errors**
   - Vercel has a 10-second timeout for serverless functions
   - Large portfolio analysis might need optimization

4. **Build Failures**
   - Check Python version compatibility
   - Ensure all dependencies are in requirements.txt

## Support

For deployment issues, check:
- [Vercel Documentation](https://vercel.com/docs)
- [Python on Vercel Guide](https://vercel.com/docs/functions/serverless-functions/runtimes/python)
- [Project Issues](https://github.com/Hassanahmed786/folioflow-cardano-analyzer/issues)