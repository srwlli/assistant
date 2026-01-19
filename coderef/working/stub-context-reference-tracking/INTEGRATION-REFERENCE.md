# Integration Reference: everything-claude-code → coderef System

**Created:** 2026-01-19
**Status:** Planning
**Related Stub:** stub-context-reference-tracking
**Reference:** https://github.com/affaan-m/everything-claude-code

---

## Executive Summary

This document outlines recommended integrations from the everything-claude-code repository into the coderef orchestration system. Focus is on three high-impact systems: **Hooks** (event automation), **Rules** (enforcement), and **Skills** (workflow templates).

**Key Insight:** everything-claude-code provides general-purpose dev workflows, while coderef has superior AST-based scanning (99% accuracy). The integration strategy is to adopt their automation/enforcement patterns while preserving our advanced analysis capabilities.

---

## 1. Hooks System (Priority: HIGH)

### What It Is
Event-triggered automation that executes shell commands or tool calls in response to file operations, tool usage, or status changes.

### Architecture
```yaml
hooks:
  - name: "auto-validate-stub"
    trigger: "write:coderef/working/*/stub.json"
    action: "mcp__papertrail__validate_stub"
    params:
      auto_fill: true
      save: true

  - name: "auto-generate-handoff"
    trigger: "write:*/plan.json"
    action: "mcp__coderef-docs__generate_handoff_context"

  - name: "auto-verify-completion"
    trigger: "edit:*/communication.json"
    condition: "status == 'complete'"
    action: "verify_workorder_completion"
```

### Integration Points

| Hook Name | Trigger | Action | Impact |
|-----------|---------|--------|--------|
| **auto-validate-stub** | stub.json created | Validate + auto-fill with papertrail | Eliminates manual validation step |
| **auto-generate-handoff** | plan.json created | Generate handoff prompt | Automates delegation workflow |
| **auto-verify-completion** | communication.json status=complete | Verify deliverables + update tracking | Automates Phase 4 verification |
| **auto-update-dashboard** | workorders.json updated | Regenerate index.html | Real-time dashboard sync |
| **auto-archive-notification** | Feature archived | Update projects.md + workorders.json | Cross-project tracking sync |

### Implementation Checklist

- [ ] Create `hooks.yaml` configuration file in `C:\Users\willh\Desktop\assistant\.claude\`
- [ ] Add file watcher system (use Node.js `chokidar` or Python `watchdog`)
- [ ] Create hook executor module that runs MCP tools or shell commands
- [ ] Add condition evaluator for context-aware triggers (e.g., `status == 'complete'`)
- [ ] Test with stub.json creation workflow
- [ ] Document hook system in CLAUDE.md

### Code Example

```yaml
# C:\Users\willh\Desktop\assistant\.claude\hooks.yaml

hooks:
  # Phase 1: Stub Creation
  - name: auto-validate-stub
    trigger: write:coderef/working/*/stub.json
    action: mcp__papertrail__validate_stub
    params:
      file_path: "${FILE_PATH}"
      auto_fill: true
      save: true
    log: "Stub validated and auto-filled: ${FILE_PATH}"

  # Phase 2: Plan Generation
  - name: auto-generate-handoff
    trigger: write:**/plan.json
    condition: workorder_id != null
    action: mcp__coderef-docs__generate_handoff_context
    params:
      plan_path: "${FILE_PATH}"
      workorder_id: "${WORKORDER_ID}"
    log: "Handoff prompt generated for ${WORKORDER_ID}"

  # Phase 4: Completion Verification
  - name: auto-verify-completion
    trigger: edit:**/communication.json
    condition: |
      json.status == "complete" &&
      json.handoff.archived == true
    action: verify_workorder_completion
    params:
      workorder_id: "${json.workorder_id}"
      project_path: "${PROJECT_PATH}"
    log: "Workorder ${json.workorder_id} verified and closed"

  # Dashboard Updates
  - name: auto-update-dashboard
    trigger: edit:workorders.json
    action: regenerate_dashboard
    debounce: 2000  # Wait 2s for multiple edits
    log: "Dashboard updated"
```

---

## 2. Rules System (Priority: MEDIUM-HIGH)

### What It Is
Always-enforced guidelines that agents must follow. Rules act as guardrails preventing protocol violations.

### Architecture
```yaml
rules:
  - name: "orchestrator-read-only"
    scope: "orchestrator"
    enforcement: "block"
    condition: "tool == 'Write' || tool == 'Edit'"
    validation: "file_path not in ['assistant/']"

  - name: "workorder-tracking-required"
    scope: "all"
    enforcement: "warn"
    condition: "tool == 'Bash' && command.includes('git commit')"
    validation: "message.match(/WO-[A-Z]+-\\d+|STUB-\\d+/)"
```

### Integration Points

| Rule Name | Scope | Enforcement | Purpose |
|-----------|-------|-------------|---------|
| **orchestrator-read-only** | Orchestrator agent | Block | Prevent orchestrator from writing to target projects |
| **workorder-tracking-required** | All agents | Warn | Ensure commits reference WO-XXX or STUB-XXX |
| **communication-json-required** | Project agents | Block | Prevent WO activation without communication.json |
| **handoff-protocol-enforced** | Orchestrator | Block | Ensure context.json + communication.json exist before handoff |
| **deliverables-before-archive** | Project agents | Block | Prevent archival without populated DELIVERABLES.md |

### Implementation Checklist

- [ ] Create `rules.yaml` configuration file in `C:\Users\willh\Desktop\assistant\.claude\`
- [ ] Add rule validator that intercepts tool calls
- [ ] Implement enforcement levels (block, warn, log)
- [ ] Create condition evaluator (access to tool name, params, context)
- [ ] Add rule violation logging
- [ ] Document rules system in CLAUDE.md

### Code Example

```yaml
# C:\Users\willh\Desktop\assistant\.claude\rules.yaml

rules:
  # Design Decision 1: Orchestrator Never Executes in Target Projects
  - name: orchestrator-read-only
    description: "Orchestrator can only read from target projects, never write"
    scope: agent:orchestrator
    enforcement: block
    triggers:
      - tool: Write
      - tool: Edit
      - tool: Bash
        condition: command.includes('>')
    validation: |
      file_path.startsWith('C:\\Users\\willh\\Desktop\\assistant\\')
    violation_message: "Orchestrator cannot write to target projects. Use handoff protocol to delegate work."

  # Design Decision 2: Workorder Tracking Required
  - name: workorder-tracking-required
    description: "All git commits must reference WO-XXX or STUB-XXX"
    scope: all
    enforcement: warn
    triggers:
      - tool: Bash
        condition: command.includes('git commit')
    validation: |
      params.command.match(/WO-[A-Z]+-\d+|STUB-\d+/)
    violation_message: "Commit message missing workorder/stub ID. Add WO-XXX or STUB-XXX."

  # Design Decision 3: communication.json Required
  - name: communication-json-required
    description: "All workorders must have communication.json before activation"
    scope: agent:orchestrator
    enforcement: block
    triggers:
      - tool: mcp__coderef-docs__generate_handoff_context
    validation: |
      fs.existsSync(path.join(project_path, 'communication.json'))
    violation_message: "Cannot generate handoff without communication.json. Run handoff protocol workflow first."

  # Design Decision 4: Deliverables Before Archive
  - name: deliverables-before-archive
    description: "Agent must populate DELIVERABLES.md before archiving"
    scope: agent:project
    enforcement: block
    triggers:
      - tool: mcp__coderef-workflow__archive_feature
    validation: |
      const deliverables = fs.readFileSync('DELIVERABLES.md', 'utf8');
      !deliverables.includes('TBD') && deliverables.includes('commits:')
    violation_message: "Run /update-deliverables before archiving. DELIVERABLES.md contains TBD values."

  # Context Window Management
  - name: mcp-limit-enforcement
    description: "Prevent enabling >10 MCPs per project (context window management)"
    scope: all
    enforcement: warn
    triggers:
      - config: mcp_servers
    validation: |
      Object.keys(mcp_servers).filter(s => s.enabled).length <= 10
    violation_message: "Warning: >10 MCPs enabled. Context window may be reduced to ~70k tokens."
```

---

## 3. Skills Library (Priority: MEDIUM)

### What It Is
Reusable workflow templates that codify multi-step processes. Skills are invoked by name and execute a predefined sequence.

### Architecture
```yaml
skill: "promote-stub-to-workorder"
description: "Convert STUB-XXX to WO-FEATURE-XXX and delegate to project agent"
steps:
  - name: "Assign workorder ID"
    action: generate_workorder_id
  - name: "Gather context"
    action: mcp__coderef-workflow__gather_context
  - name: "Create context.json"
    action: create_context_file
  - name: "Create communication.json"
    action: create_communication_file
```

### Integration Points

| Skill Name | Purpose | Steps | MCP Tools Used |
|------------|---------|-------|----------------|
| **promote-stub-to-workorder** | Automate STUB→WO promotion | 7 steps | gather_context, generate_handoff_context |
| **verify-workorder-completion** | Automate Phase 4 verification | 6 steps | validate_document, check_document_health |
| **generate-status-report** | Cross-project aggregation | 4 steps | Read multiple communication.json |
| **dependency-check** | Validate WO dependencies | 3 steps | coderef_query (depends-on) |

### Implementation Checklist

- [ ] Create `skills/` directory in `C:\Users\willh\Desktop\assistant\.claude\`
- [ ] Create skill definition schema (YAML or JSON)
- [ ] Build skill executor that runs steps sequentially
- [ ] Add step validation and rollback on failure
- [ ] Create /run-skill slash command
- [ ] Document skills library in CLAUDE.md

### Code Example

```yaml
# C:\Users\willh\Desktop\assistant\.claude\skills\promote-stub-to-workorder.yaml

name: promote-stub-to-workorder
description: "Automate STUB-XXX to WO-FEATURE-XXX promotion with full handoff protocol"
version: "1.0.0"
author: "coderef-assistant"

inputs:
  - name: stub_id
    type: string
    pattern: "STUB-\\d+"
    required: true
  - name: target_project
    type: string
    required: true
  - name: feature_name
    type: string
    required: true

outputs:
  - workorder_id
  - handoff_prompt

steps:
  - name: assign-workorder-id
    description: "Generate WO-FEATURE-XXX ID"
    action: |
      const project_prefix = target_project.toUpperCase().replace(/-/g, '_');
      const counter = getNextWorkorderCounter(target_project);
      workorder_id = `WO-${project_prefix}-${String(counter).padStart(3, '0')}`;
    outputs:
      - workorder_id

  - name: gather-context
    description: "Gather implementation context from target project"
    tool: mcp__coderef-workflow__gather_context
    params:
      project_path: "${target_project_path}"
      feature_name: "${feature_name}"
    outputs:
      - context_data

  - name: create-context-json
    description: "Create context.json in target project"
    action: |
      const context = {
        workorder_id: workorder_id,
        stub_id: stub_id,
        feature_name: feature_name,
        requirements: context_data.requirements,
        constraints: context_data.constraints,
        technical_context: context_data.technical_context
      };
      fs.writeFileSync(
        path.join(target_project_path, 'coderef/working', feature_name, 'context.json'),
        JSON.stringify(context, null, 2)
      );

  - name: create-communication-json
    description: "Create communication.json with pending_plan status"
    action: |
      const communication = {
        workorder_id: workorder_id,
        status: "pending_plan",
        handoff: {
          orchestrator_to_agent: "Awaiting handoff prompt generation",
          status: "pending_plan"
        },
        communication_log: []
      };
      fs.writeFileSync(
        path.join(target_project_path, 'coderef/working', feature_name, 'communication.json'),
        JSON.stringify(communication, null, 2)
      );

  - name: update-workorders-json
    description: "Add to orchestrator's workorders.json"
    action: |
      const workorders = JSON.parse(fs.readFileSync('workorders.json'));
      workorders.active_workorders.push({
        workorder_id: workorder_id,
        stub_id: stub_id,
        feature_name: feature_name,
        target_project: target_project,
        status: "pending_plan",
        created: new Date().toISOString()
      });
      fs.writeFileSync('workorders.json', JSON.stringify(workorders, null, 2));

  - name: generate-handoff-prompt
    description: "Generate handoff prompt for project agent"
    tool: mcp__coderef-docs__generate_handoff_context
    params:
      workorder_id: "${workorder_id}"
      context_path: "${target_project_path}/coderef/working/${feature_name}/context.json"
    outputs:
      - handoff_prompt

  - name: present-handoff
    description: "Display handoff prompt to user"
    action: |
      console.log(`\n=== WORKORDER CREATED: ${workorder_id} ===\n`);
      console.log(`Stub: ${stub_id}`);
      console.log(`Target: ${target_project}`);
      console.log(`Location: ${target_project_path}/coderef/working/${feature_name}/\n`);
      console.log("Files created:");
      console.log("  - context.json");
      console.log("  - communication.json\n");
      console.log("=== HANDOFF PROMPT ===\n");
      console.log(handoff_prompt);

rollback:
  - Delete context.json if created
  - Delete communication.json if created
  - Remove from workorders.json
  - Delete feature directory if empty

validation:
  pre:
    - Stub exists in coderef/working/
    - Target project path is valid
    - Feature name is slug format
  post:
    - context.json exists and valid JSON
    - communication.json exists and valid JSON
    - workorders.json updated
    - handoff_prompt generated
```

---

## 4. Enhanced Planning Context (Priority: LOW-MEDIUM)

### What It Is
Integration of coderef-context scanning (AST-based analysis) earlier in the planning phase to surface complexity, risk, and patterns before implementation.

### Current State
```
gather_context → create_plan → execute_plan
```

### Enhanced State
```
gather_context →
  ├── coderef_complexity (identify risky code)
  ├── coderef_patterns (detect anti-patterns)
  ├── coderef_coverage (find test gaps)
  └── create_plan (with risk-aware context)
```

### Integration Points

| Phase | MCP Tool | Purpose | Output |
|-------|----------|---------|--------|
| **Pre-Planning** | coderef_scan | Scan target project codebase | index.json + graph.json |
| **Risk Analysis** | coderef_complexity | Score complexity of affected elements | Complexity metrics |
| **Pattern Detection** | coderef_patterns | Find anti-patterns in change area | Pattern report |
| **Test Coverage** | coderef_coverage | Identify test coverage gaps | Coverage report |
| **Impact Analysis** | coderef_impact | Predict what breaks if X changes | Dependency graph |

### Implementation Checklist

- [ ] Update `mcp__coderef-workflow__gather_context` to call coderef_complexity
- [ ] Update `mcp__coderef-workflow__create_plan` to include risk_factors section
- [ ] Modify plan.json schema to add:
  - `risk_assessment` (complexity score, affected systems)
  - `test_coverage_gaps` (areas needing tests)
  - `anti_patterns_found` (issues to address)
- [ ] Update handoff prompt template to include risk summary
- [ ] Document enhanced planning in CLAUDE.md

### Code Example

```python
# Enhanced gather_context in coderef-workflow MCP server

def gather_context(project_path: str, feature_name: str) -> dict:
    """
    Enhanced context gathering with AST-based analysis
    """
    # Original context gathering
    context = {
        "requirements": extract_requirements(project_path, feature_name),
        "constraints": extract_constraints(project_path),
        "technical_context": extract_technical_context(project_path)
    }

    # NEW: Risk assessment via coderef-context
    try:
        # Scan codebase
        scan_result = mcp_call("mcp__coderef-context__coderef_scan", {
            "project_path": project_path
        })

        # Analyze complexity of affected areas
        affected_files = identify_affected_files(feature_name)
        complexity_scores = []
        for file in affected_files:
            complexity = mcp_call("mcp__coderef-context__coderef_complexity", {
                "project_path": project_path,
                "element": file
            })
            complexity_scores.append(complexity)

        # Detect patterns
        patterns = mcp_call("mcp__coderef-context__coderef_patterns", {
            "project_path": project_path
        })

        # Check test coverage
        coverage = mcp_call("mcp__coderef-context__coderef_coverage", {
            "project_path": project_path
        })

        # Add to context
        context["risk_assessment"] = {
            "complexity_scores": complexity_scores,
            "avg_complexity": sum(s["score"] for s in complexity_scores) / len(complexity_scores),
            "high_risk_areas": [s for s in complexity_scores if s["score"] > 15]
        }

        context["anti_patterns_found"] = patterns.get("anti_patterns", [])
        context["test_coverage_gaps"] = coverage.get("uncovered_areas", [])

    except Exception as e:
        # Graceful degradation if coderef-context unavailable
        context["risk_assessment"] = {"error": str(e)}

    return context
```

---

## Implementation Roadmap

### Phase 1: Hooks System (Weeks 1-2)
**Goal:** Automate stub validation, handoff generation, and completion verification

**Deliverables:**
- [ ] hooks.yaml configuration file
- [ ] File watcher system (chokidar/watchdog)
- [ ] Hook executor module
- [ ] 3 critical hooks implemented:
  - auto-validate-stub
  - auto-generate-handoff
  - auto-verify-completion
- [ ] Documentation in CLAUDE.md

**Success Criteria:**
- Stub.json auto-validates on creation
- Handoff prompts auto-generate when plan.json created
- Workorders auto-verify when communication.json status=complete

---

### Phase 2: Rules Enforcement (Weeks 3-4)
**Goal:** Prevent protocol violations programmatically

**Deliverables:**
- [ ] rules.yaml configuration file
- [ ] Rule validator interceptor
- [ ] Enforcement levels (block, warn, log)
- [ ] 4 critical rules implemented:
  - orchestrator-read-only
  - workorder-tracking-required
  - communication-json-required
  - deliverables-before-archive
- [ ] Rule violation logging system
- [ ] Documentation in CLAUDE.md

**Success Criteria:**
- Orchestrator blocked from writing to target projects
- Git commits without WO-XXX/STUB-XXX trigger warnings
- Archival blocked if DELIVERABLES.md contains TBD

---

### Phase 3: Skills Library (Weeks 5-6)
**Goal:** Codify workflows as reusable templates

**Deliverables:**
- [ ] .claude/skills/ directory structure
- [ ] Skill definition schema
- [ ] Skill executor with step validation
- [ ] 3 critical skills implemented:
  - promote-stub-to-workorder
  - verify-workorder-completion
  - generate-status-report
- [ ] /run-skill slash command
- [ ] Documentation in CLAUDE.md

**Success Criteria:**
- STUB→WO promotion fully automated via skill
- Workorder verification automated via skill
- Cross-project status reports generated via skill

---

### Phase 4: Enhanced Planning Context (Weeks 7-8)
**Goal:** Integrate AST-based scanning into planning phase

**Deliverables:**
- [ ] Updated gather_context with coderef-context calls
- [ ] Enhanced plan.json schema with risk_assessment
- [ ] Handoff prompt template with risk summary
- [ ] Documentation updates
- [ ] Integration tests

**Success Criteria:**
- Plans include complexity scores for affected areas
- Plans identify anti-patterns before implementation
- Plans surface test coverage gaps
- Handoff prompts include risk context

---

## Validation & Testing

### Hooks System Tests
```yaml
test: auto-validate-stub
  given: New stub.json created in coderef/working/test-feature/
  when: File write completes
  then:
    - Hook triggers within 1s
    - Papertrail validates stub
    - Auto-fill completes
    - Stub.json updated with defaults

test: auto-generate-handoff
  given: plan.json created with workorder_id
  when: File write completes
  then:
    - Hook triggers within 1s
    - Handoff context generated
    - Prompt displayed to user
```

### Rules System Tests
```yaml
test: orchestrator-read-only
  given: Orchestrator agent active
  when: Attempt Write to target project
  then:
    - Tool call blocked
    - Violation message displayed
    - No file written

test: workorder-tracking-required
  given: Git commit without WO-XXX
  when: Bash tool runs git commit
  then:
    - Warning displayed
    - Commit still executes (warn level)
    - Violation logged
```

### Skills System Tests
```yaml
test: promote-stub-to-workorder
  given: Valid stub in coderef/working/
  when: Skill invoked with stub_id, target_project, feature_name
  then:
    - Workorder ID assigned
    - context.json created in target project
    - communication.json created in target project
    - workorders.json updated
    - Handoff prompt generated
    - All files valid JSON
```

---

## Maintenance & Evolution

### Version Control
- All hooks, rules, and skills versioned in git
- Breaking changes require major version bump
- Backward compatibility maintained for 2 versions

### Documentation
- Each hook/rule/skill documented in CLAUDE.md
- Examples provided for common use cases
- Troubleshooting guide for failures

### Monitoring
- Hook execution logged with timestamps
- Rule violations tracked in violations.log
- Skill execution metrics (success rate, avg duration)

---

## Appendix: Comparison Matrix

| Feature | everything-claude-code | coderef System | Integration Strategy |
|---------|------------------------|----------------|---------------------|
| **Hooks** | Event-triggered automation | Manual workflows | ADOPT: High-impact automation |
| **Rules** | Always-enforced guidelines | Documentation only | ADOPT: Programmatic enforcement |
| **Skills** | Reusable workflow templates | Manual multi-step processes | ADOPT: Codify workflows |
| **Agents** | Specialized task agents | MCP-based tools | KEEP: MCP superior for context |
| **Scanning** | Heuristic/regex (estimated) | AST-based (99% accuracy) | KEEP: Strategic advantage |
| **Planning** | Agent-based | MCP workflow tools | ENHANCE: Add AST scanning |
| **MCP Integration** | Basic | 6 servers, deep integration | KEEP: Already superior |
| **Cross-project** | Not mentioned | Orchestration-first | KEEP: Core differentiator |

---

## References

- **Source Repository:** https://github.com/affaan-m/everything-claude-code
- **Related Stub:** stub-context-reference-tracking
- **Analysis Document:** (This conversation thread)
- **CLAUDE.md:** C:\Users\willh\Desktop\assistant\CLAUDE.md
- **Related Stubs:**
  - session-tracking-improvements (automation)
  - agent-completion-workflow (responsibility clarity)
  - simplify-stub-workflow (automation target)

---

**Next Steps:**
1. Review this document with user
2. Prioritize Phase 1 (Hooks) implementation
3. Create spike/prototype for file watcher + hook executor
4. Test with stub.json validation workflow
5. Document results and iterate
