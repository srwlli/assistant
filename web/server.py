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
PROJECTS_FILE = 'projects.json'

class CodeRefHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        parsed = urlparse(self.path)

        # API: Get all projects
        if parsed.path == '/api/projects':
            self.handle_get_projects()
        # API: Get folder tree
        elif parsed.path == '/api/tree':
            self.handle_tree_request(parsed)
        # API: Get file content
        elif parsed.path == '/api/file':
            self.handle_file_request(parsed)
        else:
            # Serve static files
            super().do_GET()

    def do_POST(self):
        parsed = urlparse(self.path)

        # API: Save project
        if parsed.path == '/api/projects':
            self.handle_save_project()
        else:
            self.send_error(404, "Not found")

    def do_DELETE(self):
        parsed = urlparse(self.path)

        # API: Delete project by ID
        if parsed.path.startswith('/api/projects/'):
            project_id = parsed.path.split('/')[-1]
            self.handle_delete_project(project_id)
        else:
            self.send_error(404, "Not found")

    def do_OPTIONS(self):
        """Handle CORS preflight"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def handle_get_projects(self):
        """Return all saved projects"""
        try:
            if os.path.exists(PROJECTS_FILE):
                with open(PROJECTS_FILE, 'r') as f:
                    projects = json.load(f)
            else:
                projects = []

            self.send_json_response(projects)
        except Exception as e:
            self.send_error(500, f"Error loading projects: {str(e)}")

    def handle_save_project(self):
        """Save a new project"""
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            project = json.loads(post_data)

            # Validate required fields
            if 'id' not in project or 'name' not in project or 'path' not in project:
                self.send_error(400, "Missing required fields: id, name, path")
                return

            # Validate path exists (skip validation for directory handles)
            if not project['path'].startswith('[Directory:'):
                if not os.path.exists(project['path']):
                    self.send_error(400, f"Path does not exist: {project['path']}")
                    return

            # Load existing projects
            if os.path.exists(PROJECTS_FILE):
                with open(PROJECTS_FILE, 'r') as f:
                    projects = json.load(f)
            else:
                projects = []

            # Check if project ID already exists
            existing_index = next((i for i, p in enumerate(projects) if p['id'] == project['id']), None)
            if existing_index is not None:
                # Update existing
                projects[existing_index] = project
            else:
                # Add new
                projects.append(project)

            # Save to file
            with open(PROJECTS_FILE, 'w') as f:
                json.dump(projects, f, indent=2)

            self.send_json_response({'success': True, 'project': project})
        except Exception as e:
            self.send_error(500, f"Error saving project: {str(e)}")

    def handle_delete_project(self, project_id):
        """Delete a project by ID"""
        try:
            if not os.path.exists(PROJECTS_FILE):
                self.send_error(404, "No projects found")
                return

            with open(PROJECTS_FILE, 'r') as f:
                projects = json.load(f)

            # Filter out the project
            projects = [p for p in projects if p['id'] != project_id]

            # Save updated list
            with open(PROJECTS_FILE, 'w') as f:
                json.dump(projects, f, indent=2)

            self.send_json_response({'success': True, 'deleted': project_id})
        except Exception as e:
            self.send_error(500, f"Error deleting project: {str(e)}")

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
