---
workorder_id: WO-FOUNDATION-DOCS-001
generated_by: coderef-docs v2.0.0
feature_id: foundation-documentation
doc_type: components
title: Assistant - Components Documentation
version: 2.0.0
status: APPROVED
---

# Components Documentation

**Project:** Assistant (Orchestrator CLI)
**Version:** 2.0.0
**Last Updated:** 2026-01-09

---

## Overview

The Assistant orchestrator consists of **4 component categories**: Dashboard UI components, Python automation scripts, Slash command workflows, and Electron app components. This document catalogs all components extracted from the codebase.

---

## Dashboard UI Components

**Location:** `index.html`
**Framework:** Vanilla HTML/CSS
**Purpose:** Static dashboard for visualizing workorders, stubs, and project status

### Header Component

**Element:** `<header>`
**Location:** index.html:97-99

**Features:**
- Application title with tagline
- Badge indicators (role, stub count, project count)
- Navigation links to related projects

**Structure:**
```html
<header>
  <h1>Assistant</h1>
  <p class="tagline">Orchestrator CLI - Identify, Delegate, Collect</p>
  <div class="badges">
    <span class="badge badge-role">Orchestrator</span>
    <span class="badge badge-stubs">82 Stubs</span>
    <span class="badge badge-projects">12 Projects</span>
  </div>
</header>
```

**CSS Classes:**
- `.badge` - Base badge styling
- `.badge-role` - Purple orchestrator badge
- `.badge-stubs` - Blue stub count badge
- `.badge-projects` - Green project count badge

---

### Navigation Component

**Element:** `<nav class="nav">`
**Location:** index.html:87-95

**Features:**
- Horizontal navigation bar
- Links to Assistant, MCP Servers, and active projects
- Active state highlighting

**Link Targets:**
- `./index.html` - Assistant dashboard (active)
- `file:///C:/Users/willh/.mcp-servers/index.html` - MCP Servers
- External URLs to Scrapper, Gridiron, Scriptboard, Noted

**CSS Classes:**
- `.nav` - Navigation container
- `.nav a` - Navigation links
- `.nav a.active` - Active link highlighting

---

### Principle Box Component

**Element:** `<div class="principle-box">`
**Location:** index.html:26-28

**Purpose:** Highlight core orchestrator principle

**Content:**
```html
<div class="principle-box">
  <h3>CORE PRINCIPLE</h3>
  <p class="principle-text">
    Identify, Delegate, Collect - Never Execute in Target Projects
  </p>
</div>
```

**CSS Classes:**
- `.principle-box` - Purple background container
- `.principle-text` - Large emphasized text

---

### Stats Grid Component

**Element:** `<div class="stats-grid">`
**Location:** index.html:33

**Purpose:** Display key metrics (Active WOs, Completed WOs, Stubs, Projects, Avg Time)

**Structure:**
```html
<div class="stats-grid">
  <div class="stat">
    <div class="stat-value">19</div>
    <div class="stat-label">Active WOs</div>
  </div>
  <!-- 4 more stat cards -->
</div>
```

**CSS:**
- 5-column grid layout
- Cards with border and padding
- Large numeric values with labels

---

### Workorder Card Component

**Element:** `<div class="workorder-card">`
**Location:** index.html:70-80

**Purpose:** Display individual workorder with status, project, and next action

**Structure:**
```html
<div class="workorder-card">
  <div class="workorder-header">
    <span class="workorder-id">WO-STUB-PROJECT-DISPLAY-004</span>
    <span class="workorder-status status-pending">pending_plan</span>
  </div>
  <div class="workorder-feature">stub-project-display</div>
  <div class="workorder-project">coderef-dashboard</div>
  <div class="workorder-action">Agent: Add subtitle={stub.target_project}</div>
</div>
```

**CSS Classes:**
- `.workorder-card` - Card container
- `.workorder-id` - Monospace workorder ID
- `.workorder-status` - Colored status badge
- `.status-pending`, `.status-approved`, `.status-implementing`, `.status-complete` - Status variants

---

### Stub Card Component

**Element:** `<div class="stub-card">`
**Location:** index.html:51-59

**Purpose:** Display stub ideas with priority and category

**Structure:**
```html
<div class="stub-card">
  <div class="stub-header">
    <span class="stub-id">STUB-001</span>
    <span class="stub-priority priority-high">High</span>
  </div>
  <div class="stub-name">scriptboard-assistant-integration</div>
  <div class="stub-desc">Make Scriptboard the primary visual UI</div>
</div>
```

**CSS Classes:**
- `.stub-card` - Card container
- `.stub-id` - Monospace stub ID
- `.stub-priority` - Priority badge
- `.priority-high`, `.priority-medium` - Priority color variants

---

### Workflow Box Component

**Element:** `<div class="workflow-box">`
**Location:** index.html:45-49

**Purpose:** Visualize step-by-step workflows

**Structure:**
```html
<div class="workflow-box">
  <div class="workflow-title">Stub Promotion Workflow</div>
  <div class="workflow-flow">
    <span class="step">/stub idea</span>
    <span class="arrow">→</span>
    <span class="step">STUB-XXX created</span>
    <span class="arrow">→</span>
    <span class="step">Ready for promotion</span>
  </div>
</div>
```

**CSS Classes:**
- `.workflow-box` - Container with border
- `.workflow-title` - Workflow name
- `.workflow-flow` - Flex container for steps
- `.step` - Individual step badge
- `.arrow` - Arrow separator

---

## Electron App Components

**Location:** `web/`
**Framework:** Electron + Vanilla JS
**Purpose:** Desktop file browser for CodeRef documentation

### Project Manager UI

**File:** `web/index.html`
**Purpose:** Dashboard layout with sidebar and main content area

**Structure:**
```html
<body>
  <header><!-- Title and theme toggle --></header>
  <aside><!-- Sidebar navigation --></aside>
  <main><!-- Dashboard content --></main>
</body>
```

**Layout:**
- Grid layout: 250px sidebar + fluid main content
- 60px fixed header height
- Responsive breakpoint at 768px (mobile stacks vertically)

**Components:**
1. **Header** - Title, theme toggle, user menu
2. **Sidebar** - Navigation menu (Dashboard, Projects, Workorders, Settings)
3. **Main Content Area** - Stats grid, project cards, workorder list

---

### Theme Toggle Component

**Element:** `<button onclick="toggleTheme()">`
**Location:** web/index.html:70-72

**Function:**
```javascript
function toggleTheme() {
  document.documentElement.classList.toggle('dark');
}
```

**Features:**
- Switches between light and dark modes
- Material Icons moon/sun symbol
- Persists via localStorage (if implemented)

---

### Stats Panel Component

**Element:** `.industrial-panel`
**Location:** web/index.html:121-149

**Purpose:** Display project metrics (Total Projects, Active Workorders, Completion Rate)

**Structure:**
```html
<div class="industrial-panel">
  <div class="flex flex-between items-start">
    <div>
      <p class="text-muted text-sm">TOTAL PROJECTS</p>
      <h3 style="font-size: 32px;">12</h3>
    </div>
    <span class="material-symbols-outlined">folder</span>
  </div>
</div>
```

**CSS Variables:**
- Uses CSS custom properties for theming
- `--color-ind-accent` for icon color
- `--spacing-lg` for spacing consistency

---

## Python Scripts (Automation Components)

### File Discovery Server

**File:** `web/server.py`
**Type:** HTTP Server Component
**Port:** 8080

**Endpoints:**
- `GET /api/projects` - List all projects
- `POST /api/projects` - Save new project
- `DELETE /api/projects/{id}` - Remove project
- `GET /api/tree` - Get folder tree structure
- `GET /api/file` - Read file content

**Class:** `CodeRefHandler(http.server.SimpleHTTPRequestHandler)`

**Methods:**
- `do_GET()` - Handle GET requests
- `do_POST()` - Handle POST requests
- `do_DELETE()` - Handle DELETE requests
- `do_OPTIONS()` - Handle CORS preflight
- `handle_get_projects()` - Return all projects from projects.json
- `handle_save_project()` - Validate and save project
- `handle_delete_project(project_id)` - Remove project by ID
- `handle_tree_request(parsed)` - Generate folder tree
- `handle_file_request(parsed)` - Return file content
- `send_json_response(data)` - Send JSON response with CORS headers

---

### Stub Validation Script

**File:** `validate-stubs.py`
**Type:** CLI Script
**Purpose:** Validate all stub.json files against schema

**Workflow:**
1. Load `stub-schema.json`
2. Scan `coderef/working/*/stub.json` files
3. Validate each against JSON Schema
4. Report errors and violations
5. Exit with status code (0 = success, 1 = failures)

**Usage:**
```bash
python validate-stubs.py
```

**Output:**
```
Validating stubs...
✓ STUB-001: scriptboard-assistant-integration
✓ STUB-002: tool-inventory-workflow
✗ STUB-057: wo-tracking-widget (Missing required field: category)
---
56 stubs validated, 1 error(s) found
```

---

### Target Project Inference Script

**File:** `infer-target-projects.py`
**Type:** CLI Script
**Purpose:** Auto-assign target_project to stubs based on name patterns

**Workflow:**
1. Scan all stub.json files
2. Analyze `feature_name` for project hints
3. Suggest `target_project` based on keywords
4. Update stub.json files (with confirmation)

**Pattern Matching:**
- "dashboard" → `coderef-dashboard`
- "mcp" / "server" → `mcp-servers`
- "workflow" / "plan" → `coderef-workflow`
- "orchestrator" / "assistant" → `assistant`

---

### Emoji Removal Script

**File:** `scripts/remove-emojis.py`
**Type:** Utility Script
**Purpose:** Strip emojis from markdown files

**Usage:**
```bash
python scripts/remove-emojis.py [file_path]
```

---

### CodeRef Structure Creator

**File:** `scripts/create-coderef-structure.py`
**Type:** Scaffolding Script
**Purpose:** Generate standard coderef/ folder structure in projects

**Generated Structure:**
```
coderef/
├── working/
├── archived/
├── foundation-docs/
└── user/
```

---

## Slash Command Workflows

**Location:** `.claude/commands/`
**Type:** Markdown-based command definitions

### /stub Command

**File:** `.claude/commands/stub.md`
**Purpose:** Capture new idea as STUB-XXX

**Workflow Steps:**
1. Prompt user for feature name
2. Assign next STUB-ID from projects.md
3. Create `coderef/working/{feature-name}/` folder
4. Generate `stub.json` with metadata
5. Update projects.md counter
6. Confirm to user

**Template Variables:**
- `{feature-name}` - Kebab-case identifier
- `{STUB-ID}` - Auto-incremented ID (STUB-001, STUB-002, ...)
- `{description}` - User-provided description

---

### /create-session Command

**File:** `.claude/commands/create-session.md`
**Purpose:** Initialize multi-agent session

**Generated Files:**
- `communication.json` - Inter-agent communication protocol
- `instructions.json` - Session-specific instructions

---

### /create-resource-sheet Command

**File:** `.claude/commands/create-resource-sheet.md`
**Purpose:** Generate resource tracking sheet

---

### /archive-file Command

**File:** `.claude/commands/archive-file.md`
**Purpose:** Archive files by project

**Workflow:**
1. Identify project from file path
2. Create `coderef/archived/{project}/` if needed
3. Move file to archive folder
4. Update tracking logs (if applicable)

---

## Component Dependencies

### Dependency Graph

```
index.html (Dashboard UI)
    ├── CSS (embedded styles)
    └── projects.md (data source)
    └── workorders.json (data source)

web/index.html (Electron App UI)
    ├── web/src/css/main.css
    ├── web/preload.js
    └── web/server.py (backend API)

web/server.py (HTTP Server)
    ├── projects.json (data store)
    └── File System (file browsing)

validate-stubs.py
    ├── stub-schema.json (validation rules)
    └── coderef/working/*/stub.json (target files)

Slash Commands (.claude/commands/)
    ├── projects.md (STUB-ID counter)
    ├── workorders.json (workorder tracking)
    └── File System (file creation)
```

---

## Component Patterns

### CSS Architecture

**Pattern:** BEM-like naming with semantic classes

**Naming Convention:**
- `.component` - Component base class
- `.component-element` - Component sub-element
- `.component--modifier` - Component variant

**Examples:**
- `.workorder-card` - Card component
- `.workorder-status` - Status element
- `.status-pending` - Pending status modifier

---

### Data Binding Pattern

**Pattern:** File-based data binding

**Flow:**
1. Read JSON data file
2. Parse and extract relevant data
3. Render to HTML (static or dynamic)
4. Write updates back to JSON file

**Example (Workorders):**
```javascript
// Read
const workorders = JSON.parse(fs.readFileSync('workorders.json'));

// Render
const html = workorders.active_workorders
  .map(wo => `<div class="workorder-card">...</div>`)
  .join('');

// Write (after updates)
fs.writeFileSync('workorders.json', JSON.stringify(workorders, null, 2));
```

---

### Python Script Pattern

**Pattern:** CLI script with argparse

**Structure:**
```python
#!/usr/bin/env python3
import argparse

def main():
    parser = argparse.ArgumentParser(description='...')
    parser.add_argument('input', help='...')
    args = parser.parse_args()

    # Execute logic
    result = process(args.input)

    # Report results
    print(f"✓ Success: {result}")

if __name__ == '__main__':
    main()
```

---

## Testing Components

**Note:** No explicit test files found in codebase

**Validation Components:**
- `validate-stubs.py` - Schema validation for stubs
- Manual verification via dashboard display

---

## Resources

- **[index.html](../../index.html)** - Main dashboard
- **[web/index.html](../../web/index.html)** - Electron app UI
- **[web/server.py](../../web/server.py)** - Python HTTP server
- **[.claude/commands/](../../.claude/commands/)** - Slash command workflows
- **[API.md](./API.md)** - API documentation
- **[SCHEMA.md](./SCHEMA.md)** - Schema documentation

---

**Document ID:** `assistant-components-v2.0.0`
**Last Generated:** 2026-01-09 via `/generate-docs`
