# CodeRef Explorer

**Desktop application for browsing and managing coderef documentation**

A lightweight, offline-first file explorer built with Electron, Python, and vanilla JavaScript. Browse project folders with a modern industrial UI design.

[![Version](https://img.shields.io/badge/version-1.0.0-orange.svg)](package.json)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Electron](https://img.shields.io/badge/electron-28.x-47848f.svg)](https://www.electronjs.org/)
[![Python](https://img.shields.io/badge/python-3.6+-3776ab.svg)](https://www.python.org/)

---

## Features

### Core Functionality

- **Dual Access Modes**
  - File System Access API for direct browser access (Chromium-based)
  - HTTP API fallback for typed paths and older browsers

- **Project Management**
  - Add multiple projects
  - Persistent project list (survives app restarts)
  - Quick project switcher

- **File Explorer**
  - Recursive folder tree navigation
  - Syntax-highlighted file viewer
  - JSON pretty-printing with color syntax
  - Markdown rendering support

- **Industrial UI Design**
  - Dark mode by default with light mode toggle
  - Responsive layout (desktop + mobile)
  - Zero-dependency CSS framework
  - Material Symbols icons

### Technical Features

- Offline-capable (no internet required after installation)
- IndexedDB for persistent File System Access API handles
- LocalStorage for user preferences
- Cross-platform (Windows, macOS, Linux)

---

## Quick Start

### Prerequisites

- **Node.js** 16+ (for development)
- **Python** 3.6+ (bundled in production builds)
- **Chromium-based browser** (Chrome, Edge, Brave) for File System Access API

### Installation

**Option 1: Download Installer (Recommended)**

1. Download latest release: `CodeRef Explorer Setup.exe`
2. Run installer
3. Launch CodeRef Explorer

**Option 2: Run from Source**

```bash
# Clone repository
git clone https://github.com/yourusername/coderef-explorer.git
cd coderef-explorer/web

# Install dependencies
npm install

# Start application
npm start
```

**Option 3: Browser Mode (No Electron)**

```bash
# Start Python server
python server.py

# Open browser
open http://localhost:8080/src/pages/coderef-explorer.html
```

---

## Usage

### Adding Your First Project

1. Click the **+** button in the top toolbar
2. Choose one of two methods:

   **Method A: Browse Folder (Recommended)**
   - Click "Browse Folder"
   - Select project directory in file picker
   - Project appears in dropdown

   **Method B: Type Path**
   - Enter absolute path (e.g., `/Users/name/project`)
   - Enter project name
   - Click "Add Project"

3. Project loads automatically

### Navigating Files

- Click folders to expand/collapse
- Click files to view content
- Use project dropdown to switch between projects

### Theme Toggle

- Click moon icon in header to toggle dark/light mode
- Preference persists across sessions

### Removing Projects

- Select project from dropdown
- Click trash icon
- Confirm removal

---

## Project Structure

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
│       └── coderef-explorer.html # Main file explorer
│
└── coderef/
    └── foundation-docs/          # Generated documentation
        ├── API.md               # API reference
        ├── SCHEMA.md            # Data models
        ├── COMPONENTS.md        # UI components
        └── ARCHITECTURE.md      # System architecture
```

---

## Configuration

### File System Access API Permissions

**Browser (Chrome/Edge):**
- Permissions requested on first folder access
- Granted permissions persist in IndexedDB
- Revoke via browser settings: `chrome://settings/content/fileSystem`

**Electron:**
- Auto-granted in `main.js` (lines 75-91)
- No user prompts required

### Python Server Port

Default: `8080`

To change:
```python
# server.py, line 12
PORT = 8080  # Change to desired port
```

```javascript
// main.js, line 62
mainWindow.loadURL('http://localhost:8080/...');  # Update to match
```

### Theme

Default: Dark mode

Persist across sessions via LocalStorage:
```javascript
localStorage.setItem('theme', 'light');  // or 'dark'
```

---

## Development

### Running in Development Mode

```bash
npm start
```

**Workflow:**
1. Electron launches
2. Python server starts on port 8080
3. Chromium window loads UI from `localhost:8080`
4. Edit HTML/CSS/JS files
5. Hard refresh (Ctrl+Shift+R) to see changes

**Note:** Changes to `main.js` or `server.py` require full restart

### Building for Production

```bash
# Windows installer
npm run build:win

# Output: dist/CodeRef Explorer Setup.exe
```

**Build Configuration:** `package.json:22-39`

### Development Tools

**Open DevTools:**
```javascript
// Uncomment in main.js, line 66
mainWindow.webContents.openDevTools();
```

**Inspect IndexedDB:**
1. Open DevTools
2. Application tab → Storage → IndexedDB → CodeRefExplorer

**View LocalStorage:**
1. Open DevTools
2. Application tab → Storage → Local Storage

---

## API Reference

### HTTP API

**Base URL:** `http://localhost:8080`

#### Get Projects
```http
GET /api/projects
```

#### Save Project
```http
POST /api/projects
Content-Type: application/json

{
  "id": "project-123",
  "name": "My Project",
  "path": "/path/to/project"
}
```

#### Delete Project
```http
DELETE /api/projects/{id}
```

#### Get Folder Tree
```http
GET /api/tree?path=/absolute/path
```

#### Get File Content
```http
GET /api/file?path=/absolute/path/file.txt
```

**Full API documentation:** [coderef/foundation-docs/API.md](coderef/foundation-docs/API.md)

---

## Architecture

### System Overview

```
┌─────────────────────────────┐
│   Electron Desktop App      │
│  ┌─────────┐   ┌──────────┐ │
│  │ Main    │   │ Renderer │ │
│  │ Process │──▶│ Process  │ │
│  └────┬────┘   └─────┬────┘ │
│       │              │       │
│       ▼              ▼       │
│  ┌─────────┐   ┌──────────┐ │
│  │ Python  │   │ Browser  │ │
│  │ Server  │◀──│ APIs     │ │
│  └─────────┘   └──────────┘ │
└─────────────────────────────┘
```

**Key Technologies:**
- **Frontend:** Vanilla JS, HTML5, CSS3
- **Backend:** Python HTTP server (stdlib)
- **Desktop:** Electron 28.x
- **Storage:** IndexedDB, LocalStorage, JSON files

**Full architecture documentation:** [coderef/foundation-docs/ARCHITECTURE.md](coderef/foundation-docs/ARCHITECTURE.md)

---

## Data Schema

### Project Object

```json
{
  "id": "string (unique)",
  "name": "string (display name)",
  "path": "string (absolute path or handle token)"
}
```

### Storage Locations

| Data | Storage | Persistence |
|------|---------|-------------|
| Projects | `projects.json` | App restarts |
| Directory handles | IndexedDB (`CodeRefExplorer`) | Browser restarts |
| Theme | LocalStorage (`theme`) | Forever |

**Full schema documentation:** [coderef/foundation-docs/SCHEMA.md](coderef/foundation-docs/SCHEMA.md)

---

## UI Components

### Industrial Design System

**Color Palette:**
- Accent: #ff6b00 (Orange)
- Background: #0c0c0e (Dark) / #ffffff (Light)
- Panels: #141416 (Dark) / #f5f5f5 (Light)

**Typography:**
- Display: Chakra Petch (sans-serif)
- Monospace: JetBrains Mono

**Components:**
- Buttons (primary, secondary, small)
- Panels/Cards
- Inputs
- Tables
- Alerts (success, error, warning, info)
- Modals
- Tree view
- Toast notifications

**Full component documentation:** [coderef/foundation-docs/COMPONENTS.md](coderef/foundation-docs/COMPONENTS.md)

---

## Troubleshooting

### Python Server Won't Start

**Symptom:** Blank window or "Cannot connect" error

**Solution:**
```bash
# Check if Python is installed
python --version

# Check if port 8080 is available
netstat -an | grep 8080

# Manually start server
python server.py
```

### Permission Denied (File System Access API)

**Symptom:** "Permission denied" toast notification

**Solution:**
1. Remove project
2. Re-add project via "Browse Folder" method
3. Grant permission when prompted

### Projects Not Loading After Restart

**Symptom:** Empty project list after app restart

**Solution:**
- Check if `projects.json` exists in root directory
- Verify JSON is valid: `python -m json.tool projects.json`
- If corrupted, delete and re-add projects

### DevTools Not Opening

**Solution:**
```javascript
// Uncomment in main.js, line 66
mainWindow.webContents.openDevTools();
```

Then restart app: `npm start`

---

## Security

### Current Security Posture

- HTTP server listens on `localhost` only (not exposed to network)
- No authentication (intended for local use)
- Electron renderer has no Node.js access (context isolation enabled)
- File System Access API requires user permission (browser mode)

### Recommendations for Production

- Add authentication to HTTP API
- Implement CORS origin whitelist
- Sign executables (Windows: Authenticode, macOS: notarization)
- Consider HTTPS for sensitive projects

---

## Contributing

Contributions welcome! Please follow these guidelines:

1. **Fork repository**
2. **Create feature branch:** `git checkout -b feature/my-feature`
3. **Make changes**
4. **Test thoroughly**
   - Add project via both methods
   - Navigate folder tree
   - Toggle theme
   - Test on Windows + macOS
5. **Commit:** `git commit -m "Add feature: my-feature"`
6. **Push:** `git push origin feature/my-feature`
7. **Open Pull Request**

### Code Style

- **JavaScript:** ES6+, no semicolons optional
- **CSS:** BEM-like naming, CSS variables for theming
- **Python:** PEP 8 style guide
- **HTML:** Semantic HTML5 elements

### Testing Checklist

- [ ] Dark mode works
- [ ] Light mode works
- [ ] File System Access API mode works
- [ ] HTTP API fallback works
- [ ] Projects persist across restarts
- [ ] Permissions re-validate correctly

---

## Roadmap

### Version 1.1

- [ ] Search within project files
- [ ] File type filters (e.g., show only `.md` files)
- [ ] Recent files list
- [ ] Keyboard shortcuts

### Version 2.0

- [ ] Code editor integration (Monaco Editor)
- [ ] Multi-tab file viewing
- [ ] Git integration (show modified files)
- [ ] Plugin system

---

## License

MIT License - see [LICENSE](LICENSE) file for details

---

## Links

### Documentation

- [API Reference](coderef/foundation-docs/API.md) - HTTP endpoints, browser APIs
- [Data Schema](coderef/foundation-docs/SCHEMA.md) - Data models and storage
- [UI Components](coderef/foundation-docs/COMPONENTS.md) - Design system
- [Architecture](coderef/foundation-docs/ARCHITECTURE.md) - System design

### Resources

- [Electron Documentation](https://www.electronjs.org/docs)
- [File System Access API](https://developer.mozilla.org/en-US/docs/Web/API/File_System_Access_API)
- [Material Symbols](https://fonts.google.com/icons)
- [Chakra Petch Font](https://fonts.google.com/specimen/Chakra+Petch)

---

## Credits

Built with:
- [Electron](https://www.electronjs.org/)
- [Python](https://www.python.org/)
- [Material Symbols](https://fonts.google.com/icons)
- [Marked.js](https://marked.js.org/) (Markdown rendering)

Design inspired by industrial control systems and brutalist UI.

---

**Version:** 1.0.0
**Last Updated:** 2025-12-28
**Author:** CodeRef Team

---

_For questions, issues, or feature requests, please open an issue on GitHub._
