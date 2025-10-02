#!/usr/bin/env python3
"""
Vercel Deployment Helper Script
Automates the deployment process for FolioFlow to Vercel
"""

import os
import sys
import subprocess
import json
from pathlib import Path

def check_vercel_cli():
    """Check if Vercel CLI is installed"""
    try:
        result = subprocess.run(['vercel', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Vercel CLI found: {result.stdout.strip()}")
            return True
        else:
            print("❌ Vercel CLI not found")
            return False
    except FileNotFoundError:
        print("❌ Vercel CLI not installed")
        return False

def install_vercel_cli():
    """Install Vercel CLI"""
    print("📦 Installing Vercel CLI...")
    try:
        subprocess.run(['npm', 'install', '-g', 'vercel'], check=True)
        print("✅ Vercel CLI installed successfully")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install Vercel CLI")
        return False
    except FileNotFoundError:
        print("❌ npm not found. Please install Node.js first")
        return False

def login_to_vercel():
    """Login to Vercel"""
    print("🔐 Logging into Vercel...")
    try:
        subprocess.run(['vercel', 'login'], check=True)
        print("✅ Successfully logged into Vercel")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to login to Vercel")
        return False

def deploy_to_vercel():
    """Deploy the project to Vercel"""
    print("🚀 Deploying to Vercel...")
    try:
        subprocess.run(['vercel', '--prod'], check=True)
        print("✅ Successfully deployed to Vercel")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to deploy to Vercel")
        return False

def check_environment_variables():
    """Check if required environment variables are mentioned"""
    print("\n📋 Environment Variables Checklist:")
    env_vars = [
        "AZURE_OPENAI_API_KEY",
        "AZURE_OPENAI_ENDPOINT", 
        "AZURE_OPENAI_API_VERSION",
        "AZURE_OPENAI_DEPLOYMENT_NAME"
    ]
    
    print("⚠️  Remember to set these in your Vercel dashboard:")
    for var in env_vars:
        print(f"   • {var}")
    
    print("\n🔧 How to set environment variables:")
    print("   1. Go to your Vercel dashboard")
    print("   2. Select your deployed project")
    print("   3. Go to Settings → Environment Variables")
    print("   4. Add each variable with its value")
    print("   5. Redeploy for changes to take effect")

def main():
    """Main deployment script"""
    print("🎯 FolioFlow Vercel Deployment Helper")
    print("=" * 50)
    
    # Check current directory
    if not Path('vercel.json').exists():
        print("❌ vercel.json not found. Make sure you're in the project root directory.")
        sys.exit(1)
    
    # Check Vercel CLI
    if not check_vercel_cli():
        if input("Install Vercel CLI? (y/n): ").lower() == 'y':
            if not install_vercel_cli():
                sys.exit(1)
        else:
            print("❌ Vercel CLI required for deployment")
            sys.exit(1)
    
    # Login to Vercel
    if input("Login to Vercel? (y/n): ").lower() == 'y':
        if not login_to_vercel():
            sys.exit(1)
    
    # Deploy
    if input("Deploy to Vercel? (y/n): ").lower() == 'y':
        if deploy_to_vercel():
            print("\n🎉 Deployment completed successfully!")
            check_environment_variables()
        else:
            sys.exit(1)
    
    print("\n📚 For more help, see VERCEL_DEPLOYMENT.md")

if __name__ == "__main__":
    main()