# Agent Handoff Template

**Workorder**: {WO-ID}
**Feature**: {feature-name}
**Location**: `{target-project}/coderef/working/{feature-name}/`

---

## Files to Review

1. **context.json** - Requirements, constraints, and technical context
2. **communication.json** - Workflow status and instructions
3. **plan.json** (if exists) - Implementation plan

---

## Your Workflow

### Phase 1: Planning
1. Review context.json thoroughly
2. Run `/create-plan` to generate your implementation plan
3. Update communication.json:
   ```json
   "status": "plan_submitted"
   ```
4. Wait for orchestrator approval before implementing

### Phase 2: Implementation
1. Execute approved plan
2. Update task status in plan.json as you work
3. Update communication.json:
   ```json
   "status": "implementing"
   ```

### Phase 3: Completion ⚠️ **CRITICAL**

**You MUST complete ALL of these steps before marking work complete:**

☐ **1. Update Deliverables**
```bash
/update-deliverables
```
- Captures git metrics (LOC added/removed, commits, time elapsed)
- Populates DELIVERABLES.md with actual implementation metrics
- Validates feature completion

☐ **2. Archive Feature**
```bash
/archive-feature
```
- Moves feature from `coderef/working/` to `coderef/archived/`
- Updates archive index
- Logs workorder completion

☐ **3. Update Communication Status**
Update communication.json:
```json
"status": "complete"
```

### Validation Checklist

Before setting status to "complete", verify:

- [ ] All implementation tasks finished
- [ ] All tests passing
- [ ] DELIVERABLES.md populated with metrics (not "TBD")
- [ ] Feature archived to `coderef/archived/`
- [ ] communication.json updated to "complete"

---

## Important Notes

### What You Do (Agent):
✅ **Everything** - Plan, implement, test, document, archive
✅ Run `/update-deliverables` to capture metrics
✅ Run `/archive-feature` to clean up
✅ Update communication.json status at each phase

### What Orchestrator Does:
✅ **Verify only** - Check that you completed all steps
✅ Update centralized tracking
✅ Close workorder

❌ **Orchestrator NEVER touches files in your project** - You are responsible for complete execution.

---

## Communication Protocol

**Update communication.json after EVERY phase change:**

| Phase | Status Value |
|-------|--------------|
| Received handoff | `pending_plan` |
| Plan submitted | `plan_submitted` |
| Plan approved | `approved` |
| Implementing | `implementing` |
| **Completed ALL steps** | `complete` |
| Orchestrator verified | `verified` |

**The orchestrator tracks your progress by reading communication.json.**

---

## Common Mistakes to Avoid

❌ Marking status as "complete" before running `/update-deliverables`
❌ Leaving DELIVERABLES.md with "TBD" values
❌ Not running `/archive-feature`
❌ Waiting for orchestrator to finish your work

✅ Complete the FULL workflow yourself
✅ Run both `/update-deliverables` and `/archive-feature`
✅ Only then set status to "complete"

---

**Remember: You own the complete lifecycle. The orchestrator only verifies.**
