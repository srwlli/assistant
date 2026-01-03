# CodeRef Explorer - Tool Reference

Quick reference for all commands, shortcuts, and tools.

---

## Project Management

**Add Project (Browser)**
- Click `+` button → Browse Folder → Select directory
- Requires File System Access API permission

**Add Project (Path)**
- Click `+` button → Type absolute path → Add Project
- Server validates path exists

**Switch Project**
- Use project dropdown in sidebar
- Auto-loads folder tree

**Remove Project**
- Select project → Click trash icon → Confirm
- Clears from IndexedDB and projects.json

---

## Navigation

**Expand Folder**
- Click folder name or chevron icon
- Chevron rotates 90° when expanded

**View File**
- Click file name in tree
- Content displays in main panel

**Copy File Path**
- Click copy icon in file header
- Copies absolute path to clipboard

**Copy Code**
- Click copy icon in code block
- Copies content to clipboard

---

## Theme

**Toggle Theme**
- Click moon icon in header
- Switches: dark ↔ light
- Persists in LocalStorage

---

## File Viewer

**Supported Formats**
- JSON: Syntax highlighting with color
- Markdown: Rendered with marked.js
- Text: Monospace display
- Code: Syntax highlighting

**File Actions**
- Copy path
- Copy code
- Share link (generates URL fragment)

---

## Keyboard Shortcuts

_No keyboard shortcuts currently implemented_

Roadmap: Version 1.1 will add shortcuts

---

## Browser Requirements

**Supported Browsers**
- Chrome 86+
- Edge 86+
- Brave (Chromium-based)

**Not Supported**
- Firefox (no File System Access API)
- Safari (no File System Access API)

---

## API Endpoints

**Projects**
- `GET /api/projects` - List all projects
- `POST /api/projects` - Save project
- `DELETE /api/projects/{id}` - Remove project

**Files**
- `GET /api/tree?path={path}` - Get folder tree
- `GET /api/file?path={path}` - Get file content

---

## Storage

**IndexedDB** (`CodeRefExplorer`)
- Stores File System Access API handles
- Key: project ID

**LocalStorage**
- `theme` - Current theme (dark/light)

**File System**
- `projects.json` - Project metadata

---

## Troubleshooting

**Server won't start**
- Check Python installed: `python --version`
- Check port available: `netstat -an | grep 8080`

**Permission denied**
- Remove project and re-add via Browse Folder
- Grant permission when prompted

**Projects not loading**
- Check `projects.json` exists
- Validate JSON: `python -m json.tool projects.json`

---

_Version: 1.0.0 | Last Updated: 2025-12-28_
