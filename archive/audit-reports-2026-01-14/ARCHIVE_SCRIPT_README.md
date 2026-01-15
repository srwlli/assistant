# Archive Stubs Script

## Overview

The `archive-stubs.py` script identifies and moves approximately 35 outdated or low-priority stubs from the active working directory to the archive directory. It uses a conservative approach with multiple criteria to identify clear candidates for archival.

## Features

- **Automated Analysis:** Scans all stubs in `coderef/working/` and identifies candidates
- **Conservative Criteria:** 7 identification criteria with safeguards to preserve active work
- **Batch Processing:** Archives all candidates in a single execution
- **Detailed Reporting:** Generates comprehensive report with categorization
- **Error Handling:** Gracefully handles missing/malformed stub files
- **Progress Tracking:** Console output showing status of each archived stub

## Location

**Script:** `C:\Users\willh\Desktop\assistant\archive-stubs.py`

## Usage

### Run Archival (Production)
```bash
cd "C:\Users\willh\Desktop\assistant"
python archive-stubs.py
```

### Output

The script generates:
1. **Console Output:**
   - Total stubs analyzed
   - Archival candidates identified
   - Progress of each archive operation
   - Summary statistics

2. **Files Generated:**
   - `coderef/ARCHIVAL_REPORT.txt` - Detailed report grouped by archival category

3. **Directories Modified:**
   - `coderef/working/` - Reduced from 98 to 62 stubs
   - `coderef/archived/` - Now contains 36+ archived stubs

## Archival Criteria

### 1. TEST/EXAMPLE (7 stubs)
**Threshold:** Names contain "test", "example", "stub-location"

**Purpose:** Validation scaffolding for workflow testing

**Examples:**
- `stub-location-test` - Workflow validation
- `test-and-fix-emojis` - Testing infrastructure
- `scriptboard-endpoints-test` - Endpoint validation

**Rationale:** These are temporary validation stubs, not production features

### 2. COMPLETED (1 stub)
**Threshold:** Status = "completed", "done", or "archived"

**Purpose:** Work that's finished

**Examples:**
- `coderef-timestamp-utility` - Completed utility work

**Rationale:** Finished work clutters active backlog

### 3. OBSOLETE_NAME (1 stub)
**Threshold:** Names contain "deprecated", "remove-", "delete-", "legacy-", "unused-", "stale-"

**Purpose:** Ideas no longer relevant

**Examples:**
- `remove-utility-personas` - Explicitly marked as removal

**Rationale:** Naming convention indicates work has been superseded

### 4. DUPLICATE (5 stubs)
**Threshold:** Similar features in same functional area (lower priority version)

**Purpose:** Consolidation - keep best version, archive redundant

**Examples:**
- `scanner-output-validation`, `scanner-python-detection`, `scanner-script-path-config` - Three similar scanner improvements, keep comprehensive one
- `consolidate-foundation-docs-workflow` - Duplicate of docs consolidation work

**Rationale:** Prevents scattered efforts in same area

### 5. INFRA_UTILITY_LOW (7 stubs)
**Threshold:**
- Category = "infrastructure", "utility", "refactor", "cleanup"
- Priority = "low" or "medium"
- Status = "planning"
- Created before 2026-01-06 (older than 1 week)

**Purpose:** Old infrastructure tasks with low current priority

**Examples:**
- `reorganize-gits-projects` - Old refactoring task
- `mcp-server-cleanup` - Maintenance utility
- `consolidate-project-directories` - Old restructuring idea

**Rationale:** These can be revisited if priorities change; keeping only wastes focus

### 6. LOW_PRIORITY_OLD (15 stubs)
**Threshold:**
- Priority = "low" or "medium"
- Created before 2025-12-20

**Purpose:** Old backlog items with low urgency

**Examples:**
- `ai-video-gen` - Exploratory feature from Dec 15
- `git-libraries` - Research idea from Dec 15
- `saas-ideas` - Brainstorm from Dec 15

**Rationale:** 3+ weeks old with low priority - not core focus

## Safety Features

### What's Preserved
- **CRITICAL Priority:** All CRITICAL stubs kept active
- **HIGH Priority:** All HIGH priority stubs kept active
- **Recent Stubs:** Stubs created in last 1 week kept active regardless of priority
- **Active Workorders:** All coordination stubs for orchestrator kept active
- **Project-Specific:** High-value work for target projects (Scrapper, Gridiron, etc.)

### Reversibility
- All archived stubs remain in `coderef/archived/`
- Git history preserved
- No data loss
- Can recover any stub by moving back to `working/`

## Categories Breakdown

| Category | Count | Action | Why |
|----------|-------|--------|-----|
| TEST/EXAMPLE | 7 | Archive | Temporary validation scaffolding |
| COMPLETED | 1 | Archive | Work is done |
| OBSOLETE_NAME | 1 | Archive | Explicitly marked deprecated |
| DUPLICATE | 5 | Archive | Keep best version only |
| INFRA_UTILITY_LOW | 7 | Archive | Old infrastructure tasks |
| LOW_PRIORITY_OLD | 15 | Archive | 3+ weeks old, low priority |
| **TOTAL** | **36** | **Archive** | ~37% of stub inventory |

## Impact Analysis

### Before Archival
- 98 total stubs in active backlog
- Mix of high/medium/low priorities
- Test scaffolding mixed with features
- Difficult to prioritize

### After Archival
- 62 focused, active stubs
- Clear priority distribution
- Clean backlog for decision-making
- Reduced context switching

## Example Output

```
================================================================================
ARCHIVE STUBS - Conservative Identification & Archival
================================================================================
Working directory: C:\Users\willh\Desktop\assistant\coderef\working
Archive directory: C:\Users\willh\Desktop\assistant\coderef\archived

Loaded 98 stubs
Analyzing 98 stubs...

Identified 36 archival candidates (conservative)

ARCHIVAL CANDIDATES:
--------------------------------------------------------------------------------
STUB-087     | LOW_PRIORITY_OLD     | ai-video-gen
STUB-089     | LOW_PRIORITY_OLD     | assistant-to-other-projects
...
[36 rows total]
--------------------------------------------------------------------------------

Archiving 36 stubs:
[OK]            | STUB-087     | LOW_PRIORITY_OLD     | ai-video-gen
[OK]            | STUB-089     | LOW_PRIORITY_OLD     | assistant-to-other-projects
...

Archival Summary:
  Successfully archived: 36/36
  Failed: 0/36

Report saved to: C:\Users\willh\Desktop\assistant\coderef\ARCHIVAL_REPORT.txt
```

## Script Architecture

### Main Class: ArchiveAnalysis
- **load_stubs()** - Load all stub.json files
- **analyze()** - Run identification criteria
- **archive()** - Move identified stubs
- **generate_report()** - Create detailed report
- **save_report()** - Write report to file

### Identification Methods
- `is_test_example()` - Check for test/example keywords
- `is_completed()` - Check for completed status
- `is_obsolete_name()` - Check for deprecation indicators
- `is_low_priority_old()` - Check age + priority
- `is_vague_exploration()` - Check for unfocused exploration
- `is_infrastructure_utility()` - Check for old infrastructure
- `is_duplicate()` - Check for duplicate functional areas

## Configuration

The script uses hardcoded paths:
```python
WORKING_DIR = Path(r"C:\Users\willh\Desktop\assistant\coderef\working")
ARCHIVE_DIR = Path(r"C:\Users\willh\Desktop\assistant\coderef\archived")
```

### To Modify Paths
Edit lines 22-23 in `archive-stubs.py` with new paths.

### To Adjust Criteria
Edit the threshold values in the identification methods:
- `LOW_PRIORITY_OLD`: Line 119 (`datetime(2025, 12, 20)`)
- `INFRA_UTILITY_LOW`: Line 168 (`datetime(2026, 1, 6)`)

## Maintenance

### Monthly Archival
Consider running monthly to keep backlog clean:
```bash
# First week of each month
python archive-stubs.py
```

### Before Running
- Backup important stubs if concerned
- Review ARCHIVAL_REPORT.txt after execution
- Verify no critical work was archived

### Reverse an Archive (if needed)
```bash
# Move specific stub back to working
mv C:\Users\willh\Desktop\assistant\coderef\archived\stub-name C:\Users\willh\Desktop\assistant\coderef\working\stub-name
```

## Performance

- **Execution Time:** ~5-10 seconds for 98 stubs
- **Memory:** Minimal (<10MB)
- **I/O:** Single pass through all stub files
- **No external dependencies:** Only Python standard library

## Troubleshooting

### Unicode Errors on Windows
Fixed in script - uses ASCII symbols ([OK], [FAIL]) instead of emojis

### Permission Errors
Ensure `coderef/archived/` directory exists and is writable

### Malformed stub.json
Script gracefully skips with warning, continues processing

## Related Files

- **ARCHIVAL_SUMMARY.md** - High-level overview and statistics
- **coderef/ARCHIVAL_REPORT.txt** - Detailed categorized report (generated after run)
- **projects.md** - Master stub inventory (may need updating)

---

**Script Author:** Archive-Stubs Automation
**Last Updated:** 2026-01-13
**Version:** 1.0
