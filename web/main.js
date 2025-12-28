const { app, BrowserWindow, protocol, session } = require('electron');
const path = require('path');
const { spawn } = require('child_process');

let mainWindow;
let pythonProcess;

// Enable File System Access API
app.commandLine.appendSwitch('enable-features', 'FileSystemAccessAPI');
app.commandLine.appendSwitch('enable-experimental-web-platform-features');

// Start Python server
function startPythonServer() {
  const pythonPath = 'python';
  const serverScript = path.join(__dirname, 'server.py');

  pythonProcess = spawn(pythonPath, [serverScript], {
    cwd: __dirname
  });

  pythonProcess.stdout.on('data', (data) => {
    console.log(`Python server: ${data}`);
  });

  pythonProcess.stderr.on('data', (data) => {
    console.error(`Python server error: ${data}`);
  });

  pythonProcess.on('close', (code) => {
    console.log(`Python server exited with code ${code}`);
  });
}

// Stop Python server
function stopPythonServer() {
  if (pythonProcess) {
    pythonProcess.kill();
    pythonProcess = null;
  }
}

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 1400,
    height: 900,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      nodeIntegration: false,
      contextIsolation: true,
      webSecurity: false,  // Disable to allow File System Access API
      allowRunningInsecureContent: true
    },
    title: 'CodeRef Explorer',
    icon: path.join(__dirname, 'icon.png')
  });

  // Clear cache on startup
  mainWindow.webContents.session.clearCache();

  // Wait for Python server to start (2 seconds)
  setTimeout(() => {
    mainWindow.loadURL('http://localhost:8080/src/pages/coderef-explorer.html');
  }, 2000);

  // Open DevTools in development (uncomment for debugging)
  // mainWindow.webContents.openDevTools();

  mainWindow.on('closed', () => {
    mainWindow = null;
  });
}

app.whenReady().then(() => {
  // Configure permissions for File System Access API
  session.defaultSession.setPermissionRequestHandler((webContents, permission, callback) => {
    // Auto-grant file system permissions
    if (permission === 'fileSystem') {
      callback(true);
    } else {
      callback(true); // Grant all permissions for local app
    }
  });

  // Handle permission checks
  session.defaultSession.setPermissionCheckHandler((webContents, permission, requestingOrigin, details) => {
    // Always allow file system access
    if (permission === 'fileSystem') {
      return true;
    }
    return true;
  });

  // Start Python server
  startPythonServer();

  // Create window
  createWindow();

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow();
    }
  });
});

app.on('window-all-closed', () => {
  stopPythonServer();
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('before-quit', () => {
  stopPythonServer();
});
