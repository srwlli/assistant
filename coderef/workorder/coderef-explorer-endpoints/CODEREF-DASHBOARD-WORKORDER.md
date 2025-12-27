# Workorder: Coderef Explorer Backend Implementation

**WO-ID:** WO-CODEREF-EXPLORER-DASHBOARD-001
**Feature:** coderef-explorer-endpoints
**Component:** Backend API Implementation (coderef-dashboard)
**Priority:** HIGH
**Estimated Effort:** 6-8 hours

---

## Executive Summary

Implement 7 RESTful API endpoints in coderef-dashboard MCP server that expose the entire coderef folder structure across all registered projects. These endpoints power the frontend `/coderef-assistant` explorer route.

---

## Your Responsibilities

You are building the **data foundation** for coderef exploration. The frontend depends entirely on these 7 endpoints.

---

## What You're Building

### 7 API Endpoints

#### 1. `GET /api/coderef/projects`
- List all registered projects with coderef status
- Scan each project for coderef subfolders
- Return: project list, coderef folder names, status

#### 2. `POST /api/coderef/projects`
- Accept: project_path, project_name, project_id
- Validate path exists, not duplicate
- Add to projects-registry.json
- Return: newly registered project with coderef metadata

#### 3. `DELETE /api/coderef/projects/:projectId`
- Find project, remove from registry
- Return: success + removed project_id

#### 4. `GET /api/coderef/tree`
- Recursively traverse all projects' coderef folders
- Build nested tree with files/folders, metadata, paths
- Support: optional project_id filter, optional max_depth
- Return: complete tree structure with 10+ levels of detail

#### 5. `GET /api/coderef/folder`
- Accept: project_id, folder_path, recursive (optional)
- Validate project and path (prevent traversal attacks)
- List folder contents with metadata
- For workorder folders: detect presence of communication.json, plan.json, DELIVERABLES.md
- Return: folder contents with file metadata

#### 6. `GET /api/coderef/file`
- Accept: project_id, file_path
- Read file content
- Detect MIME type / content type
- Parse JSON/YAML if applicable
- Handle binary files (base64 encode)
- Return: content + full metadata

#### 7. `GET /api/coderef/search`
- Accept: q (query), project_id (optional), file_types (optional), max_results
- Search by filename across all projects
- Search by content in text files
- Score results by relevance
- Return: matching files with context snippets, relevance scores

---

## Core Data Structure

### `projects-registry.json`

**Location:** `C:\Users\willh\Desktop\coderef-dashboard\projects-registry.json`

**Structure:**
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

## Implementation Requirements

### Code Organization

- **File:** `coderef-dashboard/server.py` (add new routes to existing MCP server)
- **Library:** `pathlib` (file system operations), `os.walk()` (directory traversal), `json` (registry), `mimetypes` (content type detection)

### Functions You'll Create

1. **`load_projects_registry()`** - Read projects-registry.json
2. **`save_projects_registry(data)`** - Write projects-registry.json
3. **`validate_project_path(path)`** - Check path exists, is directory
4. **`validate_file_path(base_path, requested_path)`** - Prevent `../` traversal attacks
5. **`get_coderef_path(project_path)`** - Return {project_path}/coderef/
6. **`scan_project_coderef(project_path)`** - Discover coderef subfolders
7. **`build_folder_tree(base_path, max_depth=3)`** - Recursive tree building
8. **`list_folder_contents(folder_path)`** - Return items with metadata
9. **`read_file_content(file_path)`** - Read file, detect type, parse if needed
10. **`search_coderef(query, projects=all)`** - File/content search across projects
11. **`get_file_metadata(file_path)`** - Size, mime type, modified date
12. **`cache_tree_results(key, data, ttl=300)`** - 5-minute caching layer

### Security Considerations

✅ **Path Validation** - Prevent `../` directory traversal
✅ **Symlink Safety** - Don't follow symlinks outside registered paths
✅ **Only Read** - Never write/delete from coderef folders
✅ **Project Whitelist** - Only serve from registered projects
✅ **Rate Limiting** - Limit search endpoint (optional for Phase 1)

### Response Format Requirements

All responses must include:
- `status` (200, 400, 404, 409, 500)
- `data` (actual response content)
- `error` (if status != 200)
- `timestamp` (ISO 8601)

Example successful response:
```json
{
  "status": 200,
  "data": {
    "projects": [...],
    "total_projects": 6
  },
  "timestamp": "2025-12-27T16:45:00Z"
}
```

Example error response:
```json
{
  "status": 404,
  "error": "Project 'unknown-project' not found in registry",
  "timestamp": "2025-12-27T16:45:00Z"
}
```

---

## Testing Checklist

### Unit Tests
- [ ] `load_projects_registry()` - Loads file correctly
- [ ] `validate_project_path()` - Accepts valid, rejects invalid paths
- [ ] `validate_file_path()` - Blocks `../` traversal attacks
- [ ] `build_folder_tree()` - Correct structure, respects max_depth
- [ ] `get_file_metadata()` - Correct MIME types, sizes

### Integration Tests
- [ ] Endpoint 1: GET /api/coderef/projects - Lists all projects
- [ ] Endpoint 2: POST /api/coderef/projects - Adds project, validates path
- [ ] Endpoint 3: DELETE /api/coderef/projects/:id - Removes project
- [ ] Endpoint 4: GET /api/coderef/tree - Returns full tree
- [ ] Endpoint 4b: GET /api/coderef/tree?project_id=X - Filters correctly
- [ ] Endpoint 5: GET /api/coderef/folder - Lists folder items
- [ ] Endpoint 5b: GET /api/coderef/folder?recursive=true - Recursive traversal
- [ ] Endpoint 6: GET /api/coderef/file - Returns file content + metadata
- [ ] Endpoint 6b: JSON files - Parsed as objects, not strings
- [ ] Endpoint 6c: Markdown files - Returned as plain text (frontend renders)
- [ ] Endpoint 7: GET /api/coderef/search - Finds files by name
- [ ] Endpoint 7b: GET /api/coderef/search - Finds files by content

### Edge Cases
- [ ] Empty folder - Returns empty items array
- [ ] Missing communication.json in workorder - Returns gracefully
- [ ] Large folder (100+ items) - Returns quickly (< 1 second)
- [ ] Deep nesting (10+ levels) - Traverses correctly
- [ ] Special characters in filenames - Escapes properly in JSON
- [ ] Binary files - Base64 encodes without crashing

---

## Reference Documentation

- **Complete Endpoint Spec:** `CODEREF-EXPLORER-ENDPOINTS.md`
- **Implementation Split:** `IMPLEMENTATION-SPLIT.md`
- **Projects Registry Schema:** See above

---

## Success Criteria

✅ All 7 endpoints implemented and tested
✅ Path validation prevents security issues
✅ Responses match documented JSON schema
✅ All edge cases handled gracefully
✅ Frontend can call all endpoints without errors
✅ Search functionality finds files across projects
✅ Caching layer reduces repeated queries by 50%+
✅ Documentation updated with actual endpoint behavior

---

## Blocking Items

None - You can start immediately.

---

## Related Work

- **Frontend:** html-tools `/coderef-assistant` route (depends on these endpoints)
- **Stub:** coderef-explorer-endpoints
- **Spec Docs:** CODEREF-EXPLORER-ENDPOINTS.md, IMPLEMENTATION-SPLIT.md

---

## Next Phase

After this is complete:
1. html-tools builds `/coderef-assistant` frontend route
2. Frontend integrates with all 7 endpoints
3. Testing: end-to-end folder exploration + file viewing
4. Optimization: caching improvements, search refinement

