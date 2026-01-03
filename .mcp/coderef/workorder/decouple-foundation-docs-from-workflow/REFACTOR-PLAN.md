# Foundation Docs Decoupling - Refactor Plan

**Stub ID:** STUB-065
**Feature:** decouple-foundation-docs-from-workflow
**Target Project:** coderef-workflow + coderef-context
**Status:** Planning
**Created:** 2025-12-30

---

## Problem Statement

`coderef-workflow` currently generates foundation docs during the `create_plan` workflow, causing:
- **Tight coupling** - Planning blocked until docs generated
- **Slow execution** - 30-60 seconds overhead per planning session
- **Responsibility blur** - Workflow server doing analysis work
- **Non-reusable** - Other workflows can't leverage generated docs

## Current Architecture

```
create_plan workflow (coderef-workflow)
  ↓
handle_coderef_foundation_docs() (tool_handlers.py:3530)
  ↓
CoderefFoundationGenerator.generate()
  ↓
Creates: ARCHITECTURE.md, SCHEMA.md, project-context.json
  ↓
Planning continues...
```

**Key Files:**
- `coderef-workflow/tool_handlers.py:3530-3600` - Foundation docs handler
- `coderef-workflow/generators/coderef_foundation_generator.py` - Generator class
- `coderef-workflow/generators/foundation_generator.py` - Legacy generator

## Proposed Architecture

```
SEPARATE LIFECYCLE:
coderef-context server
  ↓
generate_foundation_docs() tool
  ↓
Creates/updates: ARCHITECTURE.md, SCHEMA.md, project-context.json
  (Run once, update as needed)

PLANNING WORKFLOW:
create_plan workflow (coderef-workflow)
  ↓
Check if foundation docs exist
  ↓
Read existing docs → analyze → plan
  (No generation overhead)
```

## Migration Steps

### Phase 1: Move Generator to coderef-context

**Tasks:**
1. Copy `CoderefFoundationGenerator` class → `coderef-context/generators/`
2. Create new tool in `coderef-context/server.py`:
   ```python
   @server.call_tool()
   async def generate_foundation_docs(project_path: str, force_regenerate: bool = False):
       """Generate foundation docs (ARCHITECTURE, SCHEMA, project-context)"""
   ```
3. Add dependencies to `coderef-context`:
   - Git analysis utilities
   - Coderef scan integration (already present)
   - Template rendering

### Phase 2: Update coderef-workflow

**Tasks:**
1. Remove `handle_coderef_foundation_docs()` from `tool_handlers.py:3530`
2. Update `create_plan` workflow:
   ```python
   # OLD:
   await handle_coderef_foundation_docs({"project_path": path})

   # NEW:
   docs_exist = check_foundation_docs_exist(path)
   if not docs_exist:
       return warning("Run coderef-context.generate_foundation_docs first")

   analysis = read_existing_foundation_docs(path)
   ```
3. Add helper: `read_existing_foundation_docs()` - reads from disk

### Phase 3: Update Documentation

**Tasks:**
1. Update `coderef-workflow/CLAUDE.md` - Remove foundation docs generation from workflow description
2. Update `coderef-context/CLAUDE.md` - Add foundation docs generation as primary capability
3. Create migration guide for existing workflows
4. Update planning workflow guide

### Phase 4: Graceful Fallback (Optional Safety)

**Tasks:**
1. Keep legacy code path in coderef-workflow (deprecated, but functional)
2. Emit deprecation warning when used
3. Remove after 1-2 versions

## Benefits

### Performance
- ⚡ **30-60s faster** planning execution (no doc generation)
- 🔄 Docs generated once, reused many times

### Architecture
- 🎯 **Single responsibility** - Context server does analysis, workflow does planning
- 🔓 **Decoupled** - Can update docs independently of planning
- ♻️ **Reusable** - Other workflows can reference same docs

### Developer Experience
- 📖 Clearer separation: "Generate context" vs "Create plan"
- 🛠️ Easier testing (smaller, focused tools)
- 🐛 Simpler debugging (fewer moving parts per workflow)

## Impact Analysis

### Files Changed
- **coderef-workflow:** 2 files (tool_handlers.py, generators/__init__.py)
- **coderef-context:** 3 files (server.py, new generator file, __init__.py)
- **Documentation:** 3 files (2 CLAUDE.md, 1 migration guide)

### Breaking Changes
- ❌ **None** - Workflows still work with graceful fallback
- ⚠️ **Deprecation warning** - Users encouraged to migrate

### Testing Required
- ✅ coderef-context tool generates docs correctly
- ✅ coderef-workflow reads existing docs
- ✅ Error handling when docs missing
- ✅ Backward compatibility with legacy path

## Success Criteria

- [ ] Foundation docs generation tool works in coderef-context
- [ ] Planning workflow reads existing docs successfully
- [ ] No breaking changes to existing workflows
- [ ] Documentation updated across both servers
- [ ] 30-60s performance improvement measured
- [ ] All tests passing

## Rollout Plan

1. **Week 1:** Implement Phase 1 (move to coderef-context)
2. **Week 2:** Implement Phase 2 (update workflow)
3. **Week 3:** Update documentation, test migration
4. **Week 4:** Deploy, monitor, collect feedback
5. **Week 8:** Remove legacy code path (if stable)

## Open Questions

- [ ] Should we auto-generate docs on first `create_plan` call if missing?
- [ ] How to handle docs drift (code changed, docs stale)?
- [ ] Cache docs in memory vs read from disk each time?

---

**Next Steps:**
1. Review this plan with user
2. Promote STUB-065 to workorder
3. Delegate to coderef-workflow agent for implementation

**Maintained by:** CodeRef Assistant
**Attribution:** 🤖 Generated with Claude Code
