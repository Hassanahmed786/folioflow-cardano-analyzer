#!/usr/bin/env python3
"""
FolioFlow Quick Setup Helper
This script helps you configure API keys and test the setup
"""

import os
import sys
import json

def check_api_keys():
    """Check which API keys are configured"""
    print("🔍 Checking API Key Configuration...")
    print("=" * 50)
    
    try:
        # Add config to path
        config_path = os.path.join(os.path.dirname(__file__), '..', 'config')
        sys.path.append(config_path)
        import masumi_config as config
        
        # Check each API key
        keys_status = {
            "Blockfrost (Preprod)": {
                "key": config.BLOCKFROST_PROJECT_ID_PREPROD,
                "is_demo": config.BLOCKFROST_PROJECT_ID_PREPROD.startswith('preprod_demo'),
                "required": True,
                "get_url": "https://blockfrost.io/"
            },
            "OpenRouter": {
                "key": config.OPENROUTER_API_KEY,
                "is_demo": config.OPENROUTER_API_KEY.startswith('sk-or-v1-demo'),
                "required": True,
                "get_url": "https://openrouter.ai/"
            },
            "Masumi Network": {
                "key": config.MASUMI_API_KEY,
                "is_demo": config.MASUMI_API_KEY.startswith('demo_'),
                "required": False,
                "get_url": "https://masumi.network/"
            }
        }
        
        all_ready = True
        
        for service, info in keys_status.items():
            status = "❌ DEMO KEY" if info['is_demo'] else "✅ CONFIGURED"
            priority = "🔴 REQUIRED" if info['required'] else "🟡 OPTIONAL"
            
            print(f"{service:<20} {status:<15} {priority}")
            if info['is_demo'] and info['required']:
                print(f"   → Get your key at: {info['get_url']}")
                all_ready = False
        
        print("\n" + "=" * 50)
        
        if all_ready:
            print("🎉 All required API keys are configured!")
            return True
        else:
            print("⚠️  Please configure the required API keys above.")
            return False
            
    except ImportError:
        print("❌ Configuration file not found!")
        print("Please ensure config/masumi_config.py exists.")
        return False

def show_setup_instructions():
    """Show step-by-step setup instructions"""
    print("\n🚀 QUICK SETUP GUIDE")
    print("=" * 50)
    
    print("""
1. 🔑 GET BLOCKFROST API KEY (Required - FREE):
   • Go to: https://blockfrost.io/
   • Sign up for free account
   • Create new project for "Preprod" network
   • Copy your project ID
   
2. 💰 GET OPENROUTER API KEY (Required - Paid):
   • Go to: https://openrouter.ai/
   • Sign up and add payment method
   • Add $5-10 credit for testing
   • Generate API key
   
3. ⚙️ UPDATE CONFIGURATION:
   • Edit: config/masumi_config.py
   • Replace demo keys with your real keys
   
4. 🚀 START THE APP:
   • Run: .\\scripts\\start_folioflow.bat
   • Access: http://localhost:8000
""")

def generate_config_template():
    """Generate a personalized config file"""
    print("\n📝 CONFIG FILE GENERATOR")
    print("=" * 50)
    
    print("Enter your API keys (press Enter to skip):")
    
    blockfrost_key = input("Blockfrost Preprod Project ID: ").strip()
    openrouter_key = input("OpenRouter API Key: ").strip()
    masumi_key = input("Masumi API Key (optional): ").strip()
    
    # Read template
    template_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'masumi_config_template.py')
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'masumi_config.py')
    
    try:
        with open(template_path, 'r') as f:
            content = f.read()
        
        # Replace keys if provided
        if blockfrost_key:
            content = content.replace('preprod_demo_key', blockfrost_key)
        
        if openrouter_key:
            content = content.replace('sk-or-v1-demo-key', openrouter_key)
            
        if masumi_key:
            content = content.replace('demo_masumi_key_for_testing', masumi_key)
        
        # Write updated config
        with open(config_path, 'w') as f:
            f.write(content)
        
        print("✅ Configuration file updated!")
        return True
        
    except Exception as e:
        print(f"❌ Error updating config: {e}")
        return False

def test_apis():
    """Test API connections"""
    print("\n🧪 TESTING API CONNECTIONS")
    print("=" * 50)
    
    try:
        import requests
        
        # Test OpenRouter
        print("Testing OpenRouter API...")
        try:
            config_path = os.path.join(os.path.dirname(__file__), '..', 'config')
            sys.path.append(config_path)
            import masumi_config as config
            
            if not config.OPENROUTER_API_KEY.startswith('sk-or-v1-demo'):
                headers = {
                    'Authorization': f'Bearer {config.OPENROUTER_API_KEY}',
                    'Content-Type': 'application/json'
                }
                response = requests.get('https://openrouter.ai/api/v1/models', headers=headers, timeout=10)
                if response.status_code == 200:
                    print("✅ OpenRouter API - Connected")
                else:
                    print(f"❌ OpenRouter API - Error {response.status_code}")
            else:
                print("⏭️  OpenRouter API - Skipped (demo key)")
        
        except Exception as e:
            print(f"❌ OpenRouter API - Failed: {e}")
        
        # Test Blockfrost
        print("Testing Blockfrost API...")
        try:
            if not config.BLOCKFROST_PROJECT_ID_PREPROD.startswith('preprod_demo'):
                headers = {'project_id': config.BLOCKFROST_PROJECT_ID_PREPROD}
                response = requests.get('https://cardano-preprod.blockfrost.io/api/v0/network', headers=headers, timeout=10)
                if response.status_code == 200:
                    print("✅ Blockfrost API - Connected")
                else:
                    print(f"❌ Blockfrost API - Error {response.status_code}")
            else:
                print("⏭️  Blockfrost API - Skipped (demo key)")
                
        except Exception as e:
            print(f"❌ Blockfrost API - Failed: {e}")
            
    except ImportError:
        print("❌ Required packages not installed. Run: pip install requests")

def main():
    print("🎯 FolioFlow Quick Setup Helper")
    print("=" * 50)
    
    while True:
        print("\nWhat would you like to do?")
        print("1. 🔍 Check API key status")
        print("2. 📝 Generate/update config file")
        print("3. 🧪 Test API connections")
        print("4. 📖 Show setup instructions")
        print("5. 🚀 Start the app")
        print("6. ❌ Exit")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            check_api_keys()
        elif choice == '2':
            generate_config_template()
        elif choice == '3':
            test_apis()
        elif choice == '4':
            show_setup_instructions()
        elif choice == '5':
            print("\n🚀 Starting FolioFlow...")
            os.system('.\\scripts\\start_folioflow.bat')
            break
        elif choice == '6':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()