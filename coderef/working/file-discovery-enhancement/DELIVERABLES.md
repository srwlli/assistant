# DELIVERABLES: file-discovery-enhancement

**Project**: assistant
**Feature**: file-discovery-enhancement
**Workorder**: WO-FILE-DISCOVERY-ENHANCEMENT-001
**Status**: 🚧 Not Started
**Generated**: 2025-12-17

---

## Executive Summary

**Goal**: Enhance the Scriptboard orchestrator backend to automatically discover and register internal workorders, detect stale plans, and sync with workorders.json central tracking

**Description**: TBD

---

## Implementation Phases

### Phase 1: Workorders.json Integration

**Description**: Add ability to read and expose workorders.json via API

**Estimated Duration**: TBD

**Deliverables**:
- /orchestrator/workorders-master endpoint working

### Phase 2: Internal Workorder Detection

**Description**: Detect plans with workorder_id that lack communication.json

**Estimated Duration**: TBD

**Deliverables**:
- /orchestrator/internal-workorders endpoint working

### Phase 3: Stale Detection

**Description**: Add timestamp-based stale detection to plan scanning

**Estimated Duration**: TBD

**Deliverables**:
- /orchestrator/stale endpoint working
- stale_days filter on /plans

### Phase 4: Auto-Registration

**Description**: Enable automatic registration of internal workorders

**Estimated Duration**: TBD

**Deliverables**:
- POST /orchestrator/register-internal working


---

## Metrics

### Code Changes
- **Lines of Code Added**: TBD
- **Lines of Code Deleted**: TBD
- **Net LOC**: TBD
- **Files Modified**: TBD

### Commit Activity
- **Total Commits**: TBD
- **First Commit**: TBD
- **Last Commit**: TBD
- **Contributors**: TBD

### Time Investment
- **Days Elapsed**: TBD
- **Hours Spent (Wall Clock)**: TBD

---

## Task Completion Checklist

- [ ] [SCAN-001] Add /orchestrator/workorders-master endpoint to read workorders.json
- [ ] [SCAN-002] Create get_workorders_master() function to parse workorders.json
- [ ] [SCAN-003] Enhance scan_json_files() to extract workorder_id from plan.json
- [ ] [SCAN-004] Add /orchestrator/internal-workorders endpoint for plans with workorder_id but no communication.json
- [ ] [SCAN-005] Add get_file_age() utility to check modification timestamps
- [ ] [SCAN-006] Add stale_days parameter to /orchestrator/plans endpoint
- [ ] [SCAN-007] Create /orchestrator/stale endpoint to return only stale plans
- [ ] [SCAN-008] Add POST /orchestrator/register-internal endpoint to auto-register discovered workorders
- [ ] [SCAN-009] Add atomic write helper for workorders.json updates
- [ ] [SCAN-010] Update /orchestrator/stats to include stale_count and internal_count

---

## Files Created/Modified

- **backend/orchestrator_cache.py** - Optional caching layer for scan results
- **backend/orchestrator.py** - TBD

---

## Success Criteria

- All new endpoints return valid JSON responses
- Stale detection correctly identifies plans > 7 days old
- Internal workorders can be registered to workorders.json

---

## Notes

*This deliverables report was automatically generated from plan.json.*
*Use `/update-deliverables` to populate metrics from git history after implementation.*

**Last Updated**: 2025-12-17
