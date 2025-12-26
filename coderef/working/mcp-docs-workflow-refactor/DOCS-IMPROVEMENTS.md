# coderef-docs: Feature Analysis & Improvements

## Should coderef-docs Use These Features?

### ✅ YES - Apply These

#### 1. Incremental Indexing

**Description:** First doc generation takes full scan (2 minutes), subsequent runs only re-scan changed files (15 seconds)

**Value:** Regenerate docs faster on every commit

**Worth it?** ✅ YES - Same effort as coderef-context

---

#### 2. Better Code Chunking

**For API.md:**
- Group related endpoints together
- Show examples with context (not isolated)
- Link to SCHEMA.md for data models

**Value:** Better documentation quality

**Worth it?** ✅ YES - Improves readability

---

#### 3. Better Semantic Ranking

**For ARCHITECTURE.md:**
- Order sections by importance
- Highlight critical patterns first
- Demote edge cases to appendix

**For API.md:**
- List most-used endpoints first
- Group by frequency/importance
- Mark deprecated endpoints clearly

**Value:** Docs are more discoverable

**Worth it?** ✅ YES - Helps agents find what matters

---

#### 4. Relationship Visualization

**For ARCHITECTURE.md:**
- Call graphs showing module relationships
- Dependency diagrams
- Data flow visualizations

**Value:** Agents understand structure visually

**Worth it?** ✅ YES - Complements text docs

---

### ❌ NO - Don't Apply These

#### Multi-Turn Conversation

- Docs are static reference material
- No back-and-forth interaction
- Skip it

---

## Different Features for coderef-docs

coderef-docs needs NEW features unique to documentation generation:

### 1. Auto-Generated Table of Contents

Build nested TOC from document structure, link to sections, update automatically

---

### 2. Cross-References

- README → points to ARCHITECTURE
- ARCHITECTURE → points to API
- API → points to SCHEMA
- All automatic

---

### 3. Code Snippet Versioning

Track which version of code examples are shown, update when code changes, show deprecation warnings

---

### 4. Documentation Completeness Scoring

```
README: 85% (missing usage examples)
ARCHITECTURE: 92% (complete)
API: 78% (missing response codes)
SCHEMA: 100% (complete)
```

---

### 5. Out-of-Date Detection

Scan for:
- Deprecated APIs
- Functions that moved
- Changed signatures
- Flag for agent to fix

---

## Summary: Feature Distribution

| Feature | coderef-context | coderef-docs | Purpose |
|---------|-----------------|--------------|---------|
| Incremental indexing | ✅ | ✅ | Speed |
| Better code chunking | ✅ | ✅ | Quality examples |
| Better semantic ranking | ✅ | ✅ | Prioritization |
| Multi-turn conversation | ✅ | ❌ | Not applicable |
| Relationship visualization | ⚠️ Optional | ✅ | Understanding |
| Auto TOC generation | ❌ | ✅ | Navigation |
| Cross-references | ❌ | ✅ | Discoverability |
| Snippet versioning | ❌ | ✅ | Maintenance |
| Completeness scoring | ❌ | ✅ | Quality |
| Out-of-date detection | ❌ | ✅ | Accuracy |

---

## Strategic Approach

**Don't copy features blindly.**

Each tool should have features that serve its purpose.

---

## coderef-context Features

```
coderef-context features:
├── Task-specific context (agents implement)
├── Complexity scoring (agents estimate effort)
├── Edge case warnings (agents avoid bugs)
├── Incremental indexing (speed)
└── Better examples (quality)
```

---

## coderef-docs Features

```
coderef-docs features:
├── Auto-generated TOC (navigation)
├── Cross-references (discovery)
├── Relationship diagrams (understanding)
├── Out-of-date detection (accuracy)
├── Completeness scoring (quality)
├── Incremental regeneration (speed)
└── Better examples (quality)
```

---

## Overlap is Fine

Incremental indexing and better examples are shared. Different needs drive different features.

---

## Recommendation

### Phase 1: Build coderef-context (six phases)

### Phase 2: Enhance coderef-docs with:

1. Incremental regeneration
2. Better code examples (via improved chunking)
3. Semantic ranking (order by importance)
4. Auto TOC + cross-references
5. Out-of-date detection
6. Relationship diagrams

**Note:** Not the same as coderef-context enhancements—different but complementary.
