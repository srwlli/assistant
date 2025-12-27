# coderef-context vs. Available Context Tools

## Comparison Matrix

| Feature | coderef-context | Claude Context | Sourcegraph | Continue | LangChain RAG |
|---------|-----------------|----------------|-------------|----------|---------------|
| Target User | AI agents | Humans | Developers | Developers | Developers |
| Semantic search | ✅ Yes (RAG) | ✅ Yes | ❌ No | ✅ Yes | ✅ Yes |
| Code relationships | ✅ Yes (graph) | ❌ No | ✅ Yes | ❌ No | ❌ No |
| Task-specific context | ✅ Yes (Phase 2) | ❌ No | ❌ No | ❌ No | ❌ No |
| Complexity scoring | ✅ Yes (Phase 1) | ❌ No | ❌ No | ❌ No | ❌ No |
| Standards discovery | ✅ Yes (auto) | ❌ No | ❌ No | ❌ No | ❌ No |
| Code examples | ✅ Yes (Phase 5) | ❌ No | ✅ Yes | ✅ Yes | ❌ No |
| Edge case detection | ✅ Yes (Phase 3) | ❌ No | ❌ No | ❌ No | ❌ No |
| Test patterns | ✅ Yes (Phase 4) | ❌ No | ❌ No | ⚠️ Partial | ❌ No |
| Confidence scoring | ✅ Yes | ❌ No | ❌ No | ❌ No | ⚠️ Partial |
| Progressive disclosure | ✅ Yes | ❌ No | ❌ No | ❌ No | ❌ No |
| Agentic output format | ✅ Yes (Phase 6) | ❌ No | ❌ No | ❌ No | ⚠️ Partial |
| Local/offline | ✅ Yes (Chroma) | ❌ Cloud only | ❌ Cloud only | ✅ Yes | ✅ Yes |
| Multi-language | ✅ Yes (TS, Py) | ❌ No | ⚠️ Limited | ✅ Yes | ✅ Yes |
| Cost | ✅ Free | ❌ Paid | ❌ Paid | ✅ Free | ✅ Free |
| Workflow integration | ✅ Yes | ❌ No | ❌ No | ❌ No | ❌ No |
| Multi-tenant | ✅ Yes (via dashboard) | ❌ No | ✅ Yes | ❌ No | ❌ No |
| Performance | ✅ Fast | ✅ Fast | ✅ Fast | ✅ Fast | ⚠️ Slow |

---

## Detailed Comparison

### coderef-context

**Strengths:**
- Purpose-built for AI agents (not humans)
- Task-specific context generation (what to implement, not just what exists)
- Complexity scoring for effort estimation
- Edge case detection to prevent bugs
- Test pattern analysis for validation
- Auto-discovery of coding standards
- Confidence scoring on all outputs
- Progressive disclosure (agents get what they need, when they need it)
- Free, open-source, local/offline
- Integrates with coderef-workflow for planning

**Weaknesses:**
- Newer, less battle-tested than others
- Requires setup (Chroma DB for embeddings)
- Limited community (vs. LangChain)

**Best for:** AI agents doing implementation tasks within orchestrated workflows

---

### Claude Context (API)

**Strengths:**
- Simple to use
- Excellent relevance (Claude knows how to rank)
- Works great for humans asking questions
- Fast

**Weaknesses:**
- Cloud-only (privacy concerns)
- Expensive per query
- Not designed for agents
- No complexity scoring
- No standards discovery
- No task-specific context
- No workflow integration

**Best for:** Human developers asking ad-hoc questions

---

### Sourcegraph

**Strengths:**
- Comprehensive code relationship mapping
- Enterprise-ready
- Good for code search
- Multi-language support

**Weaknesses:**
- Expensive (enterprise pricing)
- Cloud-only
- Complex setup
- Not designed for agents
- No complexity scoring
- No standards discovery
- No workflow integration

**Best for:** Enterprise teams needing code search + relationship graphs

---

### Continue

**Strengths:**
- IDE integration (works where developers code)
- Free
- Code examples
- Local support option
- Decent semantic search

**Weaknesses:**
- Designed for human IDE users, not agents
- Partial test pattern support
- No complexity scoring
- No task-specific context
- No workflow integration
- No standards discovery

**Best for:** IDE-based developer assistance

---

### LangChain RAG

**Strengths:**
- Mature, widely-used
- Good semantic search
- Multi-language
- Free
- Extensible

**Weaknesses:**
- General-purpose (not agent-specific)
- Slow performance
- Requires significant setup
- No complexity scoring
- No task-specific context
- No standards discovery
- No built-in workflow integration
- Partial confidence scoring

**Best for:** General-purpose RAG applications

---

## Key Differentiators of coderef-context

### 1. Task-Specific Context (Phase 2)

coderef-context generates context **per task**:

```json
{
  "task": "Add user authentication to API",
  "related_functions": ["authenticate()", "getUserById()", ...],
  "complexity_estimate": "medium (8 hours)",
  "risk_level": "high (affects login flow)",
  "examples": [...],
  "gotchas": ["Must handle refresh tokens", ...],
  "confidence": 0.92
}
```

**Others:** Just return code snippets. Agents must infer complexity, risk, gotchas.

---

### 2. Complexity Scoring (Phase 1)

coderef-context scores effort per feature:

```
Feature A: Low (2-3 hours)
├── Uses existing patterns
├── 1-2 files to change
└── Well-tested code path

Feature B: High (16+ hours)
├── New pattern needed
├── 8+ files to change
└── Complex interactions
```

**Others:** Don't estimate effort at all.

---

### 3. Standards Discovery (Auto)

coderef-context auto-discovers standards from code:

```
Discovered UI Standards:
├── All buttons use ButtonComponent
├── Forms use FormBuilder
└── Modals use ModalDialog

Discovered Patterns:
├── Error handling: try/catch + logger.error()
├── API calls: useQuery() hook
└── State: Redux pattern
```

**Others:** No standards discovery. You have to tell them what standards exist.

---

### 4. Agentic Output Format (Phase 6)

coderef-context outputs JSON specifically formatted for agents:

```json
{
  "metadata": {
    "task": "...",
    "confidence": 0.92,
    "generated_at": "2025-12-22T10:00:00Z"
  },
  "context": {
    "related_code": [...],
    "complexity": {...},
    "gotchas": [...]
  },
  "actions": {
    "suggested_files": [...],
    "test_strategy": "..."
  }
}
```

**Others:** Return text or generic JSON. Agents must parse and interpret.

---

### 5. Workflow Integration

coderef-context is designed to feed into coderef-workflow:

```typescript
// Agent calls this
const context = await generateTaskContext(sourceDir, taskDescription);

// Gets back JSON with everything needed
// - What code to modify
// - Complexity estimate
// - Common mistakes
// - Test strategy
// - Standards to follow

// Agent uses it to implement faster, safer
```

**Others:** Standalone tools. No workflow integration.

---

## When to Use Each

| Tool | Use When |
|------|----------|
| **coderef-context** | Building AI agents within orchestrated workflows; need task-specific context, complexity scoring, standards discovery |
| **Claude Context API** | Human developers asking ad-hoc questions; okay with cloud + cost |
| **Sourcegraph** | Enterprise teams needing code relationships + search; budget available |
| **Continue** | Developers using IDEs; want integrated assistant in editor |
| **LangChain** | Building custom RAG systems; need extensibility over simplicity |

---

## coderef-context Roadmap

**Current (Phase 1-6):**
- Complexity scoring
- Task-specific context
- Edge case detection
- Test patterns
- Code examples
- Agentic formatting

**Future Enhancements:**
- Multi-language support (currently TS)
- Graph-based relationship analysis (vs. current text-based)
- Real-time codebase indexing (vs. periodic scans)
- Confidence intervals on recommendations
- Impact analysis (what breaks if we change this?)
