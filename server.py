#!/usr/bin/env python3
"""
Simple HTTP server for the Christmas Tree project
Run this from the chrismastree folder to serve the files
"""

import http.server
import socketserver
import os

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS header to allow loading local resources
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

def run_server():
    # Change to the script's directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"✨ Christmas Tree Server running at http://localhost:{PORT}")
        print(f"📁 Serving from: {os.getcwd()}")
        print("🎄 Open your browser and navigate to the URL above")
        print("⏹️  Press Ctrl+C to stop the server")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n👋 Server stopped")

if __name__ == "__main__":
    run_server()
