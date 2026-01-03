# IndexedDB Utilities Patterns

> **Purpose:** Document IndexedDB utilities used by CodeRef Explorer for persisting File System Access API directory handles
>
> **Source:** `C:\Users\willh\Desktop\assistant\web\src\pages\coderef-explorer.html` (lines 460-515)
>
> **Target Implementation:** `packages/dashboard/src/lib/coderef/indexeddb.ts`

---

## Overview

CodeRef Explorer uses IndexedDB to **persist directory handles** between sessions. This allows users to browse a folder once and have access automatically restored on subsequent visits (with permission checks).

### Why IndexedDB?

- **Persistent Storage:** Survives page reloads and browser restarts
- **Native Handle Support:** Can store `FileSystemDirectoryHandle` objects directly
- **Async API:** Non-blocking operations for better UX

---

## Database Schema

```typescript
Database Name: "CodeRefExplorer"
Version: 1
Object Store: "directoryHandles"
  - Key Path: "projectId" (string)
  - Value: { projectId: string, handle: FileSystemDirectoryHandle }
```

### Schema Design Rationale

- **Single Store:** Simple design, one store for all directory handles
- **String Key:** `projectId` matches `Project.id` for easy lookups
- **Handle Storage:** Browser serializes/deserializes handles automatically

---

## Core Operations

### 1. `openDB()` - Open or Create Database

```javascript
function openDB() {
    return new Promise((resolve, reject) => {
        const request = indexedDB.open(DB_NAME, DB_VERSION);

        request.onerror = () => reject(request.error);
        request.onsuccess = () => resolve(request.result);

        request.onupgradeneeded = (event) => {
            const db = event.target.result;
            if (!db.objectStoreNames.contains(STORE_NAME)) {
                db.createObjectStore(STORE_NAME, { keyPath: 'projectId' });
            }
        };
    });
}
```

**Key Points:**
- **Singleton Pattern:** Opens existing DB or creates new one
- **Version Management:** `onupgradeneeded` fires on first run or version bump
- **Error Handling:** Rejects promise on failure
- **Idempotent:** Safe to call multiple times

**React/TypeScript Implementation:**
```typescript
// packages/dashboard/src/lib/coderef/indexeddb.ts
const DB_NAME = 'CodeRefExplorer';
const DB_VERSION = 1;
const STORE_NAME = 'directoryHandles';

export async function openDB(): Promise<IDBDatabase> {
  return new Promise((resolve, reject) => {
    const request = indexedDB.open(DB_NAME, DB_VERSION);

    request.onerror = () => reject(request.error);
    request.onsuccess = () => resolve(request.result);

    request.onupgradeneeded = (event) => {
      const db = (event.target as IDBOpenDBRequest).result;
      if (!db.objectStoreNames.contains(STORE_NAME)) {
        db.createObjectStore(STORE_NAME, { keyPath: 'projectId' });
      }
    };
  });
}
```

---

### 2. `saveDirectoryHandle()` - Persist Directory Handle

```javascript
async function saveDirectoryHandle(projectId, dirHandle) {
    const db = await openDB();
    return new Promise((resolve, reject) => {
        const transaction = db.transaction([STORE_NAME], 'readwrite');
        const store = transaction.objectStore(STORE_NAME);
        const request = store.put({ projectId, handle: dirHandle });

        request.onsuccess = () => resolve();
        request.onerror = () => reject(request.error);
    });
}
```

**Key Points:**
- **Transaction Mode:** `'readwrite'` for write operations
- **put() Method:** Creates or updates record (upsert behavior)
- **Record Structure:** `{ projectId: string, handle: FileSystemDirectoryHandle }`
- **Atomic:** Transaction ensures all-or-nothing semantics

**Usage:**
```javascript
// After user selects folder with showDirectoryPicker
const dirHandle = await window.showDirectoryPicker({ mode: 'read' });
await saveDirectoryHandle('my-project', dirHandle);
```

**React/TypeScript Implementation:**
```typescript
export async function saveDirectoryHandle(
  projectId: string,
  dirHandle: FileSystemDirectoryHandle
): Promise<void> {
  const db = await openDB();
  return new Promise((resolve, reject) => {
    const transaction = db.transaction([STORE_NAME], 'readwrite');
    const store = transaction.objectStore(STORE_NAME);
    const request = store.put({ projectId, handle: dirHandle });

    request.onsuccess = () => resolve();
    request.onerror = () => reject(request.error);
  });
}
```

---

### 3. `getDirectoryHandle()` - Retrieve Directory Handle

```javascript
async function getDirectoryHandle(projectId) {
    const db = await openDB();
    return new Promise((resolve, reject) => {
        const transaction = db.transaction([STORE_NAME], 'readonly');
        const store = transaction.objectStore(STORE_NAME);
        const request = store.get(projectId);

        request.onsuccess = () => resolve(request.result?.handle);
        request.onerror = () => reject(request.error);
    });
}
```

**Key Points:**
- **Transaction Mode:** `'readonly'` for read-only operations (faster)
- **Optional Chaining:** `request.result?.handle` handles missing records gracefully
- **Returns:** `FileSystemDirectoryHandle | undefined`
- **No Side Effects:** Safe to call multiple times

**Usage:**
```javascript
// On page load, try to restore previous directory handle
const dirHandle = await getDirectoryHandle('my-project');
if (dirHandle) {
  // Check permissions before using
  const permission = await dirHandle.queryPermission({ mode: 'read' });
  if (permission === 'granted') {
    // Use handle to build tree
  }
}
```

**React/TypeScript Implementation:**
```typescript
export async function getDirectoryHandle(
  projectId: string
): Promise<FileSystemDirectoryHandle | undefined> {
  const db = await openDB();
  return new Promise((resolve, reject) => {
    const transaction = db.transaction([STORE_NAME], 'readonly');
    const store = transaction.objectStore(STORE_NAME);
    const request = store.get(projectId);

    request.onsuccess = () => resolve(request.result?.handle);
    request.onerror = () => reject(request.error);
  });
}
```

---

### 4. `deleteDirectoryHandle()` - Remove Directory Handle

```javascript
async function deleteDirectoryHandle(projectId) {
    const db = await openDB();
    return new Promise((resolve, reject) => {
        const transaction = db.transaction([STORE_NAME], 'readwrite');
        const store = transaction.objectStore(STORE_NAME);
        const request = store.delete(projectId);

        request.onsuccess = () => resolve();
        request.onerror = () => reject(request.error);
    });
}
```

**Key Points:**
- **Transaction Mode:** `'readwrite'` for delete operations
- **Idempotent:** Safe to delete non-existent keys (no error)
- **Cleanup:** Called when user removes project from UI

**Usage:**
```javascript
// When user clicks "Remove Project"
await deleteDirectoryHandle('my-project');
// Also delete from server: await fetch(`/api/projects/${id}`, { method: 'DELETE' })
```

**React/TypeScript Implementation:**
```typescript
export async function deleteDirectoryHandle(projectId: string): Promise<void> {
  const db = await openDB();
  return new Promise((resolve, reject) => {
    const transaction = db.transaction([STORE_NAME], 'readwrite');
    const store = transaction.objectStore(STORE_NAME);
    const request = store.delete(projectId);

    request.onsuccess = () => resolve();
    request.onerror = () => reject(request.error);
  });
}
```

---

## Integration Pattern: Hybrid Storage

### Option D Architecture

**Concept:** Single "Browse Folder" action stores **BOTH**:
1. Directory handle in IndexedDB (local access)
2. Project metadata via API (server-side persistence)

```javascript
async function confirmAddProject() {
    const name = document.getElementById('projectName').value.trim();
    const dirHandle = pendingDirectoryHandle; // From showDirectoryPicker

    const id = name.toLowerCase().replace(/\s+/g, '-');

    if (dirHandle) {
        // 1. Save directory handle to IndexedDB
        await saveDirectoryHandle(id, dirHandle);

        // 2. Save project metadata to server
        const project = { id, name, path: `[Directory: ${dirHandle.name}]` };
        await fetch('/api/projects', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(project)
        });

        // 3. UI feedback
        showToast('Project added and persisted!');
    }
}
```

**Benefits:**
- **Local-first:** Instant access if handle still valid
- **API Fallback:** If permissions revoked, fall back to server mode
- **Single UX:** User doesn't choose local vs API mode

---

## Permission Handling

### Check and Request Permissions

```javascript
async function changeProject(projectId) {
    // Try to get directory handle from IndexedDB
    const dirHandle = await getDirectoryHandle(projectId);

    if (dirHandle) {
        // 1. Check current permission state
        const permission = await dirHandle.queryPermission({ mode: 'read' });

        if (permission === 'granted') {
            // ✅ Permission already granted
            await buildTreeFromDirectoryHandle(dirHandle);
            return;
        } else if (permission === 'prompt') {
            // ⚠️ Need to request permission
            const newPermission = await dirHandle.requestPermission({ mode: 'read' });
            if (newPermission === 'granted') {
                await buildTreeFromDirectoryHandle(dirHandle);
                return;
            }
        }

        // ❌ Permission denied, fall through to server mode
        showToast('Permission denied. Please re-add this project.');
    }

    // Fallback: Load from server API
    loadFromServerAPI(projectId);
}
```

**Permission States:**
- `'granted'` - User previously granted access, handle is ready to use
- `'prompt'` - Need to call `requestPermission()` to show browser prompt
- `'denied'` - User explicitly denied access, cannot use handle

---

## Error Handling Best Practices

### 1. Database Open Failures

```typescript
try {
  const db = await openDB();
} catch (error) {
  console.error('Failed to open IndexedDB:', error);
  // Fallback: Disable local mode, use API only
  return { mode: 'api', error: 'IndexedDB unavailable' };
}
```

### 2. Transaction Failures

```typescript
try {
  await saveDirectoryHandle(projectId, dirHandle);
} catch (error) {
  console.error('Failed to save directory handle:', error);
  showToast('Warning: Local access may not persist across sessions');
  // Continue with in-memory handle only
}
```

### 3. Handle Invalidation

```typescript
try {
  const dirHandle = await getDirectoryHandle(projectId);
  if (!dirHandle) {
    // No handle stored, prompt user to browse folder
    return null;
  }

  // Handle exists, but might be stale (user deleted folder, etc.)
  await dirHandle.queryPermission({ mode: 'read' });
  return dirHandle;
} catch (error) {
  console.error('Directory handle is stale:', error);
  // Clean up invalid handle
  await deleteDirectoryHandle(projectId);
  return null;
}
```

---

## Testing Checklist

### Manual Testing

- [ ] **First Run:** Open app, IndexedDB database is created automatically
- [ ] **Browse Folder:** Click "Browse Folder", select directory, handle is saved
- [ ] **Page Reload:** Refresh browser, directory tree loads from IndexedDB
- [ ] **Permission Prompt:** Revoke permission manually, next access shows prompt
- [ ] **Permission Denial:** Click "Deny" on prompt, app falls back to API mode
- [ ] **Remove Project:** Delete project, handle is removed from IndexedDB
- [ ] **Multiple Projects:** Add 3+ projects, each has separate handle storage
- [ ] **Stale Handle:** Delete folder from file system, handle becomes invalid

### Browser DevTools

```javascript
// Inspect IndexedDB in Chrome DevTools
// Application > Storage > IndexedDB > CodeRefExplorer > directoryHandles

// Clear all data (for testing)
indexedDB.deleteDatabase('CodeRefExplorer');

// Check for stuck transactions
// Application > IndexedDB > Right-click > "Clear"
```

---

## React Hook Pattern (Recommended)

### Custom Hook: `useIndexedDB`

```typescript
// packages/dashboard/src/lib/coderef/hooks/useIndexedDB.ts
import { useState, useCallback } from 'react';
import {
  openDB,
  saveDirectoryHandle,
  getDirectoryHandle,
  deleteDirectoryHandle,
} from '../indexeddb';

export function useIndexedDB() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<Error | null>(null);

  const save = useCallback(
    async (projectId: string, handle: FileSystemDirectoryHandle) => {
      setLoading(true);
      setError(null);
      try {
        await saveDirectoryHandle(projectId, handle);
      } catch (err) {
        setError(err as Error);
      } finally {
        setLoading(false);
      }
    },
    []
  );

  const get = useCallback(async (projectId: string) => {
    setLoading(true);
    setError(null);
    try {
      return await getDirectoryHandle(projectId);
    } catch (err) {
      setError(err as Error);
      return undefined;
    } finally {
      setLoading(false);
    }
  }, []);

  const remove = useCallback(async (projectId: string) => {
    setLoading(true);
    setError(null);
    try {
      await deleteDirectoryHandle(projectId);
    } catch (err) {
      setError(err as Error);
    } finally {
      setLoading(false);
    }
  }, []);

  return { save, get, remove, loading, error };
}
```

**Usage in Component:**
```typescript
function ProjectManager() {
  const { save, get, remove } = useIndexedDB();

  const handleBrowseFolder = async () => {
    const dirHandle = await window.showDirectoryPicker({ mode: 'read' });
    await save('my-project', dirHandle);
  };

  return <button onClick={handleBrowseFolder}>Browse Folder</button>;
}
```

---

## Summary

### What Agent 2 Needs to Implement

1. **Core File:** `packages/dashboard/src/lib/coderef/indexeddb.ts`
   - `openDB()` - Database initialization
   - `saveDirectoryHandle()` - Persist handles
   - `getDirectoryHandle()` - Retrieve handles
   - `deleteDirectoryHandle()` - Clean up handles

2. **React Hook:** `packages/dashboard/src/lib/coderef/hooks/useIndexedDB.ts`
   - Wrapper for React components
   - Loading/error state management

3. **Integration Points:**
   - `ProjectManager` component: Save handles on "Browse Folder"
   - `FileTree` component: Load handle on project switch
   - `ProjectSelector` component: Delete handle on "Remove Project"

### Expected Deliverables

- [ ] `indexeddb.ts` with 4 core functions
- [ ] `useIndexedDB.ts` React hook
- [ ] Unit tests for all operations
- [ ] Integration tests with File System API
- [ ] Error handling for permission failures

---

**Next:** See `local-api-patterns.md` for File System Access API implementation patterns (Phase 3 handoff).
