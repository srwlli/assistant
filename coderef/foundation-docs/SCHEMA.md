---
workorder_id: WO-FOUNDATION-DOCS-001
generated_by: coderef-docs v2.0.0
feature_id: foundation-documentation
doc_type: schema
title: Assistant - Schema Documentation
version: 2.0.0
status: APPROVED
---

# Schema Documentation

**Project:** Assistant (Orchestrator CLI)
**Version:** 2.0.0
**Last Updated:** 2026-01-09

---

## Overview

The Assistant orchestrator uses **JSON Schema-based data models** for all system entities. This document describes the canonical schemas extracted from the codebase for stubs, workorders, projects, communication, and related data structures.

---

## Core Schemas

### Stub Schema

**File:** `stub-schema.json`
**JSON Schema Version:** Draft 07
**Purpose:** Canonical schema for all stub.json files across orchestrator and dashboard

#### Schema Definition

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Orchestrator Stub Schema",
  "description": "Canonical schema for stub.json files across orchestrator and dashboard",
  "type": "object",
  "required": [
    "stub_id",
    "feature_name",
    "description",
    "category",
    "priority",
    "status",
    "created"
  ],
  "properties": {
    "stub_id": {
      "type": "string",
      "pattern": "^STUB-\\d{3}$",
      "description": "Auto-incremented stub ID (e.g., STUB-001)"
    },
    "feature_name": {
      "type": "string",
      "minLength": 3,
      "maxLength": 100,
      "pattern": "^[a-z0-9-]+$",
      "description": "Kebab-case feature identifier matching folder name"
    },
    "description": {
      "type": "string",
      "minLength": 10,
      "maxLength": 500,
      "description": "Brief description of the feature idea"
    },
    "category": {
      "type": "string",
      "enum": [
        "feature",
        "enhancement",
        "bugfix",
        "infrastructure",
        "documentation",
        "refactor",
        "research"
      ],
      "description": "Type of work"
    },
    "priority": {
      "type": "string",
      "enum": ["low", "medium", "high", "critical"],
      "description": "Implementation priority"
    },
    "status": {
      "type": "string",
      "enum": [
        "planning",
        "ready",
        "blocked",
        "promoted",
        "abandoned"
      ],
      "description": "Current stub lifecycle status"
    },
    "created": {
      "type": "string",
      "format": "date",
      "pattern": "^\\d{4}-\\d{2}-\\d{2}$",
      "description": "Creation date in YYYY-MM-DD format"
    },
    "target_project": {
      "type": "string",
      "description": "Target project for delegation (optional until promotion)"
    },
    "promoted_to": {
      "type": "string",
      "pattern": "^WO-[A-Z0-9-]+-\\d{3}$",
      "description": "Workorder ID if promoted (e.g., WO-AUTH-001)"
    },
    "tags": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Optional tags for filtering/searching"
    },
    "notes": {
      "type": "string",
      "description": "Optional additional context or notes"
    }
  },
  "additionalProperties": false
}
```

#### Field Reference

| Field | Type | Required | Pattern/Enum | Description |
|-------|------|----------|--------------|-------------|
| `stub_id` | string | ✅ | `^STUB-\d{3}$` | Auto-incremented ID (STUB-001 to STUB-999) |
| `feature_name` | string | ✅ | `^[a-z0-9-]+$` | Kebab-case identifier (3-100 chars) |
| `description` | string | ✅ | 10-500 chars | Brief feature description |
| `category` | enum | ✅ | See enum values | Work type classification |
| `priority` | enum | ✅ | low/medium/high/critical | Implementation priority |
| `status` | enum | ✅ | See enum values | Lifecycle status |
| `created` | date | ✅ | `YYYY-MM-DD` | Creation timestamp |
| `target_project` | string | ❌ | - | Target project name |
| `promoted_to` | string | ❌ | `^WO-[A-Z0-9-]+-\d{3}$` | Workorder ID after promotion |
| `tags` | array | ❌ | string[] | Search/filter tags |
| `notes` | string | ❌ | - | Additional context |

#### Enum Values

**category:**
- `feature` - New functionality
- `enhancement` - Improvement to existing feature
- `bugfix` - Bug repair
- `infrastructure` - System/tooling improvement
- `documentation` - Documentation work
- `refactor` - Code restructuring
- `research` - Investigation/analysis

**priority:**
- `low` - Nice to have
- `medium` - Should have
- `high` - Must have soon
- `critical` - Blocking/urgent

**status:**
- `planning` - Idea captured, details being refined
- `ready` - Ready for promotion to workorder
- `blocked` - Waiting on dependency
- `promoted` - Converted to workorder
- `abandoned` - Cancelled/no longer needed

#### Example Instance

```json
{
  "stub_id": "STUB-057",
  "feature_name": "wo-tracking-widget",
  "description": "Orchestrator workorder tracking widget for dashboard UI with real-time status updates",
  "category": "feature",
  "priority": "high",
  "status": "planning",
  "created": "2025-12-20",
  "target_project": "coderef-dashboard",
  "tags": ["ui", "dashboard", "orchestrator"],
  "notes": "Integrates with workorders.json API for live data"
}
```

---

### Workorder Schema

**File:** `workorders.json`
**Purpose:** Centralized tracking of all active and completed workorders

#### Root Schema

```json
{
  "type": "object",
  "required": ["last_updated", "active_workorders", "completed_workorders"],
  "properties": {
    "last_updated": {
      "type": "string",
      "format": "date",
      "description": "Last modification date (YYYY-MM-DD)"
    },
    "active_workorders": {
      "type": "array",
      "items": { "$ref": "#/definitions/workorder" }
    },
    "completed_workorders": {
      "type": "array",
      "items": { "$ref": "#/definitions/workorder" }
    },
    "status_legend": {
      "type": "object",
      "description": "Status code definitions"
    }
  }
}
```

#### Workorder Entity Schema

```json
{
  "type": "object",
  "required": [
    "workorder_id",
    "feature_name",
    "target_project",
    "location",
    "status",
    "created"
  ],
  "properties": {
    "workorder_id": {
      "type": "string",
      "pattern": "^WO-[A-Z0-9-]+-\\d{3}$",
      "description": "Unique workorder ID (e.g., WO-AUTH-001)"
    },
    "stub_id": {
      "type": ["string", "null"],
      "pattern": "^STUB-\\d{3}$",
      "description": "Original stub ID if promoted from stub"
    },
    "feature_name": {
      "type": "string",
      "description": "Kebab-case feature identifier"
    },
    "target_project": {
      "type": "string",
      "description": "Project receiving the delegated work"
    },
    "location": {
      "type": "string",
      "description": "Absolute path to communication.json"
    },
    "status": {
      "type": "string",
      "enum": [
        "pending",
        "pending_plan",
        "plan_submitted",
        "changes_requested",
        "approved",
        "implementing",
        "complete",
        "verified",
        "closed"
      ]
    },
    "next_action": {
      "type": "string",
      "description": "Human-readable description of next step"
    },
    "created": {
      "type": "string",
      "format": "date",
      "description": "Creation date (YYYY-MM-DD)"
    },
    "type": {
      "type": "string",
      "enum": ["delegated", "internal", "audit"],
      "description": "Workorder origin type"
    },
    "priority": {
      "type": "string",
      "enum": ["low", "medium", "high", "critical"]
    },
    "scope": {
      "type": "string",
      "description": "Brief description of workorder scope"
    },
    "delegated": {
      "type": "string",
      "format": "date",
      "description": "Date delegated to project agent"
    },
    "completed": {
      "type": "string",
      "format": "date",
      "description": "Date workorder completed"
    }
  }
}
```

#### Field Reference

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `workorder_id` | string | ✅ | Unique ID (WO-FEATURE-XXX-001) |
| `stub_id` | string/null | ❌ | Original stub if promoted |
| `feature_name` | string | ✅ | Kebab-case identifier |
| `target_project` | string | ✅ | Receiving project name |
| `location` | string | ✅ | Path to communication.json |
| `status` | enum | ✅ | Current workorder status |
| `next_action` | string | ❌ | Next step description |
| `created` | date | ✅ | Creation date |
| `type` | enum | ❌ | delegated/internal/audit |
| `priority` | enum | ❌ | low/medium/high/critical |
| `scope` | string | ❌ | Brief scope description |
| `delegated` | date | ❌ | Delegation date |
| `completed` | date | ❌ | Completion date |

#### Status Flow

```
pending → pending_plan → plan_submitted → [changes_requested] →
approved → implementing → complete → verified → closed
```

#### Example Instance

```json
{
  "workorder_id": "WO-DASHBOARD-WIDGET-001",
  "stub_id": "STUB-057",
  "feature_name": "wo-tracking-widget",
  "target_project": "coderef-dashboard",
  "location": "C:\\Users\\willh\\Desktop\\coderef-dashboard\\coderef\\workorder\\wo-tracking-widget\\communication.json",
  "status": "pending_plan",
  "next_action": "Agent: Run /create-plan workflow",
  "created": "2025-12-30",
  "type": "delegated",
  "priority": "high",
  "scope": "Orchestrator workorder tracking widget for dashboard UI"
}
```

---

### Communication Schema

**File:** `communication.json` (in target project workorder folders)
**Purpose:** Handoff protocol for orchestrator → agent communication

#### Schema Definition

```json
{
  "type": "object",
  "required": ["workorder_id", "status", "handoff"],
  "properties": {
    "workorder_id": {
      "type": "string",
      "pattern": "^WO-[A-Z0-9-]+-\\d{3}$"
    },
    "status": {
      "type": "string",
      "enum": [
        "pending_plan",
        "plan_submitted",
        "changes_requested",
        "approved",
        "implementing",
        "complete",
        "verified",
        "closed"
      ]
    },
    "handoff": {
      "type": "object",
      "properties": {
        "orchestrator_to_agent": {
          "type": "string",
          "description": "Instructions from orchestrator"
        },
        "status": {
          "type": "string",
          "enum": ["pending_plan", "plan_submitted", "approved"]
        }
      }
    },
    "communication_log": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "timestamp": {
            "type": "string",
            "format": "date-time"
          },
          "from": {
            "type": "string",
            "enum": ["orchestrator", "agent"]
          },
          "message": {
            "type": "string"
          },
          "phase": {
            "type": "string",
            "enum": ["planning", "approval", "implementation", "verification"]
          }
        },
        "required": ["timestamp", "from", "message"]
      }
    }
  }
}
```

#### Example Instance

```json
{
  "workorder_id": "WO-AUTH-001",
  "status": "plan_submitted",
  "handoff": {
    "orchestrator_to_agent": "Review context.json and run /create-plan",
    "status": "plan_submitted"
  },
  "communication_log": [
    {
      "timestamp": "2025-12-20T10:30:00Z",
      "from": "orchestrator",
      "message": "Workorder delegated: Authentication system implementation",
      "phase": "planning"
    },
    {
      "timestamp": "2025-12-20T11:15:00Z",
      "from": "agent",
      "message": "Plan created: 3 phases, 12 tasks, estimated 8 hours",
      "phase": "planning"
    }
  ]
}
```

---

### Project Config Schema

**File:** `projects.config.json`
**Purpose:** Project registry and discovery rules

#### Schema Definition

```json
{
  "type": "object",
  "required": ["version", "projects", "centralized", "discovery_rules"],
  "properties": {
    "version": {
      "type": "string",
      "pattern": "^\\d+\\.\\d+\\.\\d+$"
    },
    "created": {
      "type": "string",
      "format": "date-time"
    },
    "description": {
      "type": "string"
    },
    "projects": {
      "type": "array",
      "items": {
        "$ref": "#/definitions/project"
      }
    },
    "centralized": {
      "type": "object",
      "properties": {
        "stubs_dir": {
          "type": "string",
          "description": "Central stubs directory path"
        },
        "description": {
          "type": "string"
        }
      }
    },
    "discovery_rules": {
      "type": "object",
      "properties": {
        "stub_discovery": { "type": "string" },
        "workorder_discovery": { "type": "string" },
        "workorder_trigger": { "type": "string" },
        "file_discovery": { "type": "string" }
      }
    }
  }
}
```

#### Project Entity Schema

```json
{
  "type": "object",
  "required": ["id", "name", "type", "path", "status"],
  "properties": {
    "id": {
      "type": "string",
      "description": "Unique project identifier"
    },
    "name": {
      "type": "string",
      "description": "Human-readable project name"
    },
    "type": {
      "type": "string",
      "enum": ["mcp_server", "application", "system"],
      "description": "Project classification"
    },
    "path": {
      "type": "string",
      "description": "Absolute filesystem path"
    },
    "has_workorders": {
      "type": "boolean",
      "description": "Whether project has workorder folder"
    },
    "workorder_dir": {
      "type": "string",
      "description": "Relative path to workorder directory"
    },
    "status": {
      "type": "string",
      "enum": ["active", "inactive"],
      "description": "Project status"
    },
    "description": {
      "type": "string"
    },
    "routes": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "path": { "type": "string" },
          "description": { "type": "string" }
        }
      },
      "description": "Application routes (if applicable)"
    }
  }
}
```

#### Example Instance

```json
{
  "version": "1.0.0",
  "created": "2025-12-26T13:00:00Z",
  "description": "Source of truth for all tracked projects",
  "projects": [
    {
      "id": "coderef-dashboard",
      "name": "CodeRef Dashboard",
      "type": "application",
      "path": "C:\\Users\\willh\\Desktop\\coderef-dashboard",
      "has_workorders": true,
      "workorder_dir": "coderef/workorder",
      "status": "active",
      "description": "Dashboard application with /coderef-assistant and /coderef-scout routes",
      "routes": [
        {
          "path": "/coderef-assistant",
          "description": "AI Assistant dashboard"
        }
      ]
    }
  ],
  "centralized": {
    "stubs_dir": "C:\\Users\\willh\\Desktop\\assistant\\coderef\\working",
    "description": "All stubs centralized in orchestrator"
  },
  "discovery_rules": {
    "stub_discovery": "Scan {stubs_dir}/*/ for stub.json files",
    "workorder_discovery": "Scan {project_path}/coderef/workorder/*/",
    "workorder_trigger": "Folder existence = workorder exists"
  }
}
```

---

## Validation Rules

### Stub Validation

**Enforced by:** `validate-stubs.py`

**Rules:**
1. `stub_id` must match pattern `^STUB-\d{3}$`
2. `feature_name` must be kebab-case (lowercase, hyphens only)
3. `description` must be 10-500 characters
4. `category` must be valid enum value
5. `priority` must be valid enum value
6. `status` must be valid enum value
7. `created` must be valid YYYY-MM-DD date
8. If `promoted_to` present, must match `^WO-[A-Z0-9-]+-\d{3}$`
9. No additional properties allowed

**Validation Command:**
```bash
python validate-stubs.py
```

---

### Workorder Validation

**Rules:**
1. `workorder_id` must match pattern `^WO-[A-Z0-9-]+-\d{3}$`
2. `location` must point to valid communication.json path
3. `status` must be valid enum value
4. `type` must be valid enum value (if present)
5. `priority` must be valid enum value (if present)
6. Date fields must be YYYY-MM-DD format

---

### Communication Validation

**Rules:**
1. `workorder_id` must match parent workorder ID
2. `status` must progress forward through status flow
3. `communication_log` entries must have valid timestamps
4. `from` field must be "orchestrator" or "agent"

---

## Data Relationships

### Entity Relationship Diagram

```
projects.md
    │
    ├──> STUB-XXX (in coderef/working/)
    │         │
    │         └──> promoted_to ──> WO-XXX
    │
    └──> projects.config.json
              │
              └──> project paths
                        │
                        └──> coderef/workorder/
                                  │
                                  └──> WO-XXX/
                                        ├── communication.json
                                        ├── context.json
                                        ├── plan.json
                                        └── DELIVERABLES.md

workorders.json
    │
    ├──> active_workorders[]
    │         └──> location ──> communication.json
    │
    └──> completed_workorders[]
              └──> location ──> archived communication.json
```

### Relationships

1. **Stub → Workorder**: `stub.promoted_to` references `workorder.workorder_id`
2. **Workorder → Communication**: `workorder.location` points to `communication.json` path
3. **Workorder → Stub**: `workorder.stub_id` references `stub.stub_id` (optional)
4. **Project → Workorder**: `workorder.target_project` references `project.id`

---

## Schema Versioning

**Current Version:** 2.0.0

**Version History:**

| Version | Date | Changes |
|---------|------|---------|
| 2.0.0 | 2025-12-28 | Added `projects.config.json` schema, standardized workorder schema |
| 1.0.0 | 2025-11-15 | Initial schemas for stub.json and workorders.json |

**Breaking Changes Policy:**
- Major version bump for required field changes or enum value removals
- Minor version bump for new optional fields
- Patch version bump for documentation/description updates

---

## Resources

- **[stub-schema.json](../../stub-schema.json)** - Canonical stub JSON Schema
- **[workorders.json](../../workorders.json)** - Live workorder data
- **[projects.config.json](../../projects.config.json)** - Project registry
- **[validate-stubs.py](../../validate-stubs.py)** - Stub validation script
- **[API.md](./API.md)** - API documentation

---

**Document ID:** `assistant-schema-v2.0.0`
**Last Generated:** 2026-01-09 via `/generate-docs`
