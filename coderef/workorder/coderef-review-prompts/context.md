# CodeRef Review Prompts - Context

**Created:** 2026-01-01
**Status:** Planning
**Purpose:** Standardized agent review workflow system for coderef ecosystem

---

## Overview

A structured workflow system for conducting multi-agent reviews across the coderef ecosystem. Uses `{task}-communication.json` files as the coordination mechanism, with agents producing standardized analysis outputs.

---

## Core Pattern

### 1. Input
- **Communication.json** defines:
  - Review scope (via tags)
  - Questions/categories to analyze
  - Agent list with paths
  - Expected output structure

### 2. Process
- Each agent:
  - Finds their entry by `id` match
  - Reviews specified scope
  - Fills structured `analysis` fields (JSON)
  - Adds freeform `additional_comments`
  - Updates `reply_file` with path to detailed report (optional)
  - Sets `status: "complete"`

### 3. Output
- Orchestrator aggregates responses
- Generates ecosystem-wide insights
- Creates summary reports

---

## Communication.json Structure

```json
{
  "workorder_id": "WO-XXX-001",
  "feature_name": "{task-name}",
  "created": "YYYY-MM-DD",
  "instructions": "Clear, concise agent instructions",
  "review_scope": {
    "tags": ["docs:foundation", "workflow:planning", "integration:mcp"]
  },
  "agents": [
    {
      "id": "agent-name",
      "path": "absolute/path/to/agent",
      "reply_file": "path/to/detailed-report.md",
      "status": "pending|complete",
      "analysis": {
        "category_1": {
          "how_used": "",
          "strengths": "",
          "weaknesses": "",
          "add_remove": ""
        }
      },
      "additional_comments": {
        "improvements": "",
        "weaknesses": "",
        "other": ""
      }
    }
  ],
  "expected_output": "Template showing exact format"
}
```

---

## Review Scope Tags

### Code Analysis
- `code:patterns` - Code patterns and conventions
- `code:complexity` - Complexity analysis and technical debt
- `code:architecture` - System architecture and design
- `code:dependencies` - Dependency management and relationships
- `code:quality` - Code quality metrics and standards
- `code:coverage` - Test coverage and gaps
- `code:performance` - Performance bottlenecks and optimization

### Documentation
- `docs:foundation` - Foundation docs (README, ARCHITECTURE, API, SCHEMA, COMPONENTS)
- `docs:standards` - Standards docs (ui-patterns, behavior-patterns, ux-patterns)
- `docs:workflow` - Workflow/workorder docs (plan.json, context.json, communication.json, DELIVERABLES.md)
- `docs:coderef-outputs` - .coderef/ analysis outputs (index.json, context.md, reports/, diagrams/)
- `docs:claude-md` - CLAUDE.md context documentation
- `docs:user-guides` - User-facing documentation
- `docs:api-reference` - API/tool reference documentation

### Process & Workflow
- `workflow:planning` - Planning workflows (gather_context, create_plan)
- `workflow:execution` - Execution workflows (execute_plan, update_deliverables)
- `workflow:coordination` - Multi-agent coordination patterns
- `workflow:handoff` - Agent handoff protocols
- `workflow:tracking` - Progress tracking and status updates
- `workflow:archival` - Feature archival and completion

### Integration & Tooling
- `integration:mcp` - MCP server integration patterns
- `integration:ecosystem` - Cross-server dependencies and communication
- `integration:cli` - CLI tool integration
- `integration:dashboard` - Dashboard UI integration
- `integration:git` - Git workflow integration
- `integration:testing` - Test automation integration

### Standards & Compliance
- `standards:ui` - UI component standards
- `standards:ux` - UX flow standards
- `standards:behavior` - Behavior pattern standards
- `standards:api` - API design standards
- `standards:testing` - Testing standards
- `standards:documentation` - Documentation standards

### Metadata & Governance
- `metadata:versioning` - Version tracking and compatibility
- `metadata:provenance` - Scan/workorder provenance tracking
- `metadata:timestamps` - Freshness and staleness detection
- `metadata:attribution` - Author and agent attribution
- `governance:schemas` - JSON schema definitions
- `governance:validation` - Validation rules and enforcement

### Output & Artifacts
- `output:reports` - Generated reports and summaries
- `output:diagrams` - Visual diagrams (Mermaid, Graphviz)
- `output:exports` - Export formats (JSON, JSON-LD)
- `output:deliverables` - Final deliverables and artifacts

### Agent Behavior
- `agent:personas` - Persona definitions and activation
- `agent:coordination` - Multi-agent coordination
- `agent:context` - Agent context and knowledge
- `agent:tooling` - Agent tool usage patterns

### Infrastructure
- `infra:file-structure` - Directory organization
- `infra:caching` - Caching strategies
- `infra:performance` - System performance
- `infra:scalability` - Scalability patterns

---

## Benefits

- ✅ Consistent format across all reviews
- ✅ Easy progress tracking (pending/complete status)
- ✅ Machine-readable for aggregation
- ✅ Scalable to any ecosystem component
- ✅ Reusable template for different review types

---

## Use Cases

1. **Document Effectiveness Audits** - Review how agents use ecosystem documentation
2. **Code Quality Reviews** - Analyze code patterns and standards compliance
3. **Integration Testing Coordination** - Verify cross-server integration points
4. **Standards Compliance Checks** - Ensure consistency across projects
5. **Feature Gap Analysis** - Identify missing capabilities
6. **Cross-Project Dependency Reviews** - Map and validate dependencies

---

## Dashboard UI Integration

The dashboard will provide:
- Form to create new review workflows
- Agent selection interface
- Tag picker for review scope
- Communication.json generator
- Real-time status tracking
- Response aggregation and reporting

---

## Next Steps

1. Create JSON schema for communication.json format
2. Build dashboard UI for workflow creation
3. Implement agent status tracking widget
4. Create aggregation/reporting tools
5. Document example workflows for common review types
