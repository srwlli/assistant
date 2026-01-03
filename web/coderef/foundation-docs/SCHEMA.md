# Data Schema

**Version:** 1.0.0
**Last Updated:** 2025-12-28

---

## Overview

CodeRef Explorer uses three data storage mechanisms:

1. **File-based storage** - `projects.json` for project metadata
2. **IndexedDB** - Browser database for File System Access API handles
3. **LocalStorage** - Client-side preferences (theme)

This document defines the complete data schema, relationships, and storage patterns.

---

## Data Stores

### 1. projects.json

**Location:** Root directory (`./projects.json`)
**Format:** JSON array
**Purpose:** Persistent storage of project metadata

**Schema:**
```json
[
  {
    "id": "string",
    "name": "string",
    "path": "string"
  }
]
```

**Example:**
```json
[
  {
    "id": "project-abc123",
    "name": "My Codebase",
    "path": "/Users/name/projects/my-codebase"
  },
  {
    "id": "coderef-dashboard",
    "name": "CodeRef Dashboard",
    "path": "[Directory: coderef-dashboard]"
  }
]
```

**Constraints:**
- `id` must be unique across all projects
- `path` can be:
  - Absolute file system path (e.g., `/Users/name/project`)
  - Directory handle token (format: `[Directory: {name}]`)
- Empty array `[]` is valid (no projects)

---

### 2. IndexedDB

**Database Name:** `CodeRefExplorer`
**Version:** 1
**Object Stores:**

#### directoryHandles

**Purpose:** Store File System Access API directory handles for persistent access

**Schema:**
```
keyPath: "id"
indexes: none
```

**Record Structure:**
```javascript
{
  id: string,           // Must match Project.id
  handle: FileSystemDirectoryHandle  // Browser API object (not serializable)
}
```

**Example Operations:**

```javascript
// Save
await store.put({
  id: 'project-abc123',
  handle: dirHandleFromPicker
});

// Retrieve
const record = await store.get('project-abc123');
const dirHandle = record.handle;

// Delete
await store.delete('project-abc123');
```

**Lifecycle:**
- Created on database upgrade (`onupgradeneeded`)
- Records persist across browser sessions
- Handles may require permission re-validation

---

### 3. LocalStorage

**Namespace:** Browser default
**Keys:**

| Key | Type | Values | Default | Description |
|-----|------|--------|---------|-------------|
| `theme` | string | `'dark'` \| `'light'` | `'dark'` | UI theme preference |

**Example:**
```javascript
localStorage.setItem('theme', 'light');
const theme = localStorage.getItem('theme') || 'dark';
```

---

## Data Models

### Project

**Description:** Represents a single project/folder being browsed

**Fields:**

| Field | Type | Required | Constraints | Description |
|-------|------|----------|-------------|-------------|
| `id` | string | Yes | Unique, alphanumeric + hyphens | Unique project identifier |
| `name` | string | Yes | 1-255 characters | Display name shown in UI |
| `path` | string | Yes | Absolute path or handle token | File system location |

**Validation Rules:**
- `id`: Must be unique in `projects.json`
- `name`: Cannot be empty
- `path`: Must exist (server validates unless it's a handle token)

**Example:**
```javascript
const project = {
  id: 'coderef-docs-123',
  name: 'CodeRef Documentation',
  path: '/Users/will/projects/coderef-docs'
};
```

**Path Formats:**
```javascript
// Absolute path (validated by server)
path: "/Users/name/project"
path: "C:\\Users\\name\\project"

// Directory handle token (not validated)
path: "[Directory: project-name]"
```

---

### DirectoryHandle Record

**Description:** IndexedDB record linking project ID to File System Access API handle

**Fields:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | Yes | Project ID (foreign key) |
| `handle` | FileSystemDirectoryHandle | Yes | Browser API object |

**Relationships:**
- `id` references `Project.id` (1:1)
- Handle object cannot be serialized to JSON

**Permissions:**
```javascript
// Query permission state
const permission = await handle.queryPermission({ mode: 'read' });
// Returns: 'granted' | 'denied' | 'prompt'

// Request permission
const result = await handle.requestPermission({ mode: 'read' });
// Returns: 'granted' | 'denied'
```

---

### TreeNode

**Description:** Recursive file/folder tree structure returned by `/api/tree` endpoint

**Fields:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | Yes | File or folder name (basename) |
| `path` | string | Yes | Absolute file system path |
| `type` | string | Yes | `'file'` or `'folder'` |
| `children` | TreeNode[] | Conditional | Present only if `type === 'folder'` |

**Example:**
```javascript
const tree = {
  name: 'src',
  path: '/Users/name/project/src',
  type: 'folder',
  children: [
    {
      name: 'components',
      path: '/Users/name/project/src/components',
      type: 'folder',
      children: [
        {
          name: 'Button.js',
          path: '/Users/name/project/src/components/Button.js',
          type: 'file'
        }
      ]
    },
    {
      name: 'index.js',
      path: '/Users/name/project/src/index.js',
      type: 'file'
    }
  ]
};
```

**Traversal Pattern:**
```javascript
function walkTree(node, callback) {
  callback(node);

  if (node.type === 'folder' && node.children) {
    node.children.forEach(child => walkTree(child, callback));
  }
}
```

---

### FileInfo

**Description:** File content and metadata returned by `/api/file` endpoint

**Fields:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `content` | string | Yes | UTF-8 decoded file content |
| `name` | string | Yes | File basename |
| `size` | number | Yes | File size in bytes |
| `modified` | number | Yes | Unix timestamp (seconds since epoch) |

**Example:**
```javascript
const fileInfo = {
  content: '# README\n\nThis is my project.',
  name: 'README.md',
  size: 1024,
  modified: 1703721600.0
};
```

**Size Limits:**
- No enforced maximum
- Large files (>10MB) may cause browser performance issues

---

## Relationships

### Entity Relationship Diagram

```
┌─────────────────┐
│    projects     │
│   (projects.json)│
├─────────────────┤
│ id (PK)         │
│ name            │
│ path            │
└────────┬────────┘
         │
         │ 1:1 (optional)
         │
         ▼
┌─────────────────────────┐
│   directoryHandles      │
│   (IndexedDB)           │
├─────────────────────────┤
│ id (PK, FK)             │
│ handle                  │
│  (FileSystemDirectory   │
│   Handle)               │
└─────────────────────────┘
```

**Relationships:**
- **Project → DirectoryHandle**: One-to-One (optional)
  - A project MAY have a directory handle
  - Handle only exists if project was added via File System Access API
  - Server-based projects (typed paths) have no handle

---

## Data Access Patterns

### Loading Projects on Startup

```javascript
// 1. Fetch from server
const response = await fetch('/api/projects');
const projects = await response.json();

// 2. For each project, check for directory handle
for (const project of projects) {
  const handle = await getDirectoryHandle(project.id);

  if (handle) {
    // Use File System Access API
    const permission = await handle.queryPermission({ mode: 'read' });
    if (permission === 'granted') {
      await buildTreeFromDirectoryHandle(handle);
    }
  } else if (!project.path.startsWith('[Directory:')) {
    // Fall back to server API
    const tree = await fetch(`/api/tree?path=${project.path}`).then(r => r.json());
    renderServerTree(tree);
  }
}
```

### Adding a New Project

**Via File System Access API (Browser):**
```javascript
// 1. Show directory picker
const dirHandle = await window.showDirectoryPicker({ mode: 'read' });

// 2. Generate project ID
const projectId = `project-${Date.now()}`;

// 3. Save directory handle to IndexedDB
await saveDirectoryHandle(projectId, dirHandle);

// 4. Save project metadata to server
const project = {
  id: projectId,
  name: dirHandle.name,
  path: `[Directory: ${dirHandle.name}]`
};
await fetch('/api/projects', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify(project)
});
```

**Via Manual Path Entry (Server):**
```javascript
// 1. User enters path in form
const projectPath = '/Users/name/my-project';

// 2. Generate project ID
const projectId = `project-${Date.now()}`;

// 3. Save to server (server validates path exists)
const project = {
  id: projectId,
  name: 'My Project',
  path: projectPath
};
await fetch('/api/projects', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify(project)
});

// No IndexedDB storage needed
```

### Removing a Project

```javascript
// 1. Delete from server
await fetch(`/api/projects/${projectId}`, { method: 'DELETE' });

// 2. Delete directory handle from IndexedDB
await deleteDirectoryHandle(projectId);

// 3. Reload project list
await loadProjects();
```

---

## Data Migration

**Current Version:** 1
**Migration History:** None (initial version)

**Future Migrations:**

If schema changes are needed:

1. Increment IndexedDB version
2. Handle `onupgradeneeded` event
3. Migrate existing records

**Example:**
```javascript
request.onupgradeneeded = (event) => {
  const db = event.target.result;
  const oldVersion = event.oldVersion;

  if (oldVersion < 1) {
    // Create initial stores
    db.createObjectStore('directoryHandles', { keyPath: 'id' });
  }

  if (oldVersion < 2) {
    // Add new store or modify existing
    db.createObjectStore('settings', { keyPath: 'key' });
  }
};
```

---

## Data Validation

### Server-Side Validation (Python)

**Project Creation (`POST /api/projects`):**

```python
# Required fields
if 'id' not in project or 'name' not in project or 'path' not in project:
    return 400  # Bad Request

# Path validation (skip for directory handles)
if not project['path'].startswith('[Directory:'):
    if not os.path.exists(project['path']):
        return 400  # Bad Request
```

**File Access (`GET /api/file?path=...`):**

```python
if not os.path.exists(file_path):
    return 404  # Not Found
```

### Client-Side Validation

**Before Saving Project:**
```javascript
function validateProject(project) {
  if (!project.id || project.id.trim() === '') {
    throw new Error('Project ID is required');
  }

  if (!project.name || project.name.trim() === '') {
    throw new Error('Project name is required');
  }

  if (!project.path || project.path.trim() === '') {
    throw new Error('Project path is required');
  }
}
```

---

## Performance Considerations

### IndexedDB

- **Read performance:** O(1) for key-based lookups
- **Write performance:** Asynchronous, non-blocking
- **Storage limit:** Varies by browser (typically 50% of available disk space per origin)

### projects.json

- **Read:** Full file loaded into memory on each request
- **Write:** Entire array serialized to disk
- **Scaling:** Recommend max 100-200 projects before refactoring to database

### File System Access API

- **Permission checks:** Cached per session
- **Directory traversal:** Recursive, can be slow for large folders (1000+ files)
- **File reads:** Streamed, memory-efficient

---

## Implementation References

**IndexedDB Operations:** `src/pages/coderef-explorer.html:464-514`
**Project Model:** `projects.json:1-7`
**Server Validation:** `server.py:80-89`
**TreeNode Building:** `server.py:174-200`
**FileInfo Response:** `server.py:164-170`

---

## AI Agent Notes

**For autonomous agents working with this schema:**

1. **Adding fields to Project model:**
   - Update `projects.json` structure
   - Add server-side validation in `server.py:80-89`
   - Update client-side rendering in `coderef-explorer.html:558-580`

2. **Adding new data stores:**
   - For persistent data: Add IndexedDB object store
   - For temporary data: Use in-memory JavaScript variables
   - For user preferences: Use LocalStorage

3. **Schema versioning:**
   - Increment IndexedDB version number
   - Implement migration in `onupgradeneeded` handler
   - Document changes in this file's Migration History section

4. **Testing data integrity:**
   - Verify `projects.json` is valid JSON
   - Test IndexedDB with browser DevTools (Application tab)
   - Check LocalStorage in browser DevTools (Storage tab)

---

_Generated with CodeRef foundation documentation system._
