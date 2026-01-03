# Create Stub - Quick Feature Idea Capture

**EXECUTION INSTRUCTIONS:**

When user provides a feature idea, follow these steps:

1. **Extract from user input:**
   - Feature name (convert to kebab-case)
   - Description (keep brief, 10-500 chars)

2. **Check projects.md** for next STUB-ID (look for line "Next STUB-ID: STUB-XXX")

3. **Ask user for (if not obvious):**
   - Category: feature, enhancement, bugfix, infrastructure, documentation, refactor, research
   - Priority: low, medium, high, critical (default: medium)
   - Target project (optional)

4. **Auto-detect:**
   - Status: "planning" (default for new stubs)
   - Created: Today's date in YYYY-MM-DD format

5. **Create folder:** `C:\Users\willh\Desktop\assistant\coderef\working\{feature-name}/`

6. **Create stub.json** with EXACTLY this format (matches stub-schema.json):
```json
{
  "stub_id": "STUB-XXX",
  "feature_name": "{feature-name}",
  "description": "{description}",
  "category": "{category}",
  "priority": "{priority}",
  "status": "planning",
  "created": "YYYY-MM-DD",
  "target_project": "{project}",
  "tags": ["{tag1}", "{tag2}"]
}
```

7. **Update projects.md:** Increment "Next STUB-ID" to next number

8. **Confirm:** "Stubbed: STUB-XXX: {feature-name} (from project: {target_project})"

---

## Reference Documentation

A stub is a lightweight feature/idea specification document. Stubs are simple JSON files stored in `coderef/working/{feature_name}/stub.json`.

## Quick Reference

```bash
/stub create "Feature Name" "Clear description of what you want to build"
/stub create "Feature Name" "Description" --category "feature|enhancement|bugfix|infrastructure|documentation|refactor|research"
/stub create "Feature Name" "Description" --priority "low|medium|high|critical"
/stub create "Feature Name" "Description" --target "project-name"
```

## Required Fields (7 fields)

A stub must contain these 7 required fields per stub-schema.json:

1. **stub_id**: Auto-incremented ID (STUB-001, STUB-002, etc.) - check projects.md for next ID
2. **feature_name**: Simple name of the feature (kebab-case, matches folder name)
3. **description**: 1-2 sentences describing what needs to be built (10-500 chars)
4. **category**: One of: feature, enhancement, bugfix, infrastructure, documentation, refactor, research
5. **priority**: One of: low, medium, high, critical
6. **status**: One of: planning, ready, blocked, promoted, abandoned (default: planning)
7. **created**: Date in YYYY-MM-DD format (NOT ISO timestamp)

**Optional fields:**
- **target_project**: Project where work will be done (e.g., "assistant", "coderef-workflow")
- **promoted_to**: Workorder ID if promoted (e.g., "WO-AUTH-001")
- **tags**: Array of strings for filtering/searching
- **notes**: Additional context or notes

## Example Usage

```bash
/stub create "user-auth" "Add JWT-based user authentication with refresh tokens"
/stub create "performance-cache" "Implement Redis caching layer for API responses" --category "improvement" --priority "high"
/stub create "dark-mode" "Add theme toggle for dark/light mode" --priority "medium"
```

## Generated File Structure

When you create a stub, it generates a file at `coderef/working/{feature_name}/stub.json`:

```json
{
  "stub_id": "STUB-075",
  "feature_name": "user-auth",
  "description": "Add JWT-based user authentication with refresh tokens",
  "category": "feature",
  "priority": "high",
  "status": "planning",
  "created": "2025-12-27",
  "target_project": "backend-api",
  "tags": ["authentication", "security", "jwt"]
}
```

## Schema Enforcement Rules

⚠️ **IMPORTANT**: Stubs are deliberately simple and lightweight. Do NOT add:
- ❌ `vision`, `problem`, `solution` fields (use a full plan instead)
- ❌ `code_example`, `implementation_phases`, `benefits` (way too complex)
- ❌ Long descriptions or explanations (keep 1-2 sentences, 10-500 chars)
- ❌ Fields not in stub-schema.json (additionalProperties: false)
- ❌ Backticks, template literals, or code blocks in strings

## When to Create a Stub vs. Plan

| Use Case | File | Format |
|----------|------|--------|
| Quick idea, not ready to implement | `/stub` | Simple JSON (6 required fields) |
| Ready to implement, need detailed plan | `/plan` | Comprehensive JSON (10+ sections) |
| Learning from past work | `/archived/` | Completed feature reference |

## Validation

All stubs are validated against stub-schema.json:
- ✅ Valid JSON syntax (must parse correctly)
- ✅ Contains 7 required fields (stub_id, feature_name, description, category, priority, status, created)
- ✅ Optional fields: target_project, promoted_to, tags, notes
- ✅ category must be: feature, enhancement, bugfix, infrastructure, documentation, refactor, research
- ✅ priority must be: low, medium, high, critical
- ✅ status must be: planning, ready, blocked, promoted, abandoned
- ✅ created format: YYYY-MM-DD (NOT ISO timestamp)
- ✅ stub_id format: STUB-XXX (check projects.md for next ID)

**If validation fails**: Dashboard will skip incomplete stubs and show:
```
⚠️ Skipping incomplete stub at {feature-name}/stub.json: Missing fields [category, priority]
Required fields: feature_name, description, category, priority, status, created
Action: Add missing required fields to the stub
```

## Workflow

1. Create stub when you have a feature idea
2. Review the stub (should take 30 seconds to read)
3. When ready to implement: `/plan create` based on the stub
4. Move to plan mode for detailed design
5. After completion: `/archive` the feature

---

## Workflow Steps

1. **Check projects.md** for next STUB-ID (e.g., STUB-075)
2. **Create folder**: `coderef/working/{feature-name}/`
3. **Create stub.json** with all 7 required fields
4. **Update projects.md**: Increment Next STUB-ID to STUB-076
5. **Verify**: Check dashboard for validation errors

---

*Stubs are NOT design documents. Keep them simple. 7 required fields + 4 optional = lightweight ideas. Follow stub-schema.json exactly.*
