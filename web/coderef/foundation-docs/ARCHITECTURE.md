# System Architecture

**Version:** 1.0.0
**Last Updated:** 2025-12-28

---

## Overview

CodeRef Explorer is a hybrid desktop/web application for browsing and managing coderef documentation. The architecture combines:

- **Electron** - Desktop app wrapper with native OS integration
- **Python HTTP Server** - Backend API for file system operations
- **Vanilla JavaScript** - Frontend with zero framework dependencies
- **File System Access API** - Browser-native directory access (Chromium)

The system prioritizes **simplicity**, **portability**, and **offline-first** functionality.

---

## System Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                     Electron Process                         │
│  ┌──────────────┐                      ┌─────────────────┐  │
│  │  Main        │                      │  Renderer       │  │
│  │  Process     │─────────IPC─────────▶│  Process        │  │
│  │  (Node.js)   │                      │  (Chromium)     │  │
│  └──────┬───────┘                      └────────┬────────┘  │
│         │                                       │            │
│         │ spawn                                 │            │
│         ▼                                       │            │
│  ┌──────────────────────┐                      │            │
│  │  Python HTTP Server  │◀─────HTTP────────────┘            │
│  │  (localhost:8080)    │                                   │
│  └──────────┬───────────┘                                   │
│             │                                                │
└─────────────┼────────────────────────────────────────────────┘
              │
              ▼
       ┌──────────────┐
       │  File System │
       │  (projects)  │
       └──────────────┘
```

---

## Technology Stack

### Frontend

| Technology | Version | Purpose |
|------------|---------|---------|
| HTML5 | - | Semantic markup, File System Access API |
| CSS3 | - | Custom "Industrial UI" design system |
| JavaScript (ES6+) | - | Client-side logic, no transpilation |
| Material Symbols | - | Icon library (Google CDN) |
| Marked.js | 4.x | Markdown rendering (optional) |

**Browser Requirements:**
- Chromium-based (Chrome, Edge, Brave)
- File System Access API support
- IndexedDB support

---

### Backend

| Technology | Version | Purpose |
|------------|---------|---------|
| Python | 3.x | HTTP server |
| http.server | stdlib | HTTP request handling |
| json | stdlib | Data serialization |
| pathlib | stdlib | File system operations |

**Python Requirements:** 3.6+ (uses f-strings, pathlib)

---

### Desktop

| Technology | Version | Purpose |
|------------|---------|---------|
| Electron | 28.x | Desktop app wrapper |
| electron-builder | 24.x | Windows/macOS/Linux builds |

**Node.js Requirements:** 16+ (for Electron development)

---

## Architecture Patterns

### 1. Client-Server Hybrid

```
┌───────────────┐
│  Browser UI   │
└───────┬───────┘
        │
        ├─────┐
        │     │
        ▼     ▼
   ┌─────┐  ┌──────────────┐
   │ FS  │  │ HTTP Server  │
   │ API │  │ (Python)     │
   └─────┘  └──────────────┘
```

**Two Modes:**
- **File System Access API** - Direct browser access (requires permissions)
- **HTTP API** - Server-mediated access (fallback for typed paths)

**Benefits:**
- Offline-capable (no external dependencies)
- Flexible deployment (browser or Electron)
- Graceful degradation

---

### 2. Event-Driven UI

```javascript
// No framework - vanilla event handlers
document.getElementById('project-select').onchange = (e) => {
  changeProject(e.target.value);
};

function changeProject(projectId) {
  // 1. Update state
  currentProject = projects.find(p => p.id === projectId);

  // 2. Fetch data
  const dirHandle = await getDirectoryHandle(projectId);

  // 3. Render UI
  await buildTreeFromDirectoryHandle(dirHandle);
}
```

**Pattern:**
- Direct DOM manipulation (no virtual DOM)
- Async/await for data fetching
- Minimal state management (in-memory JavaScript variables)

---

### 3. Layered Data Access

```
┌─────────────────────────┐
│  UI Components          │
├─────────────────────────┤
│  Data Access Layer      │
│  - loadProjects()       │
│  - saveProject()        │
│  - getDirectoryHandle() │
├─────────────────────────┤
│  Storage Layer          │
│  - HTTP API             │
│  - IndexedDB            │
│  - LocalStorage         │
└─────────────────────────┘
```

**Implementation:** `src/pages/coderef-explorer.html:464-876`

---

## Data Flow

### Project Loading Sequence

```
1. Page Load
   └─▶ initTheme() - Restore theme preference
   └─▶ loadProjects() - Fetch from HTTP API

2. loadProjects()
   └─▶ GET /api/projects
   └─▶ Store in memory: projects = [...]
   └─▶ renderProjectSelector()
   └─▶ changeProject(projects[0].id)

3. changeProject(id)
   └─▶ getDirectoryHandle(id) from IndexedDB
   └─▶ If handle exists:
       └─▶ Check permissions
       └─▶ buildTreeFromDirectoryHandle()
   └─▶ Else if path exists:
       └─▶ GET /api/tree?path=...
       └─▶ renderServerTree()

4. buildTreeFromDirectoryHandle(handle)
   └─▶ Recursive directory traversal
   └─▶ Render tree nodes
   └─▶ Attach click handlers

5. User clicks file
   └─▶ loadFileFromHandle() or loadServerFile()
   └─▶ displayFileContent()
```

---

### Adding Project Sequence

```
1. User clicks "Add Project" button
   └─▶ showAddProjectDialog()

2. User chooses method:
   ├─▶ Option A: Browse Folder (File System Access API)
   │   └─▶ window.showDirectoryPicker()
   │   └─▶ Save handle to IndexedDB
   │   └─▶ POST /api/projects with path = "[Directory: {name}]"
   │
   └─▶ Option B: Type Path (HTTP API)
       └─▶ User enters absolute path
       └─▶ POST /api/projects with path = "/absolute/path"
       └─▶ Server validates path exists

3. confirmAddProject()
   └─▶ Validate inputs
   └─▶ Generate unique ID
   └─▶ Save to server + IndexedDB
   └─▶ Reload projects
   └─▶ Close modal
```

**Implementation:** `src/pages/coderef-explorer.html:719-843`

---

## Directory Structure

```
web/
├── index.html                    # Dashboard page
├── main.js                       # Electron main process
├── preload.js                    # Electron preload script
├── server.py                     # Python HTTP server
├── package.json                  # Node.js dependencies
├── projects.json                 # Project metadata (runtime)
│
├── src/
│   ├── css/
│   │   └── main.css             # Industrial UI design system
│   │
│   └── pages/
│       ├── coderef-explorer.html         # Main file explorer
│       └── coderef-explorer.backup.html  # Backup/reference
│
├── mock-data/                    # (Optional) Test data
│
├── coderef/
│   └── foundation-docs/          # Generated documentation
│       ├── API.md
│       ├── SCHEMA.md
│       ├── COMPONENTS.md
│       └── ARCHITECTURE.md (this file)
│
└── node_modules/                 # NPM dependencies (dev only)
```

---

## Process Lifecycle

### Electron Application Startup

```javascript
// 1. App ready
app.whenReady().then(() => {
  // 2. Configure File System Access API permissions
  session.defaultSession.setPermissionRequestHandler(...);

  // 3. Start Python server
  startPythonServer();

  // 4. Wait 2 seconds for server to start
  setTimeout(() => {
    // 5. Create window and load UI
    createWindow();
    mainWindow.loadURL('http://localhost:8080/src/pages/coderef-explorer.html');
  }, 2000);
});

// 6. Before quit: Stop Python server
app.on('before-quit', () => {
  stopPythonServer();
});
```

**Implementation:** `main.js:73-115`

---

### Python Server Lifecycle

```python
# 1. Spawn process from Electron
pythonProcess = spawn('python', ['server.py'])

# 2. Server binds to localhost:8080
with socketserver.TCPServer(("", 8080), CodeRefHandler) as httpd:
    httpd.serve_forever()

# 3. Handle requests until killed
# 4. On app quit: pythonProcess.kill()
```

**Implementation:** `server.py:210-213`, `main.js:13-40`

---

## Security Architecture

### Electron Security

```javascript
// Preload script (sandboxed context)
webPreferences: {
  preload: path.join(__dirname, 'preload.js'),
  nodeIntegration: false,        // No Node.js in renderer
  contextIsolation: true,        // Separate contexts
  webSecurity: false,            // Allow File System Access API
  allowRunningInsecureContent: true
}
```

**Security Model:**
- Renderer process has no Node.js access
- IPC communication via `contextBridge` only
- Limited API surface: platform detection, version info

**Implementation:** `main.js:46-51`

---

### HTTP Server Security

**Current:**
- Listens on `localhost` only (127.0.0.1:8080)
- No authentication
- CORS enabled (`Access-Control-Allow-Origin: *`)

**Risks:**
- No protection if malicious site accesses `localhost:8080`
- File system paths exposed in API responses

**Mitigations:**
- Intended for local development only
- Do not expose to network interfaces
- Consider CORS origin whitelist for production

**Implementation:** `server.py:54-58`, `server.py:202-208`

---

### File System Access API Security

**Browser Security Model:**
- User must explicitly grant permission via picker dialog
- Permissions are per-origin, per-directory
- Permissions persist across sessions (stored in IndexedDB)
- Permissions can be revoked by user

**Electron Override:**
```javascript
// Auto-grant all file system permissions
session.defaultSession.setPermissionRequestHandler((webContents, permission, callback) => {
  if (permission === 'fileSystem') {
    callback(true);  // Always allow
  }
});
```

**Rationale:** Desktop app has full file system access anyway

**Implementation:** `main.js:75-91`

---

## Build & Deployment

### Development Mode

```bash
# 1. Install dependencies
npm install

# 2. Start Electron (auto-starts Python server)
npm start
```

**Requirements:**
- Node.js 16+
- Python 3.6+
- Windows/macOS/Linux

---

### Production Build

```bash
# Build for Windows
npm run build:win

# Output: dist/CodeRef Explorer Setup.exe
```

**electron-builder Configuration:**
```json
{
  "build": {
    "appId": "com.coderef.explorer",
    "productName": "CodeRef Explorer",
    "files": [
      "main.js",
      "preload.js",
      "server.py",
      "src/**/*",
      "mock-data/**/*"
    ],
    "win": {
      "target": "nsis",
      "icon": "icon.ico"
    }
  }
}
```

**Output:**
- Single-file installer (NSIS)
- Bundles Python script + Node.js + Chromium
- No external dependencies required

**Implementation:** `package.json:22-39`

---

### Deployment Options

| Mode | Use Case | Setup |
|------|----------|-------|
| **Electron Desktop** | End users, offline access | Download installer, run |
| **Standalone Browser** | Development, testing | `python server.py` + open Chrome |
| **Server Mode** | Team access, shared projects | Deploy server.py to LAN, access via browser |

---

## Performance Considerations

### File System Traversal

```javascript
// Recursive directory traversal
async function renderDirectoryNode(dirHandle, parentElement) {
  const entries = [];
  for await (const entry of dirHandle.values()) {
    entries.push(entry);
  }

  // Sort: folders first, then files
  entries.sort((a, b) => {
    if (a.kind !== b.kind) {
      return a.kind === 'directory' ? -1 : 1;
    }
    return a.name.localeCompare(b.name);
  });

  // Render recursively
  for (const entry of entries) {
    if (entry.kind === 'directory') {
      await renderDirectoryNode(entry, childrenDiv);
    }
  }
}
```

**Performance:**
- O(n) where n = total files + folders
- Async iteration prevents UI blocking
- May be slow for large projects (10,000+ files)

**Optimization Opportunities:**
- Lazy loading (only expand visible folders)
- Virtual scrolling for file lists
- Web Workers for heavy processing

**Implementation:** `src/pages/coderef-explorer.html:636-695`

---

### IndexedDB Caching

- **Read:** O(1) for key-based lookups
- **Write:** Asynchronous, non-blocking
- **Storage:** 50% of available disk (typical browser limit)

**Bottleneck:** Permission re-validation on each page load

---

### HTTP API

- **Small projects (<100 files):** Negligible overhead
- **Large projects (1000+ files):** Tree building may take 1-2 seconds
- **Optimization:** Cache tree structure in memory or IndexedDB

---

## Error Handling

### Global Error Strategy

```javascript
try {
  const response = await fetch('/api/projects');
  if (!response.ok) {
    throw new Error(`HTTP ${response.status}`);
  }
  const data = await response.json();
} catch (error) {
  console.error('Error loading projects:', error);
  showToast('Error loading projects');
}
```

**Patterns:**
- Try/catch for async operations
- User-friendly error messages (toast notifications)
- Log full error to console for debugging

**Implementation:** Throughout `coderef-explorer.html`

---

### Server Error Handling

```python
try:
    # Perform operation
    content = f.read()
    self.send_json_response({'content': content})
except Exception as e:
    self.send_error(500, f"Error reading file: {str(e)}")
```

**Patterns:**
- Broad exception catching (simplicity over specificity)
- Descriptive error messages
- HTTP status codes (400, 404, 500)

**Implementation:** `server.py` (throughout)

---

## Extensibility Points

### Adding New API Endpoints

1. Add handler method to `CodeRefHandler` class in `server.py`
2. Route in `do_GET`, `do_POST`, or `do_DELETE`
3. Update `API.md` documentation

**Example:**
```python
def do_GET(self):
    if parsed.path == '/api/search':
        self.handle_search_request(parsed)
    else:
        super().do_GET()

def handle_search_request(self, parsed):
    query = parse_qs(parsed.query).get('q', [''])[0]
    results = perform_search(query)
    self.send_json_response(results)
```

---

### Adding New UI Components

1. Define styles in `src/css/main.css`
2. Follow naming convention: `.industrial-component-variant`
3. Use CSS variables for theming
4. Test in dark + light modes
5. Update `COMPONENTS.md` documentation

---

### Integrating External Tools

**File preview:** Add file type handlers in `displayFileContent()`
```javascript
if (fileName.endsWith('.md')) {
  contentDiv.innerHTML = marked.parse(content);
} else if (fileName.endsWith('.pdf')) {
  // Add PDF viewer
}
```

**Code editor:** Integrate Monaco Editor or CodeMirror
```html
<script src="monaco-editor.js"></script>
<script>
  const editor = monaco.editor.create(document.getElementById('editor'), {
    value: fileContent,
    language: 'javascript'
  });
</script>
```

---

## Testing Strategy

### Manual Testing Checklist

- [ ] Add project via File System Access API
- [ ] Add project via manual path entry
- [ ] Navigate folder tree
- [ ] View file content
- [ ] Remove project
- [ ] Theme toggle (dark ↔ light)
- [ ] Permission denied handling
- [ ] Invalid path error handling

### Automated Testing (Future)

**Recommended:**
- **Playwright** - E2E testing for Electron app
- **pytest** - Python server API testing
- **Jest** - JavaScript unit testing

---

## Deployment Checklist

- [ ] Update version in `package.json`
- [ ] Test on Windows/macOS/Linux
- [ ] Verify Python server starts correctly
- [ ] Check File System Access API permissions
- [ ] Build installer: `npm run build:win`
- [ ] Test installer on clean machine
- [ ] Sign executable (Windows: Authenticode, macOS: notarization)
- [ ] Upload to release distribution

---

## AI Agent Notes

**For autonomous agents working with this architecture:**

1. **Modifying main process:**
   - Changes to `main.js` require Electron restart
   - Test File System Access API permissions thoroughly
   - Ensure Python server cleanup on exit

2. **Server changes:**
   - Restart required for server.py changes
   - Validate all file paths before access
   - Test CORS handling for new endpoints

3. **Frontend changes:**
   - No build step - edit HTML/CSS/JS directly
   - Hard refresh (Ctrl+Shift+R) to clear cache
   - Test in both File System API and HTTP API modes

4. **Data persistence:**
   - projects.json survives app restarts
   - IndexedDB handles survive browser restarts
   - LocalStorage survives both

---

_Generated with CodeRef foundation documentation system._
