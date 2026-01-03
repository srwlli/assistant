# How to Run Tests - Testing Agent Instructions

**Workorder:** WO-RESOURCE-SHEET-CONSOLIDATION-001-TESTING
**Status:** Ready to Execute
**Estimated Time:** 2-4 hours

---

## Quick Start (3 Steps)

### Step 1: Run the Test Runner
```bash
cd C:\Users\willh\Desktop\assistant\coderef\workorder\resource-sheet-consolidation\testing
python test-runner.py
```

This will:
- Generate test execution guide
- Create result templates
- Show you what to test and how

### Step 2: Execute Individual Tests

The test runner will tell you to run these:

```bash
# Test 2: Element Type Detection (45 min)
python test_detection.py

# Test 3: Graph Auto-Fill (30 min)
python test_autofill.py

# Test 4: Validation Pipeline (30 min)
python test_validation.py

# Test 5: Performance Benchmarks (20 min)
python test_performance.py
```

**Note:** Test 1 (Routing) requires manual verification in Claude Code - see test-runner.py output for instructions.

### Step 3: Review Results & Report

After all tests complete:
1. Check `TESTING-SUMMARY.md` for GO/NO-GO decision
2. Verify all 5 critical requirements passed
3. Update parent `instructions.json` with results
4. Notify orchestrator

---

## What Gets Tested

| Test | What | Critical Requirement | Pass Criteria |
|------|------|---------------------|---------------|
| TEST-ROUTING | MCP tool invocation | CR-1 | 100% routing to MCP |
| TEST-DETECTION | 20 element types | CR-2 | ≥80% confidence |
| TEST-AUTOFILL | Graph auto-fill | CR-3 | 60-80% completion |
| TEST-VALIDATION | 4-gate pipeline | CR-4 | 100% error detection |
| TEST-PERFORMANCE | End-to-end timing | CR-5 | <2s total time |

---

## What Gets Built (Implementation Already Complete)

You're testing these deliverables from Phase 3:

### Phase 3A: papertrail
- `detection_module.py` - 3-stage detection algorithm
- `module_registry.py` - Tool 2 checklists (8 methods)
- `validation_pipeline.py` - 4-gate validation
- `element-type-mapping.json` - 20 element types

### Phase 3B: coderef-system
- `graph-helpers.ts` - 4 query functions
- Auto-fill rates: imports 90%, exports 95%, consumers 70%, dependencies 75%

### Phase 3C: coderef-docs
- `writing_standards.py` - Tool 1 quality controls
- 4-tier documentation (2,407 lines)

---

## Results You'll Generate

After running all tests, you'll have:

```
testing/
├── test-results.json           # Overall results
├── detection-results.json      # 20 element type results
├── autofill-results.json       # 5 test elements with percentages
├── validation-results.json     # 5 resource sheets with scores
├── performance-results.json    # 10 timing runs
└── TESTING-SUMMARY.md          # Final GO/NO-GO decision
```

---

## GO/NO-GO Decision

**GO (All Pass):** All 5 critical requirements meet thresholds → Deploy to production
**NO-GO (Any Fail):** 1+ critical requirement fails → Execute rollback plan
**CONDITIONAL GO:** Minor issues only → Deploy with known issues documented

---

## Questions?

- **Test specs:** See `instructions.json` in this folder
- **What was built:** See `PHASE-3A-COMPLETION-CERTIFICATE.md` in parent folder
- **Overall status:** See `STATUS-UPDATE.md` in parent folder

---

**Ready to test? Run:** `python test-runner.py`
