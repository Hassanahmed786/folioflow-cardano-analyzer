#!/usr/bin/env python3
"""
FolioFlow API - Vercel Serverless Function
"""

from flask import Flask, jsonify
import os
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        "service": "FolioFlow API",
        "status": "healthy",
        "message": "API is working on Vercel!",
        "timestamp": datetime.now().isoformat()
    })

@app.route('/test')
def test():
    return jsonify({
        "test": "success",
        "message": "Vercel deployment working!",
        "timestamp": datetime.now().isoformat()
    })

@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    return jsonify({
        "message": "Analysis endpoint is working",
        "note": "This is a simplified version for testing",
        "timestamp": datetime.now().isoformat()
    })

# This is what Vercel needs for serverless functions
if __name__ == '__main__':
    app.run(debug=True)