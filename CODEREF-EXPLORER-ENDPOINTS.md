# Coderef Folder Explorer - Endpoint Architecture

**Purpose:** Wire coderef folders from all projects into dashboard for browsing and exploration
**Route:** `/coderef-assistant`
**Backend:** coderef-dashboard MCP server (Python)
**Frontend:** html-tools `/coderef-assistant` route (JavaScript)

---

## Core Concept

1. **Projects Registry** - User can add/remove projects
2. **Multi-Project Scanning** - Discover all coderef folders across projects
3. **Unified Endpoint** - Single API gateway to explore all coderefs
4. **Dynamic Updates** - Adding new project = immediately accessible via API

---

## Endpoint Specifications

### 1. GET `/api/coderef/projects`

**Purpose:** List all registered projects with coderef folders

**Response:**
```json
{
  "projects": [
    {
      "project_id": "assistant",
      "project_name": "Orchestrator",
      "project_path": "C:\\Users\\willh\\Desktop\\assistant",
      "coderef_path": "C:\\Users\\willh\\Desktop\\assistant\\coderef",
      "has_coderef": true,
      "coderef_folders": ["working", "workorder", "archived", "standards"],
      "status": "active",
      "added_date": "2025-12-27T10:00:00Z"
    },
    {
      "project_id": "mcp-coderef-workflow",
      "project_name": "CodeRef Workflow MCP",
      "project_path": "C:\\Users\\willh\\.mcp-servers\\coderef-workflow",
      "coderef_path": "C:\\Users\\willh\\.mcp-servers\\coderef-workflow\\coderef",
      "has_coderef": true,
      "coderef_folders": ["workorder", "archived"],
      "status": "active",
      "added_date": "2025-12-25T14:30:00Z"
    },
    {
      "project_id": "mcp-coderef-context",
      "project_name": "CodeRef Context MCP",
      "project_path": "C:\\Users\\willh\\.mcp-servers\\coderef-context",
      "coderef_path": "C:\\Users\\willh\\.mcp-servers\\coderef-context\\coderef",
      "has_coderef": false,
      "coderef_folders": [],
      "status": "active",
      "added_date": "2025-12-25T14:00:00Z"
    }
  ],
  "total_projects": 6,
  "projects_with_coderef": 4,
  "total_coderef_items": 127
}
```

---

### 2. POST `/api/coderef/projects`

**Purpose:** Register a new project for coderef exploration

**Request:**
```json
{
  "project_path": "C:\\Users\\willh\\Desktop\\my-new-project",
  "project_name": "My New Project",
  "project_id": "my-new-project"
}
```

**Response:**
```json
{
  "success": true,
  "project": {
    "project_id": "my-new-project",
    "project_name": "My New Project",
    "project_path": "C:\\Users\\willh\\Desktop\\my-new-project",
    "coderef_path": "C:\\Users\\willh\\Desktop\\my-new-project\\coderef",
    "has_coderef": true,
    "coderef_folders": ["workorder", "archived"],
    "status": "active"
  },
  "message": "Project registered successfully"
}
```

**Errors:**
- `400` - Invalid path or missing required fields
- `404` - Project path not found
- `409` - Project already registered

---

### 3. DELETE `/api/coderef/projects/:projectId`

**Purpose:** Unregister a project from coderef explorer

**Response:**
```json
{
  "success": true,
  "message": "Project 'my-new-project' unregistered",
  "project_id": "my-new-project"
}
```

---

### 4. GET `/api/coderef/tree`

**Purpose:** Get full tree structure of all projects' coderef folders

**Query Parameters:**
- `project_id` (optional) - Filter to single project
- `max_depth` (optional, default: 3) - Limit tree depth

**Response:**
```json
{
  "tree": [
    {
      "project_id": "assistant",
      "project_name": "Orchestrator",
      "name": "coderef",
      "type": "directory",
      "path": "coderef",
      "full_path": "C:\\Users\\willh\\Desktop\\assistant\\coderef",
      "children": [
        {
          "name": "workorder",
          "type": "directory",
          "path": "coderef/workorder",
          "children": [
            {
              "name": "auth-system",
              "type": "directory",
              "path": "coderef/workorder/auth-system",
              "children": [
                {
                  "name": "plan.json",
                  "type": "file",
                  "path": "coderef/workorder/auth-system/plan.json",
                  "size": 4096,
                  "mime_type": "application/json",
                  "modified": "2025-12-26T10:30:00Z"
                },
                {
                  "name": "DELIVERABLES.md",
                  "type": "file",
                  "path": "coderef/workorder/auth-system/DELIVERABLES.md",
                  "size": 2048,
                  "mime_type": "text/markdown",
                  "modified": "2025-12-26T11:00:00Z"
                }
              ]
            }
          ]
        },
        {
          "name": "archived",
          "type": "directory",
          "path": "coderef/archived",
          "children": []
        }
      ]
    },
    {
      "project_id": "mcp-coderef-workflow",
      "project_name": "CodeRef Workflow MCP",
      "name": "coderef",
      "type": "directory",
      "path": "coderef",
      "children": [...]
    }
  ],
  "total_files": 127,
  "total_folders": 34
}
```

---

### 5. GET `/api/coderef/folder`

**Purpose:** Get contents of a specific coderef folder across all projects

**Query Parameters:**
- `project_id` (required) - Which project
- `folder_path` (required) - Path relative to coderef root (e.g., `workorder`, `archived/feature-1`)
- `recursive` (optional, default: false) - Include nested contents

**Response:**
```json
{
  "project_id": "assistant",
  "folder_path": "coderef/workorder",
  "full_path": "C:\\Users\\willh\\Desktop\\assistant\\coderef\\workorder",
  "items": [
    {
      "name": "auth-system",
      "type": "directory",
      "path": "workorder/auth-system",
      "size": null,
      "modified": "2025-12-26T10:30:00Z",
      "file_count": 3,
      "has_communication_json": true,
      "has_plan_json": true,
      "has_deliverables_md": true
    },
    {
      "name": "dashboard-tracking-api",
      "type": "directory",
      "path": "workorder/dashboard-tracking-api",
      "size": null,
      "modified": "2025-12-26T14:00:00Z",
      "file_count": 2,
      "has_communication_json": true,
      "has_plan_json": true,
      "has_deliverables_md": false
    },
    {
      "name": ".gitignore",
      "type": "file",
      "path": "workorder/.gitignore",
      "size": 256,
      "mime_type": "text/plain",
      "modified": "2025-12-26T09:00:00Z"
    }
  ],
  "total_items": 12,
  "total_folders": 10,
  "total_files": 2
}
```

---

### 6. GET `/api/coderef/file`

**Purpose:** Get complete file content from any coderef folder

**Query Parameters:**
- `project_id` (required) - Which project
- `file_path` (required) - Full path relative to coderef root (e.g., `workorder/auth-system/plan.json`)

**Response:**
```json
{
  "project_id": "assistant",
  "file_path": "workorder/auth-system/plan.json",
  "full_path": "C:\\Users\\willh\\Desktop\\assistant\\coderef\\workorder\\auth-system\\plan.json",
  "name": "plan.json",
  "size": 4096,
  "mime_type": "application/json",
  "content_type": "json",
  "modified": "2025-12-26T10:30:00Z",
  "content": {
    "workorder_id": "WO-AUTH-001",
    "feature_name": "user-authentication",
    "status": "implementing",
    "phases": [...]
  },
  "raw_content": "{\"workorder_id\": \"WO-AUTH-001\", ...}"
}
```

**Supported Content Types:**
- `json` - Parsed JSON object
- `markdown` - Raw markdown (frontend renders)
- `text` - Plain text
- `yaml` - Parsed YAML
- `csv` - Raw CSV
- `binary` - Base64 encoded (images, etc.)
- `unknown` - Raw content

---

### 7. GET `/api/coderef/search`

**Purpose:** Search across all coderef folders in all projects

**Query Parameters:**
- `q` (required) - Search query
- `project_id` (optional) - Limit to single project
- `file_types` (optional) - Comma-separated (json, md, txt)
- `max_results` (optional, default: 50)

**Response:**
```json
{
  "query": "authentication",
  "results": [
    {
      "project_id": "assistant",
      "file_path": "workorder/auth-system/plan.json",
      "full_path": "C:\\Users\\willh\\Desktop\\assistant\\coderef\\workorder\\auth-system\\plan.json",
      "name": "plan.json",
      "mime_type": "application/json",
      "match_type": "filename",
      "context": "auth-system/plan.json",
      "relevance_score": 0.95
    },
    {
      "project_id": "assistant",
      "file_path": "archived/completed-features/auth-v1/DELIVERABLES.md",
      "full_path": "C:\\Users\\willh\\Desktop\\assistant\\coderef\\archived\\completed-features\\auth-v1\\DELIVERABLES.md",
      "name": "DELIVERABLES.md",
      "mime_type": "text/markdown",
      "match_type": "content",
      "context": "...JWT authentication implementation with refresh tokens...",
      "relevance_score": 0.87
    }
  ],
  "total_matches": 23,
  "search_time_ms": 145
}
```

---

## Backend Data Structure

### Projects Registry File

**Location:** `coderef-dashboard/projects-registry.json`

```json
{
  "projects": [
    {
      "project_id": "assistant",
      "project_name": "Orchestrator",
      "project_path": "C:\\Users\\willh\\Desktop\\assistant",
      "enabled": true,
      "added_date": "2025-12-27T10:00:00Z",
      "last_scanned": "2025-12-27T15:30:00Z"
    },
    {
      "project_id": "mcp-coderef-workflow",
      "project_name": "CodeRef Workflow MCP",
      "project_path": "C:\\Users\\willh\\.mcp-servers\\coderef-workflow",
      "enabled": true,
      "added_date": "2025-12-25T14:30:00Z",
      "last_scanned": "2025-12-27T15:25:00Z"
    }
  ],
  "default_projects": ["assistant", "mcp-coderef-workflow", "mcp-coderef-docs", "mcp-coderef-personas"],
  "version": "1.0.0"
}
```

---

## Implementation Notes

### Backend (coderef-dashboard)
- **Language:** Python (MCP server)
- **Libraries Needed:**
  - `pathlib` - File system operations
  - `os.walk()` - Directory traversal
  - `json` - Parse project registry
  - `mimetypes` - Detect file types
- **Features:**
  - Scan projects on demand
  - Cache folder structures (5-minute TTL)
  - Validate paths (no path traversal exploits)
  - Handle symlinks safely
  - Return graceful errors for missing folders

### Frontend (html-tools)
- **Route:** `/coderef-assistant`
- **Calls:**
  - `GET /api/coderef/projects` - Load project list
  - `GET /api/coderef/tree` - Build sidebar tree
  - `GET /api/coderef/folder?project_id=X&folder_path=Y` - Navigate folders
  - `GET /api/coderef/file?project_id=X&file_path=Y` - Load file content
  - `POST /api/coderef/projects` - Add new project
  - `DELETE /api/coderef/projects/:id` - Remove project
  - `GET /api/coderef/search?q=X` - Search documents

### Security Considerations
- ✅ Validate all paths (prevent `../` traversal)
- ✅ Only allow reading from registered project paths
- ✅ Don't expose full file system
- ✅ Scan only for `coderef/` subdirectory
- ✅ Rate limit search endpoint

---

## Frontend Integration

Frontend will call endpoints like:

```javascript
// Load all projects
const projects = await apiClient.get('/api/coderef/projects');

// Get tree for project
const tree = await apiClient.get('/api/coderef/tree?project_id=assistant');

// Navigate to folder
const folder = await apiClient.get('/api/coderef/folder?project_id=assistant&folder_path=workorder');

// Load file
const file = await apiClient.get('/api/coderef/file?project_id=assistant&file_path=workorder/auth-system/plan.json');

// Search
const results = await apiClient.get('/api/coderef/search?q=authentication');

// Add project
await apiClient.post('/api/coderef/projects', {
  project_path: 'C:\\new\\path',
  project_name: 'New Project'
});
```

Frontend handles rendering based on file type (markdown to HTML, JSON pretty-print, etc.).

