// FolioFlow Masumi Network Integration
// Frontend component for Masumi AI Agent integration

class MasumiIntegration {
    constructor() {
        this.agentEndpoint = 'http://localhost:5000/agent';
        this.masumiPaymentService = 'http://localhost:3001';
        this.agentIdentifier = 'folioflow-portfolio-analyzer';
        this.analysisPrice = 5000000; // 5 ADA in lovelace
    }

    async getAgentCapabilities() {
        try {
            const response = await fetch(`${this.agentEndpoint}/capabilities`);
            return await response.json();
        } catch (error) {
            console.error('Failed to get agent capabilities:', error);
            return null;
        }
    }

    async requestPaidAnalysis(walletAddress) {
        try {
            // Step 1: Create payment request through Masumi
            console.log('🔄 Creating payment request...');
            const paymentRequest = await this.createPaymentRequest(walletAddress);
            
            if (!paymentRequest) {
                throw new Error('Failed to create payment request');
            }

            // Step 2: Show payment modal to user
            console.log('💳 Showing payment interface...');
            const paymentCompleted = await this.showPaymentModal(paymentRequest);
            
            if (!paymentCompleted) {
                throw new Error('Payment cancelled by user');
            }

            // Step 3: Request analysis from agent
            console.log('🤖 Requesting AI analysis...');
            const analysis = await this.requestAnalysis(
                paymentRequest.blockchain_identifier,
                walletAddress,
                paymentRequest.input_hash
            );

            return analysis;

        } catch (error) {
            console.error('Paid analysis failed:', error);
            throw error;
        }
    }

    async createPaymentRequest(walletAddress) {
        try {
            const inputData = {
                wallet_address: walletAddress,
                service: 'portfolio_analysis',
                timestamp: Date.now()
            };

            const inputHash = await this.createHash(JSON.stringify(inputData));

            const response = await fetch(`${this.masumiPaymentService}/api/v1/payment/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer your_masumi_api_key' // Should be configured
                },
                body: JSON.stringify({
                    inputHash: inputHash,
                    network: 'Preprod', // or 'Mainnet'
                    agentIdentifier: this.agentIdentifier,
                    RequestedFunds: [{
                        amount: this.analysisPrice.toString(),
                        unit: ''
                    }],
                    payByTime: new Date(Date.now() + 3600000).toISOString(), // 1 hour
                    submitResultTime: new Date(Date.now() + 7200000).toISOString(), // 2 hours
                    unlockTime: new Date(Date.now() + 10800000).toISOString(), // 3 hours
                    externalDisputeUnlockTime: new Date(Date.now() + 86400000).toISOString() // 24 hours
                })
            });

            if (response.ok) {
                const data = await response.json();
                return {
                    blockchain_identifier: data.data.blockchainIdentifier,
                    input_hash: inputHash,
                    payment_amount: this.analysisPrice,
                    payment_deadline: data.data.payByTime
                };
            }

            return null;
        } catch (error) {
            console.error('Payment request creation failed:', error);
            return null;
        }
    }

    async showPaymentModal(paymentRequest) {
        return new Promise((resolve) => {
            // Create payment modal
            const modal = document.createElement('div');
            modal.className = 'masumi-payment-modal';
            modal.innerHTML = `
                <div class="modal-content">
                    <div class="modal-header">
                        <h3>💳 Pay for AI Portfolio Analysis</h3>
                        <button class="close-btn" onclick="this.closest('.masumi-payment-modal').remove(); resolve(false);">&times;</button>
                    </div>
                    <div class="modal-body">
                        <div class="payment-info">
                            <div class="service-details">
                                <h4>🤖 FolioFlow AI Agent</h4>
                                <p>Advanced portfolio analysis with tax intelligence</p>
                            </div>
                            <div class="pricing">
                                <span class="amount">${this.analysisPrice / 1000000} ADA</span>
                                <span class="usd-equivalent">≈ $1.50 USD</span>
                            </div>
                        </div>
                        
                        <div class="payment-methods">
                            <h4>Select Payment Method:</h4>
                            <button class="payment-btn wallet-payment" onclick="this.handleWalletPayment('${paymentRequest.blockchain_identifier}')">
                                🔗 Pay with Connected Wallet
                            </button>
                            <button class="payment-btn qr-payment">
                                📱 Show QR Code
                            </button>
                        </div>
                        
                        <div class="payment-details">
                            <p><strong>Payment ID:</strong> ${paymentRequest.blockchain_identifier.substring(0, 20)}...</p>
                            <p><strong>Deadline:</strong> ${new Date(paymentRequest.payment_deadline).toLocaleString()}</p>
                        </div>
                        
                        <div class="payment-status" id="payment-status">
                            <p>⏳ Waiting for payment...</p>
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button class="cancel-btn" onclick="this.closest('.masumi-payment-modal').remove(); resolve(false);">Cancel</button>
                        <button class="check-payment-btn" onclick="this.checkPaymentStatus('${paymentRequest.blockchain_identifier}')">Check Payment</button>
                    </div>
                </div>
            `;

            // Add modal styles
            const style = document.createElement('style');
            style.textContent = `
                .masumi-payment-modal {
                    position: fixed;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    background: rgba(0, 0, 0, 0.8);
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    z-index: 10000;
                }
                .masumi-payment-modal .modal-content {
                    background: linear-gradient(135deg, #1a1a2e, #16213e);
                    border-radius: 15px;
                    padding: 30px;
                    max-width: 500px;
                    width: 90%;
                    color: white;
                    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
                }
                .payment-btn {
                    width: 100%;
                    padding: 15px;
                    margin: 10px 0;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                    border: none;
                    border-radius: 8px;
                    cursor: pointer;
                    font-size: 16px;
                    transition: transform 0.2s;
                }
                .payment-btn:hover {
                    transform: translateY(-2px);
                }
                .amount {
                    font-size: 24px;
                    font-weight: bold;
                    color: #00d4ff;
                }
            `;
            document.head.appendChild(style);

            // Add modal to page
            document.body.appendChild(modal);

            // Add global functions for modal
            window.handleWalletPayment = async (blockchainId) => {
                await this.processWalletPayment(blockchainId);
            };

            window.checkPaymentStatus = async (blockchainId) => {
                const verified = await this.verifyPayment(blockchainId);
                if (verified) {
                    modal.remove();
                    resolve(true);
                } else {
                    document.getElementById('payment-status').innerHTML = '<p>❌ Payment not confirmed yet</p>';
                }
            };
        });
    }

    async processWalletPayment(blockchainIdentifier) {
        try {
            if (!connectedWallet) {
                showError('Please connect your wallet first');
                return;
            }

            // Get payment address from Masumi
            const paymentAddress = await this.getPaymentAddress(blockchainIdentifier);
            
            // Note: This is a simplified payment flow - in a real implementation,
            // you would need to use a transaction building library like Lucid or Mesh
            console.warn('Wallet payment flow needs proper transaction building implementation');
            
            // For now, show a simplified payment interface
            showError('Payment integration requires additional transaction building libraries. Using free analysis instead.');
            return false;
            
        } catch (error) {
            console.error('Wallet payment failed:', error);
            document.getElementById('payment-status').innerHTML = '<p>❌ Payment failed</p>';
        }
    }

    async getPaymentAddress(blockchainIdentifier) {
        // Get the smart contract address for this payment
        // This would typically be provided by Masumi Payment Service
        return 'addr_test1wz7j4kmg2cs7yf92uat3ed4a3u97kr7axxr4avaz0lhwdsqukgwfm'; // Preprod
    }

    async verifyPayment(blockchainIdentifier) {
        try {
            const response = await fetch(`${this.masumiPaymentService}/api/v1/payment/resolve-blockchain-identifier`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer your_masumi_api_key'
                },
                body: JSON.stringify({
                    blockchainIdentifier: blockchainIdentifier,
                    network: 'Preprod'
                })
            });

            if (response.ok) {
                const data = await response.json();
                return data.data?.onChainState === 'FundsLocked';
            }
            return false;
        } catch (error) {
            console.error('Payment verification failed:', error);
            return false;
        }
    }

    async requestAnalysis(blockchainIdentifier, walletAddress, inputHash) {
        try {
            const response = await fetch(`${this.agentEndpoint}/analyze`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    blockchain_identifier: blockchainIdentifier,
                    wallet_address: walletAddress,
                    input_hash: inputHash
                })
            });

            if (response.ok) {
                return await response.json();
            } else if (response.status === 402) {
                throw new Error('Payment not verified');
            } else {
                throw new Error('Analysis request failed');
            }
        } catch (error) {
            console.error('Analysis request failed:', error);
            throw error;
        }
    }

    async createHash(data) {
        const encoder = new TextEncoder();
        const dataBuffer = encoder.encode(data);
        const hashBuffer = await crypto.subtle.digest('SHA-256', dataBuffer);
        const hashArray = Array.from(new Uint8Array(hashBuffer));
        return hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
    }

    // Enhanced UI for Masumi integration
    addMasumiUIElements() {
        // Add Masumi branding and agent status
        const masumiInfo = document.createElement('div');
        masumiInfo.className = 'masumi-integration-info';
        masumiInfo.innerHTML = `
            <div class="masumi-badge">
                <span class="masumi-logo">🔗</span>
                <span>Powered by Masumi Network</span>
            </div>
            <div class="agent-status">
                <span class="status-indicator active">●</span>
                <span>AI Agent Active</span>
            </div>
        `;

        // Add to header
        const header = document.querySelector('header');
        if (header) {
            header.appendChild(masumiInfo);
        }
    }
}

// Initialize Masumi integration
const masumiIntegration = new MasumiIntegration();

// Enhanced analyze button for Masumi payments
function initializeMasumiIntegration() {
    // Update existing analyze button - remove existing listeners first
    const analyzeBtn = document.getElementById('analyze-btn');
    if (analyzeBtn) {
        // Clone the button to remove all existing event listeners
        const newAnalyzeBtn = analyzeBtn.cloneNode(true);
        analyzeBtn.parentNode.replaceChild(newAnalyzeBtn, analyzeBtn);
        
        // Add the new combined event listener
        newAnalyzeBtn.addEventListener('click', async () => {
            if (!connectedWallet) {
                showError('Please connect your wallet first');
                return;
            }

            try {
                // Validate wallet connection before showing options
                if (!connectedWallet.instance && !connectedWallet.address) {
                    showError('Wallet connection invalid. Please reconnect your wallet.');
                    return;
                }

                // Show payment option
                const choice = confirm('Choose analysis type:\n\nOK = Premium AI Analysis (5 ADA)\nCancel = Basic Analysis (Free)');
                
                if (choice) {
                    // Paid Masumi agent analysis
                    showLoading('🤖 Processing payment and AI analysis...');
                    
                    // For now, redirect to free analysis since payment isn't fully implemented
                    showError('Premium analysis coming soon! Using free analysis instead.');
                    await window.analyzeTransactions(); // Call the original function
                } else {
                    // Free basic analysis - call the original analyze function
                    await window.analyzeTransactions();
                }
            } catch (error) {
                showError('Analysis failed: ' + error.message);
            }
        });
    }

    // Add Masumi UI elements
    masumiIntegration.addMasumiUIElements();
}

function displayPremiumResults(result) {
    // Enhanced results display for premium Masumi analysis
    const premiumBadge = '<span class="premium-badge">🤖 AI Premium</span>';
    
    // Update results with premium features
    hideAllSections();
    portfolioSummary.innerHTML = `
        <div class="premium-header">
            ${premiumBadge}
            <h3>Advanced AI Portfolio Analysis</h3>
        </div>
        <div class="analysis-grid">
            ${JSON.stringify(result.analysis, null, 2)}
        </div>
        <div class="masumi-verification">
            <p>✅ Verified by Masumi Network</p>
            <p>Result Hash: ${result.result_hash}</p>
            <p>Agent: ${result.agent.name} v${result.agent.version}</p>
        </div>
    `;
    
    resultsSection.classList.remove('hidden');
}

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    // Wait for main script to be fully loaded
    function waitForMainScript() {
        if (typeof window.analyzeTransactions === 'function' && 
            typeof showError === 'function' && 
            typeof showLoading === 'function') {
            console.log('✅ Main script loaded, initializing Masumi integration...');
            initializeMasumiIntegration();
        } else {
            console.log('⏳ Waiting for main script to load...');
            setTimeout(waitForMainScript, 100);
        }
    }
    
    // Start checking after a short delay
    setTimeout(waitForMainScript, 500);
});