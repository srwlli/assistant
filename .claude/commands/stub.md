# Create or Update a Stub

A stub is a lightweight feature/idea specification document. Stubs are simple JSON files stored in `coderef/working/{feature_name}/stub.json`.

## Quick Reference

```bash
/stub create "Feature Name" "Clear description of what you want to build"
/stub create "Feature Name" "Description" --category "feature|fix|improvement|idea|refactor|test"
/stub create "Feature Name" "Description" --priority "high|medium|low"
```

## Required Fields (6 fields, plus 1 optional)

A stub must contain these 6 required fields:

1. **feature_name**: Simple name of the feature (kebab-case)
2. **description**: 1-2 sentences describing what needs to be built
3. **category**: One of: feature, fix, improvement, idea, refactor, test
4. **priority**: One of: high, medium, low, critical
5. **status**: Always "stub" when created (never use other values)
6. **created**: ISO 8601 timestamp (auto-generated)

**Optional field:**
- **stub_id**: Auto-generated (STUB-001, STUB-002, etc.) - added in newer stubs for tracking
- **context**: Conversation context from when stub was created

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
  "feature_name": "user-auth",
  "description": "Add JWT-based user authentication with refresh tokens",
  "category": "feature",
  "priority": "high",
  "status": "stub",
  "created": "2025-12-27T10:30:00Z"
}
```

**With optional fields (newer stubs):**
```json
{
  "stub_id": "STUB-001",
  "feature_name": "user-auth",
  "description": "Add JWT-based user authentication with refresh tokens",
  "category": "feature",
  "priority": "high",
  "status": "stub",
  "created": "2025-12-27T10:30:00Z",
  "context": "Discussion about auth needs from feature planning session"
}
```

## Schema Enforcement Rules

⚠️ **IMPORTANT**: Stubs are deliberately simple and lightweight. Do NOT add:
- ❌ `vision`, `problem`, `solution` fields (use a full plan instead)
- ❌ `code_example`, `implementation_phases`, `benefits` (way too complex)
- ❌ Long descriptions or explanations (keep 1-2 sentences only)
- ❌ Nested objects or arrays (7 simple fields only)
- ❌ Backticks, template literals, or code blocks in strings

## When to Create a Stub vs. Plan

| Use Case | File | Format |
|----------|------|--------|
| Quick idea, not ready to implement | `/stub` | Simple JSON (6 required fields) |
| Ready to implement, need detailed plan | `/plan` | Comprehensive JSON (10+ sections) |
| Learning from past work | `/archived/` | Completed feature reference |

## Validation

All stubs are automatically validated:
- ✅ Valid JSON syntax (must parse correctly)
- ✅ Contains 6 required fields (feature_name, description, category, priority, status, created)
- ✅ Optional fields allowed (stub_id, context)
- ✅ No invalid characters (backticks, template literals)
- ✅ No nested objects or complex arrays
- ✅ Auto-generated stub_id, created, status (when not provided)

**If validation fails**: The API will skip invalid stubs and provide specific error messages. Check the console for details and fix the stub.json file.

## Workflow

1. Create stub when you have a feature idea
2. Review the stub (should take 30 seconds to read)
3. When ready to implement: `/plan create` based on the stub
4. Move to plan mode for detailed design
5. After completion: `/archive` the feature

---

*Stubs are NOT design documents. Keep them simple. 6 required fields + 2 optional = lightweight ideas. If you need many more fields, you're designing a plan, not a stub.*
