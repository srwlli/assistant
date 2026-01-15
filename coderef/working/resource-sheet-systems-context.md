# Resource Sheet Systems - Context Document

**Created:** 2026-01-02
**Purpose:** Decision-making context for two parallel resource sheet implementations

---

## Executive Summary

You have **TWO separate resource sheet systems** both located in `coderef-docs` MCP server:

1. **Python Implementation** (`resource_sheet/`) - Working MCP runtime (Phase 1 complete)
2. **TypeScript Documentation** (`modules/resource-sheet/`) - Comprehensive specs & templates (Phase 2 complete)

Both systems were built for the same purpose but with different approaches and completion levels.

---

## System Comparison

| Aspect | Python System | TypeScript System |
|--------|---------------|-------------------|
| **Location** | `C:\Users\willh\.mcp-servers\coderef-docs\resource_sheet` | `C:\Users\willh\.mcp-servers\coderef-docs\modules\resource-sheet` |
| **Purpose** | Executable MCP tool runtime | Documentation specs & templates |
| **Language** | Python | TypeScript + Markdown |
| **Status** | ✅ Phase 1 complete (17/22 tasks, 77%) | ✅ Phase 1 & 2 specs complete |
| **Files** | 17 Python files | 28 files (TypeScript + Markdown) |
| **LOC** | ~2,761 LOC (Python code) | ~7,380 LOC (TypeScript + Markdown) |
| **Tests** | 13/13 passing (100% coverage) | None (documentation only) |
| **Commits** | e5d09a9, 48d5a5b, ae8289c, e596faa | d4be925 |
| **Workorder** | WO-RESOURCE-SHEET-MCP-TOOL-001 | Same workorder |
| **Auto-fill Rate** | 50% (Phase 1), target 60%+ (Phase 2) | 60-70% (documented target) |
| **Detection Accuracy** | ~85% (Phase 1), target 90%+ (Phase 2) | 90%+ (documented target) |
| **Output Formats** | 3 (Markdown, JSON Schema, JSDoc) | 3 (same) |
| **Module System** | 4 universal + 0 conditional (Phase 1) | 4 universal + 11 conditional (documented) |

---

## Python System Deep Dive

### What It Is
A **working MCP tool** that generates resource sheet documentation from code analysis.

### Architecture
```
resource_sheet/
├── __init__.py (84 LOC)              # Package entry point
├── types.py (162 LOC)                # Type definitions
├── detection/
│   ├── analyzer.py (154 LOC)         # CodeAnalyzer - reads .coderef/index.json
│   └── characteristics.py (144 LOC)  # CharacteristicsDetector - 20+ code patterns
├── composition/
│   └── composer.py (259 LOC)         # DocumentComposer - assembles 3 formats
├── modules/
│   ├── __init__.py (159 LOC)         # ModuleRegistry
│   ├── _universal/                   # 4 modules
│   │   ├── architecture.py (172 LOC) # ✅ Full implementation
│   │   ├── integration.py (160 LOC)  # ✅ Full implementation
│   │   ├── testing.py (35 LOC)       # ⏳ Stub (Phase 2)
│   │   └── performance.py (35 LOC)   # ⏳ Stub (Phase 2)
│   └── conditional/                  # 11 modules
│       ├── hooks/ (4 files, 253 LOC)
│       ├── network/ (4 files, 468 LOC)
│       ├── state/ (2 files, 261 LOC)
│       └── ui/ (3 files, 344 LOC)
└── examples/
    ├── sample-authservice.md
    ├── sample-authservice.schema.json
    └── sample-authservice.jsdoc.txt
```

### Key Features
- ✅ **Operational MCP tool** - Callable via `generate_resource_sheet` (13th tool in coderef-docs)
- ✅ **3 generation modes** - reverse-engineer, template, refresh
- ✅ **CodeRef integration** - Reads `.coderef/index.json` for analysis
- ✅ **Graceful fallback** - Works without `.coderef/` (manual mode)
- ✅ **3 output formats** - Markdown, JSON Schema, JSDoc
- ✅ **Test coverage** - 13/13 tests passing (detection, selection, integration)
- ✅ **Performance** - < 5 seconds end-to-end

### Current Limitations (Phase 1)
- ⏳ **50% auto-fill** (below 60% target) - only 2/4 universal modules fully implemented
- ⏳ **85% detection** (below 90% target) - conditional modules not yet implemented
- ⏳ **Testing/Performance modules are stubs** - intentional Phase 1 scope limitation
- ⏳ **11 conditional modules planned but not implemented**

### Phase 2 Roadmap (5 remaining tasks)
1. **MODULE-002**: Implement 11 conditional modules (endpoints, auth, errors, state, props, etc.)
2. **PAPER-001**: Integrate Papertrail UDS headers/footers
3. **TEST-004**: Add React component integration test
4. **TEST-005**: Validate 60%+ auto-fill rate
5. Achieve 90%+ detection accuracy

---

## TypeScript System Deep Dive

### What It Is
A **comprehensive documentation system** with specs, templates, and guides for generating resource sheets manually or via automation.

### Architecture
```
modules/resource-sheet/
├── README.md (880 lines)                       # Complete documentation
├── RESOURCE-SHEET-SYSTEM.md (1,460 lines)      # Authoritative guide for agents
├── MODULE-CATEGORIES-GUIDE.md (19 KB)          # Category classification
├── PROGRESS.md                                 # Implementation tracking
├── types.ts                                    # TypeScript type definitions
├── index.ts                                    # Main entry point
├── _universal/ (4 markdown templates)
│   ├── architecture.md
│   ├── integration.md
│   ├── testing.md
│   └── performance.md
├── conditional/ (11 markdown templates)
│   ├── accessibility.md
│   ├── auth.md
│   ├── endpoints.md
│   ├── errors.md
│   ├── events.md
│   ├── lifecycle.md
│   ├── persistence.md
│   ├── props.md
│   ├── routing.md
│   ├── state.md
│   └── validation.md
├── detection/ (3 TypeScript modules)
│   ├── analyzer.ts
│   ├── classifier.ts
│   └── selector.ts
├── composition/
│   └── composer.ts
└── output/ (3 generators)
    ├── markdown-generator.ts
    ├── schema-generator.ts
    └── jsdoc-generator.ts
```

### Key Features
- ✅ **Complete specifications** - 1,460-line authoritative guide
- ✅ **15 module templates** - 4 universal + 11 conditional (all documented)
- ✅ **8 user-friendly categories** - tools, ui, services, state, data, generators, infrastructure, testing
- ✅ **Kitchen analogy** - Intuitive category explanations
- ✅ **Composable architecture** - LEGO block approach vs rigid templates
- ✅ **3-step workflow** - Detect → Select → Assemble
- ✅ **Dual usage modes** - Automated (60-70% auto-fill) and Manual (agent-guided)
- ✅ **Quality standards** - Refactor safety, onboarding optimization, validation checklist
- ✅ **Integration strategy** - Works with `.coderef/` or standalone

### What's NOT Implemented
- ❌ **No executable code** - Only TypeScript/markdown specs, not working runtime
- ❌ **No tests** - Documentation only, no test suite
- ❌ **No MCP tool integration** - Specs exist but not connected to MCP server

---

## Key Innovation: Composable Modules

**Old Approach (Rejected):**
- 20 rigid templates (top-level-widget, stateful-container, api-client, etc.)
- Massive duplication (copy "State" across 10+ templates)
- Hard to maintain (update "Performance" in 20 places)
- Technical jargon (developers don't think in these terms)

**New Approach (Both Systems):**
- **4 universal modules** - Always included (architecture, integration, testing, performance)
- **11 conditional modules** - Selected based on code characteristics
  - `endpoints` → triggers: fetch/axios calls
  - `auth` → triggers: JWT/tokens
  - `errors` → triggers: try/catch, error classes
  - `state` → triggers: useState, Redux, Zustand
  - `props` → triggers: React components with props
  - `events` → triggers: addEventListener, onClick
  - `lifecycle` → triggers: useEffect, componentDidMount
  - `validation` → triggers: Zod, Yup validators
  - `persistence` → triggers: localStorage, IndexedDB
  - `routing` → triggers: Next.js router, React Router
  - `accessibility` → triggers: ARIA attributes

**LEGO Analogy:** Instead of 20 pre-built structures, provide 15 blocks that snap together based on what you're building.

---

## Detection Logic (Both Systems)

**Step 1: Read `.coderef/index.json`**
```json
{
  "elements": [{
    "name": "FileTree",
    "type": "function",
    "file": "src/components/FileTree.tsx",
    "metadata": {
      "hasJSX": true,
      "props": ["tree", "onFileSelect"],
      "hooks": ["useState", "useEffect"]
    }
  }]
}
```

**Step 2: Analyze Characteristics**
- `isReactComponent` → hasJSX = true
- `usesState` → hooks includes useState
- `hasProps` → props.length > 0
- `hasLifecycle` → hooks includes useEffect

**Step 3: Classify Category**
- Category: `ui/components` (has JSX, in components/ folder)
- Confidence: 95%

**Step 4: Select Modules**
- Universal: architecture, integration, testing, performance
- Conditional: state (useState), props (has props), lifecycle (useEffect)

---

## Output Format (Both Systems)

**⚠️ CRITICAL:** Every resource sheet generates **ALL 3 formats**:

### 1. Markdown Documentation (.md)
- **File:** `coderef/foundation-docs/{ELEMENT-NAME}.md`
- **Size:** 15-25 KB typical
- **Sections:** Executive summary + dynamic module sections
- **Example:** `FILE-TREE.md` (22 KB, 8 sections)

### 2. JSON Schema (.json)
- **File:** `coderef/schemas/{element-name}-schema.json`
- **Size:** 8-15 KB typical
- **Format:** JSON Schema Draft 7
- **Example:** `file-tree-schema.json` (12 KB)

### 3. JSDoc Suggestions (.txt)
- **File:** `coderef/foundation-docs/.jsdoc/{element-name}-jsdoc.txt`
- **Size:** 2-5 KB typical
- **Format:** Copy-paste JSDoc comments
- **Example:** `file-tree-jsdoc.txt` (3 KB)

---

## Relationship Between Systems

**Hypothesis:** These appear to be **parallel implementations** of the same vision:

1. **Python System** = Executable runtime (bottom-up approach)
   - Started with minimal viable product (4 modules)
   - Built working MCP tool first
   - Tests prove it works
   - Plan to expand to 15 modules in Phase 2

2. **TypeScript System** = Complete specification (top-down approach)
   - Started with comprehensive documentation
   - Documented all 15 modules upfront
   - TypeScript types define interfaces
   - Plan to implement runtime later

**Current State:**
- Python has **working tool** but incomplete module coverage (4/15)
- TypeScript has **complete specs** but no working implementation

**Ideal State:**
- One unified system with working runtime + complete module coverage

---

## Decision Points

### Option 1: Consolidate to Python
**Pros:**
- ✅ Working MCP tool (13/13 tests passing)
- ✅ Already integrated with coderef-docs server
- ✅ Performance validated (< 5s end-to-end)
- ✅ Users can use it today

**Cons:**
- ⏳ Only 4/15 modules implemented (27% complete)
- ⏳ Need to implement 11 conditional modules from scratch
- ⏳ Documentation less comprehensive than TypeScript version

**Action:**
- Migrate TypeScript module templates to Python
- Implement 11 conditional modules (MODULE-002)
- Archive TypeScript version as documentation reference

---

### Option 2: Consolidate to TypeScript
**Pros:**
- ✅ Complete 15-module architecture documented
- ✅ Comprehensive 1,460-line guide
- ✅ Better category system (8 categories vs Python's implicit)
- ✅ Quality standards defined (refactor safety, validation)

**Cons:**
- ❌ No working implementation (just specs)
- ❌ No tests
- ❌ Not integrated with MCP server
- ❌ Need to implement everything from scratch

**Action:**
- Port Python's working detection/composition logic to TypeScript
- Implement all 15 modules based on specs
- Write test suite
- Integrate with MCP server

---

### Option 3: Keep Both (Hybrid)
**Pros:**
- ✅ Python for runtime (fast, tested, working)
- ✅ TypeScript for specs (comprehensive, maintained)
- ✅ No migration risk

**Cons:**
- ⚠️ Maintenance burden (2 systems to keep in sync)
- ⚠️ Confusion about which is source of truth
- ⚠️ Duplication of effort

**Action:**
- Establish clear roles (Python = runtime, TypeScript = specs)
- Create synchronization workflow (TypeScript specs → Python templates)
- Document relationship in both systems

---

### Option 4: Merge Gradually
**Pros:**
- ✅ Preserve Python's working runtime
- ✅ Adopt TypeScript's superior architecture/docs
- ✅ Incremental migration reduces risk

**Cons:**
- ⏳ Slower path to completion
- ⏳ Temporary inconsistency during migration

**Action:**
1. Copy TypeScript module templates to Python `templates/` directory
2. Update Python to use template files (not hardcoded strings)
3. Implement 11 conditional modules from TypeScript specs
4. Gradually enhance documentation to match TypeScript quality
5. Archive TypeScript implementation when complete

---

## Recommended Decision Framework

**Ask yourself:**

1. **What's the priority?**
   - **Speed to production** → Option 1 (Python, already working)
   - **Long-term maintainability** → Option 2 (TypeScript, better architecture)
   - **Risk aversion** → Option 4 (Gradual merge)

2. **Who will maintain this?**
   - **Python developers** → Option 1
   - **TypeScript developers** → Option 2
   - **Mixed team** → Option 3 (keep both)

3. **What's the use case?**
   - **Need it now** → Option 1 (Python works today)
   - **Building foundation for future** → Option 2 (TypeScript specs are comprehensive)
   - **Both** → Option 4 (gradual migration)

4. **What's the technical debt tolerance?**
   - **Low tolerance** → Option 2 or 4 (clean slate or gradual improvement)
   - **Medium tolerance** → Option 1 (working but incomplete)
   - **High tolerance** → Option 3 (keep both, sync manually)

---

## Usage Comparison

### Python System (Today)
```python
from generators.resource_sheet_generator import ResourceSheetGenerator

generator = ResourceSheetGenerator()
result = await generator.generate(
    element_name="FileTree",
    project_path="/path/to/project",
    mode="reverse-engineer",
    auto_analyze=True
)

# ✅ Works now
# ⚠️ Only 50% auto-fill (4 modules)
# ⚠️ 85% detection accuracy
```

### TypeScript System (Documented, Not Implemented)
```typescript
import { generateResourceSheet } from './modules/resource-sheet';

const result = await generateResourceSheet({
  project_path: '/path/to/project',
  element_name: 'FileTree',
  mode: 'reverse-engineer',
  output_path: '/path/to/output'
});

// ❌ Not implemented yet
// ✅ Would give 60-70% auto-fill (15 modules)
// ✅ Would give 90%+ detection accuracy
```

---

## File Paths (Quick Reference)

**Python System:**
```
C:\Users\willh\.mcp-servers\coderef-docs\resource_sheet\
```

**TypeScript System:**
```
C:\Users\willh\.mcp-servers\coderef-docs\modules\resource-sheet\
```

**Python Tests:**
```
C:\Users\willh\.mcp-servers\coderef-docs\tests\test_resource_sheet.py
```

**Workorder:**
```
C:\Users\willh\.mcp-servers\coderef-docs\coderef\workorder\resource-sheet-mcp-tool\
```

---

## Next Steps

1. **Review this document** - Understand both systems fully
2. **Choose consolidation strategy** - Options 1-4 above
3. **Create implementation plan** - Based on chosen option
4. **Update workorder** - Document decision and rationale
5. **Execute migration/completion** - Implement chosen path
6. **Update documentation** - Reflect final architecture

---

## Questions to Consider

1. **Do you need resource sheets now or later?**
   - Now → Use Python (works today)
   - Later → Invest in TypeScript (better long-term)

2. **Will you build more MCP tools in Python or TypeScript?**
   - Python → Stick with Python ecosystem
   - TypeScript → Migrate to TypeScript for consistency

3. **How important is the 60% auto-fill target?**
   - Critical → Need 11 conditional modules (TypeScript has specs)
   - Nice-to-have → Python's 50% may be sufficient

4. **How important is 90% detection accuracy?**
   - Critical → Need conditional modules (TypeScript has full logic)
   - Nice-to-have → Python's 85% may be sufficient

5. **What's the maintenance plan?**
   - One person → One system (Option 1 or 2)
   - Team → Could maintain both (Option 3)

---

**END OF CONTEXT DOCUMENT**

**Decision Time:** Review the comparison above and choose your path forward.
