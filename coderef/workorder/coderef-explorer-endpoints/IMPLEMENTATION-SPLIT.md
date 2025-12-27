# Coderef Explorer - Implementation Split (html-tools vs coderef-dashboard)

## Project: html-tools (Frontend)

**Location:** `C:\Users\willh\Desktop\html-tools`

### What html-tools Needs to Build

#### 1. Route: `/coderef-assistant`
- **File:** `tools/coderef-assistant/index.html`
- **Purpose:** Main explorer UI for browsing coderef folders
- **Responsibilities:**
  - Render sidebar with project list (from `/api/coderef/projects`)
  - Build folder tree navigation (from `/api/coderef/tree`)
  - Display file/folder contents (from `/api/coderef/folder`)
  - Render file content with syntax highlighting (from `/api/coderef/file`)
  - Handle file type rendering:
    - `.md` → Markdown to HTML
    - `.json` → Pretty-printed JSON with collapsible tree
    - `.txt` → Plain text
    - Images → Display inline
    - Others → Raw content preview
  - Show breadcrumb navigation
  - Display file metadata (size, modified date, type)

#### 2. App Logic: `tools/coderef-assistant/app.js`
- **Responsibilities:**
  - Load projects list on startup
  - Initialize sidebar with tree structure
  - Handle folder/file clicks to navigate
  - API calls:
    - `GET /api/coderef/projects`
    - `GET /api/coderef/tree?project_id=X`
    - `GET /api/coderef/folder?project_id=X&folder_path=Y`
    - `GET /api/coderef/file?project_id=X&file_path=Y`
    - `GET /api/coderef/search?q=X`
  - Render file content based on mime type
  - Handle add/remove project forms
  - Search functionality with result display

#### 3. Styles: `tools/coderef-assistant/styles.css`
- Project selector dropdown
- Folder tree sidebar (collapsible/expandable)
- Main content area for file display
- Breadcrumb styling
- File type indicators
- Search bar and results

#### 4. Utilities
- **Markdown to HTML renderer** (use markdown-it or similar)
- **JSON formatter** (collapsible tree view)
- **Syntax highlighter** (for code content)
- **API client calls** (already have shared api-client.js)

---

## Project: coderef-dashboard (Backend API)

**Location:** `C:\Users\willh\Desktop\coderef-dashboard`

### What coderef-dashboard Needs to Build

#### 1. Endpoint: `GET /api/coderef/projects`
- **Location:** `server.py` (add new route)
- **Responsibilities:**
  - Read `projects-registry.json`
  - For each project, check if `{project_path}/coderef/` exists
  - Scan for coderef subfolders (working, workorder, archived, standards)
  - Return JSON response with all projects and their coderef status
  - Cache results (5-minute TTL)

#### 2. Endpoint: `POST /api/coderef/projects`
- **Location:** `server.py` (add new route)
- **Responsibilities:**
  - Validate request (project_path, project_name, project_id)
  - Check if path exists (404 if not)
  - Check if already registered (409 if duplicate)
  - Add to `projects-registry.json`
  - Scan new project's coderef folder
  - Return newly registered project

#### 3. Endpoint: `DELETE /api/coderef/projects/:projectId`
- **Location:** `server.py` (add new route)
- **Responsibilities:**
  - Find project in `projects-registry.json`
  - Remove from registry
  - Return success confirmation

#### 4. Endpoint: `GET /api/coderef/tree`
- **Location:** `server.py` (add new route)
- **Responsibilities:**
  - Read all registered projects
  - For each project, recursively traverse `coderef/` folder
  - Build nested tree structure with:
    - Folder names, types, paths
    - File names, types, paths, sizes, mime types, modified dates
  - Support optional filtering by project_id
  - Support max_depth parameter
  - Return complete tree JSON

#### 5. Endpoint: `GET /api/coderef/folder`
- **Location:** `server.py` (add new route)
- **Responsibilities:**
  - Query params: project_id, folder_path
  - Validate project exists in registry
  - Validate folder_path (prevent path traversal)
  - List folder contents with metadata:
    - File/folder names
    - Types
    - Sizes
    - Modified dates
    - For workorder folders: detect presence of communication.json, plan.json, DELIVERABLES.md
  - Support recursive flag
  - Return folder contents JSON

#### 6. Endpoint: `GET /api/coderef/file`
- **Location:** `server.py` (add new route)
- **Responsibilities:**
  - Query params: project_id, file_path
  - Validate project exists
  - Validate file_path (prevent path traversal)
  - Read file content
  - Detect MIME type / content type
  - Parse JSON/YAML if applicable
  - Handle binary files (base64 encode)
  - Return file content + metadata JSON

#### 7. Endpoint: `GET /api/coderef/search`
- **Location:** `server.py` (add new route)
- **Responsibilities:**
  - Query params: q (search term), project_id (optional), file_types (optional), max_results
  - Search by filename across all projects
  - Search by content in text files
  - Filter by file type if provided
  - Score results by relevance
  - Return matching files with context snippets

#### 8. Data Structure: `projects-registry.json`
- **Location:** `coderef-dashboard/projects-registry.json`
- **Content:**
  - Array of project objects
  - Fields: project_id, project_name, project_path, enabled, added_date, last_scanned
  - Default projects pre-populated

#### 9. Utility Functions
- **Path validation** - Prevent directory traversal attacks
- **File system traversal** - Safe recursive folder scanning
- **MIME type detection** - Determine content type for rendering
- **Caching layer** - Cache tree/folder listings (TTL: 5 minutes)
- **Content parsers** - Parse JSON, YAML, handle text/binary

---

## Summary: Work Distribution

### html-tools (Frontend) - 40% of work
- 1 new route: `/coderef-assistant/`
- UI: sidebar tree, main content area, breadcrumb, metadata display
- File rendering: Markdown → HTML, JSON pretty-print, syntax highlighting
- API integration: Call 7 endpoints via apiClient
- ~200 lines JavaScript, ~150 lines CSS

### coderef-dashboard (Backend) - 60% of work
- 7 new endpoints (GET /api/coderef/*)
- projects-registry.json management
- Safe file I/O with validation
- Tree traversal and caching
- Content parsing and MIME detection
- ~400-500 lines Python

---

## Dependencies

### html-tools Needs From coderef-dashboard
- All 7 endpoints functional
- Correct JSON response formats
- Proper MIME types in file responses
- Search working across projects

### coderef-dashboard Needs From html-tools
- None (one-way dependency)

---

## Implementation Order

1. **Phase 1 (coderef-dashboard):** Create `projects-registry.json` + endpoints 1-3 (projects management)
2. **Phase 2 (coderef-dashboard):** Create endpoints 4-7 (file exploration, search)
3. **Phase 3 (html-tools):** Build `/coderef-assistant` route, integrate with all endpoints
4. **Phase 4 (both):** Testing, polish, caching optimization

