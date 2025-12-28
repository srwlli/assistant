// Preload script for Electron security
// Runs in isolated context with access to both Node.js and DOM

const { contextBridge } = require('electron');

// Expose safe APIs to renderer process if needed
contextBridge.exposeInMainWorld('electron', {
  platform: process.platform,
  versions: {
    node: process.versions.node,
    chrome: process.versions.chrome,
    electron: process.versions.electron
  }
});

console.log('CodeRef Explorer - Preload script loaded');
