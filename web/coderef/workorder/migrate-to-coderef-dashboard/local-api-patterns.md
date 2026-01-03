# Local API Implementation Guide

> **Phase 3 Handoff Document**
>
> **From:** Agent 1 (Source Code Extraction & Documentation)
>
> **To:** Agent 2 (React/Next.js Implementation in Dashboard)
>
> **Purpose:** Complete implementation guide for File System Access API integration

---

## 📋 Overview

This guide provides **everything Agent 2 needs** to implement local mode (File System Access API) in the CodeRef Dashboard. It consolidates:

1. TypeScript type definitions
2. IndexedDB utilities
3. File System API logic
4. Permission handling
5. React component patterns

---

## 📂 File Structure

### Files Agent 2 Must Create

```
packages/dashboard/src/
├── lib/coderef/
│   ├── types.ts                  ✅ Use template from workorder folder
│   ├── indexeddb.ts               ✅ Implement from indexeddb-patterns.md
│   ├── local-access.ts            ✅ Implement from file-system-api-logic-extraction.md
│   ├── permissions.ts             ✅ Implement from permission-checking-patterns.md
│   └── __tests__/
│       ├── indexeddb.test.ts
│       ├── local-access.test.ts
│       └── permissions.test.ts
├── components/coderef/
│   ├── ProjectManager.tsx         ✅ Implement from project-manager-requirements.md
│   └── __tests__/
│       └── ProjectManager.test.tsx
└── app/api/coderef/
    └── ... (Agent 2's Phase 4 work)
```

---

## 🔧 Step-by-Step Implementation

### Step 1: Copy Type Definitions

**File:** `packages/dashboard/src/lib/coderef/types.ts`

**Action:** Copy verbatim from workorder folder:
```bash
cp coderef/workorder/migrate-to-coderef-dashboard/types.ts \
   packages/dashboard/src/lib/coderef/types.ts
```

**Also add:** `file-system-api-types.d.ts` to project root or `src/types/` directory

---

### Step 2: Implement IndexedDB Utilities

**File:** `packages/dashboard/src/lib/coderef/indexeddb.ts`

**Reference:** `indexeddb-patterns.md`

**Core Functions:**
```typescript
export async function openDB(): Promise<IDBDatabase>;
export async function saveDirectoryHandle(
  projectId: string,
  dirHandle: FileSystemDirectoryHandle
): Promise<void>;
export async function getDirectoryHandle(
  projectId: string
): Promise<FileSystemDirectoryHandle | undefined>;
export async function deleteDirectoryHandle(
  projectId: string
): Promise<void>;
```

**Test Coverage:**
- Database creation
- Handle save/retrieve
- Handle deletion
- Concurrent access
- Error handling

---

### Step 3: Implement File System Access Logic

**File:** `packages/dashboard/src/lib/coderef/local-access.ts`

**Reference:** `file-system-api-logic-extraction.md`

**Core Functions:**
```typescript
export async function showDirectoryPicker(): Promise<FileSystemDirectoryHandle | null>;

export async function buildTreeFromHandle(
  dirHandle: FileSystemDirectoryHandle,
  parentPath?: string
): Promise<TreeNode>;

export async function loadFileFromHandle(
  fileHandle: FileSystemFileHandle
): Promise<FileInfo>;

export async function getFileHandleByPath(
  dirHandle: FileSystemDirectoryHandle,
  relativePath: string
): Promise<FileSystemFileHandle | null>;
```

**Test Coverage:**
- Directory picker (mock window.showDirectoryPicker)
- Tree building (recursive)
- File loading
- Path traversal
- Error handling (AbortError, permission denied)

---

### Step 4: Implement Permission Management

**File:** `packages/dashboard/src/lib/coderef/permissions.ts`

**Reference:** `permission-checking-patterns.md`

**Core Functions:**
```typescript
export async function checkPermission(
  dirHandle: FileSystemDirectoryHandle,
  mode?: 'read' | 'readwrite'
): Promise<PermissionCheckResult>;

export async function requestPermission(
  dirHandle: FileSystemDirectoryHandle,
  mode?: 'read' | 'readwrite'
): Promise<boolean>;

export async function ensurePermission(
  dirHandle: FileSystemDirectoryHandle,
  mode?: 'read' | 'readwrite'
): Promise<boolean>;

export function isFileSystemAccessSupported(): boolean;
```

**Test Coverage:**
- Permission state checks ('granted', 'prompt', 'denied')
- Permission requests
- Feature detection
- Error handling (stale handles)

---

### Step 5: Implement ProjectManager Component

**File:** `packages/dashboard/src/components/coderef/ProjectManager.tsx`

**Reference:** `project-manager-requirements.md`

**Key Requirements:**
- ✅ `'use client'` directive at top of file
- ✅ Project selector dropdown
- ✅ "Add Project" button → modal
- ✅ "Remove Project" button
- ✅ "Browse Folder" flow (hybrid storage)

**Critical Flow:**
```typescript
// In "Browse Folder" handler
const dirHandle = await showDirectoryPicker();
if (dirHandle) {
  // 1. Save to IndexedDB
  await saveDirectoryHandle(projectId, dirHandle);

  // 2. Save to API
  await fetch('/api/coderef/projects', {
    method: 'POST',
    body: JSON.stringify({ id, name, path: `[Directory: ${dirHandle.name}]` })
  });

  // 3. Update UI
  onProjectChange(newProject);
}
```

**Test Coverage:**
- Load projects on mount
- Project selection
- Add project (typed path)
- Add project (browsed folder)
- Remove project
- Form validation
- Modal open/close

---

## 🔀 Hybrid Mode Integration

### Option D Architecture

**Concept:** Single "Browse Folder" action performs **dual storage**:

```typescript
// packages/dashboard/src/lib/coderef/hybrid-router.ts

export async function loadProjectTree(
  project: Project
): Promise<{ tree: TreeNode; mode: 'local' | 'api' }> {
  // Step 1: Try local mode first
  if (project.path.startsWith('[Directory:')) {
    const dirHandle = await getDirectoryHandle(project.id);

    if (dirHandle) {
      const hasPermission = await ensurePermission(dirHandle);

      if (hasPermission) {
        // ✅ Local mode succeeded
        const tree = await buildTreeFromHandle(dirHandle);
        return { tree, mode: 'local' };
      }
    }
  }

  // Step 2: Fallback to API mode
  const response = await fetch(`/api/coderef/tree?projectId=${project.id}`);
  const tree = await response.json();
  return { tree, mode: 'api' };
}
```

**Benefits:**
- **Transparent:** User doesn't choose local vs API
- **Resilient:** Auto-fallback if permissions revoked
- **Fast:** Local mode is instant, API is reliable backup

---

## 🧪 Testing Strategy

### Unit Tests

**IndexedDB:**
```typescript
// packages/dashboard/src/lib/coderef/__tests__/indexeddb.test.ts

import { openDB, saveDirectoryHandle, getDirectoryHandle } from '../indexeddb';

describe('IndexedDB utilities', () => {
  beforeEach(() => {
    // Mock IndexedDB
    global.indexedDB = require('fake-indexeddb');
  });

  test('saveDirectoryHandle stores handle', async () => {
    const mockHandle = {} as FileSystemDirectoryHandle;
    await saveDirectoryHandle('test-project', mockHandle);

    const retrieved = await getDirectoryHandle('test-project');
    expect(retrieved).toBe(mockHandle);
  });
});
```

**Local Access:**
```typescript
// packages/dashboard/src/lib/coderef/__tests__/local-access.test.ts

import { showDirectoryPicker, buildTreeFromHandle } from '../local-access';

describe('File System Access API', () => {
  test('showDirectoryPicker returns handle', async () => {
    // Mock window.showDirectoryPicker
    global.window.showDirectoryPicker = jest.fn().mockResolvedValue({
      name: 'test-folder',
      kind: 'directory',
    });

    const handle = await showDirectoryPicker();
    expect(handle).toBeDefined();
    expect(handle?.name).toBe('test-folder');
  });

  test('buildTreeFromHandle creates correct structure', async () => {
    const mockDirHandle = {
      name: 'root',
      kind: 'directory',
      values: jest.fn().mockImplementation(async function* () {
        yield { name: 'file.txt', kind: 'file' };
        yield { name: 'subfolder', kind: 'directory', values: jest.fn().mockImplementation(async function* () {}) };
      }),
    } as unknown as FileSystemDirectoryHandle;

    const tree = await buildTreeFromHandle(mockDirHandle);

    expect(tree.name).toBe('root');
    expect(tree.children).toHaveLength(2);
    expect(tree.children?.[0].type).toBe('folder'); // Folders first
    expect(tree.children?.[1].type).toBe('file');
  });
});
```

### Integration Tests

**Component Testing:**
```typescript
// packages/dashboard/src/components/coderef/__tests__/ProjectManager.test.tsx

import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { ProjectManager } from '../ProjectManager';

describe('ProjectManager', () => {
  test('loads projects from API', async () => {
    global.fetch = jest.fn().mockResolvedValue({
      json: async () => ({
        success: true,
        data: [{ id: 'test', name: 'Test Project', path: '/test' }],
      }),
    });

    render(<ProjectManager onProjectChange={jest.fn()} />);

    await waitFor(() => {
      expect(screen.getByText('Test Project')).toBeInTheDocument();
    });
  });

  test('browse folder opens directory picker', async () => {
    const mockHandle = { name: 'my-folder' };
    global.window.showDirectoryPicker = jest.fn().mockResolvedValue(mockHandle);

    render(<ProjectManager onProjectChange={jest.fn()} />);

    // Open modal
    fireEvent.click(screen.getByTitle('Add new project'));

    // Click browse button
    fireEvent.click(screen.getByText('Browse'));

    await waitFor(() => {
      expect(window.showDirectoryPicker).toHaveBeenCalled();
      expect(screen.getByDisplayValue('[Directory: my-folder]')).toBeInTheDocument();
    });
  });
});
```

### Manual Testing Checklist

- [ ] **Feature Detection:** Open in Chrome → File System API available
- [ ] **Feature Detection:** Open in Firefox → API fallback enabled
- [ ] **Browse Folder:** Click "Browse Folder" → directory picker opens
- [ ] **Permission Grant:** Select folder → permission automatically granted → tree builds
- [ ] **Page Reload:** Reload page → select project → permission prompt appears
- [ ] **Permission Request:** Click "Allow" on prompt → tree builds
- [ ] **Permission Denied:** Click "Deny" on prompt → fallback to API mode
- [ ] **Project Remove:** Delete project → IndexedDB handle removed
- [ ] **Stale Handle:** Delete folder from file system → graceful error handling

---

## 🚨 Common Pitfalls

### 1. Missing 'use client' Directive

**Error:**
```
ReferenceError: window is not defined
```

**Fix:** Add `'use client';` at the top of any component using File System API

---

### 2. Not Checking Permissions

**Error:** File read fails silently after page reload

**Fix:** Always use `ensurePermission()` before accessing handles from IndexedDB

---

### 3. Storing File Handles

**Error:** `DOMException: Failed to execute 'put' on 'IDBObjectStore'`

**Fix:** Only store **directory handles** in IndexedDB, not file handles. Use path traversal to get file handles.

---

### 4. Sync vs Async Iteration

**Error:**
```typescript
for (const entry of dirHandle.values()) { // ❌ Wrong
  // ...
}
```

**Fix:**
```typescript
for await (const entry of dirHandle.values()) { // ✅ Correct
  // ...
}
```

---

### 5. AbortError Handling

**Error:** Uncaught error when user cancels directory picker

**Fix:**
```typescript
try {
  const handle = await window.showDirectoryPicker();
} catch (error) {
  if (error.name === 'AbortError') {
    // User cancelled, not an error
    return null;
  }
  throw error;
}
```

---

## 📊 Performance Considerations

### 1. Tree Building

**Slow:**
```typescript
// Recursively building entire tree upfront
const tree = await buildTreeFromHandle(dirHandle); // 5-10 seconds for large projects
```

**Fast:**
```typescript
// Lazy-load tree nodes on expand
const rootChildren = await getDirectoryChildren(dirHandle); // < 100ms
// Only load subdirectories when user expands folder
```

**Recommendation:** For MVP, build full tree upfront (simpler). Optimize later if needed.

---

### 2. File Reading

**Slow:**
```typescript
// Reading all files on tree build
const files = await Promise.all(fileHandles.map(h => h.getFile()));
```

**Fast:**
```typescript
// Only read file when user clicks
onClick={async () => {
  const file = await fileHandle.getFile();
  const content = await file.text();
}}
```

**Recommendation:** Only read files on-demand (current app behavior).

---

### 3. IndexedDB Access

**Slow:**
```typescript
// Opening DB on every operation
async function getHandle(id: string) {
  const db = await openDB(); // Opens DB each time
  // ...
}
```

**Fast:**
```typescript
// Keep DB connection open
let db: IDBDatabase | null = null;

async function openDB() {
  if (!db) {
    db = await indexedDB.open('CodeRefExplorer', 1);
  }
  return db;
}
```

**Recommendation:** Use simple approach (open on each call) for MVP. Optimize later if needed.

---

## 🔐 Security Best Practices

### 1. Read-Only Mode

Always use `mode: 'read'` unless write access is explicitly needed:

```typescript
await dirHandle.requestPermission({ mode: 'read' }); // ✅ Recommended
await dirHandle.requestPermission({ mode: 'readwrite' }); // ❌ Avoid
```

### 2. Sensitive Directory Warning

```typescript
const SENSITIVE_PATTERNS = [
  /^C:\\Windows/i,
  /^\/System/,
  /^C:\\Program Files/i,
];

if (SENSITIVE_PATTERNS.some(p => p.test(dirHandle.name))) {
  toast.warning('Warning: This is a system directory. Proceed with caution.');
}
```

### 3. Path Validation

```typescript
function isValidRelativePath(path: string): boolean {
  // Prevent directory traversal attacks
  return !path.includes('..') && !path.startsWith('/');
}
```

---

## 📦 Dependencies

### NPM Packages

```json
{
  "dependencies": {
    "@radix-ui/react-dialog": "^1.0.0", // Modal (ProjectManager)
    "lucide-react": "^0.300.0",          // Icons
    "react-hot-toast": "^2.4.0"          // Notifications
  },
  "devDependencies": {
    "@types/wicg-file-system-access": "^2023.10.0", // TypeScript types
    "fake-indexeddb": "^5.0.0",          // IndexedDB testing
    "@testing-library/react": "^14.0.0"  // Component testing
  }
}
```

---

## ✅ Phase 3 Deliverables Checklist

### Files Created by Agent 1 (✅ Complete)

- [x] `file-system-api-types.d.ts` - TypeScript API definitions
- [x] `types.ts` - Shared data structures
- [x] `indexeddb-patterns.md` - IndexedDB implementation guide
- [x] `file-system-api-logic-extraction.md` - Core File System API patterns
- [x] `permission-checking-patterns.md` - Permission flow documentation
- [x] `project-manager-requirements.md` - ProjectManager component spec
- [x] `local-api-patterns.md` - This comprehensive guide

### Files to be Created by Agent 2 (⏳ Pending)

- [ ] `lib/coderef/types.ts` (copy from template)
- [ ] `lib/coderef/indexeddb.ts` (implement 4 functions)
- [ ] `lib/coderef/local-access.ts` (implement 4 functions)
- [ ] `lib/coderef/permissions.ts` (implement 4 functions)
- [ ] `components/coderef/ProjectManager.tsx` (full component)
- [ ] Unit tests for all modules
- [ ] Integration tests for ProjectManager

---

## 🎯 Agent 2 Next Steps

### Phase 3 Complete (Agent 1)

Agent 1 has extracted and documented all File System API patterns. Phase 3 deliverables are ready for handoff.

### Phase 5 Dependencies (Agent 2)

Before starting Phase 5 (Hybrid Mode Logic), Agent 2 must:

1. **Complete Phase 4:** Implement Next.js API routes
2. **Receive Phase 3 Handoff:** Review all documentation files in workorder folder
3. **Implement Local Access:** Create `indexeddb.ts`, `local-access.ts`, `permissions.ts`
4. **Implement ProjectManager:** Create component with hybrid storage
5. **Test Integration:** Verify local mode works end-to-end

### Phase 5 Goal

Create `hybrid-router.ts` that intelligently routes between:
- **Local mode** (File System API + IndexedDB)
- **API mode** (Next.js routes)

With automatic fallback if permissions are denied.

---

## 📞 Support

**Questions?** Refer to:
- `file-system-api-logic-extraction.md` - Core API patterns
- `permission-checking-patterns.md` - Permission flow
- `indexeddb-patterns.md` - Storage patterns
- `project-manager-requirements.md` - UI component spec

**Issues?**
- Check browser compatibility (Chrome/Edge only)
- Verify 'use client' directive is present
- Test with browser DevTools (Application > Storage)

---

## 🎉 Summary

Agent 1 has completed **Phase 3: File System API Extraction** with 7 comprehensive documentation files. Agent 2 now has everything needed to implement local mode in the dashboard.

**Key Achievements:**
- ✅ Full TypeScript type definitions
- ✅ IndexedDB utilities patterns
- ✅ File System API logic extraction
- ✅ Permission management patterns
- ✅ ProjectManager component requirements
- ✅ Hybrid mode architecture design

**Agent 2 can now:**
- Implement all local-mode functionality
- Create ProjectManager component
- Integrate with Phase 4 API routes (parallel work)
- Build Phase 5 hybrid router

---

**🚀 Ready for Agent 2 to begin implementation!**
