# CodeRef Explorer - User Guide

Complete guide to installing, using, and mastering CodeRef Explorer.

---

## Table of Contents

1. [What is CodeRef Explorer?](#what-is-coderef-explorer)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [How It Works](#how-it-works)
5. [Getting Started](#getting-started)
6. [Core Workflows](#core-workflows)
7. [Best Practices](#best-practices)
8. [Troubleshooting](#troubleshooting)
9. [Quick Reference](#quick-reference)

---

## What is CodeRef Explorer?

CodeRef Explorer is a desktop application for browsing and managing coderef documentation across multiple projects. It combines:

- **File System Access API** - Direct browser access to folders (no uploads)
- **HTTP API** - Python server for file operations
- **Electron Desktop App** - Native OS integration
- **Industrial UI** - Dark-first design with light mode support

### Key Benefits

- **Offline-first** - No internet required after installation
- **Multi-project** - Manage unlimited projects simultaneously
- **Zero-dependency UI** - Fast, lightweight vanilla JavaScript
- **Cross-platform** - Windows, macOS, Linux support

---

## Prerequisites

### System Requirements

| Component | Requirement |
|-----------|-------------|
| Operating System | Windows 10+, macOS 10.13+, or Linux (Ubuntu 18.04+) |
| RAM | 2 GB minimum, 4 GB recommended |
| Disk Space | 200 MB for application + project sizes |
| Python | 3.6+ (bundled in installer) |

### Browser Requirements (Browser Mode)

- Chrome 86+
- Edge 86+
- Brave (Chromium-based)

**Not Supported:** Firefox, Safari (missing File System Access API)

---

## Installation

### Option 1: Desktop Installer (Recommended)

**Windows:**
1. Download `CodeRef Explorer Setup.exe` from releases
2. Run installer (may show Windows SmartScreen warning)
3. Click "More info" → "Run anyway"
4. Follow installation wizard
5. Launch from Start Menu or Desktop shortcut

**macOS:**
1. Download `CodeRef Explorer.dmg`
2. Open DMG file
3. Drag app to Applications folder
4. Right-click → Open (first launch only)
5. Grant permissions if prompted

**Linux:**
1. Download `coderef-explorer.AppImage`
2. Make executable: `chmod +x coderef-explorer.AppImage`
3. Run: `./coderef-explorer.AppImage`

### Option 2: Run from Source

**Prerequisites:** Node.js 16+, Python 3.6+

```bash
# Clone repository
git clone https://github.com/yourusername/coderef-explorer.git
cd coderef-explorer/web

# Install Node dependencies
npm install

# Start application
npm start
```

### Option 3: Browser Mode (No Electron)

**Prerequisites:** Python 3.6+

```bash
# Navigate to project
cd coderef-explorer/web

# Start Python server
python server.py

# Open browser
open http://localhost:8080/src/pages/coderef-explorer.html
```

---

## How It Works

### Architecture Overview

```
┌─────────────────────────────────────┐
│         Your Computer               │
│                                     │
│  ┌──────────────────────────────┐  │
│  │   Electron Desktop App        │  │
│  │                               │  │
│  │  ┌──────────┐  ┌───────────┐ │  │
│  │  │ Browser  │  │  Python   │ │  │
│  │  │ UI       │─▶│  Server   │ │  │
│  │  └─────┬────┘  └─────┬─────┘ │  │
│  └────────┼─────────────┼───────┘  │
│           │             │           │
│           ▼             ▼           │
│     ┌──────────┐  ┌──────────┐     │
│     │ IndexedDB│  │  Files   │     │
│     │ (handles)│  │ (projects)│    │
│     └──────────┘  └──────────┘     │
└─────────────────────────────────────┘
```

### Data Flow

1. **Electron** launches and starts Python server
2. **Browser UI** loads from `localhost:8080`
3. **User adds project** via File System Access API or path entry
4. **Directory handle** stored in IndexedDB (browser mode)
5. **Project metadata** saved to `projects.json` (server)
6. **File access** via direct handle or HTTP API fallback

---

## Getting Started

### First Launch

1. **Application opens** to project selector view
2. **No projects yet** - Empty state displayed
3. **Click `+` button** to add your first project

### Adding Your First Project

#### Method A: Browse Folder (Recommended)

1. Click **+** button in toolbar
2. Modal appears: "Add New Project"
3. Click **"Browse Folder"** button
4. File picker opens
5. Navigate to project folder (e.g., `C:\Users\name\my-project`)
6. Click **"Select Folder"**
7. Permission prompt appears (browser mode)
8. Click **"Allow"**
9. Project appears in dropdown with folder name
10. Folder tree loads automatically

**Advantages:**
- Direct browser access (faster)
- Permissions persist across sessions
- Works offline

**Disadvantages:**
- Requires Chromium-based browser
- Permission prompt on first access

---

#### Method B: Type Path

1. Click **+** button in toolbar
2. Modal appears: "Add New Project"
3. Enter **Project Name** (e.g., "My Awesome Project")
4. Enter **Project Path** (e.g., `/Users/name/projects/my-project`)
5. Click **"Add Project"**
6. Server validates path exists
7. Project appears in dropdown
8. Folder tree loads via HTTP API

**Advantages:**
- Works in any browser
- No permission prompts

**Disadvantages:**
- Requires server API
- Path must exist on disk

---

### Navigating Your Project

#### Folder Tree

```
📁 my-project/
├── 📁 src/
│   ├── 📁 components/
│   │   ├── 📄 Button.js
│   │   └── 📄 Header.js
│   └── 📄 index.js
├── 📁 docs/
│   └── 📄 README.md
└── 📄 package.json
```

**Actions:**
- **Click folder** → Expand/collapse
- **Click file** → View content in main panel
- **Hover** → Orange highlight

#### File Viewer

When you click a file:

1. **File loads** in main content area
2. **Header shows**:
   - File name
   - File size
   - Last modified date
   - Action buttons (copy, share)
3. **Content displays**:
   - JSON: Syntax highlighted
   - Markdown: Rendered HTML
   - Code: Monospace font
   - Text: Plain display

**File Actions:**
- 📋 **Copy Path** - Copies absolute path to clipboard
- 📋 **Copy Code** - Copies file content
- 🔗 **Share Link** - Generates shareable URL (browser mode)

---

### Switching Projects

1. Use **project dropdown** in sidebar
2. Select different project
3. Tree reloads for new project

**Note:** Only one project visible at a time

---

### Theme Toggle

1. Click **moon icon** in header
2. Theme switches: dark ↔ light
3. Preference saved to LocalStorage
4. Persists across app restarts

---

## Core Workflows

### Workflow 1: Daily Project Browsing

**Scenario:** You have 5 projects and need to check documentation daily

**Steps:**
1. Launch CodeRef Explorer
2. All 5 projects appear in dropdown (from previous sessions)
3. Select project from dropdown
4. Navigate folder tree to find doc
5. View file content
6. Switch to next project

**Time:** ~10 seconds per project

---

### Workflow 2: Adding New Projects in Bulk

**Scenario:** Onboarding 10 new projects

**Method A: Scripted (Advanced)**

Create `projects.json` manually:
```json
[
  {"id": "proj-1", "name": "Project 1", "path": "/path/to/proj1"},
  {"id": "proj-2", "name": "Project 2", "path": "/path/to/proj2"}
]
```

Place in app directory, restart app.

**Method B: UI (Beginner)**

1. Click `+` → Browse Folder → Add
2. Repeat for each project

**Time:** ~30 seconds per project (UI), ~5 minutes total (scripted)

---

### Workflow 3: Sharing Project Access

**Scenario:** Teammate needs access to same projects

**Option A: Share projects.json**

1. Locate `projects.json` in app directory
2. Send file to teammate
3. Teammate places in their app directory
4. Both see same project list

**Option B: Export Paths**

1. Open `projects.json`
2. Copy project paths
3. Share paths with teammate
4. Teammate adds manually

**Limitation:** File System Access API handles don't transfer (each user must grant permissions)

---

### Workflow 4: Removing Obsolete Projects

**Scenario:** 3 projects are archived and no longer needed

**Steps:**
1. Select project from dropdown
2. Click **trash icon**
3. Confirm removal
4. Project removed from list
5. Repeat for other projects

**Note:** This only removes from CodeRef Explorer. Files on disk are not deleted.

---

## Best Practices

### Do ✅

- **Use Browse Folder** for frequently accessed projects (faster)
- **Use Type Path** for one-time access or server mode
- **Name projects descriptively** (shows in dropdown)
- **Remove obsolete projects** to keep dropdown clean
- **Use dark mode** to reduce eye strain
- **Grant permissions** when prompted (File System Access API)

### Don't ❌

- **Don't delete `projects.json`** (loses all projects)
- **Don't move project folders** without updating paths
- **Don't use Firefox/Safari** (missing API support)
- **Don't expose server to network** (security risk)
- **Don't manually edit IndexedDB** (can corrupt handles)

### Tips 💡

- **Organize projects by type** - Use descriptive names like "Docs-ProjectX"
- **Check permissions** - If tree won't load, re-add project
- **Restart for server changes** - Changes to `server.py` require restart
- **Use DevTools for debugging** - Uncomment line 66 in `main.js`
- **Backup projects.json** - Keep a copy in safe location

---

## Troubleshooting

### Problem: Python Server Won't Start

**Symptoms:**
- Blank window
- "Cannot connect to server" error
- Window opens but no content loads

**Solutions:**

1. **Check Python installed:**
   ```bash
   python --version
   # Should show: Python 3.6+
   ```

2. **Check port availability:**
   ```bash
   netstat -an | grep 8080
   # Should be empty (port not in use)
   ```

3. **Start server manually:**
   ```bash
   cd /path/to/coderef-explorer/web
   python server.py
   # Should show: Server running at http://localhost:8080/
   ```

4. **Check firewall:**
   - Allow Python through firewall
   - Allow Electron through firewall

---

### Problem: Permission Denied (File System Access API)

**Symptoms:**
- Toast notification: "Permission denied"
- Folder tree won't load
- Files won't open

**Solutions:**

1. **Remove and re-add project:**
   - Click trash icon
   - Click `+` → Browse Folder
   - Grant permission when prompted

2. **Check browser permissions:**
   - Chrome: `chrome://settings/content/fileSystem`
   - Edge: `edge://settings/content/fileSystem`
   - Verify origin has access

3. **Try Type Path method:**
   - Use absolute path instead of handle
   - Bypasses permission system

---

### Problem: Projects Not Loading After Restart

**Symptoms:**
- Empty project dropdown
- "No projects" message
- Projects disappeared

**Solutions:**

1. **Check projects.json exists:**
   ```bash
   ls projects.json
   # Should exist in app directory
   ```

2. **Validate JSON:**
   ```bash
   python -m json.tool projects.json
   # Should pretty-print JSON
   # If error: JSON is corrupted
   ```

3. **Restore from backup:**
   - Replace corrupted `projects.json` with backup
   - Or re-add projects manually

4. **Check file permissions:**
   - Ensure `projects.json` is readable
   - Check file owner and permissions

---

### Problem: File Content Not Displaying

**Symptoms:**
- File clicks do nothing
- Content area stays blank
- Loading indicator spins forever

**Solutions:**

1. **Check file permissions:**
   - Ensure file is readable
   - Try opening file in text editor

2. **Check file size:**
   - Large files (>10MB) may be slow
   - Try smaller test file

3. **Check browser console:**
   - Open DevTools (F12)
   - Check Console tab for errors
   - Report errors to support

4. **Try different access mode:**
   - If using handle, try Type Path
   - If using Type Path, try Browse Folder

---

### Problem: DevTools Won't Open

**Symptom:**
- F12 does nothing
- Right-click menu has no "Inspect"

**Solution:**

1. Open `main.js`
2. Find line 66:
   ```javascript
   // mainWindow.webContents.openDevTools();
   ```
3. Uncomment:
   ```javascript
   mainWindow.webContents.openDevTools();
   ```
4. Restart app: `npm start`

---

## Quick Reference

### Project Management

| Action | Method |
|--------|--------|
| Add project | Click `+` → Browse Folder or Type Path |
| Switch project | Use dropdown in sidebar |
| Remove project | Select project → Click trash icon |
| View project list | Open `projects.json` in text editor |

### Navigation

| Action | Method |
|--------|--------|
| Expand folder | Click folder name or chevron |
| View file | Click file name |
| Copy path | Click copy icon in file header |
| Copy content | Click copy icon in code block |

### Theme

| Action | Method |
|--------|--------|
| Toggle theme | Click moon icon |
| Set default | Edit LocalStorage: `theme` key |

### Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| _None_ | No shortcuts in v1.0 |

_Roadmap: v1.1 will add keyboard shortcuts_

### File Support

| Format | Rendering |
|--------|-----------|
| `.json` | Syntax highlighted |
| `.md` | Rendered HTML (marked.js) |
| `.js`, `.py`, `.css` | Monospace, syntax highlight |
| `.txt` | Plain text |

### Storage Locations

| Data | Location |
|------|----------|
| Projects | `projects.json` (app directory) |
| Directory handles | IndexedDB (`CodeRefExplorer` database) |
| Theme | LocalStorage (`theme` key) |

---

## Next Steps

Now that you've completed the user guide:

1. **Add your projects** - Start with 2-3 key projects
2. **Explore the UI** - Click around, try features
3. **Read FEATURES.md** - Learn about advanced capabilities
4. **Check quickref.md** - Keep handy for fast lookups
5. **Join community** - Report issues, request features

---

**Questions or Issues?**

- GitHub Issues: https://github.com/yourusername/coderef-explorer/issues
- Documentation: See `coderef/foundation-docs/` for technical details

---

_Version: 1.0.0 | Last Updated: 2025-12-28_
