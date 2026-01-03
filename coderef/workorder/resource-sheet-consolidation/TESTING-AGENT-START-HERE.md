# TESTING AGENT - START HERE (Phase 4)

**Workorder:** WO-RESOURCE-SHEET-CONSOLIDATION-001
**Your Role:** Execute approved test plan and validate implementation
**Status:** ✅ Ready to execute (all Phase 3 work complete)
**Date:** 2026-01-03

---

## STEP 1: Read Your Test Plan

**File:** `C:\Users\willh\.mcp-servers\coderef\sessions\resource-sheet-consolidation-testing\test-plan.json`

**What you'll find:**
- 49 test cases across 7 categories
- 5 critical requirements with pass/fail criteria
- Rollback plan for critical failures

---

## STEP 2: Read Your Test Cases

**File:** `C:\Users\willh\.mcp-servers\coderef\sessions\resource-sheet-consolidation-testing\test-cases.json`

**What you'll find:**
- Detailed test case definitions
- Step-by-step execution instructions
- Expected results and evidence requirements

---

## STEP 3: Read Your Execution Guide

**File:** `C:\Users\willh\.mcp-servers\coderef\sessions\resource-sheet-consolidation-testing\testing-handoff.md`

**What you'll find:**
- Bash/Python code snippets for automation
- Performance measurement methodology
- Evidence collection procedures
- Results aggregation scripts

---

## STEP 4: Review What Was Built (Phase 3 Deliverables)

### Papertrail Deliverables (Phase 3A)
- `C:\Users\willh\.mcp-servers\coderef-docs\generators\detection_module.py` - 3-stage detection algorithm
- `C:\Users\willh\.mcp-servers\coderef-docs\resource_sheet\module_registry.py` - Tool 2 checklists (8 methods)
- `C:\Users\willh\.mcp-servers\coderef-docs\generators\validation_pipeline.py` - 4-gate validation
- `C:\Users\willh\.mcp-servers\coderef-docs\resource_sheet\mapping\element-type-mapping.json` - 20 element types

### coderef-system Deliverables (Phase 3B)
- `graph-helpers.ts` - 4 query functions (getImportsForElement, getExportsForElement, getConsumersForElement, getDependenciesForElement)
- Auto-fill rates: imports 90%, exports 95%, consumers 70%, dependencies 75%

### coderef-docs Deliverables (Phase 3C)
- `writing_standards.py` - Tool 1 quality controls (315 lines)
- 4-tier documentation hierarchy (2,407 lines total)

**Summary:** See `PHASE-3A-COMPLETION-CERTIFICATE.md` for papertrail deliverables breakdown

---

## STEP 5: Your Test Execution Strategy

### Category 1: Routing Validation (3 tests, 15 min)
**Critical Requirement:** CR-1 (100% MCP tool invocation)
- Test slash command routing
- Verify element_type parameter passthrough
- Validate backward compatibility

### Category 2: Element Type Detection (24 tests, 45 min)
**Critical Requirement:** CR-2 (80%+ confidence for 20 types)
- Test all 20 element types
- Validate 3-stage detection algorithm
- Measure confidence scores

### Category 3: Graph Integration Auto-Fill (5 tests, 30 min)
**Critical Requirement:** CR-3 (60-80% average completion rate)
- Test 4 query functions
- Measure auto-fill percentage
- Validate graph data accuracy

### Category 4: Validation Pipeline (5 tests, 30 min)
**Critical Requirement:** CR-4 (100% error detection)
- Test all 4 gates
- Validate scoring system (0-100)
- Test edge cases

### Category 5: Performance Benchmarks (4 tests, 20 min)
**Critical Requirement:** CR-5 (<2s total generation time)
- Measure end-to-end timing
- Time breakdown by stage
- 95th percentile analysis

### Category 6: Output Format Validation (4 tests, 30 min)
- Test markdown output
- Test JSON output
- Test JSDoc output
- P1 batch regression (10 files)

### Category 7: Edge Cases & Error Handling (4 tests, 20 min)
- Test graceful degradation
- Test missing dependencies
- Test invalid inputs
- Test error recovery

**Total Estimated Time:** 2-4 hours

---

## STEP 6: Critical Requirements (Your GO/NO-GO Decision Framework)

| Requirement | Target | Test Categories | Failure = Rollback |
|-------------|--------|-----------------|-------------------|
| CR-1: Routing Works | 100% | Category 1 | YES - Critical |
| CR-2: Element Detection | 80%+ confidence | Category 2 | YES - Critical |
| CR-3: Auto-Fill | 60-80% average | Category 3 | YES - Critical |
| CR-4: Validation Pipeline | 100% error detection | Category 4 | YES - Critical |
| CR-5: Performance | <2s total | Category 5 | YES - Critical |

**GO Decision:** All 5 critical requirements PASS
**NO-GO Decision:** Any 1 critical requirement FAIL → Rollback plan in test-plan.json

---

## STEP 7: Evidence Collection

**For each test, collect:**
- Logs from MCP tool invocation
- Timing data (Python timeit, 10 iterations)
- Output diffs vs expected results
- Performance metrics (average, p95, max)

**Save evidence to:**
`C:\Users\willh\.mcp-servers\coderef\sessions\resource-sheet-consolidation-testing\evidence\`

---

## STEP 8: Results Reporting

**Generate 4 reports:**
1. `test-results.json` - All test case outcomes (pass/fail)
2. `test-report.md` - Summary for orchestrator
3. `performance-report.md` - Timing breakdown
4. `regression-report.md` - P1 batch comparison

**Save to:**
`C:\Users\willh\.mcp-servers\coderef\sessions\resource-sheet-consolidation-testing\results\`

---

## STEP 9: Update Status

**File:** `C:\Users\willh\.mcp-servers\coderef\sessions\resource-sheet-consolidation-testing\instructions.json`

**Update as you work:**
```json
{
  "agents": {
    "testing_agent": {
      "status": "executing",  // Change from "plan_approved_standing_by"
      "tasks": [
        {"id": "TEST-P1", "status": "in_progress"},  // Update as you go
        {"id": "TEST-FILL", "status": "pending"},
        {"id": "TEST-DETECT", "status": "pending"},
        {"id": "TEST-VALID", "status": "pending"}
      ]
    }
  }
}
```

---

## STEP 10: Signal Completion to Orchestrator

**When all tests complete:**

1. Update instructions.json → status: "complete"
2. Create `TESTING-COMPLETION-SUMMARY.md` with:
   - GO/NO-GO decision
   - Critical requirements results
   - Test pass/fail counts
   - Performance metrics
   - Rollback recommendation (if needed)

3. Notify orchestrator via main instructions.json:
   `C:\Users\willh\Desktop\assistant\coderef\workorder\resource-sheet-consolidation\instructions.json`

---

## Quick Checklist

- [ ] Read test-plan.json (comprehensive strategy)
- [ ] Read test-cases.json (49 detailed test cases)
- [ ] Read testing-handoff.md (execution scripts)
- [ ] Review Phase 3 deliverables (what to test)
- [ ] Execute Category 1 tests (routing)
- [ ] Execute Category 2 tests (detection)
- [ ] Execute Category 3 tests (auto-fill)
- [ ] Execute Category 4 tests (validation)
- [ ] Execute Category 5 tests (performance)
- [ ] Execute Category 6 tests (output formats)
- [ ] Execute Category 7 tests (edge cases)
- [ ] Collect evidence for all tests
- [ ] Generate 4 reports (results, summary, performance, regression)
- [ ] Make GO/NO-GO decision
- [ ] Update instructions.json
- [ ] Create TESTING-COMPLETION-SUMMARY.md
- [ ] Signal orchestrator

---

## Questions?

All test specifications are in:
- `test-plan.json` - Strategy and critical requirements
- `test-cases.json` - Detailed test definitions
- `testing-handoff.md` - Execution guide with code snippets

**Phase 3 deliverables to test:**
- See `PHASE-3A-COMPLETION-CERTIFICATE.md` for papertrail outputs
- See `STATUS-UPDATE.md` for overall progress

---

**Estimated Time:** 2-4 hours for all 49 test cases
**Critical:** All 5 requirements must PASS for GO decision

**Good luck!** 🧪
