#!/usr/bin/env python3
"""
FolioFlow API - Simple test endpoint for Vercel
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)
CORS(app, origins=["*"])

@app.route('/')
def health():
    """Simple health check"""
    return jsonify({
        "service": "FolioFlow API",
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "message": "API is working!"
    })

@app.route('/test')
def test():
    """Test endpoint"""
    return jsonify({
        "test": "success",
        "message": "Vercel deployment working!",
        "timestamp": datetime.now().isoformat()
    })

# Vercel export
def handler(request, response):
    return app

# Alternative export format
application = app

if __name__ == '__main__':
    app.run(debug=True, port=5000)