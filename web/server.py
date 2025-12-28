#!/usr/bin/env python3
"""
Simple HTTP server with file browsing API for CodeRef Explorer
"""
import http.server
import socketserver
import json
import os
from urllib.parse import parse_qs, urlparse
from pathlib import Path

PORT = 8080

class CodeRefHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        parsed = urlparse(self.path)

        # API: Get folder tree
        if parsed.path == '/api/tree':
            self.handle_tree_request(parsed)
        # API: Get file content
        elif parsed.path == '/api/file':
            self.handle_file_request(parsed)
        else:
            # Serve static files
            super().do_GET()

    def handle_tree_request(self, parsed):
        """Return folder structure as JSON"""
        params = parse_qs(parsed.query)
        folder_path = params.get('path', [''])[0]

        if not folder_path or not os.path.exists(folder_path):
            self.send_error(400, "Invalid path")
            return

        try:
            tree = self.build_tree(folder_path)
            self.send_json_response(tree)
        except Exception as e:
            self.send_error(500, f"Error reading directory: {str(e)}")

    def handle_file_request(self, parsed):
        """Return file content"""
        params = parse_qs(parsed.query)
        file_path = params.get('path', [''])[0]

        if not file_path or not os.path.exists(file_path):
            self.send_error(404, "File not found")
            return

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            file_info = {
                'content': content,
                'name': os.path.basename(file_path),
                'size': os.path.getsize(file_path),
                'modified': os.path.getmtime(file_path)
            }
            self.send_json_response(file_info)
        except Exception as e:
            self.send_error(500, f"Error reading file: {str(e)}")

    def build_tree(self, path):
        """Build folder tree structure"""
        tree = {
            'name': os.path.basename(path),
            'path': path,
            'type': 'folder',
            'children': []
        }

        try:
            entries = sorted(os.listdir(path))

            for entry in entries:
                full_path = os.path.join(path, entry)

                if os.path.isdir(full_path):
                    tree['children'].append(self.build_tree(full_path))
                else:
                    tree['children'].append({
                        'name': entry,
                        'path': full_path,
                        'type': 'file'
                    })
        except PermissionError:
            pass

        return tree

    def send_json_response(self, data):
        """Send JSON response"""
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

with socketserver.TCPServer(("", PORT), CodeRefHandler) as httpd:
    print(f"Server running at http://localhost:{PORT}/")
    print("Press Ctrl+C to stop")
    httpd.serve_forever()
