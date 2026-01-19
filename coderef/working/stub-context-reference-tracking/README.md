# stub-context-reference-tracking

**Status:** Planning
**Created:** 2026-01-19
**Tag:** UPDATE
**Reference:** https://github.com/affaan-m/everything-claude-code

---

## Overview

Enhancement to the coderef stub/workorder system based on analysis of the everything-claude-code repository. Adds three high-impact systems: **Hooks** (event automation), **Rules** (enforcement), and **Skills** (workflow templates).

**Key Finding:** everything-claude-code provides excellent automation patterns, while coderef has superior AST-based code analysis (99% accuracy). Integration strategy focuses on adopting their automation/enforcement patterns while preserving our advanced scanning capabilities.

---

## Documents in This Stub

### 1. **INTEGRATION-REFERENCE.md** (Primary Document)
Comprehensive integration guide covering:
- Hooks System - Event-triggered automation
- Rules System - Always-enforced guidelines
- Skills Library - Reusable workflow templates
- Enhanced Planning - AST scanning integration
- Implementation roadmap (4 phases, 8 weeks)

**Key Sections:**
- Architecture diagrams for each system
- Integration points with existing coderef MCP servers
- Implementation checklists
- Code examples
- Validation & testing strategies

### 2. **hooks-implementation-example.js**
Production-ready reference implementation showing:
- File watcher system (chokidar)
- Condition evaluator
- Action executor (MCP tools, shell commands, custom actions)
- Hook matcher (glob patterns)
- Complete hooks engine with debouncing, logging

**Usage:**
```bash
node hooks-implementation-example.js
```

### 3. **hooks.yaml.example**
Sample configuration file with 20+ hooks covering:
- Stub validation (auto-validate on creation)
- Handoff automation (auto-generate prompts)
- Completion verification (auto-verify workorders)
- Dashboard updates (real-time sync)
- Quality checks (frontmatter validation, naming conventions)

**To Use:**
1. Copy to `.claude/hooks.yaml`
2. Customize triggers and actions
3. Start hooks engine

### 4. **stub.json**
Enhanced stub schema demonstrating proposed additions:
- `context` field with reference URLs, related workorders, implementation phases
- `tags` array for classification (UPDATE, NEW, ENHANCEMENT, BUGFIX)
- `documentation` array linking to reference docs

---

## Quick Start

### 1. Review Integration Reference
```bash
# Read comprehensive guide
C:\Users\willh\Desktop\assistant\coderef\working\stub-context-reference-tracking\INTEGRATION-REFERENCE.md
```

### 2. Test Hooks System
```bash
# Install dependencies
npm install chokidar js-yaml

# Run hooks engine example
node hooks-implementation-example.js

# In another terminal, test by creating a stub
mkdir coderef/working/test-feature
echo '{"feature_name": "test"}' > coderef/working/test-feature/stub.json

# Check hooks engine output for auto-validation
```

### 3. Configure Your Hooks
```bash
# Copy example config
cp hooks.yaml.example .claude/hooks.yaml

# Edit to match your workflow
# Start with these 3 critical hooks:
#   - auto-validate-stub
#   - auto-generate-handoff
#   - auto-verify-completion
```

---

## Implementation Roadmap

### Phase 1: Hooks System (Weeks 1-2)
**Priority:** HIGH
**Impact:** Eliminates manual orchestration tasks

**Deliverables:**
- [ ] hooks.yaml configuration
- [ ] File watcher system
- [ ] Hook executor
- [ ] 3 critical hooks (validate, handoff, verify)

**Success Criteria:**
- Stubs auto-validate on creation
- Handoff prompts auto-generate
- Workorders auto-verify on completion

### Phase 2: Rules Enforcement (Weeks 3-4)
**Priority:** MEDIUM-HIGH
**Impact:** Prevents protocol violations

**Deliverables:**
- [ ] rules.yaml configuration
- [ ] Rule validator interceptor
- [ ] 4 critical rules (read-only, tracking, communication, deliverables)

**Success Criteria:**
- Orchestrator blocked from writing to targets
- Commits without WO-XXX trigger warnings
- Archive blocked without deliverables

### Phase 3: Skills Library (Weeks 5-6)
**Priority:** MEDIUM
**Impact:** Reusable workflow templates

**Deliverables:**
- [ ] .claude/skills/ directory
- [ ] Skill executor
- [ ] 3 critical skills (promote, verify, status-report)

**Success Criteria:**
- STUB→WO fully automated
- Verification automated
- Status reports generated on demand

### Phase 4: Enhanced Planning (Weeks 7-8)
**Priority:** LOW-MEDIUM
**Impact:** Better planning with risk awareness

**Deliverables:**
- [ ] gather_context with coderef_complexity
- [ ] plan.json with risk_assessment
- [ ] Handoff prompts with risk summary

**Success Criteria:**
- Plans include complexity scores
- Plans identify anti-patterns
- Plans surface test gaps

---

## Key Insights from everything-claude-code

### What to Adopt
1. **Hooks** - Event automation eliminates manual tasks
2. **Rules** - Programmatic enforcement prevents mistakes
3. **Skills** - Codified workflows ensure consistency

### What to Keep (Ours is Better)
1. **AST-based scanning** - 99% accuracy vs heuristics
2. **MCP architecture** - 6 integrated servers vs basic setup
3. **Cross-project orchestration** - Unique differentiator

### Strategic Advantage
Our coderef-context MCP server provides:
- Relationship graphs (calls, imports, dependencies)
- Impact analysis (what breaks if X changes)
- Complexity metrics (cyclomatic, cognitive)
- Pattern detection (anti-patterns, test gaps)

**Next step:** Surface these insights earlier in planning phase via Enhanced Planning (Phase 4)

---

## Files & Relationships

### Created Files
```
stub-context-reference-tracking/
├── README.md (this file)
├── stub.json (enhanced schema example)
├── INTEGRATION-REFERENCE.md (primary guide)
├── hooks-implementation-example.js (reference code)
└── hooks.yaml.example (configuration template)
```

### Related Stubs
- `session-tracking-improvements` - Real-time sync automation (hooks candidate)
- `agent-completion-workflow` - Responsibility clarity (rules candidate)
- `simplify-stub-workflow` - Workflow automation (skills candidate)

### Related Workorders
- None yet (this is stub phase)

---

## Next Actions

1. **User Review** - Review INTEGRATION-REFERENCE.md for feedback
2. **Prioritize** - Confirm Phase 1 (Hooks) as starting point
3. **Spike** - Build minimal hooks prototype with 1 hook (auto-validate-stub)
4. **Test** - Validate with real stub creation workflow
5. **Iterate** - Refine based on results, add more hooks

---

## Questions to Consider

1. **Hooks Engine Location** - Run as background process or integrated into Claude Code CLI?
2. **MCP vs Shell** - Prefer MCP tools or shell commands for actions?
3. **Error Handling** - Block on hook failure or continue with warnings?
4. **Logging** - Centralized log file or per-hook logs?
5. **Configuration** - Single hooks.yaml or separate configs per project?

---

## References

- **Source:** https://github.com/affaan-m/everything-claude-code
- **Analysis:** (Conversation thread with detailed comparison)
- **Primary Doc:** INTEGRATION-REFERENCE.md
- **Implementation:** hooks-implementation-example.js
- **Config:** hooks.yaml.example

---

**Maintained by:** CodeRef Assistant (Orchestrator Persona)
