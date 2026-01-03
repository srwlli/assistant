# API Reference

**Version:** 1.0.0
**Last Updated:** 2025-12-28

---

## Overview

CodeRef Explorer exposes three API layers:

1. **HTTP REST API** - Python backend server for project management and file operations
2. **Browser APIs** - File System Access API, IndexedDB, and LocalStorage
3. **Electron IPC** - Minimal platform and version detection

This document provides complete API specifications, request/response formats, and error handling patterns.

---

## HTTP REST API

Base URL: `http://localhost:8080`

### Endpoints

#### 1. Get All Projects

```http
GET /api/projects
```

Retrieves list of all saved projects from `projects.json`.

**Response 200 OK:**
```json
[
  {
    "id": "project-123",
    "name": "My Project",
    "path": "/path/to/project"
  },
  {
    "id": "project-456",
    "name": "Another Project",
    "path": "[Directory: Handle-UUID]"
  }
]
```

**Response 500 Internal Server Error:**
```json
{
  "error": "Error loading projects: {error_message}"
}
```

---

#### 2. Save Project

```http
POST /api/projects
Content-Type: application/json
```

Saves or updates a project. Creates `projects.json` if it doesn't exist.

**Request Body:**
```json
{
  "id": "project-123",
  "name": "My Project",
  "path": "/absolute/path/to/project"
}
```

**Required Fields:**
- `id` (string) - Unique project identifier
- `name` (string) - Display name
- `path` (string) - Absolute file system path or `[Directory: Handle]` token

**Response 200 OK:**
```json
{
  "success": true,
  "project": {
    "id": "project-123",
    "name": "My Project",
    "path": "/absolute/path/to/project"
  }
}
```

**Response 400 Bad Request:**
```json
{
  "error": "Missing required fields: id, name, path"
}
```

```json
{
  "error": "Path does not exist: /invalid/path"
}
```

**Response 500 Internal Server Error:**
```json
{
  "error": "Error saving project: {error_message}"
}
```

**Behavior:**
- If project with same `id` exists, it will be updated
- If project is new, it will be appended to the list
- Directory handle paths (format: `[Directory: ...]`) skip validation

---

#### 3. Delete Project

```http
DELETE /api/projects/{project_id}
```

Deletes a project by ID from `projects.json`.

**Path Parameters:**
- `project_id` (string) - Unique project identifier

**Example:**
```bash
curl -X DELETE http://localhost:8080/api/projects/project-123
```

**Response 200 OK:**
```json
{
  "success": true,
  "deleted": "project-123"
}
```

**Response 404 Not Found:**
```json
{
  "error": "No projects found"
}
```

**Response 500 Internal Server Error:**
```json
{
  "error": "Error deleting project: {error_message}"
}
```

---

#### 4. Get Folder Tree

```http
GET /api/tree?path={absolute_path}
```

Returns recursive folder structure as JSON tree.

**Query Parameters:**
- `path` (string, required) - Absolute file system path

**Example:**
```bash
curl "http://localhost:8080/api/tree?path=/Users/name/project"
```

**Response 200 OK:**
```json
{
  "name": "project",
  "path": "/Users/name/project",
  "type": "folder",
  "children": [
    {
      "name": "src",
      "path": "/Users/name/project/src",
      "type": "folder",
      "children": [
        {
          "name": "main.js",
          "path": "/Users/name/project/src/main.js",
          "type": "file"
        }
      ]
    },
    {
      "name": "README.md",
      "path": "/Users/name/project/README.md",
      "type": "file"
    }
  ]
}
```

**Response 400 Bad Request:**
```json
{
  "error": "Invalid path"
}
```

**Response 500 Internal Server Error:**
```json
{
  "error": "Error reading directory: {error_message}"
}
```

**Behavior:**
- Directories without read permissions are skipped silently
- Entries are sorted alphabetically
- Tree is fully recursive

---

#### 5. Get File Content

```http
GET /api/file?path={absolute_path}
```

Reads and returns file content with metadata.

**Query Parameters:**
- `path` (string, required) - Absolute file system path

**Example:**
```bash
curl "http://localhost:8080/api/file?path=/Users/name/project/README.md"
```

**Response 200 OK:**
```json
{
  "content": "# My Project\n\nThis is the README.",
  "name": "README.md",
  "size": 34,
  "modified": 1703721600.0
}
```

**Fields:**
- `content` (string) - UTF-8 decoded file content
- `name` (string) - File basename
- `size` (integer) - File size in bytes
- `modified` (float) - Unix timestamp of last modification

**Response 404 Not Found:**
```json
{
  "error": "File not found"
}
```

**Response 500 Internal Server Error:**
```json
{
  "error": "Error reading file: {error_message}"
}
```

---

#### 6. CORS Preflight

```http
OPTIONS /*
```

Handles CORS preflight requests for cross-origin access.

**Response Headers:**
```
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: GET, POST, DELETE, OPTIONS
Access-Control-Allow-Headers: Content-Type
```

---

## Browser APIs

### File System Access API

Used for directory access when running in Chromium-based browsers.

**Directory Picker:**
```javascript
const dirHandle = await window.showDirectoryPicker({
  mode: 'read'
});

// dirHandle: FileSystemDirectoryHandle
```

**Read Directory:**
```javascript
for await (const entry of dirHandle.values()) {
  if (entry.kind === 'file') {
    const file = await entry.getFile();
    const content = await file.text();
  } else if (entry.kind === 'directory') {
    // Recursive traversal
  }
}
```

**Permissions:**
- Auto-granted in Electron (configured in `main.js:75-91`)
- Requires user permission in browser

---

### IndexedDB API

Database: `CodeRefExplorer`
Object Store: `directoryHandles`
Key Path: `id`

**Open Database:**
```javascript
function openDB() {
  return new Promise((resolve, reject) => {
    const request = indexedDB.open('CodeRefExplorer', 1);

    request.onupgradeneeded = (event) => {
      const db = event.target.result;
      if (!db.objectStoreNames.contains('directoryHandles')) {
        db.createObjectStore('directoryHandles', { keyPath: 'id' });
      }
    };

    request.onsuccess = () => resolve(request.result);
    request.onerror = () => reject(request.error);
  });
}
```

**Save Directory Handle:**
```javascript
async function saveDirectoryHandle(id, handle) {
  const db = await openDB();
  const tx = db.transaction('directoryHandles', 'readwrite');
  const store = tx.objectStore('directoryHandles');

  await store.put({ id, handle });
  return new Promise((resolve, reject) => {
    tx.oncomplete = resolve;
    tx.onerror = () => reject(tx.error);
  });
}
```

**Get Directory Handle:**
```javascript
async function getDirectoryHandle(id) {
  const db = await openDB();
  const tx = db.transaction('directoryHandles', 'readonly');
  const store = tx.objectStore('directoryHandles');

  return new Promise((resolve, reject) => {
    const request = store.get(id);
    request.onsuccess = () => resolve(request.result?.handle);
    request.onerror = () => reject(request.error);
  });
}
```

**Delete Directory Handle:**
```javascript
async function deleteDirectoryHandle(id) {
  const db = await openDB();
  const tx = db.transaction('directoryHandles', 'readwrite');
  const store = tx.objectStore('directoryHandles');

  await store.delete(id);
  return new Promise((resolve, reject) => {
    tx.oncomplete = resolve;
    tx.onerror = () => reject(tx.error);
  });
}
```

---

### LocalStorage API

**Theme Persistence:**
```javascript
// Save theme
localStorage.setItem('theme', 'dark');

// Load theme
const theme = localStorage.getItem('theme') || 'dark';
```

**Keys:**
- `theme` - Current theme (`'dark'` or `'light'`)

---

## Electron IPC

**Exposed in Preload (`preload.js:7-14`):**

```javascript
window.electron.platform
// Returns: 'win32', 'darwin', 'linux'

window.electron.versions
// Returns: {
//   node: '18.0.0',
//   chrome: '110.0.0',
//   electron: '28.0.0'
// }
```

**No other IPC channels exposed.** All file operations use File System Access API or HTTP API.

---

## Authentication & Security

**Current Implementation:** None

- No authentication required for HTTP API
- Server runs on localhost only (`127.0.0.1:8080`)
- CORS enabled with `Access-Control-Allow-Origin: *`
- Electron security:
  - `nodeIntegration: false`
  - `contextIsolation: true`
  - `webSecurity: false` (allows File System Access API)

**Security Notes:**
- Server is intended for local development only
- Do not expose server to network interfaces
- File System Access API requires user permission in browsers
- Electron auto-grants file system permissions

---

## Error Handling

### HTTP Status Codes

| Code | Meaning | Example |
|------|---------|---------|
| 200 | OK | Successful request |
| 400 | Bad Request | Invalid parameters or missing fields |
| 404 | Not Found | Resource does not exist |
| 500 | Internal Server Error | Server-side exception |

### Error Response Format

All errors return JSON with `error` field:

```json
{
  "error": "Error description here"
}
```

### Client-Side Error Handling

**Recommended Pattern:**
```javascript
try {
  const response = await fetch('http://localhost:8080/api/projects');

  if (!response.ok) {
    const error = await response.json();
    throw new Error(error.error || 'Request failed');
  }

  const data = await response.json();
  // Handle success

} catch (error) {
  console.error('API Error:', error.message);
  // Show user-friendly error message
}
```

---

## Rate Limiting

**Current Implementation:** None

Server has no rate limiting. All requests are processed immediately.

---

## Data Models

### Project Object

```typescript
interface Project {
  id: string;           // Unique identifier (UUID recommended)
  name: string;         // Display name
  path: string;         // Absolute path or '[Directory: Handle-UUID]'
}
```

### Tree Node

```typescript
interface TreeNode {
  name: string;         // File or folder name
  path: string;         // Absolute path
  type: 'file' | 'folder';
  children?: TreeNode[]; // Only for folders
}
```

### File Info

```typescript
interface FileInfo {
  content: string;      // UTF-8 content
  name: string;         // Basename
  size: number;         // Bytes
  modified: number;     // Unix timestamp
}
```

---

## Implementation References

**Server Implementation:** `server.py:15-214`
**File System Access:** `src/pages/coderef-explorer.html:464-876`
**IndexedDB:** `src/pages/coderef-explorer.html:464-518`
**Electron IPC:** `preload.js:7-14`

---

## AI Agent Notes

**For autonomous agents working with this codebase:**

1. **Adding new API endpoints**: Extend `CodeRefHandler` class in `server.py` with new `do_GET`, `do_POST`, or `do_DELETE` methods
2. **Modifying data models**: Update `projects.json` schema and validation in `handle_save_project` (line 73)
3. **Security considerations**: Server is localhost-only. Do not add network bindings without authentication
4. **Testing**: Use `curl` for API testing. Python server runs on port 8080.
5. **Browser compatibility**: File System Access API requires Chromium (Chrome/Edge). Not supported in Firefox/Safari.

---

_Generated with CodeRef foundation documentation system._
