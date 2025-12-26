# HANDOFF: WO-FILE-DISCOVERY-ENHANCEMENT-001

**Feature:** file-discovery-enhancement
**Target Project:** Scriptboard
**Workorder Type:** Delegated (Implementation Ready)
**Status:** Approved - Begin Phase 1 Implementation

---

## Overview

Enhance the Scriptboard orchestrator backend (`backend/orchestrator.py`) to provide full visibility into workorders across all projects by adding:

- Central `workorders.json` integration
- Internal workorder detection (plans without `communication.json`)
- Stale plan detection (>7 days without updates)
- Auto-registration of discovered workorders

---

## Your Task

**Location:** `C:\Users\willh\Desktop\clipboard_compannion\next\coderef\working\file-discovery-enhancement\`

### Files You Have

1. **plan.json** - Complete 4-phase, 10-task implementation plan
2. **communication.json** - Workflow tracking (update after each phase)

### External References

- **workorders.json:** `C:\Users\willh\Desktop\assistant\workorders.json` (read this for structure)
- **Target file:** `backend/orchestrator.py` (add new endpoints here)

---

## Implementation Plan (4 Phases, 10 Tasks)

### Phase 1: Workorders.json Integration
**Tasks:** SCAN-001, SCAN-002

- [ ] SCAN-001: Add `GET /orchestrator/workorders-master` endpoint
- [ ] SCAN-002: Create `get_workorders_master()` function to parse workorders.json

**Deliverable:** `/orchestrator/workorders-master` endpoint returns central workorders.json content

---

### Phase 2: Internal Workorder Detection
**Tasks:** SCAN-003, SCAN-004

- [ ] SCAN-003: Enhance `scan_json_files()` to extract `workorder_id` from plan.json
- [ ] SCAN-004: Add `GET /orchestrator/internal-workorders` endpoint

**Deliverable:** `/orchestrator/internal-workorders` endpoint detects plans with workorder_id but no communication.json

---

### Phase 3: Stale Detection
**Tasks:** SCAN-005, SCAN-006, SCAN-007, SCAN-010

- [ ] SCAN-005: Add `get_file_age()` utility to check modification timestamps
- [ ] SCAN-006: Add `stale_days` parameter to `/orchestrator/plans` endpoint
- [ ] SCAN-007: Create `GET /orchestrator/stale` endpoint
- [ ] SCAN-010: Update `/orchestrator/stats` to include `stale_count` and `internal_count`

**Deliverables:**
- `/orchestrator/stale?days=7` endpoint (default 7 days)
- Enhanced `/stats` with stale counts
- Stale filtering on `/plans` endpoint

---

### Phase 4: Auto-Registration
**Tasks:** SCAN-008, SCAN-009

- [ ] SCAN-008: Add `POST /orchestrator/register-internal` endpoint
- [ ] SCAN-009: Add `atomic_write_json()` helper for safe workorders.json updates

**Deliverable:** `POST /orchestrator/register-internal` safely registers discovered internal workorders to workorders.json

---

## Success Criteria

### Functional
- All 5 new endpoints return valid JSON responses
- Stale detection correctly identifies plans > 7 days old
- Internal workorders can be registered to workorders.json

### Quality
- No performance regression on existing endpoints
- Graceful handling of missing/malformed files

---

## Workflow Instructions

1. **Review plan.json** for detailed task descriptions
2. **Implement Phase 1** (SCAN-001, SCAN-002)
3. **Update communication.json:**
   ```json
   {
     "phases": [
       {
         "phase": 1,
         "status": "implementing"  // or "complete"
       }
     ],
     "communication_log": [
       {
         "timestamp": "2025-12-19T...",
         "author": "Scriptboard Agent",
         "message": "Phase 1 complete - /workorders-master endpoint working"
       }
     ]
   }
   ```
4. **Repeat for Phase 2, 3, 4**
5. **Final update:** Set workorder status to "complete" in communication.json

---

## Key Implementation Notes

### Existing Code Patterns (orchestrator.py)

- **File scanning:** `scan_json_files()` uses `os.walk()` pattern (lines 40-61)
- **Endpoint pattern:** FastAPI routes with try/except error handling
- **Stats aggregation:** See `/stats` endpoint (lines 124-157)

### New Endpoints Summary

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/orchestrator/workorders-master` | GET | Return workorders.json content |
| `/orchestrator/internal-workorders` | GET | Plans with workorder_id, no communication.json |
| `/orchestrator/stale?days=7` | GET | Plans older than N days |
| `/orchestrator/register-internal` | POST | Register internal WO to workorders.json |
| `/orchestrator/stats` | GET | Enhanced with stale_count, internal_count |

### Risk Mitigation

- **Performance:** Add caching for scan results (optional: `orchestrator_cache.py`)
- **Race conditions:** Use `atomic_write_json()` helper for workorders.json updates

---

## Testing Strategy

### Manual Tests
1. GET `/orchestrator/workorders-master` - verify returns workorders.json
2. GET `/orchestrator/stale?days=7` - verify identifies old plans
3. GET `/orchestrator/internal-workorders` - verify finds plans without communication.json
4. POST `/orchestrator/register-internal` with payload - verify adds to workorders.json
5. GET `/orchestrator/stats` - verify shows stale_count and internal_count

---

## Communication

**Update communication.json after EVERY phase completion.**

When all 4 phases are complete:
1. Set workorder.status = "complete" in communication.json
2. Add final entry to communication_log with summary
3. Report back to orchestrator

---

## Questions?

Refer to:
- **plan.json** - Detailed task breakdown
- **workorders.json** - Structure and existing entries
- **orchestrator.py** - Existing patterns and endpoints

---

**Ready to implement. Begin Phase 1.**
