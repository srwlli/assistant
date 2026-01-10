# API Documentation

**Project:** Assistant (Orchestrator CLI)
**Version:** 2.0.0
**Last Updated:** 2026-01-09

---

## Overview

The Assistant orchestrator uses a **file-based API architecture** with JSON data stores and HTTP endpoints for the CodeRef Explorer desktop application. The system operates on three levels:

1. **File-based APIs** - JSON files that serve as data contracts between orchestrator and project agents
2. **Python HTTP Server** - RESTful endpoints for the Electron app
3. **MCP Server Integration** - Tool-based APIs exposed via 6 MCP servers

---

## File-Based APIs

### Workorder API (`workorders.json`)

**Location:** `C:\Users\willh\Desktop\assistant\workorders.json`

**Purpose:** Centralized tracking of all active and completed workorders across projects

**Endpoints (via file reads):**

```bash
# Read all workorders
Read: workorders.json

# Filter active workorders
JSONPath: $.active_workorders[*]

# Filter by status
JSONPath: $.active_workorders[?(@.status=='pending_plan')]

# Filter by target project
JSONPath: $.active_workorders[?(@.target_project=='coderef-dashboard')]
```

**Schema:**
```json
{
  "last_updated": "YYYY-MM-DD",
  "active_workorders": [
    {
      "workorder_id": "WO-FEATURE-XXX-001",
      "stub_id": "STUB-XXX",
      "feature_name": "feature-name",
      "target_project": "project-name",
      "location": "C:\\path\\to\\communication.json",
      "status": "pending_plan | plan_submitted | approved | implementing | complete",
      "next_action": "Description of next step",
      "created": "YYYY-MM-DD",
      "type": "delegated | internal | audit",
      "priority": "low | medium | high | critical",
      "scope": "Brief description of workorder scope"
    }
  ],
  "completed_workorders": [...]
}
```

**Real Endpoints Extracted:**
- 19 active workorders tracked
- 6 completed workorders archived
- Status values: `pending_plan`, `plan_submitted`, `approved`, `implementing`, `complete`, `verified`, `closed`

---

### Stub API (`stub.json`)

**Location:** `C:\Users\willh\Desktop\assistant\coderef\working\{feature-name}\stub.json`

**Purpose:** Capture and track ideas before promotion to workorders

**Schema:**
```json
{
  "stub_id": "STUB-XXX",
  "feature_name": "kebab-case-name",
  "description": "Brief description (10-500 chars)",
  "category": "feature | enhancement | bugfix | infrastructure | documentation | refactor | research",
  "priority": "low | medium | high | critical",
  "status": "planning | ready | blocked | promoted | abandoned",
  "created": "YYYY-MM-DD",
  "target_project": "project-name (optional)",
  "promoted_to": "WO-FEATURE-XXX-001 (optional)",
  "tags": ["tag1", "tag2"],
  "notes": "Additional context (optional)"
}
```

**Validation:** Enforced via `stub-schema.json` (JSON Schema Draft 07)

**Real Data:**
- Next STUB-ID: `STUB-082`
- 56+ stubs tracked across High/Medium priority tiers
- 12 active projects

---

### Project Config API (`projects.config.json`)

**Location:** `C:\Users\willh\Desktop\assistant\projects.config.json`

**Purpose:** Source of truth for project discovery and workorder scanning

**Schema:**
```json
{
  "version": "1.0.0",
  "projects": [
    {
      "id": "project-id",
      "name": "Project Name",
      "type": "mcp_server | application | system",
      "path": "C:\\absolute\\path",
      "has_workorders": true,
      "workorder_dir": "coderef/workorder",
      "status": "active | inactive",
      "description": "Project description"
    }
  ],
  "centralized": {
    "stubs_dir": "C:\\Users\\willh\\Desktop\\assistant\\coderef\\working"
  },
  "discovery_rules": {
    "stub_discovery": "Scan {stubs_dir}/*/ for stub.json",
    "workorder_discovery": "Scan {project_path}/coderef/workorder/*/",
    "workorder_trigger": "Folder existence = workorder exists"
  }
}
```

**Registered Projects:**
- `mcp-coderef-context`
- `mcp-coderef-workflow`
- `mcp-coderef-docs`
- `mcp-coderef-personas`
- `coderef-dashboard`

---

### Communication API (`communication.json`)

**Location:** `{target_project}/coderef/workorder/{feature-name}/communication.json`

**Purpose:** Handoff protocol for orchestrator → agent delegation

**Schema:**
```json
{
  "workorder_id": "WO-FEATURE-XXX-001",
  "status": "pending_plan | plan_submitted | changes_requested | approved | implementing | complete | verified | closed",
  "handoff": {
    "orchestrator_to_agent": "Instructions from orchestrator",
    "status": "pending_plan | plan_submitted | approved"
  },
  "communication_log": [
    {
      "timestamp": "2025-12-20T10:30:00Z",
      "from": "orchestrator | agent",
      "message": "Status update or instructions",
      "phase": "planning | approval | implementation | verification"
    }
  ]
}
```

**Status Flow:**
```
pending_plan → plan_submitted → [changes_requested] → approved →
implementing → complete → verified → closed
```

---

## HTTP Server API (Python)

**Server:** `web/server.py`
**Port:** 8080
**Base URL:** `http://localhost:8080`

### Endpoints

#### `GET /api/projects`

**Description:** Retrieve all saved projects

**Response:**
```json
[
  {
    "id": "project-id",
    "name": "Project Name",
    "path": "C:\\path\\to\\project"
  }
]
```

**Status Codes:**
- `200 OK` - Projects returned
- `500 Internal Server Error` - Failed to load projects.json

---

#### `POST /api/projects`

**Description:** Save a new project

**Request Body:**
```json
{
  "id": "unique-project-id",
  "name": "Project Name",
  "path": "C:\\path\\to\\project"
}
```

**Validation:**
- Required fields: `id`, `name`, `path`
- Path must exist (unless Directory Handle)
- ID must be unique

**Response:**
```json
{
  "message": "Project saved successfully",
  "project": { ... }
}
```

**Status Codes:**
- `200 OK` - Project created/updated
- `400 Bad Request` - Validation failed
- `500 Internal Server Error` - Write failed

---

#### `DELETE /api/projects/{id}`

**Description:** Delete a project by ID

**Response:**
```json
{
  "message": "Project deleted successfully"
}
```

**Status Codes:**
- `200 OK` - Project deleted
- `404 Not Found` - Project ID not found
- `500 Internal Server Error` - Delete failed

---

#### `GET /api/tree?path={absolute_path}`

**Description:** Get folder tree structure

**Query Parameters:**
- `path` (string) - Absolute path to directory

**Response:**
```json
{
  "name": "folder-name",
  "path": "C:\\path\\to\\folder",
  "type": "directory",
  "children": [
    {
      "name": "file.txt",
      "path": "C:\\path\\to\\folder\\file.txt",
      "type": "file"
    }
  ]
}
```

---

#### `GET /api/file?path={absolute_path}`

**Description:** Get file content

**Query Parameters:**
- `path` (string) - Absolute path to file

**Response:**
```json
{
  "path": "C:\\path\\to\\file.txt",
  "content": "File contents as string"
}
```

**Status Codes:**
- `200 OK` - File content returned
- `404 Not Found` - File not found
- `500 Internal Server Error` - Read failed

---

## Slash Command API

Slash commands are invoked via the `.claude/commands/` system and execute workflows.

### `/stub [idea]`

**Description:** Capture new idea as STUB-XXX

**Implementation:** `.claude/commands/stub.md`

**Workflow:**
1. Create `coderef/working/{feature-name}/` folder
2. Assign next STUB-ID from `projects.md`
3. Generate `stub.json` with metadata
4. Update `projects.md` next STUB-ID counter
5. Confirm with user

**Example:**
```bash
/stub wo-tracking-widget
```

**Output:**
```
Stubbed: STUB-057: wo-tracking-widget
Next STUB-ID updated to: STUB-058
```

---

### `/create-session`

**Description:** Create multi-agent session with communication and instructions

**Implementation:** `.claude/commands/create-session.md`

**Generated Files:**
- `communication.json`
- `instructions.json`

---

### `/archive-file`

**Description:** Archive files to `assistant/coderef/archived/{project}/`

**Implementation:** `.claude/commands/archive-file.md`

**Workflow:**
1. Identify project from file path
2. Create archive directory: `coderef/archived/{project}/`
3. Move file to archive
4. Update tracking logs

---

## MCP Server Integration APIs

The Assistant integrates with 6 MCP servers via tool-based APIs.

### coderef-docs Tools

**Server:** `C:\Users\willh\.mcp-servers\coderef-docs`

**Tools:**
- `log_workorder` - Log new WO-XXX to global workorder log
- `get_workorder_log` - Query workorder history
- `generate_handoff_context` - Auto-generate handoff prompts from plan.json
- `generate_foundation_docs` - Generate POWER framework docs (API, SCHEMA, COMPONENTS, ARCHITECTURE, README)
- `generate_individual_doc` - Generate single foundation document with code intelligence

---

### coderef-workflow Tools

**Server:** `C:\Users\willh\.mcp-servers\coderef-workflow`

**Tools (used by project agents):**
- `gather_context` - Capture requirements for workorder
- `create_plan` - Generate implementation plan (saves to plan.json)
- `execute_plan` - Convert plan to TodoWrite task list
- `update_deliverables` - Record git metrics (LOC, commits, time)
- `archive_feature` - Move completed work to coderef/archived/

---

### coderef-personas Tools

**Server:** `C:\Users\willh\.mcp-servers\coderef-personas`

**Tools:**
- `activate_persona` - Load CodeRef Assistant persona
- `list_personas` - List available personas
- `get_persona` - Get persona definition

---

## API Usage Examples

### Example 1: Promote Stub to Workorder

```javascript
// Step 1: Read stub
const stub = readJSON('coderef/working/wo-tracking-widget/stub.json');

// Step 2: Create workorder entry
const workorder = {
  workorder_id: 'WO-DASHBOARD-WIDGET-001',
  stub_id: stub.stub_id,
  feature_name: stub.feature_name,
  target_project: 'coderef-dashboard',
  location: 'C:\\Users\\willh\\Desktop\\coderef-dashboard\\coderef\\workorder\\wo-tracking-widget\\communication.json',
  status: 'pending_plan',
  created: new Date().toISOString().split('T')[0],
  type: 'delegated',
  priority: stub.priority,
  scope: stub.description
};

// Step 3: Update workorders.json
const workorders = readJSON('workorders.json');
workorders.active_workorders.push(workorder);
writeJSON('workorders.json', workorders);

// Step 4: Create communication.json in target project
const communication = {
  workorder_id: workorder.workorder_id,
  status: 'pending_plan',
  handoff: {
    orchestrator_to_agent: 'Review context.json and run /create-plan',
    status: 'pending_plan'
  }
};
writeJSON(workorder.location, communication);
```

---

### Example 2: Check Workorder Status

```javascript
// Read workorders.json
const workorders = readJSON('workorders.json');

// Filter by target project
const dashboardWorkorders = workorders.active_workorders
  .filter(wo => wo.target_project === 'coderef-dashboard');

// Check status
dashboardWorkorders.forEach(wo => {
  console.log(`${wo.workorder_id}: ${wo.status} - ${wo.next_action}`);
});
```

---

### Example 3: Query via Python Server

```bash
# Get all projects
curl http://localhost:8080/api/projects

# Save new project
curl -X POST http://localhost:8080/api/projects \
  -H "Content-Type: application/json" \
  -d '{"id": "test-project", "name": "Test Project", "path": "C:\\test"}'

# Get file tree
curl "http://localhost:8080/api/tree?path=C:\\Users\\willh\\Desktop\\assistant"

# Read file content
curl "http://localhost:8080/api/file?path=C:\\Users\\willh\\Desktop\\assistant\\projects.md"
```

---

## Error Handling

### File-Based APIs
- **Missing File:** Return empty default structure or error message
- **Invalid JSON:** Log parse error, return null
- **Permission Denied:** Check file permissions, alert user

### HTTP Server
- **CORS:** Enabled via `Access-Control-Allow-Origin: *`
- **400 Bad Request:** Invalid request body or missing required fields
- **404 Not Found:** Resource not found
- **500 Internal Server Error:** Server-side failure (logged to console)

---

## Rate Limits

**File-Based APIs:** No rate limits (local filesystem)

**HTTP Server:** No rate limits (local development server)

**MCP Tools:** Rate limits defined per MCP server (refer to MCP server docs)

---

## Authentication

**File-Based APIs:** No authentication (local filesystem access)

**HTTP Server:** No authentication (localhost-only, development mode)

**MCP Servers:** Authenticated via Claude Desktop MCP configuration

---

## Versioning

**API Version:** 2.0.0

**Versioning Strategy:**
- Major: Breaking changes to file schemas or endpoint contracts
- Minor: New endpoints or optional fields
- Patch: Bug fixes, no schema changes

**Backward Compatibility:**
- File schemas support additional properties (forward compatible)
- HTTP endpoints maintain consistent response structure

---

## Resources

- **[Workorders JSON](../../workorders.json)** - Live workorder tracking
- **[Projects Config](../../projects.config.json)** - Project registry
- **[Stub Schema](../../stub-schema.json)** - Canonical stub validation schema
- **[Python Server](../../web/server.py)** - HTTP server implementation
- **[SCHEMA.md](./SCHEMA.md)** - Detailed schema documentation

---

**Document ID:** `assistant-api-v2.0.0`
**Last Generated:** 2026-01-09 via `/generate-docs`
