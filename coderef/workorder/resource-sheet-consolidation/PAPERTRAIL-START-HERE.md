# PAPERTRAIL AGENT - START HERE

**Workorder:** WO-RESOURCE-SHEET-CONSOLIDATION-001
**Your Role:** Build template generation engine with UDS validation
**Status:** Ready to start
**Date:** 2026-01-03

---

## STEP 1: Read Your Instructions

**File:** `C:\Users\willh\Desktop\assistant\coderef\workorder\resource-sheet-consolidation\instructions.json`

Look for the section: `"agents" → "papertrail"`

**Your 4 tasks:**
1. MAP-001: Create element-type-mapping.json
2. DETECT-001: Implement 3-stage detection algorithm
3. PORT-002: Port Tool 2 checklists into ModuleRegistry
4. VALID-001: Build 4-gate validation pipeline

---

## STEP 2: Read Your Detailed Handoff

**File:** `C:\Users\willh\Desktop\assistant\coderef\workorder\resource-sheet-consolidation\PAPERTRAIL-HANDOFF.md`

This has complete specs for all 4 tasks.

---

## STEP 3: Read Your Reference Material

**Your original design from synthesis session:**
`C:\Users\willh\.mcp-servers\coderef\sessions\reference-sheet-reconciliation\papertrail-output.json`

This is YOUR spec - you designed the unified template schema.

---

## STEP 4: IMPORTANT - Review Existing Work First

**Before starting:** Check if coderef-docs agent already completed MAP-001 or DETECT-001.

**How to check:**
1. Look for: `element-type-mapping.json` in coderef-docs MCP server
2. Look for: detection module in coderef-docs generators/

**If found:**
- Review the work against your unified_template_schema
- Validate it matches your design
- Fix if incorrect, approve if correct

**If not found:**
- Start fresh with your original design

---

## STEP 5: Your Work Location

**Where to create files:**
`C:\Users\willh\.mcp-servers\coderef-docs\`

**Your 4 deliverables:**
1. `modules/resource-sheet/mapping/element-type-mapping.json`
2. `generators/detection_module.py`
3. `modules/resource-sheet/module_registry.py`
4. `generators/validation_pipeline.py`

---

## STEP 6: Update Status as You Work

**File:** `C:\Users\willh\Desktop\assistant\coderef\workorder\resource-sheet-consolidation\instructions.json`

**Update the papertrail section:**
```json
{
  "agents": {
    "papertrail": {
      "tasks": [
        {"id": "MAP-001", "status": "complete"},  // Update when done
        {"id": "DETECT-001", "status": "in_progress"},  // Update as you work
        {"id": "PORT-002", "status": "pending"},
        {"id": "VALID-001", "status": "pending"}
      ]
    }
  }
}
```

---

## QUICK SUMMARY

1. ✅ Read instructions.json (your task list)
2. ✅ Read PAPERTRAIL-HANDOFF.md (detailed specs)
3. ✅ Read papertrail-output.json (your original design)
4. 🔍 Check if coderef-docs already did MAP-001/DETECT-001
5. 🛠️ Build your 4 deliverables in coderef-docs server
6. 📝 Update instructions.json status as you work

---

## Questions?

All specs are in PAPERTRAIL-HANDOFF.md. Your original design is in papertrail-output.json.

**Start with REVIEW-001** - check for existing work before building from scratch.

---

**Estimated Time:** 6-8 hours total for all 4 tasks

**Good luck!** 📋
