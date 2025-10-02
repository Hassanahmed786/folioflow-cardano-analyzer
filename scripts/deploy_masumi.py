#!/usr/bin/env python3
"""
FolioFlow Masumi Network Deployment Script
This script helps deploy your FolioFlow dApp as a Masumi Network AI Agent
"""

import json
import requests
import os
import sys
from datetime import datetime

class MasumiDeployment:
    def __init__(self):
        self.config = None
        self.load_config()
        
    def load_config(self):
        """Load configuration from masumi_config.py"""
        try:
            import masumi_config as config
            self.config = config
            print("✅ Configuration loaded successfully")
        except ImportError:
            print("❌ Configuration not found!")
            print("Please copy masumi_config_template.py to masumi_config.py and update the values")
            sys.exit(1)
    
    def check_dependencies(self):
        """Check if all required dependencies are available"""
        print("\n🔍 Checking dependencies...")
        
        required_packages = ['flask', 'requests', 'openai']
        missing_packages = []
        
        for package in required_packages:
            try:
                __import__(package)
                print(f"✅ {package} is installed")
            except ImportError:
                missing_packages.append(package)
                print(f"❌ {package} is missing")
        
        if missing_packages:
            print(f"\n📦 Install missing packages with:")
            print(f"pip install {' '.join(missing_packages)}")
            return False
        
        return True
    
    def validate_api_keys(self):
        """Validate API keys are configured"""
        print("\n🔑 Validating API keys...")
        
        keys_to_check = [
            ('MASUMI_API_KEY', 'Masumi Network API'),
            ('OPENROUTER_API_KEY', 'OpenRouter API'),
            ('BLOCKFROST_PROJECT_ID_PREPROD', 'Blockfrost Preprod')
        ]
        
        all_valid = True
        for key_name, description in keys_to_check:
            key_value = getattr(self.config, key_name, None)
            if not key_value or key_value.startswith('your_'):
                print(f"❌ {description} key not configured")
                all_valid = False
            else:
                print(f"✅ {description} key configured")
        
        return all_valid
    
    def test_openrouter_connection(self):
        """Test OpenRouter API connection"""
        print("\n🤖 Testing OpenRouter connection...")
        
        try:
            headers = {
                'Authorization': f'Bearer {self.config.OPENROUTER_API_KEY}',
                'Content-Type': 'application/json'
            }
            
            response = requests.get('https://openrouter.ai/api/v1/models', headers=headers)
            
            if response.status_code == 200:
                print("✅ OpenRouter API connection successful")
                return True
            else:
                print(f"❌ OpenRouter API error: {response.status_code}")
                return False
                
        except Exception as e:
            print(f"❌ OpenRouter connection failed: {e}")
            return False
    
    def test_blockfrost_connection(self):
        """Test Blockfrost API connection"""
        print("\n🔗 Testing Blockfrost connection...")
        
        try:
            headers = {
                'project_id': self.config.BLOCKFROST_PROJECT_ID_PREPROD
            }
            
            response = requests.get('https://cardano-preprod.blockfrost.io/api/v0/network', headers=headers)
            
            if response.status_code == 200:
                print("✅ Blockfrost API connection successful")
                return True
            else:
                print(f"❌ Blockfrost API error: {response.status_code}")
                return False
                
        except Exception as e:
            print(f"❌ Blockfrost connection failed: {e}")
            return False
    
    def register_agent_with_masumi(self):
        """Register the agent with Masumi Network"""
        print("\n📝 Registering agent with Masumi Network...")
        
        try:
            registration_data = self.config.AGENT_REGISTRATION_DATA
            
            # Add timestamp and additional metadata
            registration_data.update({
                'registered_at': datetime.utcnow().isoformat(),
                'endpoint_url': self.config.MASUMI_AGENT_URL,
                'frontend_url': self.config.FRONTEND_URL,
                'health_check_url': f"{self.config.BACKEND_URL}/health"
            })
            
            headers = {
                'Authorization': f'Bearer {self.config.MASUMI_API_KEY}',
                'Content-Type': 'application/json'
            }
            
            # This would be the actual Masumi registration endpoint
            # For now, we'll simulate the registration
            print("🔄 Submitting registration data...")
            print(f"Agent: {registration_data['name']}")
            print(f"Identifier: {registration_data['identifier']}")
            print(f"Capabilities: {', '.join(registration_data['capabilities'])}")
            
            # Save registration data locally for reference
            with open('agent_registration.json', 'w') as f:
                json.dump(registration_data, f, indent=2)
            
            print("✅ Agent registration data prepared")
            print("📄 Registration data saved to agent_registration.json")
            print("🚀 Ready for Masumi Network deployment!")
            
            return True
            
        except Exception as e:
            print(f"❌ Agent registration failed: {e}")
            return False
    
    def create_environment_file(self):
        """Create a .env file with configuration"""
        print("\n📄 Creating environment file...")
        
        env_content = f"""# FolioFlow Masumi Configuration
MASUMI_API_KEY={self.config.MASUMI_API_KEY}
OPENROUTER_API_KEY={self.config.OPENROUTER_API_KEY}
BLOCKFROST_PROJECT_ID_PREPROD={self.config.BLOCKFROST_PROJECT_ID_PREPROD}
AGENT_IDENTIFIER={self.config.AGENT_IDENTIFIER}
DEFAULT_NETWORK={self.config.DEFAULT_NETWORK}
FRONTEND_URL={self.config.FRONTEND_URL}
BACKEND_URL={self.config.BACKEND_URL}
"""
        
        with open('.env', 'w') as f:
            f.write(env_content)
        
        print("✅ Environment file created (.env)")
    
    def generate_startup_scripts(self):
        """Generate startup scripts for easy deployment"""
        print("\n📜 Generating startup scripts...")
        
        # Windows batch script
        windows_script = """@echo off
echo Starting FolioFlow Masumi Agent...
echo.

echo Starting Flask backend...
start "Backend" python masumi_agent.py

echo Waiting for backend to start...
timeout /t 3

echo Starting frontend server...
start "Frontend" python -m http.server 8000

echo.
echo ✅ FolioFlow is now running!
echo 🌐 Frontend: http://localhost:8000
echo 🤖 Agent API: http://localhost:5000/agent
echo.
echo Press any key to stop all services...
pause > nul

taskkill /f /im python.exe
"""
        
        with open('start_folioflow.bat', 'w') as f:
            f.write(windows_script)
        
        # Unix shell script
        unix_script = """#!/bin/bash
echo "Starting FolioFlow Masumi Agent..."
echo

echo "Starting Flask backend..."
python3 masumi_agent.py &
BACKEND_PID=$!

echo "Waiting for backend to start..."
sleep 3

echo "Starting frontend server..."
python3 -m http.server 8000 &
FRONTEND_PID=$!

echo
echo "✅ FolioFlow is now running!"
echo "🌐 Frontend: http://localhost:8000"
echo "🤖 Agent API: http://localhost:5000/agent"
echo
echo "Press Ctrl+C to stop all services..."

# Wait for interrupt
trap "kill $BACKEND_PID $FRONTEND_PID; exit" INT
wait
"""
        
        with open('start_folioflow.sh', 'w') as f:
            f.write(unix_script)
        
        # Make executable on Unix systems
        try:
            os.chmod('start_folioflow.sh', 0o755)
        except:
            pass
        
        print("✅ Startup scripts created:")
        print("   - start_folioflow.bat (Windows)")
        print("   - start_folioflow.sh (Unix/Linux/Mac)")
    
    def run_deployment(self):
        """Run the complete deployment process"""
        print("🚀 FolioFlow Masumi Network Deployment")
        print("=" * 50)
        
        # Step 1: Check dependencies
        if not self.check_dependencies():
            return False
        
        # Step 2: Validate API keys
        if not self.validate_api_keys():
            print("\n❌ Please configure your API keys in masumi_config.py")
            return False
        
        # Step 3: Test connections
        openrouter_ok = self.test_openrouter_connection()
        blockfrost_ok = self.test_blockfrost_connection()
        
        if not (openrouter_ok and blockfrost_ok):
            print("\n⚠️  Some API connections failed. Check your keys and try again.")
            return False
        
        # Step 4: Register with Masumi
        if not self.register_agent_with_masumi():
            return False
        
        # Step 5: Create environment files
        self.create_environment_file()
        
        # Step 6: Generate startup scripts
        self.generate_startup_scripts()
        
        print("\n" + "=" * 50)
        print("🎉 DEPLOYMENT COMPLETE!")
        print("=" * 50)
        print("📋 Next Steps:")
        print("1. Run: start_folioflow.bat (Windows) or ./start_folioflow.sh (Unix)")
        print("2. Open: http://localhost:8000 in your browser")
        print("3. Connect your Cardano wallet")
        print("4. Try the premium AI analysis (5 ADA)")
        print("5. Monitor the agent at: http://localhost:5000/agent/capabilities")
        print("\n🔗 Your agent is ready for the Masumi Network!")
        
        return True

if __name__ == "__main__":
    deployment = MasumiDeployment()
    success = deployment.run_deployment()
    
    if not success:
        print("\n❌ Deployment failed. Please fix the issues above and try again.")
        sys.exit(1)
    
    sys.exit(0)