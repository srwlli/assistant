# Permission Checking Patterns

> **Purpose:** Document permission flow for File System Access API
>
> **Source:** `C:\Users\willh\Desktop\assistant\web\src\pages\coderef-explorer.html` (lines 588-609)
>
> **Target:** `packages/dashboard/src/lib/coderef/permissions.ts`

---

## Overview

File System Access API requires **explicit user permission** to access directories. Permissions are:
- **Session-persistent:** Granted until browser tab closes
- **Browser-controlled:** Cannot be bypassed programmatically
- **Re-requestable:** Can prompt user again if previously denied

---

## Permission States

### Three Possible States

| State      | Meaning                                  | Action Required                    |
|------------|------------------------------------------|------------------------------------|
| `'granted'` | User previously granted access           | ✅ Use handle immediately          |
| `'prompt'`  | Need to request permission from user     | ⚠️ Call `requestPermission()`     |
| `'denied'`  | User explicitly denied access            | ❌ Cannot use, fall back to API   |

### State Transitions

```
Initial Access
     ↓
[Browser Picker] → User selects folder → 'granted'
                                      ↓
                                  Page reload
                                      ↓
                          [Check Permission State]
                                      ↓
                    ┌─────────────────┼─────────────────┐
                    ↓                 ↓                 ↓
                'granted'         'prompt'          'denied'
                    ↓                 ↓                 ↓
               Use handle     Request permission   Fallback to API
                                      ↓
                              ┌───────┴───────┐
                              ↓               ↓
                          'granted'       'denied'
                              ↓               ↓
                         Use handle    Fallback to API
```

---

## Source Code (Current App)

### Lines 588-609

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

    // Fallback: Load from server
    loadFromServerAPI(currentProject);
}
```

---

## Implementation Pattern

### File: `packages/dashboard/src/lib/coderef/permissions.ts`

```typescript
export type PermissionState = 'granted' | 'prompt' | 'denied';

export interface PermissionCheckResult {
  state: PermissionState;
  hasAccess: boolean;
  needsRequest: boolean;
}

/**
 * Check permission state for a directory handle
 *
 * @param dirHandle - FileSystemDirectoryHandle to check
 * @param mode - Access mode ('read' or 'readwrite')
 * @returns Permission check result
 */
export async function checkPermission(
  dirHandle: FileSystemDirectoryHandle,
  mode: 'read' | 'readwrite' = 'read'
): Promise<PermissionCheckResult> {
  try {
    const state = await dirHandle.queryPermission({ mode });

    return {
      state,
      hasAccess: state === 'granted',
      needsRequest: state === 'prompt',
    };
  } catch (error) {
    console.error('Permission check failed:', error);

    return {
      state: 'denied',
      hasAccess: false,
      needsRequest: false,
    };
  }
}

/**
 * Request permission from user
 *
 * @param dirHandle - FileSystemDirectoryHandle to request permission for
 * @param mode - Access mode ('read' or 'readwrite')
 * @returns true if permission granted, false otherwise
 */
export async function requestPermission(
  dirHandle: FileSystemDirectoryHandle,
  mode: 'read' | 'readwrite' = 'read'
): Promise<boolean> {
  try {
    const state = await dirHandle.requestPermission({ mode });
    return state === 'granted';
  } catch (error) {
    console.error('Permission request failed:', error);
    return false;
  }
}

/**
 * Check and request permission if needed
 *
 * @param dirHandle - FileSystemDirectoryHandle to ensure access for
 * @param mode - Access mode ('read' or 'readwrite')
 * @returns true if access granted (either already had or user approved), false otherwise
 */
export async function ensurePermission(
  dirHandle: FileSystemDirectoryHandle,
  mode: 'read' | 'readwrite' = 'read'
): Promise<boolean> {
  // Step 1: Check current permission state
  const check = await checkPermission(dirHandle, mode);

  if (check.hasAccess) {
    // Already have permission
    return true;
  }

  if (check.needsRequest) {
    // Need to request permission
    return await requestPermission(dirHandle, mode);
  }

  // Permission denied
  return false;
}
```

---

## Usage Patterns

### Pattern 1: On Project Switch

```typescript
async function loadProject(projectId: string) {
  // Get directory handle from IndexedDB
  const dirHandle = await getDirectoryHandle(projectId);

  if (!dirHandle) {
    // No handle stored, use API mode
    await loadProjectFromAPI(projectId);
    return;
  }

  // Check and request permission if needed
  const hasPermission = await ensurePermission(dirHandle);

  if (hasPermission) {
    // ✅ Local mode
    const tree = await buildTreeFromHandle(dirHandle);
    setProjectTree(tree);
    setAccessMode('local');
  } else {
    // ❌ Permission denied, fallback to API
    toast.warning('Permission denied. Using server mode instead.');
    await loadProjectFromAPI(projectId);
  }
}
```

### Pattern 2: On File Load

```typescript
async function loadFile(fileHandle: FileSystemFileHandle) {
  try {
    // Check permission on parent directory handle first
    // (File handles inherit permissions from directory)
    const file = await fileHandle.getFile();
    const content = await file.text();

    return {
      name: file.name,
      content,
      size: file.size,
      modified: file.lastModified,
    };
  } catch (error) {
    // Permission error or file deleted
    console.error('Failed to load file:', error);
    throw new Error('Failed to read file. Permission may have been revoked.');
  }
}
```

### Pattern 3: Permission Check Before Tree Build

```typescript
async function changeProject(project: Project) {
  if (project.path.startsWith('[Directory:')) {
    // Browsed folder, try local mode
    const dirHandle = await getDirectoryHandle(project.id);

    if (dirHandle) {
      const hasPermission = await ensurePermission(dirHandle);

      if (hasPermission) {
        // Build tree from handle
        const tree = await buildTreeFromHandle(dirHandle);
        onTreeLoad(tree, 'local');
        return;
      }

      // Permission denied
      toast.error('Permission denied. Please re-add this project.');
    }
  }

  // Typed path or permission denied, use API mode
  await loadProjectFromAPI(project.path);
}
```

---

## Error Handling

### 1. Handle Stale Handles

When directory is deleted from file system, handle becomes stale:

```typescript
async function verifyHandleValidity(
  dirHandle: FileSystemDirectoryHandle
): Promise<boolean> {
  try {
    // Try to check permission (will fail if handle is stale)
    await dirHandle.queryPermission({ mode: 'read' });
    return true;
  } catch (error) {
    console.error('Directory handle is stale:', error);

    // Clean up invalid handle
    await deleteDirectoryHandle(projectId);

    return false;
  }
}
```

### 2. Handle Browser Rejections

User can close permission prompt without responding:

```typescript
async function requestPermissionSafely(
  dirHandle: FileSystemDirectoryHandle
): Promise<boolean> {
  try {
    return await requestPermission(dirHandle);
  } catch (error) {
    // User closed prompt or browser blocked request
    console.warn('Permission request was blocked:', error);
    return false;
  }
}
```

### 3. Handle Concurrent Requests

Only request permission once at a time:

```typescript
let pendingPermissionRequest: Promise<boolean> | null = null;

async function ensurePermissionThrottled(
  dirHandle: FileSystemDirectoryHandle
): Promise<boolean> {
  // If already requesting, wait for that request
  if (pendingPermissionRequest) {
    return await pendingPermissionRequest;
  }

  // Start new request
  pendingPermissionRequest = ensurePermission(dirHandle);

  try {
    return await pendingPermissionRequest;
  } finally {
    pendingPermissionRequest = null;
  }
}
```

---

## User Experience Patterns

### 1. Permission Prompt UX

```tsx
function PermissionPrompt({ onGrant, onDeny }: PermissionPromptProps) {
  return (
    <div className="p-4 bg-orange-950 border border-orange-700 rounded-md">
      <h4 className="font-semibold mb-2">Permission Required</h4>
      <p className="text-sm text-zinc-300 mb-3">
        This project needs permission to access your local folder.
      </p>
      <div className="flex gap-2">
        <button
          onClick={onGrant}
          className="px-3 py-1 bg-orange-600 hover:bg-orange-700 rounded text-sm"
        >
          Grant Access
        </button>
        <button
          onClick={onDeny}
          className="px-3 py-1 bg-zinc-700 hover:bg-zinc-600 rounded text-sm"
        >
          Use Server Mode
        </button>
      </div>
    </div>
  );
}
```

**When to show:**
- Permission state is `'prompt'`
- User clicks on project that needs permission
- Before showing browser's native permission dialog

### 2. Permission Denied Message

```tsx
function PermissionDeniedAlert({ projectName, onReAdd }: PermissionDeniedAlertProps) {
  return (
    <div className="p-4 bg-red-950 border border-red-700 rounded-md">
      <h4 className="font-semibold mb-2">Permission Denied</h4>
      <p className="text-sm text-zinc-300 mb-3">
        You denied access to "{projectName}". You can re-add this project to grant permission again.
      </p>
      <button
        onClick={onReAdd}
        className="px-3 py-1 bg-red-600 hover:bg-red-700 rounded text-sm"
      >
        Re-add Project
      </button>
    </div>
  );
}
```

### 3. Auto-Fallback to API

```typescript
async function loadProjectWithFallback(project: Project) {
  // Try local mode first
  const dirHandle = await getDirectoryHandle(project.id);

  if (dirHandle) {
    const hasPermission = await ensurePermission(dirHandle);

    if (hasPermission) {
      // ✅ Local mode succeeded
      const tree = await buildTreeFromHandle(dirHandle);
      setAccessMode('local');
      setProjectTree(tree);
      return;
    }
  }

  // ❌ Fallback to API mode (silent, no error)
  const tree = await fetchTreeFromAPI(project.id);
  setAccessMode('api');
  setProjectTree(tree);

  // Optional: Show info toast
  toast.info('Using server mode for this project');
}
```

---

## Testing Scenarios

### Manual Testing Checklist

- [ ] **First Browse:** Select folder → permission automatically granted
- [ ] **Page Reload:** Refresh browser → permission state is 'prompt'
- [ ] **Request Permission:** Click project → browser shows prompt → click "Allow"
- [ ] **Deny Permission:** Click project → browser shows prompt → click "Deny" → fallback to API
- [ ] **Revoke Permission Manually:** Chrome DevTools → Application → Storage → clear IndexedDB → permission state becomes 'prompt'
- [ ] **Delete Folder:** Delete folder from file system → handle becomes stale → error handled gracefully
- [ ] **Multiple Projects:** Switch between projects → each has separate permission state

### Browser DevTools Testing

**Chrome:**
1. Open DevTools → Application → Storage
2. Scroll to "File System API" section
3. View granted permissions
4. Revoke permissions for testing

**Firefox:**
File System Access API not supported (test API fallback)

**Edge:**
Same as Chrome (Chromium-based)

---

## Browser Compatibility

### Feature Detection

```typescript
export function isFileSystemAccessSupported(): boolean {
  return (
    typeof window !== 'undefined' &&
    'showDirectoryPicker' in window
  );
}
```

**Usage:**
```typescript
if (!isFileSystemAccessSupported()) {
  // Hide "Browse Folder" button, show info message
  return (
    <div className="text-sm text-zinc-400">
      File System Access API not supported in this browser. Please type the full path.
    </div>
  );
}
```

### Browser Support Matrix

| Browser        | Supported | Notes                                  |
|----------------|-----------|----------------------------------------|
| Chrome 86+     | ✅        | Full support                           |
| Edge 86+       | ✅        | Full support (Chromium-based)          |
| Firefox        | ❌        | Not supported (in development)         |
| Safari         | ❌        | Not supported                          |
| Electron       | ✅        | Full support (uses Chromium)           |

**Recommendation:** Always provide API fallback for Firefox/Safari users.

---

## Security Considerations

### 1. Read-Only Access

```typescript
// ✅ Always use read mode for CodeRef Explorer
await dirHandle.queryPermission({ mode: 'read' });

// ❌ Don't request write permission unless needed
await dirHandle.queryPermission({ mode: 'readwrite' });
```

**Why?**
- Read-only is safer (prevents accidental modifications)
- Faster permission grant (users trust read-only more)
- CodeRef Explorer only needs to read files

### 2. Permission Scope

Permissions are **per-origin**:
- `localhost:3000` has separate permissions from `my-dashboard.app`
- Users must grant permission again when deploying to production

### 3. No Sensitive Directories

```typescript
// Warn users against selecting sensitive folders
const SENSITIVE_PATTERNS = [
  /^C:\\Windows/i,
  /^\/System/,
  /node_modules$/,
  /\.git$/,
];

function isSensitiveDirectory(dirName: string): boolean {
  return SENSITIVE_PATTERNS.some(pattern => pattern.test(dirName));
}

// In ProjectManager component
if (isSensitiveDirectory(dirHandle.name)) {
  toast.warning('Warning: This appears to be a system directory. Proceed with caution.');
}
```

---

## Summary: Implementation Checklist

### Files to Create

- [ ] `packages/dashboard/src/lib/coderef/permissions.ts` - Core permission logic
- [ ] `packages/dashboard/src/lib/coderef/__tests__/permissions.test.ts` - Unit tests

### Core Functions

- [ ] `checkPermission()` - Query permission state
- [ ] `requestPermission()` - Request permission from user
- [ ] `ensurePermission()` - Check + request if needed (recommended)
- [ ] `verifyHandleValidity()` - Check if handle is still valid
- [ ] `isFileSystemAccessSupported()` - Feature detection

### Integration Points

- [ ] `ProjectManager` component - Request permission on project switch
- [ ] `FileTree` component - Check permission before loading tree
- [ ] `FileViewer` component - Handle permission errors on file read
- [ ] `HybridRouter` component - Fallback to API if permission denied

### UX Components

- [ ] Permission prompt UI (pre-browser dialog)
- [ ] Permission denied alert
- [ ] Auto-fallback to API mode (silent)
- [ ] Browser compatibility warning

---

**Next:** See `local-api-patterns.md` for the complete implementation guide (LOCAL-004).
