from http.server import BaseHTTPRequestHandler
import json
from datetime import datetime
import urllib.parse

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        # Parse the path
        parsed_path = urllib.parse.urlparse(self.path)
        path = parsed_path.path
        
        if path == '/' or path == '':
            response = {
                "service": "FolioFlow API",
                "status": "healthy",
                "message": "API is working on Vercel!",
                "timestamp": datetime.now().isoformat(),
                "endpoints": ["/", "/test", "/analyze"]
            }
        elif path == '/test':
            response = {
                "test": "success",
                "message": "Vercel deployment working!",
                "timestamp": datetime.now().isoformat()
            }
        else:
            response = {
                "error": "Endpoint not found",
                "path": path,
                "available_endpoints": ["/", "/test", "/analyze"]
            }
        
        self.wfile.write(json.dumps(response).encode())
    
    def do_POST(self):
        if self.path == '/analyze':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            response = {
                "message": "Analysis endpoint is working",
                "note": "This is a simplified version for testing",
                "timestamp": datetime.now().isoformat(),
                "status": "ready for full implementation"
            }
            
            self.wfile.write(json.dumps(response).encode())
        else:
            self.do_GET()
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        self.end_headers()