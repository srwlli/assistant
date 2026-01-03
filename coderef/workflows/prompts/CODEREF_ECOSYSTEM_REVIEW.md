# CODEREF Ecosystem Review Prompt

**Version:** 1.0.0
**Category:** Agent Coordination
**Output Format:** JSON

---

## What It Does

Standardized prompt for agents to analyze how they use coderef ecosystem documents and propose improvements. Enables systematic ecosystem reviews with structured, aggregatable feedback.

**Output:** JSON analysis of 4 document categories with usage patterns, strengths, weaknesses, and recommendations.

---

## How to Use

### 1. Variable Substitution

Replace these variables in the prompt template:

- `{{agent_id}}` - Agent identifier (e.g., `coderef-docs`)
- `{{agent_path}}` - Full path to agent server/project
- `{{workorder_id}}` - Tracking ID (e.g., `WO-DOC-OUTPUT-AUDIT-001`)

### 2. Assign to Agent

Add to `communication.json` or paste directly into agent chat:

```json
{
  "agents": [
    {
      "id": "coderef-docs",
      "status": "pending",
      "prompt": "CODEREF_ECOSYSTEM_REVIEW"
    }
  ]
}
```

### 3. Agent Executes

Agent reviews their codebase and outputs structured JSON covering:

- **foundation_docs** - How they use README, ARCHITECTURE, SCHEMA, etc.
- **standards_docs** - How they use ui-patterns, behavior-patterns, etc.
- **workflow_workorder_docs** - How they use plan.json, DELIVERABLES.md, etc.
- **coderef_analysis_outputs** - How they use .coderef/index.json, context.md, etc.

### 4. Orchestrator Aggregates

Collect all agent responses and generate unified ecosystem improvement report.

---

## Why This Approach

### Problem

Ad-hoc ecosystem improvements are reactive and fragmented. No systematic way to gather agent perspectives on documentation effectiveness.

### Solution

Structured review template with:
- **Consistent schema** - All agents answer the same questions
- **JSON output** - Machine-readable for aggregation
- **Tag-based scoping** - 40+ tags for granular analysis
- **Provenance tracking** - Workorder IDs link reviews to improvements

### Benefits

1. **Systematic** - Every agent reviews the same document categories
2. **Aggregatable** - JSON responses merge into ecosystem-wide view
3. **Actionable** - Identifies specific gaps with concrete recommendations
4. **Traceable** - Workorder IDs connect reviews to changes
5. **Reusable** - Template works for any ecosystem review type

---

## Document Categories

### 1. Foundation Docs

**Files:** README.md, ARCHITECTURE.md, API.md, COMPONENTS.md, SCHEMA.md, CLAUDE.md

**Review Focus:**
- Do you read these for context?
- Do you generate/update them?
- Are they comprehensive enough for your workflows?
- What's missing?

### 2. Standards Docs

**Files:** ui-patterns.md, behavior-patterns.md, ux-patterns.md, standards-overview.md

**Review Focus:**
- Do you enforce these standards?
- Do you reference them in outputs?
- Are patterns relevant to your domain?
- What patterns are missing?

### 3. Workflow/Workorder Docs

**Files:** context.json, plan.json, communication.json, DELIVERABLES.md

**Review Focus:**
- How do you interact with workorder lifecycle?
- Do you read/write these files?
- Are schemas clear and complete?
- What friction points exist?

### 4. CodeRef Analysis Outputs

**Files:** .coderef/index.json, context.md, patterns.json, coverage.json, diagrams/, exports/

**Review Focus:**
- Do you generate these outputs?
- Do you consume them for analysis?
- Are schemas documented?
- What's the utilization rate?

---

## Integration Points

### Workflow Integration

- **Workflow:** `coderef-improvement-workflow-process`
- **Coordination File:** `document-output-audit-communication.json`
- **Phase:** 2 (Agent Review)

### Dashboard Integration

- **Route:** `/prompts` (coderef-dashboard)
- **Step 1:** Select `CODEREF_ECOSYSTEM_REVIEW` from library
- **Step 2:** Add agent variables as attachments
- **Step 3:** Export JSON and paste into agent chat
- **Step 4:** Save agent response to coordination file

---

## Output Schema

```json
{
  "agent_id": "string",
  "workorder_id": "string",
  "reply_file": "string (absolute path)",
  "status": "complete | pending",
  "analysis": {
    "foundation_docs": {
      "how_used": "string (50-500 chars)",
      "strengths": "string (50-500 chars)",
      "weaknesses": "string (50-500 chars)",
      "add_remove": "string (50-500 chars)"
    },
    "standards_docs": { /* same structure */ },
    "workflow_workorder_docs": { /* same structure */ },
    "coderef_analysis_outputs": { /* same structure */ }
  },
  "additional_comments": {
    "improvements": "string",
    "weaknesses": "string",
    "other": "string"
  }
}
```

---

## Quality Standards

### Response Quality

- **Specificity** - Concrete examples with file/line references
- **Honesty** - Real gaps and friction points, not aspirational
- **Constructiveness** - Actionable improvements, not just complaints
- **Conciseness** - 50-500 chars per field (complete but focused)

### JSON Requirements

- **Pure JSON** - No markdown formatting, no code blocks
- **Valid syntax** - Passes JSON.parse()
- **Complete schema** - All required fields present
- **Consistent structure** - Matches template exactly

---

## Example Usage

### Variables

```json
{
  "agent_id": "coderef-docs",
  "agent_path": "C:\\Users\\willh\\.mcp-servers\\coderef-docs",
  "workorder_id": "WO-DOC-OUTPUT-AUDIT-001"
}
```

### Agent Response (excerpt)

```json
{
  "agent_id": "coderef-docs",
  "workorder_id": "WO-DOC-OUTPUT-AUDIT-001",
  "reply_file": "C:\\Users\\willh\\.mcp-servers\\coderef-docs\\coderef-document-audit-reply.json",
  "status": "complete",
  "analysis": {
    "foundation_docs": {
      "how_used": "GENERATOR: Auto-generate README, ARCHITECTURE, API, SCHEMA from templates. Read existing docs for deep extraction during planning.",
      "strengths": "Templates provide consistent structure. Deep extraction mode captures 90% of context.",
      "weaknesses": "No versioning. Limited to 500-char preview. Missing POWER framework validation.",
      "add_remove": "ADD: Semantic search. ADD: Version tracking. ADD: POWER compliance checker."
    }
  }
}
```

---

## Use Cases

### UC-1: Quarterly Ecosystem Review

Review all 8 agents quarterly to identify systemic documentation gaps.

### UC-2: Pre-Refactor Analysis

Before major refactors, gather agent perspectives on what documentation would help.

### UC-3: New Agent Onboarding

When adding new MCP servers, use template to identify documentation needs upfront.

### UC-4: Documentation ROI Analysis

Track which docs are actually used vs. ignored to prioritize maintenance efforts.

---

## Related Resources

- **Prompts Library Guide:** `coderef/workflows/prompts/prompts-library-guide.md`
- **Improvement Workflow:** `coderef/workflows/coderef-improvement-workflow-process.md`
- **Dashboard Workflow:** `coderef/workflows/coderef-dashboard-prompts-workflow-standards.md`
- **Communication Pattern:** `coderef/working/document-output-audit/document-output-audit-communication.json`

---

**Created:** 2026-01-01
**Workorder:** WO-DOC-OUTPUT-AUDIT-001
**MCP Attribution:** coderef-assistant (orchestrator)
