# WO-CODEREF-CONTEXT-HEALTH-001: CLI Health Check Implementation

**Workorder:** WO-CODEREF-CONTEXT-HEALTH-001
**Feature:** coderef-context-cli-health-check
**Priority:** P1 - Immediate (Week 1)
**Effort:** Low (2 hours)
**Impact:** High - Eliminates single point of failure risk

---

## Context: MCP Ecosystem Deep-Dive Analysis

Your team just completed a comprehensive 3-phase analysis of the entire CodeRef Ecosystem (coderef-context, coderef-workflow, coderef-docs, coderef-personas).

**Key Finding from Phase 2 Analysis:**
> coderef-context CLI is a **CRITICAL single point of failure**. If @coderef/core CLI becomes unavailable, the entire ecosystem fails (0 tools work in 3/4 servers).

**Phase 3 Roadmap Recommendation:**
This workorder is Priority #1 for Week 1 of the stabilization phase.

---

## Full Session Documentation

**Read these documents for complete context:**

1. **`C:\Users\willh\Desktop\assistant\session-mcp-capabilities.json`**
   - Phase 1: All 4 servers' deep-dive analyses (tools, capabilities, limitations, gaps)
   - Phase 2: Cross-server sync findings (overlaps, integration opportunities, critical blockers)
   - Full dependency graph showing coderef-context as single point of failure

2. **`C:\Users\willh\Desktop\assistant\PHASE-3-ROADMAP-SYNTHESIS.md`**
   - Complete 12-week roadmap across 5 implementation phases
   - Strategic priorities (P1/P2/P3)
   - This workorder is Phase 0, Task #1

---

## Your Task

Implement CLI health check at coderef-context server startup.

### What to Do

1. **Add startup health check** when coderef-context MCP server initializes
   - Verify that @coderef/core CLI exists at: `C:/Users/willh/Desktop/projects/coderef-system/packages/cli`
   - Verify the CLI is executable
   - If missing: Log warning and set server to degraded mode
   - If present: Log info message confirming availability

2. **Implement graceful error handling**
   - When CLI is unavailable and tool is called:
     - Return clear error message: "CLI unavailable. Set CODEREF_CLI_PATH environment variable or install @coderef/core"
     - Don't spawn subprocess if CLI doesn't exist
     - Fail fast with actionable error

3. **Enable graceful degradation mode** (future Phase 0 task)
   - Set server-level flag: `cli_available = True/False`
   - Log this flag on startup
   - Future task: return cached results from previous session if CLI unavailable

### Success Criteria

- ✅ Server startup checks CLI existence
- ✅ Warning logged if CLI missing
- ✅ Clear error message returned to users (not generic CLI error)
- ✅ No subprocess spawned if CLI unavailable
- ✅ Can activate graceful degradation mode later without code changes

---

## Files & References

**Stub:** `coderef/working/coderef-context-cli-health-check/stub.json`

**Communication:** `communication.json` (below)

**Related P1 Tasks (same phase):**
- Session memoization for coderef-context
- coderef-docs ↔ coderef-context integration
- Real-time coordination dashboard
- Auto-changelog from commits

---

## Related Stubs in Same Phase

Once this completes, priority shifts to:
1. `coderef-context-session-memoization` - Cache scan/query results to avoid redundant CLI calls
2. `coderef-docs-coderef-context-integration` - Call coderef-context from doc generation
3. `coderef-docs-auto-changelog` - Parse conventional commits for auto-changelog

---

## Implementation Notes

**Location in coderef-context:**
- Server initialization code (likely in `server.py` or equivalent startup hook)
- Add before any tool registration
- Should complete in <100ms (just filesystem check)

**Testing:**
- Test with CLI present (should pass)
- Test with CLI renamed/deleted (should log warning)
- Test tool call with CLI unavailable (should return clear error)

**Degradation Strategy (Phase 0, Task 2):**
- Capture this flag as `cli_available` variable
- In Phase 0 Task 2 (graceful degradation), use this flag to decide:
  - If True: Execute normal subprocess call
  - If False: Return cached result or degraded response

---

## Communication

**Status:** Pending agent assignment

After you start work:
1. Update this workorder's `communication.json` with your progress
2. Update status as you move through phases (planning → implementing → testing)
3. Track blockers and dependencies in communication log

---

## Quick Reference: Full Synthesis

**System Health Score:** 2/10 (fault tolerance) → Target: 7/10

**Critical Blocker Count:** 5
- This workorder addresses #1 (CLI availability)

**Total Phase 0 Effort:** 8 hours across 4 tasks
- This task: 2 hours
- Session memoization: 2 hours
- Graceful degradation: 2 hours
- coderef-docs integration: 2 hours (done in parallel with docs team)

**Why P1:** Stabilization must complete before real-time coordination can be tested. You're unblocking the entire roadmap.

---

## Recommended Next Steps (After Completion)

1. Mark as complete in `communication.json`
2. Create stub for `coderef-context-session-memoization`
3. Begin Phase 0 Task 2 (graceful degradation) or coordinate with docs team on integration

---

## Reference Documents Location

- Full ecosystem analysis: `C:\Users\willh\Desktop\assistant\session-mcp-capabilities.json`
- 12-week roadmap: `C:\Users\willh\Desktop\assistant\PHASE-3-ROADMAP-SYNTHESIS.md`
- This workorder stub: `C:\Users\willh\Desktop\assistant\coderef\working\coderef-context-cli-health-check\stub.json`
- This handoff: `C:\Users\willh\Desktop\assistant\coderef\working\coderef-context-cli-health-check\HANDOFF-WO-CONTEXT-HEALTH-001.md`
