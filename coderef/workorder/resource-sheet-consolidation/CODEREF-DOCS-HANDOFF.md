# CODEREF-DOCS AGENT HANDOFF - WO-RESOURCE-SHEET-CONSOLIDATION-001

**From:** coderef-assistant (Orchestrator)
**To:** coderef-docs Agent
**Date:** 2026-01-03
**Status:** Phase 1 Complete - Ready for Phase 2-3 Implementation

---

## Executive Summary

**Your Task:** Implement Phases 2-3 of resource sheet consolidation by routing `/create-resource-sheet` to your existing MCP tool and enhancing it with missing features from Tool 1 + Tool 2.

**Context:** A 4-agent synthesis session (WO-REFERENCE-SHEET-RECONCILIATION-001) analyzed two separate resource sheet systems and discovered that **you already have a working MCP tool** (v3.4.0 `generate_resource_sheet` with Phase 1 complete). We just need to route the slash command to it and enhance it.

**Deliverable:** Unified resource sheet system with 60-80% auto-fill, 20 element types, 4-gate validation.

---

## What's Already Done (Phase 1 - Orchestrator)

✅ Added deprecation warnings to both .md files (kept for reference)
✅ Updated documentation references
✅ Created this handoff document

**Files Changed:**
- `.claude/commands/create-resource-sheet.md` - Deprecation notice added
- `.claude/commands/resource-sheet-catalog.md` - Deprecation notice added

---

## Your Work (Phases 2-3)

### Phase 2: Route Slash Command to MCP Tool (1-2 hours)

**ROUTE-001:** Update `/create-resource-sheet` slash command implementation
- **Current:** Loads .md file as text template
- **New:** Call `mcp__coderef-docs__generate_resource_sheet`
- **Location:** Check Claude Code slash command system (likely `.claude/commands/` or command registry)
- **Implementation:** Route command to your MCP tool handler

**ROUTE-002:** Add `element_type` parameter passthrough
- If user specifies element type: pass to MCP tool
- If not specified: let MCP tool auto-detect
- Example: `/create-resource-sheet Button.tsx design-system` → element_type="design-system"

**TEST-ROUTE:** Test basic routing
- Run `/create-resource-sheet` on simple target
- Verify MCP tool is called
- Verify output is generated

---

### Phase 3: Full MCP Tool Enhancement (12-16 hours)

#### A. Element Type Detection (MAP-001, DETECT-001)

**MAP-001:** Create `element-type-mapping.json`
- Map 20 element types from Tool 2 to your conditional modules
- Location: `coderef-docs/modules/resource-sheet/mapping/element-type-mapping.json`
- Schema:
```json
{
  "element_types": [
    {
      "rank": 1,
      "element_type": "top_level_widgets",
      "detection_patterns": ["Page suffix", "Widget suffix"],
      "conditional_modules": ["composition_hierarchy", "user_workflows"],
      "checklist_items": ["Composition hierarchy", "User workflows", "State orchestration"]
    }
    // ... 19 more
  ]
}
```

**DETECT-001:** Implement 3-stage detection algorithm
- **Stage 1:** Filename pattern matching (20 regex patterns, 80-95% confidence)
- **Stage 2:** Code analysis refinement (+10-20% confidence boost)
- **Stage 3:** Fallback to default with manual review prompt
- Reference: `papertrail-output.json` section "element_type_detection"

#### B. Graph Integration (GRAPH-001, GRAPH-002)

**GRAPH-001:** Create `graph-helpers.ts` with 4 query functions
- `getImportsForElement(graph, nodeId)` → Dependencies section (90% auto-fill)
- `getExportsForElement(graph, nodeId)` → Public API section (95% auto-fill)
- `getConsumersForElement(graph, nodeId)` → Usage Examples section (70% auto-fill)
- `getDependenciesForElement(graph, nodeId)` → Required Dependencies section (75% auto-fill)
- Reference: `coderef-system-output.json` section "graph_query_patterns"

**GRAPH-002:** Integrate graph queries into template renderer
- Load graph from `.coderef/exports/graph.json`
- Run 4 queries in parallel (<50ms target)
- Auto-fill template sections with graph data
- Target: 60-80% overall completion rate
- Reference: `coderef-system-output.json` section "integration_with_unified_system"

#### C. Tool 1 + Tool 2 Features (PORT-001, PORT-002)

**PORT-001:** Port Tool 1 writing guidelines to post-processor
- Source: `.claude/commands/create-resource-sheet.md` sections on voice/tone/precision
- Implementation: Post-processing step that applies writing standards to generated output
- Rules:
  - Imperative voice
  - No hedging ("should probably" → "must")
  - Active voice
  - Tables for structured data
  - No ambiguous statements

**PORT-002:** Integrate Tool 2 checklists into ModuleRegistry
- Source: `.claude/commands/resource-sheet-catalog.md` (20 element types with checklists)
- Implementation: Add checklist metadata to each conditional module
- Format: Inject as "#### Checklist" H4 heading with bullet points in relevant sections

#### D. Validation Pipeline (VALID-001)

**VALID-001:** Build 4-gate validation pipeline
- **Gate 1:** Structural Validation (4 checks - header, summary, required sections, state ownership)
- **Gate 2:** Content Quality (4 checks - no placeholders, exhaustiveness, voice compliance, tables)
- **Gate 3:** Element-Specific Validation (3 checks - focus areas, required sections, element tables)
- **Gate 4:** Auto-Fill Threshold (1 check - >= 60% completion)
- Reference: `coderef-docs-output.json` section "quality_gate_templates"
- Scoring: Pass if all critical checks pass, Warn if major failures, Reject if critical failures

#### E. Documentation Hierarchy (DOCS-001)

**DOCS-001:** Create 4-tier documentation hierarchy
1. **RESOURCE-SHEET-USER-GUIDE.md** (coderef/user/) - Primary user guide
2. **MODULE-REFERENCE.md** (coderef/foundation-docs/) - Technical deep dive (15 modules)
3. **ELEMENT-TYPE-CATALOG.md** (coderef/foundation-docs/) - All 20 types catalog
4. **QUICK-REFERENCE-CARD.md** (coderef/user/) - One-page cheat sheet
- Reference: `coderef-docs-output.json` section "user_documentation_structure"

---

## Success Criteria

After your implementation:

✅ **Routing works:** `/create-resource-sheet` calls your MCP tool (100% of invocations)
✅ **Detection works:** All 20 element types detected with 80%+ confidence
✅ **Auto-fill works:** 60-80% average completion rate (test with 15 P1 examples)
✅ **Validation works:** 4-gate pipeline catches critical/major/minor errors
✅ **Performance:** <2 seconds total generation time

---

## Reference Materials

### Agent Synthesis Outputs (Read These First)

**Primary:**
- `C:\Users\willh\.mcp-servers\coderef\sessions\reference-sheet-reconciliation\orchestrator-output.md` - Complete synthesis
- `C:\Users\willh\.mcp-servers\coderef\sessions\reference-sheet-reconciliation\coderef-output.md` - Consolidation design

**Secondary:**
- `papertrail-output.md` - Unified template schema (13 base + 20 overlays)
- `coderef-system-output.md` - Graph integration mappings
- `coderef-docs-output.md` - Documentation standards (that's you!)

### Legacy Files (For Reference)

- `.claude/commands/create-resource-sheet.md` - Tool 1 (240 lines - agent framework)
- `.claude/commands/resource-sheet-catalog.md` - Tool 2 (634 lines - 20 element types)

### P1 Batch Examples (For Testing)

**Location:** `C:\Users\willh\.mcp-servers\coderef-workflow\coderef\reference-sheets\`
**Files:** 15 reference sheets (5 elements × 3 formats each)
- CONSTANTS.md, ERROR-RESPONSES.md, MCP-CLIENT.md, TYPE-DEFS.md, VALIDATION.md
- Use these to validate your enhancements work correctly

---

## Implementation Checklist

### Phase 2: Routing (1-2 hours)
- [ ] ROUTE-001: Route slash command to MCP tool
- [ ] ROUTE-002: Add element_type parameter passthrough
- [ ] TEST-ROUTE: Test basic routing

### Phase 3: Enhancement (12-16 hours)
- [ ] MAP-001: Create element-type-mapping.json
- [ ] DETECT-001: Implement 3-stage detection
- [ ] GRAPH-001: Create graph-helpers.ts
- [ ] GRAPH-002: Integrate graph queries
- [ ] PORT-001: Port Tool 1 guidelines
- [ ] PORT-002: Port Tool 2 checklists
- [ ] VALID-001: Build 4-gate validation
- [ ] DOCS-001: Create 4-tier documentation

### Testing (2-4 hours)
- [ ] TEST-P1: Regenerate 15 P1 examples
- [ ] TEST-FILL: Validate 60-80% auto-fill
- [ ] TEST-DETECT: Validate element detection
- [ ] TEST-VALID: Validate validation pipeline

---

## Communication Protocol

Update `communication.json` as you progress:

```json
{
  "workorder_id": "WO-RESOURCE-SHEET-CONSOLIDATION-001",
  "agent": "coderef-docs",
  "status": "in_progress",
  "phase_completed": null,
  "tasks_completed": [],
  "notes": "Starting Phase 2: Routing implementation"
}
```

**Status Values:**
- `not_started` → `in_progress` → `phase_2_complete` → `phase_3_complete` → `testing` → `complete`

---

## Questions? Blockers?

If you encounter issues:
1. Check the agent synthesis outputs (especially `coderef-output.md`)
2. Review your existing MCP tool Phase 1 implementation
3. Reference the P1 batch examples for expected output format
4. Update `communication.json` with blocker details

---

## Next Steps After Completion

When you finish Phases 2-3:
1. Update `communication.json` status to "complete"
2. Document any deviations from plan
3. List any known issues or future enhancements
4. Signal completion to orchestrator

I'll then run Phase 4 testing and verify deliverables.

---

**Ready to begin!** Start with Phase 2 routing, then move to Phase 3 enhancements.

**Estimated Total Time:** 15-20 hours for complete implementation.

**Good luck!** 🚀
