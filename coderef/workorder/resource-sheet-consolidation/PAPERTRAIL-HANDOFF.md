# PAPERTRAIL AGENT HANDOFF - WO-RESOURCE-SHEET-CONSOLIDATION-001

**From:** CodeRef Assistant (Orchestrator)
**To:** Papertrail Agent
**Date:** 2026-01-03
**Priority:** High
**Status:** Phase 3A - Template Engine & UDS Validation

---

## Executive Summary

**Your Mission:** Build the template generation engine with UDS (Unified Documentation Standard) enforcement for the resource sheet consolidation system.

**Current Status:** coderef-docs agent completed Phase 2 (MCP routing) and may have started MAP-001 and DETECT-001. **You must review their work first** to ensure it aligns with your unified template schema from the synthesis session.

**Your Domain:** Template generation engine, UDS enforcement, element detection (3-stage algorithm), 4-gate validation pipeline.

---

## What Happened Before You

### Phase 1: Orchestrator (Complete) ✅
- Added deprecation warnings to both .md files (kept for reference)
- Created initial handoff documents
- Updated documentation

### Phase 2: coderef-docs (Complete) ✅
- ROUTE-001: Routed /create-resource-sheet to MCP tool ✅
- ROUTE-002: Added element_type passthrough ✅
- TEST-ROUTE: Tested basic routing ✅

### **IMPORTANT: Work That May Need Review** 🔍
coderef-docs agent reported completing:
- MAP-001: Create element-type-mapping.json ✅
- DETECT-001: Implement 3-stage detection 🔄 (in progress)

**Your First Task:** Review this work to ensure it matches your unified template schema design from papertrail-output.json.

---

## Your Tasks (Phase 3A)

### **REVIEW-001: Review Existing Work** (Priority: CRITICAL)

**What to review:**
1. Check if MAP-001 (element-type-mapping.json) exists
2. Check if DETECT-001 (detection module) was started
3. Compare against your unified_template_schema from papertrail-output.json

**What to validate:**
- ✅ All 20 element types present with correct detection patterns
- ✅ Schema matches unified_template_schema structure
- ✅ 3-stage detection algorithm properly implemented (filename → code → fallback)
- ✅ Confidence scoring present (80-95% target)

**If work exists and is correct:**
- Mark MAP-001 as complete
- Mark DETECT-001 as complete
- Move to PORT-002 and VALID-001

**If work exists but incorrect:**
- Document issues in notes
- Revise to match unified template schema
- Complete properly before moving forward

**If work doesn't exist:**
- Start from scratch with your original design
- Follow unified_template_schema from synthesis

---

### **MAP-001: Create element-type-mapping.json**

**Status:** needs_review (may already exist from coderef-docs)

**Specification:** Your papertrail-output.json section "element_specific_overlays"

**Required Structure:**
```json
{
  "schema_version": "1.0.0",
  "element_types": [
    {
      "rank": 1,
      "element_type": "top_level_widgets",
      "detection_patterns": {
        "filename": ["Page suffix", "Widget suffix"],
        "code_analysis": ["top-level component", "route target"]
      },
      "additional_sections": ["composition_hierarchy", "user_workflows", "layout_contracts", "performance_budget"],
      "checklist_overlay": [
        "Composition hierarchy",
        "User workflows",
        "State orchestration",
        "Integration points",
        "Layout contracts",
        "Lifecycle events",
        "Performance budget",
        "Accessibility root"
      ],
      "conditional_modules": ["composition_hierarchy", "user_workflows", "state_orchestration"],
      "auto_fill_rate": "65%"
    }
    // ... 19 more element types
  ]
}
```

**All 20 Element Types (from rank 1-20):**
1. top_level_widgets
2. stateful_containers
3. global_state_layer
4. custom_hooks
5. api_client
6. data_models
7. persistence_subsystem
8. eventing_messaging
9. routing_navigation
10. file_tree_primitives
11. context_menu_commands
12. drag_drop_system
13. keyboard_shortcuts
14. clipboard_handlers
15. undo_redo_stack
16. design_system_components
17. error_recovery
18. build_scripts
19. test_utilities
20. documentation_generator

**Location:** `coderef-docs/modules/resource-sheet/mapping/element-type-mapping.json`

**Reference:** Lines 126-200 of papertrail-output.json

---

### **DETECT-001: Implement 3-Stage Detection Algorithm**

**Status:** needs_review (may be in progress from coderef-docs)

**Specification:** Your papertrail-output.json design + synthesis recommendations

**3-Stage Detection:**

**Stage 1: Filename Pattern Matching (80-95% confidence)**
- Input: File path (e.g., "components/UserDashboard/UserDashboardPage.tsx")
- Logic: Regex matching against detection_patterns.filename from mapping
- Output: Ranked list of matching element types with confidence scores
- Example: "Page suffix" → top_level_widgets (95% confidence)

**Stage 2: Code Analysis Refinement (+10-20% confidence boost)**
- Input: File AST or code structure
- Logic: Scan for patterns (useState, imports, exports, JSDoc)
- Output: Updated confidence scores
- Example: Detect "route target" in router config → +15% confidence

**Stage 3: Fallback to Manual Review (<80% confidence)**
- Input: Ambiguous cases (e.g., "utils/helpers.ts")
- Logic: Prompt user for element type with suggestions
- Output: User-selected type or default to "utility_modules"

**Performance Target:**
- Stage 1 only: <5ms per file
- Stage 1+2: <50ms per file
- Cache results for session

**Implementation Location:** `coderef-docs/generators/detection_module.py`

**Reference:** papertrail-output.json section "element_type_detection"

---

### **PORT-002: Port Tool 2 Checklists into ModuleRegistry**

**Status:** pending

**Source:** `.claude/commands/resource-sheet-catalog.md` (20 element types with checklists)

**Task:** Convert Tool 2's checklists into conditional modules for the template engine

**Implementation:**
1. **Extract checklists** from lines 63-634 of resource-sheet-catalog.md
2. **Create ModuleRegistry class** that maps element_type → checklist items
3. **Inject as H4 sections** in relevant template sections

**Example Mapping:**
```python
# ModuleRegistry.py
class ModuleRegistry:
    def get_checklist_for_element(self, element_type: str) -> List[str]:
        CHECKLISTS = {
            "top_level_widgets": [
                "Composition hierarchy",
                "User workflows",
                "State orchestration",
                "Integration points",
                "Layout contracts",
                "Lifecycle events",
                "Performance budget",
                "Accessibility root"
            ],
            "custom_hooks": [
                "Side effects",
                "Cleanup guarantees",
                "Dependency array",
                "Return contract",
                "Stale closure bugs",
                "Composition patterns",
                "Testing approach",
                "Performance gotchas"
            ]
            # ... 18 more element types
        }
        return CHECKLISTS.get(element_type, [])
```

**Usage in Template:**
```markdown
#### Checklist
- [ ] Composition hierarchy
- [ ] User workflows
- [ ] State orchestration
- [ ] Integration points
```

**Location:** `coderef-docs/modules/resource-sheet/module_registry.py`

**Reference:** resource-sheet-catalog.md lines 63-634 (20 element types)

---

### **VALID-001: Build 4-Gate Validation Pipeline**

**Status:** pending

**Specification:** Your papertrail-output.json quality gate design

**4-Gate Validation System:**

**Gate 1: Structural Validation (4 checks)**
- ✅ Header metadata present (agent, date, task)
- ✅ Executive summary present (2-4 sentences)
- ✅ Required sections present (13 base sections from Tool 1)
- ✅ State ownership table present (if element is stateful)

**Gate 2: Content Quality (4 checks)**
- ✅ No TODO/FIXME/PLACEHOLDER markers
- ✅ Exhaustiveness (all persistence keys documented, all state documented)
- ✅ Voice compliance (imperative voice, no hedging like "should probably")
- ✅ Tables used for structured data (not prose)

**Gate 3: Element-Specific Validation (3 checks)**
- ✅ Focus areas from element type present
- ✅ Required sections for element type present
- ✅ Element-specific tables populated (e.g., hook signature for custom_hooks)

**Gate 4: Auto-Fill Threshold (1 check)**
- ✅ >= 60% completion rate (measure filled fields vs total fields)

**Scoring System:**
- **Pass:** All critical checks pass (Gates 1, 3, 4 required)
- **Warn:** Major failures (Gate 2 violations)
- **Reject:** Critical failures (<60% auto-fill, missing required sections)

**Implementation:**
```python
# validation_pipeline.py
class ValidationPipeline:
    def validate(self, resource_sheet: str, element_type: str) -> ValidationResult:
        results = {
            "gate_1": self._validate_structure(resource_sheet),
            "gate_2": self._validate_content(resource_sheet),
            "gate_3": self._validate_element_specific(resource_sheet, element_type),
            "gate_4": self._validate_auto_fill_threshold(resource_sheet)
        }
        return self._compute_score(results)

    def _compute_score(self, results: Dict) -> ValidationResult:
        critical_gates = [results["gate_1"], results["gate_3"], results["gate_4"]]
        if all(g.passed for g in critical_gates):
            return ValidationResult(status="pass", score=self._calculate_score(results))
        elif any(g.critical_failure for g in critical_gates):
            return ValidationResult(status="reject", score=0)
        else:
            return ValidationResult(status="warn", score=self._calculate_score(results))
```

**Location:** `coderef-docs/generators/validation_pipeline.py`

**Reference:** papertrail-output.json section "quality_gate_templates"

---

## Your Deliverables

1. **element-type-mapping.json** - 20 element types with detection patterns
2. **detection_module.py** - 3-stage detection algorithm
3. **module_registry.py** - Tool 2 checklists as conditional modules
4. **validation_pipeline.py** - 4-gate quality validation system

**Validation Criteria:**
- All 20 element types present in mapping
- Detection algorithm achieves 80%+ confidence on P1 batch examples
- Checklists match Tool 2 spec (resource-sheet-catalog.md)
- Validation pipeline catches violations in test cases

---

## Reference Materials

**Primary:**
- **papertrail-output.json** - Your unified template schema design (complete spec)
- Location: `C:\Users\willh\.mcp-servers\coderef\sessions\reference-sheet-reconciliation\papertrail-output.json`

**Secondary:**
- **.claude/commands/resource-sheet-catalog.md** - 20 element types with checklists (634 lines)
- **orchestrator-output.md** - Complete synthesis overview

**Test Data:**
- **15 P1 batch examples** - `C:\Users\willh\.mcp-servers\coderef-workflow\coderef\reference-sheets\`

---

## Success Criteria

✅ **REVIEW-001 complete:** Existing work validated or corrected
✅ **MAP-001 complete:** 20 element types mapped with detection patterns
✅ **DETECT-001 complete:** 3-stage detection algorithm working (80%+ confidence)
✅ **PORT-002 complete:** Tool 2 checklists integrated as conditional modules
✅ **VALID-001 complete:** 4-gate validation pipeline passing test cases

**Performance Targets:**
- Detection: <50ms per file
- Validation: <100ms per resource sheet
- Overall: Supports 60-80% auto-fill rate

---

## Communication Protocol

Update `instructions.json` as you progress:

```json
{
  "agents": {
    "papertrail": {
      "tasks": [
        {"id": "MAP-001", "status": "complete"},
        {"id": "DETECT-001", "status": "complete"},
        {"id": "PORT-002", "status": "in_progress"},
        {"id": "VALID-001", "status": "pending"}
      ]
    }
  }
}
```

**Completion:** Set `agents.papertrail.status = "complete"` when all 4 tasks done.

---

## Next Steps

1. **Start with REVIEW-001** - Check if coderef-docs completed MAP-001/DETECT-001
2. **Validate or implement** MAP-001 and DETECT-001 against your unified_template_schema
3. **Implement PORT-002** - Port Tool 2 checklists into ModuleRegistry
4. **Implement VALID-001** - Build 4-gate validation pipeline
5. **Test with P1 batch** - Validate detection and validation on 15 examples
6. **Report completion** - Update instructions.json status

---

**Estimated Time:** 6-8 hours total

**Ready to begin!** Start with reviewing any existing work from coderef-docs, then proceed with your template engine implementation.

**Good luck!** 📋
