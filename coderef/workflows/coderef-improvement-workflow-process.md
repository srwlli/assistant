# CodeRef Improvement Workflow Process

**Version:** 1.0.0
**Purpose:** Standardized process for improving code, workflows, and processes through systematic agent review

---

## WHAT

**A structured workflow for agents to review, analyze, and propose improvements to any aspect of the coderef ecosystem**

### What It Does
- Coordinates multi-agent reviews across the ecosystem
- Captures structured feedback (strengths, weaknesses, improvements)
- Tracks review progress via communication.json
- Aggregates insights for ecosystem-wide improvements

### What It Requires
- Review scope definition (via tags)
- Agent list with paths
- Communication.json coordination file
- Analysis structure template

### What It Produces
- `{task}-communication.json` - Agent coordination and responses
- Agent-specific analysis (structured JSON fields)
- Aggregated improvement recommendations
- Actionable next steps

---

## HOW

### How It Works (5 Phases)

**Phase 1: Define Review Scope**
1. Select review tags (docs, code, workflow, integration, etc.)
2. Choose target agents (servers/projects to review)
3. Define analysis questions (how_used, strengths, weaknesses, add_remove)

**Phase 2: Generate Communication File**
1. Create `{task}-communication.json` with:
   - Workorder ID
   - Agent list (id, path, status)
   - Review scope (tags)
   - Analysis structure template
2. Save to `coderef/working/{task}/`

**Phase 3: Agent Review**
1. Each agent finds their entry by `id`
2. Reviews specified scope (documents, code, patterns)
3. Fills structured `analysis` fields
4. Adds freeform `additional_comments`
5. Updates `status: "complete"`

**Phase 4: Progress Tracking**
1. Orchestrator reads communication.json
2. Monitors agent status (pending/complete)
3. Identifies blockers or incomplete reviews

**Phase 5: Aggregation & Action**
1. Collect all agent responses
2. Identify common themes (recurring weaknesses, shared improvements)
3. Generate summary report
4. Create actionable workorders for top improvements

### How Tags Define Scope

**Tag Format:** `category:specific-area`

**Tag Selection:**
- Single tag: Narrow review (e.g., `docs:foundation` only)
- Multiple tags: Broad review (e.g., `docs:foundation`, `workflow:planning`, `integration:mcp`)
- All tags in category: Comprehensive audit (e.g., all `docs:*` tags)

**Tag Usage in Communication.json:**
```json
{
  "review_scope": {
    "tags": ["docs:foundation", "docs:standards", "workflow:planning"]
  }
}
```

### How Agents Respond

**Required Fields:**
- `how_used` - How this component/doc is used
- `strengths` - What works well
- `weaknesses` - What's missing or unclear
- `add_remove` - Specific suggestions

**Optional Fields:**
- `additional_comments.improvements` - General improvements
- `additional_comments.weaknesses` - Systemic issues
- `additional_comments.other` - Anything else

**Response Location:**
- Directly in communication.json under agent's entry
- OR separate file with path in `reply_file` field

---

## WHY

### Why This Process Exists

**Problem:** Ad-hoc improvements are reactive and fragmented
- No systematic way to identify ecosystem gaps
- Agent feedback scattered across conversations
- Hard to prioritize improvements
- No tracking of what was reviewed/when

**Solution:** Structured review workflow
- Proactive improvement discovery
- Consistent feedback format across all agents
- Clear prioritization via aggregation
- Full audit trail in communication.json

### Why Tag-Based Scoping

**Flexibility:**
- Review exactly what you need (narrow or broad)
- Mix categories (code + docs + workflow in one review)
- Reusable taxonomy across all reviews

**Clarity:**
- Agents know exactly what to focus on
- No ambiguity about review boundaries
- Consistent categorization

**Scalability:**
- Add new tags as ecosystem grows
- Agents self-select relevant tags
- Easy to run targeted vs comprehensive reviews

### Why Communication.json

**Single Source of Truth:**
- All agents update same file
- Real-time progress visibility
- No manual status checking

**Machine-Readable:**
- Automated aggregation
- Status tracking via scripts
- Integration with dashboard

**Version-Controlled:**
- Git history of reviews
- Reproducible analysis
- Diff-able improvements over time

### Why Structured + Freeform

**Structured Analysis:**
- Ensures completeness (all agents answer same questions)
- Aggregatable (can group by field)
- Comparable (strengths vs weaknesses counts)

**Freeform Comments:**
- Captures nuanced insights
- Allows unexpected findings
- Gives agents flexibility

**Both Together:**
- Quantitative + qualitative data
- Structured for automation, flexible for discovery

---

## Review Scope Tags

### Code Analysis
- `code:patterns` - Code patterns and conventions
- `code:complexity` - Complexity analysis and technical debt
- `code:architecture` - System architecture and design
- `code:dependencies` - Dependency management
- `code:quality` - Code quality metrics
- `code:coverage` - Test coverage
- `code:performance` - Performance optimization

### Documentation
- `docs:foundation` - Foundation docs (README, ARCHITECTURE, API, SCHEMA, COMPONENTS)
- `docs:standards` - Standards docs (ui-patterns, behavior-patterns, ux-patterns)
- `docs:workflow` - Workflow/workorder docs (plan.json, context.json, communication.json)
- `docs:coderef-outputs` - .coderef/ analysis outputs
- `docs:claude-md` - CLAUDE.md context documentation
- `docs:user-guides` - User-facing documentation
- `docs:api-reference` - API/tool reference

### Process & Workflow
- `workflow:planning` - Planning workflows
- `workflow:execution` - Execution workflows
- `workflow:coordination` - Multi-agent coordination
- `workflow:handoff` - Agent handoff protocols
- `workflow:tracking` - Progress tracking
- `workflow:archival` - Feature archival

### Integration & Tooling
- `integration:mcp` - MCP server integration
- `integration:ecosystem` - Cross-server dependencies
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
- `metadata:versioning` - Version tracking
- `metadata:provenance` - Scan/workorder provenance
- `metadata:timestamps` - Freshness detection
- `metadata:attribution` - Author attribution
- `governance:schemas` - JSON schema definitions
- `governance:validation` - Validation rules

### Output & Artifacts
- `output:reports` - Generated reports
- `output:diagrams` - Visual diagrams
- `output:exports` - Export formats
- `output:deliverables` - Final deliverables

### Agent Behavior
- `agent:personas` - Persona definitions
- `agent:coordination` - Multi-agent coordination
- `agent:context` - Agent context and knowledge
- `agent:tooling` - Agent tool usage

### Infrastructure
- `infra:file-structure` - Directory organization
- `infra:caching` - Caching strategies
- `infra:performance` - System performance
- `infra:scalability` - Scalability patterns

---

## Communication.json Structure

```json
{
  "workorder_id": "WO-IMPROVEMENT-XXX-001",
  "feature_name": "{task-name}",
  "created": "YYYY-MM-DD",
  "instructions": "AGENT: Review scope, fill analysis, update status",
  "review_scope": {
    "tags": ["tag1", "tag2", "tag3"]
  },
  "agents": [
    {
      "id": "agent-name",
      "path": "/absolute/path/to/agent",
      "reply_file": "optional/path/to/detailed-report.md",
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
  ]
}
```

---

## Use Cases

### Document Effectiveness Audit
**Goal:** Understand how agents use ecosystem documentation
**Tags:** `docs:foundation`, `docs:standards`, `docs:workflow`, `docs:coderef-outputs`
**Agents:** All MCP servers + coderef-system + coderef-dashboard
**Outcome:** Identify missing docs, stale content, integration gaps

### Code Quality Review
**Goal:** Assess code patterns and technical debt
**Tags:** `code:patterns`, `code:complexity`, `code:quality`
**Agents:** coderef-context, coderef-system, coderef-dashboard
**Outcome:** Refactoring priorities, pattern standardization

### Workflow Optimization
**Goal:** Streamline planning and execution workflows
**Tags:** `workflow:planning`, `workflow:execution`, `workflow:coordination`
**Agents:** coderef-workflow, coderef-docs, coderef-personas
**Outcome:** Workflow improvements, bottleneck removal

### Integration Testing
**Goal:** Verify cross-server integration points
**Tags:** `integration:ecosystem`, `integration:mcp`
**Agents:** All MCP servers
**Outcome:** Integration issues, missing handoffs, dependency problems

### Standards Compliance Check
**Goal:** Ensure consistency across projects
**Tags:** `standards:ui`, `standards:api`, `standards:documentation`
**Agents:** coderef-docs, coderef-dashboard, target projects
**Outcome:** Standards violations, pattern inconsistencies

---

## Agent Instructions

### For Agents Being Reviewed
1. Read communication.json at `coderef/working/{task}/{task}-communication.json`
2. Find your entry by matching `id` field
3. For each tag in `review_scope.tags`, analyze the specified area
4. Fill in `analysis` fields (how_used, strengths, weaknesses, add_remove)
5. Add any additional insights to `additional_comments`
6. Update `status` to `complete`
7. Optionally create detailed report and link in `reply_file`

### For Orchestrator
1. Define review scope (tags) and select agents
2. Generate communication.json using template
3. Save to `coderef/working/{task}/`
4. Monitor agent status (poll communication.json)
5. After all agents complete:
   - Aggregate responses
   - Identify common themes
   - Generate summary report
   - Create workorders for top improvements
6. Archive communication.json to `coderef/workorder/{task}/`

---

## Dashboard Integration

**Workflow Creation UI:**
- Form to define review scope (tag picker)
- Agent selection (multi-select from available agents)
- Communication.json generator
- Save to filesystem

**Status Tracking Widget:**
- Real-time agent completion status
- Progress bar (X of Y agents complete)
- Agent-specific status indicators

**Aggregation View:**
- Summary of all responses
- Theme detection (common weaknesses/improvements)
- Actionable recommendations list

---

## Future Enhancements

- Auto-aggregation scripts (analyze communication.json → generate report)
- Dashboard widgets for review creation/tracking
- Template library (common review types)
- Historical comparison (track improvements over time)
- Agent notification system (alert when review assigned)
- Workflow scheduling (periodic reviews)
- Integration with workorder system (auto-create improvement workorders)
