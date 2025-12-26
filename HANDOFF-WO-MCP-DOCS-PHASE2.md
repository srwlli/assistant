# WO-MCP-DOCS-002: Phase 2 - Cross-Server Sync Analysis

**Workorder:** WO-MCP-DOCS-002
**Session:** MCP-Server-Capabilities-Deep-Dive
**Phase:** 2 (Cross-Server Sync)
**Agent:** Docs Analysis Agent
**Location:** `C:\Users\willh\.mcp-servers\coderef-docs\`

---

## Your Task

Phase 1 is complete. All 4 servers have analyzed themselves. Now analyze how **coderef-docs** fits into the broader MCP ecosystem.

You have access to the complete findings from all 4 servers:
- ✅ coderef-context (code intelligence & AST analysis)
- ✅ coderef-workflow (planning/execution orchestration)
- ✅ coderef-docs (your server)
- ✅ coderef-personas (expert personas system)

---

## What to Analyze

### 1. **Missing Intelligence Sources**
- coderef-context can extract code elements, signatures, and patterns
- Could you be using coderef-context for auto-population of API, COMPONENTS, SCHEMA docs?
- What information from coderef-context would make your templates intelligent?

### 2. **Workflow Integration**
- How does workflow currently use your docs tools?
- Could docs generation be triggered automatically at phase completion?
- Are there workflow milestones where docs should auto-update?

### 3. **Standards & Auditing Role**
- Your standards system only covers UI/behavior/UX patterns
- What other standard types should exist (API, architecture, database, security)?
- Could coderef-context help discover additional pattern types?

### 4. **Template Extensibility**
- Your fixed 7-template enum is rigid
- Could you support custom templates?
- What would be needed to make the system template-agnostic?

### 5. **Documentation Automation**
- What's preventing full end-to-end doc automation?
- Could changelog be auto-generated from commits?
- Could code examples be auto-extracted into docs?

---

## Output Format

Update `C:\Users\willh\Desktop\assistant\session-mcp-capabilities.json`

In the `phase_2_analysis` section, add your findings. Then update your own `servers.coderef-docs` section with:

```json
{
  "phase_2_review": {
    "intelligence_gap": {
      "issue": "coderef-docs templates are placeholders - Claude writes content manually",
      "opportunity": "coderef-context can provide code intelligence for auto-population",
      "example": "API.md template could call coderef-context to extract endpoint signatures, parameters, return types"
    },
    "workflow_integration": [
      "workflow calls update_all_documentation at feature completion",
      "Missing: automatic doc generation triggered by phase completion",
      "Missing: real-time doc updates as implementation progresses"
    ],
    "standards_gaps": [
      "Only 3 pattern types: UI, behavior, UX",
      "Missing: API standards, architecture standards, database standards, security standards",
      "Missing: testing patterns, error handling patterns, deployment patterns",
      "Opportunity: Use coderef-context to discover additional pattern types"
    ],
    "template_limitations": [
      "Fixed enum of 7 templates prevents customization",
      "No way for users to define custom doc types",
      "System is brittle - adding templates requires code changes",
      "Could implement: Custom template builder, template marketplace"
    ],
    "automation_opportunities": [
      "Auto-changelog from commits (use git log + commit parsing)",
      "Code reference extraction (call coderef-context for signatures/examples)",
      "Auto-SCHEMA generation from database models (if models exist)",
      "Auto-API docs from endpoint signatures (if coderef-context provides)",
      "Auto-COMPONENTS from UI component registry (if registry exists)"
    ],
    "dependencies_analysis": {
      "depends_on": [
        "git - For record_changes, check_consistency",
        "coderef/standards/ - For audit/consistency checking"
      ],
      "should_depend_on": [
        "coderef-context - For code-driven auto-population (currently missing)"
      ]
    },
    "role_in_ecosystem": "Documentation generation layer. Template-driven system that provides POWER framework but lacks code intelligence. Currently semi-manual (Claude writes content). Should be more automated with coderef-context integration.",
    "recommendations": [
      "Integrate with coderef-context for auto-population of code-dependent docs (API, SCHEMA, COMPONENTS)",
      "Implement auto-changelog from git commit messages with semantic commit parsing",
      "Expand standards discovery to 6+ pattern types (API, architecture, database, security, testing, deployment)",
      "Create custom template support to make system extensible",
      "Implement continuous doc updates triggered by workflow phase completion",
      "Add code example extraction to pull signatures/examples into docs automatically"
    ]
  }
}
```

---

## Reference Files

- **Shared Document:** `C:\Users\willh\Desktop\assistant\session-mcp-capabilities.json` (read all servers)
- **Your Phase 1 Data:** `servers.coderef-docs` section
- **Communication:** `C:\Users\willh\.mcp-servers\coderef-docs\communication.json`

---

## Next Phase (After All 4 Agents Complete)

Once all agents complete Phase 2 and contribute to `phase_2_analysis`:
- Phase 3: Orchestrator synthesizes aggregate roadmap (doc automation priorities, code intelligence integration, template extensibility)

**You will provide input for the final roadmap.**
