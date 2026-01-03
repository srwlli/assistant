# CodeRef Explorer - Quick Reference

Fast scannable reference for common tasks and commands.

---

## Installation

```bash
# Windows
Download: CodeRef Explorer Setup.exe
Run installer → Follow wizard → Launch

# macOS
Download: CodeRef Explorer.dmg
Open DMG → Drag to Applications → Right-click → Open

# Linux
Download: coderef-explorer.AppImage
chmod +x coderef-explorer.AppImage
./coderef-explorer.AppImage

# From Source
git clone repo → npm install → npm start
```

---

## Quick Start

```
1. Launch app
2. Click + button
3. Browse Folder or Type Path
4. Click file to view
```

---

## Project Management

### Add Project (Browser Method)

```
1. Click + button
2. Click "Browse Folder"
3. Select directory in picker
4. Grant permission → Done
```

**Result:** Direct file access, faster performance

---

### Add Project (Path Method)

```
1. Click + button
2. Enter project name
3. Enter absolute path: /path/to/project
4. Click "Add Project"
```

**Result:** HTTP API access, works in any browser

---

### Switch Projects

```
Use dropdown in sidebar
↓
Select project name
↓
Tree reloads automatically
```

---

### Remove Project

```
1. Select project from dropdown
2. Click trash icon (🗑️)
3. Confirm removal
```

**Note:** Files on disk not deleted

---

## Navigation

### Folder Tree

```
📁 Folder (collapsed)  → Click to expand
📂 Folder (expanded)   → Click to collapse
📄 File                → Click to view content
```

**Hover:** Orange highlight
**Active:** Orange background + left border

---

### File Viewer

**View file:**
```
Click filename in tree
↓
Content displays in main panel
```

**Metadata shown:**
- File name
- File size (human-readable)
- Last modified (timestamp)
- Absolute path

---

## File Actions

### Copy Path

```
Click 📋 icon in file header
↓
Absolute path copied to clipboard
```

**Example:** `/Users/name/project/src/index.js`

---

### Copy Code

```
Click copy icon in code block
↓
File content copied to clipboard
```

**Preserves formatting**

---

### Share Link (Future)

```
Click 🔗 icon
↓
Shareable URL generated
```

**Status:** Roadmap v1.1

---

## Theme

### Toggle Theme

```
Click moon icon in header
↓
Theme switches: dark ↔ light
```

**Persistence:** Saved to LocalStorage

---

### Default Theme

```javascript
// Set via LocalStorage
localStorage.setItem('theme', 'dark');  // or 'light'
```

---

## File Support

| Extension | Rendering | Features |
|-----------|-----------|----------|
| `.json` | Syntax highlighted | Color coding, indentation |
| `.md` | Rendered HTML | marked.js, clickable links |
| `.js`, `.py` | Syntax highlighted | Monospace, basic colors |
| `.css`, `.html` | Syntax highlighted | Monospace |
| `.txt` | Plain text | Monospace |
| Binary | ❌ Not supported | Shows error message |

---

## Keyboard Shortcuts

**Current:** None

**Roadmap v1.1:**
- `Ctrl+P` - File finder
- `Ctrl+F` - Search in file
- `Ctrl+B` - Toggle sidebar
- `Ctrl+,` - Settings
- `Esc` - Close modal

---

## API Endpoints

### Projects

**List all projects:**
```http
GET /api/projects
```

**Response:**
```json
[
  {"id": "proj-1", "name": "My Project", "path": "/path/to/project"}
]
```

---

**Save project:**
```http
POST /api/projects
Content-Type: application/json

{"id": "proj-1", "name": "My Project", "path": "/path/to/project"}
```

**Response:**
```json
{"success": true, "project": {...}}
```

---

**Delete project:**
```http
DELETE /api/projects/{id}
```

**Response:**
```json
{"success": true, "deleted": "proj-1"}
```

---

### Files

**Get folder tree:**
```http
GET /api/tree?path=/absolute/path
```

**Response:**
```json
{
  "name": "project",
  "path": "/absolute/path",
  "type": "folder",
  "children": [...]
}
```

---

**Get file content:**
```http
GET /api/file?path=/absolute/path/file.txt
```

**Response:**
```json
{
  "content": "File content here",
  "name": "file.txt",
  "size": 1024,
  "modified": 1703721600.0
}
```

---

## Storage Locations

| Data | Storage | Path |
|------|---------|------|
| Projects | File system | `./projects.json` |
| Directory handles | IndexedDB | `CodeRefExplorer` database |
| Theme | LocalStorage | `theme` key |

---

## Configuration

### Server Port

**Default:** 8080

**Change:**
```python
# server.py, line 12
PORT = 8080  # Change to desired port
```

```javascript
// main.js, line 62
mainWindow.loadURL('http://localhost:8080/...');
```

---

### DevTools

**Enable:**
```javascript
// main.js, line 66
// Uncomment:
mainWindow.webContents.openDevTools();
```

**Restart:** `npm start`

---

## Troubleshooting

### Server Won't Start

**Check Python:**
```bash
python --version
# Should show: Python 3.6+
```

**Check port:**
```bash
netstat -an | grep 8080
# Should be empty
```

**Start manually:**
```bash
python server.py
```

---

### Permission Denied

**Fix:**
```
1. Remove project (trash icon)
2. Re-add via "Browse Folder"
3. Grant permission when prompted
```

**Alternative:** Use "Type Path" method

---

### Projects Not Loading

**Check file:**
```bash
ls projects.json
# Should exist
```

**Validate JSON:**
```bash
python -m json.tool projects.json
# Should pretty-print
```

**Fix:** Restore from backup or re-add projects

---

### File Won't Open

**Check permissions:**
```bash
ls -la /path/to/file
# Check readable
```

**Try different mode:**
- File System API → Type Path
- Type Path → Browse Folder

---

## Browser Compatibility

| Browser | File System API | HTTP API | Recommended |
|---------|----------------|----------|-------------|
| Chrome 86+ | ✅ Yes | ✅ Yes | ✅ Best choice |
| Edge 86+ | ✅ Yes | ✅ Yes | ✅ Best choice |
| Brave | ✅ Yes | ✅ Yes | ✅ Best choice |
| Firefox | ❌ No | ✅ Yes | ⚠️ Limited |
| Safari | ❌ No | ✅ Yes | ⚠️ Limited |

---

## Performance

### Typical Operations

| Operation | Time | Notes |
|-----------|------|-------|
| Add project | <2s | File System API |
| Switch project | <1s | Cached handles |
| Load tree | <3s | 1000 files |
| View file | <0.5s | <1MB |
| Toggle theme | Instant | CSS variables |

---

### Resource Usage

| Metric | Value |
|--------|-------|
| RAM (idle) | ~150MB |
| RAM (active) | ~250MB |
| Disk space | ~180MB |
| CPU (idle) | <1% |
| Network | 0 (offline) |

---

### Limits

| Resource | Limit | Notes |
|----------|-------|-------|
| Projects | Unlimited | Disk-limited |
| Files/project | 10,000+ | Slow >50k |
| File size | 10MB | Slow for larger |
| IndexedDB | ~50% disk | Browser-dependent |

---

## Security Checklist

**Current:**
- [x] Local-only server (localhost)
- [x] Context isolation (Electron)
- [x] No external requests
- [x] No analytics/tracking

**Production (Recommended):**
- [ ] Add authentication
- [ ] Enable HTTPS
- [ ] CORS whitelist
- [ ] Code sign executables

---

## Development

### Run from Source

```bash
npm install
npm start
```

**Auto-restarts:** No (restart manually)

---

### Build Installer

```bash
# Windows
npm run build:win
# Output: dist/CodeRef Explorer Setup.exe

# macOS (on macOS only)
npm run build:mac
# Output: dist/CodeRef Explorer.dmg

# Linux
npm run build:linux
# Output: dist/coderef-explorer.AppImage
```

---

### Enable DevTools

```javascript
// main.js, line 66
mainWindow.webContents.openDevTools();
```

---

### Inspect Storage

**IndexedDB:**
```
DevTools → Application → Storage → IndexedDB → CodeRefExplorer
```

**LocalStorage:**
```
DevTools → Application → Storage → Local Storage
```

**projects.json:**
```bash
cat projects.json
```

---

## Data Models

### Project

```json
{
  "id": "string (unique)",
  "name": "string (display)",
  "path": "string (absolute path or [Directory: handle])"
}
```

---

### TreeNode

```json
{
  "name": "string",
  "path": "string (absolute)",
  "type": "file | folder",
  "children": [TreeNode] // if folder
}
```

---

### FileInfo

```json
{
  "content": "string (UTF-8)",
  "name": "string",
  "size": number,
  "modified": number // Unix timestamp
}
```

---

## Common Workflows

### Daily Use

```
1. Launch app
2. Select project from dropdown
3. Navigate to file
4. View content
5. Copy path/code as needed
6. Switch to next project
```

**Time:** ~10 seconds per project

---

### Bulk Add Projects

**Scripted:**
```json
// Create projects.json
[
  {"id": "p1", "name": "Proj 1", "path": "/path/1"},
  {"id": "p2", "name": "Proj 2", "path": "/path/2"}
]
```

**UI:**
```
Repeat: + → Browse Folder → Add
```

---

### Share with Team

**Option A: Share projects.json**
```
1. Copy projects.json
2. Send to teammate
3. They place in app directory
4. Restart app
```

**Option B: Export paths**
```
1. Open projects.json
2. Copy paths
3. Share list
4. Teammates add manually
```

---

## Tips & Tricks

### Best Practices

✅ **Do:**
- Use Browse Folder for frequent access
- Name projects descriptively
- Remove obsolete projects
- Grant permissions when prompted
- Use dark mode for eye comfort

❌ **Don't:**
- Delete projects.json
- Move folders without updating paths
- Use Firefox/Safari (limited support)
- Expose server to network
- Manually edit IndexedDB

---

### Optimize Performance

**For large projects (10k+ files):**
1. Use Type Path method (HTTP API)
2. Avoid expanding all folders
3. Close unused projects

**For fast switching:**
1. Use Browse Folder (cached handles)
2. Grant persistent permissions
3. Keep projects.json < 1MB

---

## Links

**Documentation:**
- [API Reference](../foundation-docs/API.md)
- [Data Schema](../foundation-docs/SCHEMA.md)
- [UI Components](../foundation-docs/COMPONENTS.md)
- [Architecture](../foundation-docs/ARCHITECTURE.md)
- [User Guide](USER-GUIDE.md)
- [Features](FEATURES.md)

**External:**
- [Electron Docs](https://electronjs.org/docs)
- [File System Access API](https://developer.mozilla.org/en-US/docs/Web/API/File_System_Access_API)
- [Material Symbols](https://fonts.google.com/icons)

---

## Version Info

**Current:** 1.0.0
**Released:** 2025-12-28
**Platform:** Windows, macOS, Linux
**License:** MIT

---

## Support

**Issues:** https://github.com/yourusername/coderef-explorer/issues
**Docs:** See `coderef/` directory for complete documentation

---

_Quick reference optimized for fast scanning and common tasks._
