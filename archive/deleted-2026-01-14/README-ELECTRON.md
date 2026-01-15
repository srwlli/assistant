# CodeRef Explorer - Electron Desktop App

## Setup

1. **Install Node.js** (if not already installed)
   - Download from: https://nodejs.org/
   - Version 18+ recommended

2. **Install dependencies**
   ```bash
   cd C:\Users\willh\Desktop\assistant\web
   npm install
   ```

## Running the App

### Development Mode
```bash
npm start
```

This will:
- Start the Python server automatically
- Open the Electron window
- Enable hot-reload (restart to see changes)

### Build Executable

**Windows .exe:**
```bash
npm run build:win
```

This creates:
- `dist/CodeRef Explorer Setup 1.0.0.exe` - Installer
- `dist/win-unpacked/` - Portable version

**Output location:** `C:\Users\willh\Desktop\assistant\web\dist\`

## Features

- ✅ Standalone desktop app (no browser needed)
- ✅ Built-in Python server (auto-starts/stops)
- ✅ File System Access API support
- ✅ Native window controls
- ✅ Offline-ready

## File Structure

```
web/
├── main.js              # Electron entry point
├── preload.js           # Security/context bridge
├── package.json         # Dependencies & build config
├── server.py            # Python backend (bundled)
├── src/                 # HTML/CSS/JS files
└── dist/                # Built executables (after build)
```

## Distribution

After building, share:
- **Installer:** `dist/CodeRef Explorer Setup 1.0.0.exe` (users install)
- **Portable:** `dist/win-unpacked/` folder (copy & run)

## Requirements

**Runtime:**
- Python 3.x must be installed on user's system
- Windows 10/11

**Development:**
- Node.js 18+
- npm 9+

## Troubleshooting

**"Python not found" error:**
- Ensure Python is in PATH
- Or update `main.js` line 9 with full Python path

**Port 8080 already in use:**
- Close other instances
- Or change port in `server.py` and `main.js`

**Build fails:**
- Run `npm install` again
- Check Node.js version: `node --version`
