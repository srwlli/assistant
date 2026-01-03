# File System API Logic Extraction

> **Purpose:** Extract core File System Access API patterns from CodeRef Explorer for React implementation
>
> **Source:** `C:\Users\willh\Desktop\assistant\web\src\pages\coderef-explorer.html`
>
> **Target:** Agent 2 to implement in `packages/dashboard/src/lib/coderef/local-access.ts`

---

## Pattern 1: Show Directory Picker

### Source Code (Lines 733-766)

```javascript
async function browseFolderForPath() {
    try {
        // Check if File System Access API is supported
        if (!window.showDirectoryPicker) {
            showToast('File System Access API not supported. Please type the full path instead.');
            return;
        }

        const dirHandle = await window.showDirectoryPicker({
            mode: 'read'
        });

        pendingDirectoryHandle = dirHandle;

        // Set folder name as path
        document.getElementById('projectPath').value = `[Directory: ${dirHandle.name}]`;

        // Auto-populate project name if empty
        const nameInput = document.getElementById('projectName');
        if (!nameInput.value) {
            nameInput.value = dirHandle.name;
        }

        // Manually enable the Add button
        document.getElementById('addProjectBtn').disabled = false;

        showToast(`Selected folder: ${dirHandle.name}`);
    } catch (error) {
        if (error.name !== 'AbortError') {
            console.error('Error selecting folder:', error);
            showToast('Error selecting folder');
        }
    }
}
```

### Key Insights

1. **Feature Detection:** Always check `if (!window.showDirectoryPicker)` before using
2. **Mode:** Use `{ mode: 'read' }` for read-only access (faster, safer)
3. **Error Handling:** `AbortError` is normal (user cancelled), other errors should be logged
4. **UX Pattern:** Auto-populate form fields from selected directory

### React/TypeScript Implementation

```typescript
// packages/dashboard/src/lib/coderef/local-access.ts

export async function showDirectoryPicker(): Promise<FileSystemDirectoryHandle | null> {
  try {
    // Feature detection
    if (!('showDirectoryPicker' in window)) {
      throw new Error('File System Access API not supported in this browser');
    }

    const dirHandle = await window.showDirectoryPicker({
      mode: 'read',
    });

    return dirHandle;
  } catch (error) {
    if ((error as Error).name === 'AbortError') {
      // User cancelled, not an error
      return null;
    }

    console.error('Error selecting folder:', error);
    throw error;
  }
}
```

**Usage in React Component:**
```typescript
const handleBrowseFolder = async () => {
  try {
    const dirHandle = await showDirectoryPicker();
    if (!dirHandle) return; // User cancelled

    // Save to IndexedDB
    await saveDirectoryHandle(projectId, dirHandle);

    // Update UI
    setProjectName(dirHandle.name);
    setProjectPath(`[Directory: ${dirHandle.name}]`);
  } catch (error) {
    toast.error('File System Access API not supported');
  }
};
```

---

## Pattern 2: Build Tree from Directory Handle

### Source Code (Lines 630-696)

```javascript
async function buildTreeFromDirectoryHandle(dirHandle, parentPath = '') {
    const treeContainer = document.querySelector('.tree-container');
    treeContainer.innerHTML = '';

    await renderDirectoryNode(dirHandle, treeContainer, true, parentPath + dirHandle.name);
}

async function renderDirectoryNode(dirHandle, parentElement, isRoot = false, fullPath = '') {
    // Create folder element
    const folderDiv = document.createElement('div');
    folderDiv.className = `tree-item folder ${isRoot ? 'active' : ''}`;
    folderDiv.onclick = () => toggleFolder(folderDiv);

    folderDiv.innerHTML = `
        <span class="material-symbols-outlined chevron ${isRoot ? 'expanded' : ''}">chevron_right</span>
        <span class="material-symbols-outlined icon">folder</span>
        <span>${dirHandle.name}</span>
    `;

    parentElement.appendChild(folderDiv);

    // Create children container
    const childrenDiv = document.createElement('div');
    childrenDiv.className = `tree-children ${isRoot ? 'show' : ''}`;

    // Get all entries
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

    // Render subdirectories
    for (const entry of entries) {
        if (entry.kind === 'directory') {
            await renderDirectoryNode(entry, childrenDiv, false, fullPath + '/' + entry.name);
        }
    }

    // Render files
    for (const entry of entries) {
        if (entry.kind === 'file') {
            const fileDiv = document.createElement('div');
            fileDiv.className = 'tree-item file';
            fileDiv.onclick = async (e) => {
                e.stopPropagation();
                await loadFileFromHandle(entry, fileDiv, fullPath + '/' + entry.name);
            };

            fileDiv.innerHTML = `
                <span class="material-symbols-outlined icon">description</span>
                <span>${entry.name}</span>
            `;

            childrenDiv.appendChild(fileDiv);
        }
    }

    parentElement.appendChild(childrenDiv);
}
```

### Key Insights

1. **Async Iteration:** `for await (const entry of dirHandle.values())` is the correct pattern
2. **Entry Types:** Check `entry.kind === 'directory'` vs `'file'`
3. **Sorting:** Folders first, then files, alphabetically within each group
4. **Recursion:** Call `renderDirectoryNode()` for subdirectories
5. **Path Building:** Accumulate full paths as you recurse (`fullPath + '/' + entry.name`)

### React/TypeScript Implementation

```typescript
// packages/dashboard/src/lib/coderef/local-access.ts

export async function buildTreeFromHandle(
  dirHandle: FileSystemDirectoryHandle,
  parentPath: string = ''
): Promise<TreeNode> {
  const entries: (FileSystemFileHandle | FileSystemDirectoryHandle)[] = [];

  // Collect all entries
  for await (const entry of dirHandle.values()) {
    entries.push(entry);
  }

  // Sort: folders first, then files, alphabetically
  entries.sort((a, b) => {
    if (a.kind !== b.kind) {
      return a.kind === 'directory' ? -1 : 1;
    }
    return a.name.localeCompare(b.name);
  });

  // Build children array
  const children: TreeNode[] = [];

  for (const entry of entries) {
    const fullPath = parentPath ? `${parentPath}/${entry.name}` : entry.name;

    if (entry.kind === 'directory') {
      // Recursively build subtree
      const subtree = await buildTreeFromHandle(entry, fullPath);
      children.push(subtree);
    } else {
      // File node
      children.push({
        name: entry.name,
        type: 'file',
        path: fullPath,
      });
    }
  }

  return {
    name: dirHandle.name,
    type: 'folder',
    path: parentPath || dirHandle.name,
    children,
  };
}
```

**Usage in React Component:**
```typescript
const loadProjectTree = async (projectId: string) => {
  // Get directory handle from IndexedDB
  const dirHandle = await getDirectoryHandle(projectId);
  if (!dirHandle) return null;

  // Check permissions
  const permission = await dirHandle.queryPermission({ mode: 'read' });
  if (permission !== 'granted') {
    const newPermission = await dirHandle.requestPermission({ mode: 'read' });
    if (newPermission !== 'granted') return null;
  }

  // Build tree
  const tree = await buildTreeFromHandle(dirHandle);
  return tree;
};
```

---

## Pattern 3: Load File from Handle

### Source Code (Lines 698-718)

```javascript
async function loadFileFromHandle(fileHandle, element, filePath) {
    // Remove active class from all tree items
    document.querySelectorAll('.tree-item').forEach(item => {
        item.classList.remove('active');
    });
    // Add active to clicked item
    element.classList.add('active');

    try {
        const file = await fileHandle.getFile();
        const content = await file.text();

        currentFileContent = content;
        currentFilePath = filePath;

        displayFileContent(file.name, content, filePath, file.size, file.lastModified);
    } catch (error) {
        console.error('Error reading file:', error);
        showToast('Error reading file');
    }
}
```

### Key Insights

1. **getFile():** Returns a `File` object (standard browser API)
2. **file.text():** Async method to read content as string
3. **Metadata:** File object has `name`, `size`, `lastModified` properties
4. **Error Handling:** Wrap in try/catch (permissions might have changed)

### React/TypeScript Implementation

```typescript
// packages/dashboard/src/lib/coderef/local-access.ts

export async function loadFileFromHandle(
  fileHandle: FileSystemFileHandle
): Promise<FileInfo> {
  try {
    const file = await fileHandle.getFile();
    const content = await file.text();

    return {
      name: file.name,
      content,
      path: fileHandle.name, // Will be overridden with full path by caller
      size: file.size,
      modified: file.lastModified,
    };
  } catch (error) {
    console.error('Error reading file:', error);
    throw new Error(`Failed to read file: ${fileHandle.name}`);
  }
}
```

**Usage in React Component:**
```typescript
const handleFileClick = async (fileHandle: FileSystemFileHandle, fullPath: string) => {
  try {
    const fileInfo = await loadFileFromHandle(fileHandle);
    fileInfo.path = fullPath; // Set full path for UI

    setCurrentFile(fileInfo);
    setActiveFilePath(fullPath);
  } catch (error) {
    toast.error('Failed to read file');
  }
};
```

---

## Pattern 4: Permission Management

### Source Code (Lines 583-628)

```javascript
async function changeProject(projectId) {
    currentProject = projects.find(p => p.id === projectId);
    if (!currentProject) return;

    // Try to get directory handle from IndexedDB
    try {
        const dirHandle = await getDirectoryHandle(projectId);

        if (dirHandle) {
            // Verify we still have permission
            const permission = await dirHandle.queryPermission({ mode: 'read' });

            if (permission === 'granted') {
                // Build tree from directory handle
                await buildTreeFromDirectoryHandle(dirHandle);
                return;
            } else if (permission === 'prompt') {
                // Request permission
                const newPermission = await dirHandle.requestPermission({ mode: 'read' });
                if (newPermission === 'granted') {
                    await buildTreeFromDirectoryHandle(dirHandle);
                    return;
                }
            }

            // Permission denied, fall through to server mode
            showToast('Permission denied. Please re-add this project.');
        }
    } catch (error) {
        console.error('Error accessing directory handle:', error);
    }

    // Fallback: Load from server (for manually typed paths)
    if (currentProject.path && !currentProject.path.startsWith('[Directory:')) {
        try {
            const response = await fetch(`/api/tree?path=${encodeURIComponent(currentProject.path)}`);
            const tree = await response.json();
            renderServerTree(tree);
        } catch (error) {
            console.error('Error loading project tree:', error);
            showToast('Error loading project folder');
        }
    } else {
        showToast('Please grant permission to access this folder');
    }
}
```

### Key Insights

1. **Three-Step Permission Check:**
   - `queryPermission({ mode: 'read' })` - Check current state
   - If `'prompt'`, call `requestPermission({ mode: 'read' })` - Show browser prompt
   - If `'denied'` or request fails, fall back to API mode

2. **Permission States:**
   - `'granted'` - Ready to use immediately
   - `'prompt'` - Need to request (user previously granted but needs re-confirmation)
   - `'denied'` - User explicitly denied, cannot use

3. **Fallback Strategy:** Always have a server-mode fallback for when permissions fail

### React/TypeScript Implementation

```typescript
// packages/dashboard/src/lib/coderef/local-access.ts

export async function checkAndRequestPermission(
  dirHandle: FileSystemDirectoryHandle
): Promise<boolean> {
  try {
    // Check current permission state
    const permission = await dirHandle.queryPermission({ mode: 'read' });

    if (permission === 'granted') {
      return true;
    }

    if (permission === 'prompt') {
      // Request permission from user
      const newPermission = await dirHandle.requestPermission({ mode: 'read' });
      return newPermission === 'granted';
    }

    // Permission denied
    return false;
  } catch (error) {
    console.error('Permission check failed:', error);
    return false;
  }
}
```

**Usage in React Component:**
```typescript
const loadProject = async (projectId: string) => {
  // Try local mode first
  const dirHandle = await getDirectoryHandle(projectId);

  if (dirHandle) {
    const hasPermission = await checkAndRequestPermission(dirHandle);

    if (hasPermission) {
      // ✅ Local mode
      const tree = await buildTreeFromHandle(dirHandle);
      setProjectTree(tree);
      setAccessMode('local');
      return;
    }

    // ⚠️ Permission denied
    toast.warning('Permission denied. Falling back to server mode.');
  }

  // ❌ Fallback to API mode
  const tree = await fetchTreeFromAPI(projectId);
  setProjectTree(tree);
  setAccessMode('api');
};
```

---

## Pattern 5: Storing File Handles for Nested Access

### Challenge

Directory handles can be stored in IndexedDB, but **file handles cannot** be stored directly. You must:
1. Store the **directory handle** (root)
2. Navigate to files using path traversal

### Solution: Path Traversal Helper

```typescript
// packages/dashboard/src/lib/coderef/local-access.ts

export async function getFileHandleByPath(
  dirHandle: FileSystemDirectoryHandle,
  relativePath: string
): Promise<FileSystemFileHandle | null> {
  try {
    const pathParts = relativePath.split('/').filter(Boolean);
    let currentHandle: FileSystemDirectoryHandle | FileSystemFileHandle = dirHandle;

    for (let i = 0; i < pathParts.length; i++) {
      const part = pathParts[i];

      if (i === pathParts.length - 1) {
        // Last part is the file
        if (currentHandle.kind === 'directory') {
          return await currentHandle.getFileHandle(part);
        }
      } else {
        // Intermediate directory
        if (currentHandle.kind === 'directory') {
          currentHandle = await currentHandle.getDirectoryHandle(part);
        } else {
          return null; // Path invalid
        }
      }
    }

    return null;
  } catch (error) {
    console.error('Error traversing path:', error);
    return null;
  }
}
```

**Usage:**
```typescript
// Load file by relative path
const fileHandle = await getFileHandleByPath(dirHandle, 'coderef/context.json');
if (fileHandle) {
  const fileInfo = await loadFileFromHandle(fileHandle);
  console.log(fileInfo.content);
}
```

---

## Summary: Core Functions for Agent 2

### File: `packages/dashboard/src/lib/coderef/local-access.ts`

```typescript
// 1. Show directory picker
export async function showDirectoryPicker(): Promise<FileSystemDirectoryHandle | null>;

// 2. Build tree from handle
export async function buildTreeFromHandle(
  dirHandle: FileSystemDirectoryHandle,
  parentPath?: string
): Promise<TreeNode>;

// 3. Load file from handle
export async function loadFileFromHandle(
  fileHandle: FileSystemFileHandle
): Promise<FileInfo>;

// 4. Check and request permissions
export async function checkAndRequestPermission(
  dirHandle: FileSystemDirectoryHandle
): Promise<boolean>;

// 5. Path traversal helper
export async function getFileHandleByPath(
  dirHandle: FileSystemDirectoryHandle,
  relativePath: string
): Promise<FileSystemFileHandle | null>;
```

### Expected Deliverables

- [ ] `local-access.ts` with 5 core functions
- [ ] Unit tests for each function
- [ ] Integration tests with IndexedDB
- [ ] Error handling for all edge cases
- [ ] TypeScript types from `types.ts` and `file-system-api-types.d.ts`

---

**Next:** See `project-manager-requirements.md` for UI component integration patterns (LOCAL-002).
