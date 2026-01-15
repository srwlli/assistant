# Scanner & Context Enhancement - Complete Integration Session

**Date:** 2026-01-14
**Session Type:** Multi-Phase Cross-Ecosystem Enhancement
**Duration:** 8-10 weeks

---

## Executive Summary

This document outlines a comprehensive session to enhance the scanner and context systems, then integrate those improvements into workflow and docs MCP servers. The session is structured in 3 phases to ensure proper dependency flow and validation at each stage.

**Source Documents:**
- `C:/Users/willh/.mcp-servers/coderef-context/CONTEXT-LEVERAGE-ANALYSIS.md` - Context underutilization analysis
- `C:\Users\willh\Desktop\coderef-dashboard\packages\coderef-core\coderef\resources-sheets\Scanner-Effectiveness-Improvements-RESOURCE-SHEET.md` - Scanner roadmap

**Key Insight:** We're only using 40% of available `.coderef/` resources, and the scanner has 15 prioritized improvements (accuracy, performance, coverage) that will benefit the entire ecosystem.

---

## Integration Analysis

### How coderef-workflow uses context data

**Current State (v2.0.0):**
- **Planning analyzer** reads `.coderef/index.json`, `patterns.json`, `coverage.json`, `complexity.json` (5 separate file reads)
- **MCP tool calls**: `coderef_query`, `coderef_impact`, `coderef_complexity`, `coderef_diagram`
- **AI-powered planning** loads all 5 coderef data types to generate file-specific tasks with exact line numbers
- **Telemetry tracking**: Logs data sources used (📁 file reads, 🔧 MCP tools, 📄 docs)

**Current Bottleneck:**
- 5 separate file reads instead of 1 enhanced MCP call
- No access to diagrams, generated docs, or pre-computed complexity
- Misses 60% of available context data

### How coderef-docs uses context data

**Current State (v4.0.0):**
- **Standards establishment** reads `.coderef/index.json` for pattern extraction
- **MCP integration**: Uses coderef-context for drift detection and semantic pattern analysis (80% quality vs 55% regex-only)
- **Foundation docs** currently use basic file scanning (NOT leveraging enhanced context!)
- **Resource sheets** could benefit from element metadata

**Current Bottleneck:**
- `generate_foundation_docs` does basic file scanning instead of using scanner
- No access to enhanced scanner accuracy (85% vs potential 95%)
- Missing Python pattern coverage (+30% elements)

---

## Integration Opportunities

### 1. Workflow gets BETTER planning context

**Current:** Reads 5 separate files → 6 total operations
**Proposed:** Call enhanced `coderef_context` once → 1 operation

**Benefits:**
- 6x fewer operations
- 95% context quality vs 40%
- Auto-includes diagrams, patterns, complexity hotspots
- Gets pre-generated docs summary

**Implementation:**
- Update `planning_analyzer.py`: `analyze_project_for_planning()`
- Replace 5 file reads with single `coderef_context` MCP call
- Update AI planning prompt to use new context fields

### 2. Docs gets RICHER foundation docs

**Current:** Basic file scanning → 85% accuracy, limited patterns
**Proposed:** Use enhanced scanner + context → 95% accuracy, 30% more elements

**Benefits:**
- Better accuracy in ARCHITECTURE.md (interfaces, decorators detected)
- Richer API.md (complete function signatures, relationships)
- Enhanced COMPONENTS.md (class properties, arrow methods)
- Faster generation (parallel processing)

**Implementation:**
- Update `generate_foundation_docs` to use enhanced scanner
- Add `coderef_context` call for architecture overview
- Leverage populated `patterns.json`, `complexity.json`

---

## Session Structure: 3 Phases

### Phase 1: Core Enhancements (Week 1-2)

**Lead Agents:** coderef-context, coderef-dashboard

#### coderef-context Tasks

1. **Enhance coderef_context tool** (Priority 1 from CONTEXT-LEVERAGE-ANALYSIS.md)
   - Auto-include `diagram-wrapped.md` content
   - Add `elements_by_type` breakdown (function: 89, class: 12, etc.)
   - Add generated docs summary (from `.coderef/generated-docs/README.md`)
   - Add complexity hotspots array
   - Add key modules list

2. **Add new CodeRefReader methods:**
   - `get_generated_docs(doc_type)` - Read auto-generated docs
   - `get_diagram_wrapped()` - Read pre-formatted diagram with notes
   - `get_element_stats()` - Get element type breakdown

3. **Populate empty reports:**
   - Enhance scanner to create `patterns.json` (handlers, decorators, imports)
   - Enhance scanner to create `validation.json` (CodeRef2 tag coverage)
   - Add `complexity.json` with pre-computed metrics

**Deliverables:**
- Enhanced `coderef_context` tool with 95% context quality (vs 40%)
- `patterns.json` populated with handlers, decorators, common imports
- `validation.json` populated with tag coverage data
- `complexity.json` with cyclomatic complexity metrics

**Success Metrics:**
- Tool call reduction: 6 calls → 1 call
- Context quality: 40% → 95%
- Response time: 0.3s → 0.05s

#### coderef-dashboard Tasks

**Location:** `C:\Users\willh\Desktop\coderef-dashboard\packages\coderef-core\`

**Target Files:**
- `src/scanner/scanner.ts` - Main scanner implementation
- `src/scanner/types.ts` - Type definitions (ElementData, ScanOptions)
- `src/fileGeneration/detectPatterns.ts` - Pattern detection logic

1. **Scanner Quick Win #1: Pattern Ordering** (4 hours)
   - **File:** `src/scanner/scanner.ts` lines 18-44 (LANGUAGE_PATTERNS)
   - Reorder LANGUAGE_PATTERNS by TYPE_PRIORITY (constant → component → hook → class → method → function)
   - Add `exclusive` flag for short-circuit matching
   - **Impact:** 15% performance improvement

2. **Scanner Quick Win #2: Configuration Presets** (6 hours)
   - **File:** `src/scanner/scanner.ts` (new section)
   - Define 7 presets: nextjs, react, python, monorepo, go, rust, java
   - Implement auto-detection logic (package.json, pyproject.toml, Cargo.toml, etc.)
   - Add `preset` parameter to ScanOptions in `types.ts`
   - **Impact:** 10x easier configuration

3. **Scanner Quick Win #3: Structured Error Reporting** (8 hours)
   - **File:** `src/scanner/types.ts` (new ScanError interface)
   - **File:** `src/scanner/scanner.ts` lines 552 (error handling)
   - Create ScanError interface with type, severity, file, line, suggestion
   - Add suggestion database for common errors (encoding, permissions, syntax)
   - Return errors array alongside elements (non-throwing)
   - **Impact:** 3x faster debugging

4. **Scanner Quick Win #4: Python Pattern Expansion** (4 hours)
   - **File:** `src/scanner/scanner.ts` lines 18-44 (Python patterns)
   - Add decorators pattern: `/@([a-zA-Z0-9_]+)/g`
   - Add properties pattern: `/@property\s+def\s+([a-zA-Z0-9_]+)/g`
   - Add static methods pattern: `/@staticmethod\s+def\s+([a-zA-Z0-9_]+)/g`
   - Add nested classes pattern: `/^\s{4,}class\s+([a-zA-Z0-9_]+)/gm`
   - **Impact:** +30% Python coverage

**Deliverables:**
- 4 quick wins implemented in coderef-core package (22 hours total)
- Scanner performance +15% faster
- Configuration time 15-30 min → 30 sec
- Python coverage 3 patterns → 7 patterns

**Success Metrics:**
- Scan speed improvement: +15%
- Configuration time: 30 seconds (vs 15-30 minutes)
- Python elements detected: +30-40%
- Error resolution time: 20 min → 5-7 min

---

### Phase 2: Workflow & Docs Integration (Week 3-4)

**Lead Agents:** coderef-workflow, coderef-docs

#### coderef-workflow Tasks

1. **Update planning analyzer** (`planning_analyzer.py`)
   - **Current:** Reads 5 separate files (index.json, patterns.json, coverage.json, complexity.json, drift.json)
   - **Proposed:** Single `coderef_context` MCP call
   - **Change:** Modify `analyze_project_for_planning()` function (lines 120-180)

   ```python
   # OLD (5 file reads):
   index = self._load_coderef_index()
   patterns = self._load_coderef_patterns()
   coverage = self._load_coderef_coverage()
   complexity = self._load_coderef_complexity()
   drift = self._load_coderef_drift()

   # NEW (1 MCP call):
   context = await call_mcp_tool("coderef_context", {
       "project_path": project_path,
       "include_diagrams": True,
       "include_patterns": True,
       "include_complexity": True
   })
   ```

2. **Update AI planning prompt** (`planning_generator.py`)
   - Add new context fields to 190-line agent prompt:
     - `architecture_diagram` (Mermaid)
     - `visual_architecture` (diagram-wrapped.md)
     - `complexity_hotspots` (high-complexity files)
     - `documentation_summary` (generated docs)
   - **Change:** Modify `_build_agent_prompt()` function (lines 176-365)

3. **Test enhanced planning workflow:**
   - Create test workorder with complex feature
   - Verify plan.json includes file-specific tasks with line numbers
   - Compare plan quality: baseline vs enhanced context
   - Measure planning speed improvement

**Deliverables:**
- Updated `planning_analyzer.py` with single MCP call
- Enhanced AI planning prompt with new context fields
- Test results showing 6x faster planning
- Richer `plan.json` files with better architectural understanding

**Success Metrics:**
- Planning speed: 6x faster (0.3s → 0.05s for context gathering)
- Plan quality: File-specific tasks with exact line numbers
- Context completeness: 40% → 95%

#### coderef-docs Tasks

1. **Update foundation docs generation** (`docs_handlers/foundation_docs.py`)
   - Replace basic file scanning with enhanced scanner
   - Add `coderef_context` call for architecture overview
   - Use populated `patterns.json` for coding conventions
   - Use `complexity.json` for identifying critical modules
   - **Files affected:**
     - `generate_foundation_docs()` handler
     - `generate_individual_doc()` for ARCHITECTURE.md, API.md

2. **Enhance establish_standards** (already has MCP integration)
   - Verify it uses enhanced scanner outputs
   - Test pattern quality improvement (55% → 80%)
   - Validate standards docs accuracy

3. **Test enhanced doc generation:**
   - Generate foundation docs with enhanced scanner
   - Compare accuracy: interfaces detected, decorators captured
   - Measure generation speed with parallel scanning
   - Validate UDS compliance

**Deliverables:**
- Updated `generate_foundation_docs` using enhanced scanner
- Improved ARCHITECTURE.md with complete element detection
- Enhanced API.md with full function signatures and relationships
- Test results showing accuracy improvements

**Success Metrics:**
- Element detection accuracy: 85% → 95%
- Python elements in docs: +30% coverage
- Generation speed: 3-5x faster (parallel processing)
- Standards quality: 55% → 80% (MCP patterns)

#### Integration Testing

**coderef-testing Tasks:**
1. Create test workorders in multiple languages (TS, Python, Go)
2. Run planning workflow with enhanced context
3. Generate foundation docs with enhanced scanner
4. Compare before/after metrics
5. Validate integration points between all 4 servers

**Deliverables:**
- Integration test suite (10+ test cases)
- Performance benchmarks (before/after)
- Validation report with pass/fail metrics

---

### Phase 3: Scanner Accuracy & Performance (Week 5-10)

**Lead Agents:** coderef-dashboard, coderef-testing

#### Week 5-7: Accuracy Improvements

**Tasks:**

1. **P1.1: Hybrid AST + Regex Approach** (2-3 days implementation + 1-2 days testing)
   - Add `useAST: boolean` to ScanOptions (default: false)
   - Extend existing `js-call-detector.ts` (acorn parser) to extract element types
   - Detect interfaces, type aliases, decorators, class properties, arrow methods
   - Fallback to regex on AST parse errors
   - **Impact:** 85% → 95% accuracy for TypeScript/JavaScript

2. **P1.2: Context-Aware Comment Filtering** (1-2 days implementation + 1 day testing)
   - Add `skipComments: 'smart' | 'basic' | false` to ScanOptions
   - Use acorn's `onComment` callback for accurate comment detection
   - Track string/template/regex context to avoid false positives
   - Preserve `'basic'` as default for backward compatibility
   - **Impact:** Reduce false negatives by 10-15%

3. **P1.3: Extended Python Patterns** (4-6 hours implementation + 4 hours testing)
   - Already done in Phase 1 Quick Win #4
   - Additional testing with comprehensive Python fixtures

**Deliverables:**
- Hybrid AST + Regex scanner (95% accuracy)
- Smart comment filtering (10% fewer false negatives)
- Test suites with 20+ TypeScript/JavaScript fixtures
- Test suites with 10+ Python fixtures

**Success Metrics:**
- TypeScript/JavaScript accuracy: 85% → 95%
- False negatives: 15% → 5%
- Python coverage: +30% (already achieved in Phase 1)

#### Week 8-10: Performance Improvements

**Tasks:**

1. **P2.4: Parallel File Processing** (4-5 days implementation + 2 days testing)
   - Use Node.js worker threads (4-8 workers, configurable)
   - Batch files into chunks (100 files per worker)
   - Aggregate results via message passing
   - Graceful fallback to sequential on errors
   - Add `parallel`, `workers`, `batchSize` to ScanOptions
   - **Impact:** 3-5x faster scanning

2. **P2.5: Content-Aware Caching with LRU** (2 days implementation + 1 day testing)
   - Replace global Map with `lru-cache` package
   - Add content hashing (SHA-256 of first 1KB)
   - Implement TTL (1 hour default) and LRU eviction
   - Cap at 1000 entries (~50MB)
   - **Impact:** Eliminate false cache hits, cap memory at 50MB

3. **P2.6: Pattern Execution Optimization** (already done in Phase 1 Quick Win #1)
   - Verify 15% performance improvement persists
   - Additional optimization for exclusive matching

**Deliverables:**
- Worker thread pool implementation
- LRU cache with content hashing
- Performance benchmarks (sequential vs parallel)
- Memory usage profiling

**Success Metrics:**
- Scan speed (500 files): 1185ms → 300-400ms
- Scan speed (5000 files): 20-30s → 5-8s
- Memory usage: Unbounded → 50MB cap
- Cache hit rate: 60% → 80%

#### Re-Integration Testing

**coderef-workflow + coderef-docs Tasks:**
1. Re-run planning workflows with accurate scanner
2. Re-generate foundation docs with fast scanner
3. Measure end-to-end improvements
4. Validate all integration points still working

**Deliverables:**
- Complete integration validation report
- End-to-end performance metrics
- Production readiness assessment

---

## Agent Roles Summary

### Primary Implementation
- **coderef-context** - Enhance MCP tools to expose 100% of `.coderef/` resources (Phase 1)
- **coderef-dashboard** - Implement scanner improvements: quick wins, accuracy, performance (Phase 1, 3)
- **coderef-workflow** - Integrate enhanced context into planning workflows (Phase 2)
- **coderef-docs** - Integrate enhanced scanner/context into doc generation (Phase 2)

### Testing & Validation
- **coderef-testing** - Create test fixtures, run benchmarks, performance profiling (Phase 2, 3)
- **papertrail** - Validate schemas, outputs, UDS compliance (All phases)

### Coordination & Support
- **coderef-assistant** - Track cross-project handoffs and dependencies (All phases)
- **coderef-personas** - Provide specialized expertise for each agent (All phases)
- **coderef-system** - System-level orchestration and conflict resolution (All phases)

---

## Output Files Structure

### Phase 1 Outputs
```
C:\Users\willh\.mcp-servers\coderef\sessions\scanner-context-enhancement\
├── orchestrator-phase1-report.md
├── coderef-context-phase1-output.json
├── coderef-dashboard-phase1-output.md
├── papertrail-phase1-validation.json
└── phase1-integration-test-results.md
```

### Phase 2 Outputs
```
C:\Users\willh\.mcp-servers\coderef\sessions\scanner-context-enhancement\
├── orchestrator-phase2-report.md
├── coderef-workflow-phase2-output.md
├── coderef-docs-phase2-output.md
├── coderef-testing-phase2-integration-tests.json
└── phase2-integration-validation.md
```

### Phase 3 Outputs
```
C:\Users\willh\.mcp-servers\coderef\sessions\scanner-context-enhancement\
├── orchestrator-phase3-report.md
├── coderef-dashboard-phase3-accuracy-output.md
├── coderef-dashboard-phase3-performance-output.json
├── coderef-testing-phase3-benchmarks.json
├── coderef-workflow-phase3-reintegration.md
├── coderef-docs-phase3-reintegration.md
└── phase3-final-validation.md
```

### Final Synthesis
```
C:\Users\willh\.mcp-servers\coderef\sessions\scanner-context-enhancement\
└── orchestrator-final-synthesis.md
```

---

## Success Metrics Summary

### Context Enhancement (Phase 1)
| Metric | Baseline | Target | Status |
|--------|----------|--------|--------|
| Tool calls (planning) | 6 calls | 1 call | Phase 1 |
| Context quality | 40% | 95% | Phase 1 |
| Response time | 0.3s | 0.05s | Phase 1 |
| Scanner performance | Baseline | +15% | Phase 1 |
| Python coverage | 3 patterns | 7 patterns | Phase 1 |

### Integration Benefits (Phase 2)
| Metric | Baseline | Target | Status |
|--------|----------|--------|--------|
| Planning speed | 0.3s context | 0.05s context | Phase 2 |
| Plan quality | Generic tasks | File-specific + line numbers | Phase 2 |
| Docs accuracy | 85% | 95% | Phase 2 |
| Standards quality | 55% (regex) | 80% (MCP) | Phase 2 |

### Scanner Improvements (Phase 3)
| Metric | Baseline | Target | Status |
|--------|----------|--------|--------|
| TS/JS accuracy | 85% | 95% | Phase 3 |
| Python elements | +30% | (achieved Phase 1) | Phase 1 |
| Scan speed (500 files) | 1185ms | 300-400ms | Phase 3 |
| Scan speed (5000 files) | 20-30s | 5-8s | Phase 3 |
| Memory usage | Unbounded | 50MB cap | Phase 3 |
| False negatives | 15% | 5% | Phase 3 |

---

## Key Integration Points

### coderef-context → coderef-workflow
**Before Phase 1:**
- Workflow reads 5 separate `.coderef/` files
- No diagrams, no generated docs, no complexity hotspots
- 40% context quality

**After Phase 2:**
- Workflow calls `coderef_context` once
- Gets diagrams, patterns, docs, complexity automatically
- 95% context quality, 6x faster

### coderef-core (scanner in dashboard) → coderef-docs
**Before Phase 1:**
- Docs use basic file scanning (85% accuracy)
- Missing interfaces, decorators, Python patterns
- Slow sequential processing

**After Phase 2 + Phase 3:**
- Docs use enhanced scanner from coderef-core (95% accuracy)
- Detects all TypeScript/Python constructs
- 3-5x faster with parallel processing

### coderef-context → coderef-docs
**Before Phase 1:**
- Docs don't use `coderef_context` for foundation docs
- Manual file scanning for architecture overview

**After Phase 2:**
- Docs call `coderef_context` for architecture section
- Pre-digested diagrams, patterns, complexity in ARCHITECTURE.md

---

## Dependencies & Prerequisites

### Required for Phase 1
- coderef-context MCP server (Python) - `C:\Users\willh\.mcp-servers\coderef-context\`
- coderef-core scanner (TypeScript) - `C:\Users\willh\Desktop\coderef-dashboard\packages\coderef-core\`
- `.coderef/` directory structure exists in projects
- Access to MCP tool communication layer

### Required for Phase 2
- Phase 1 complete (enhanced context + quick wins)
- coderef-workflow MCP server (Python)
- coderef-docs MCP server (Python)
- Test projects with multiple languages

### Required for Phase 3
- Node.js ≥16.0 (worker threads)
- Multi-core CPU (parallel processing)
- 512MB+ RAM (large project scans)
- `lru-cache` npm package
- `acorn` npm package (already integrated)

---

## Risk Assessment

### High Risk Items
**P2.4: Parallel File Processing (Phase 3)**
- **Risk:** Worker thread crashes, serialization issues
- **Mitigation:** Graceful fallback to sequential, comprehensive error handling
- **Testing:** 1000+ file fixtures, worker crash scenarios

**Integration Breakage (Phase 2)**
- **Risk:** Enhanced context changes break workflow/docs
- **Mitigation:** Backward compatibility, comprehensive integration tests
- **Testing:** Run existing workorder workflows, validate outputs

### Medium Risk Items
**P1.1: Hybrid AST + Regex (Phase 3)**
- **Risk:** AST parsing failures, performance degradation
- **Mitigation:** Regex fallback, optional opt-in (default: false)
- **Testing:** 20+ TypeScript fixtures, performance benchmarks

**Phase 2 Dependencies**
- **Risk:** Phase 1 incomplete or buggy
- **Mitigation:** Comprehensive Phase 1 validation before starting Phase 2
- **Testing:** Integration test suite must pass 95%+

### Low Risk Items
**Quick Wins (Phase 1)**
- **Risk:** Minimal (isolated improvements)
- **Mitigation:** Independent testing per improvement
- **Testing:** 4 separate test suites

---

## Timeline & Resource Allocation

### Phase 1: Core Enhancements
- **Duration:** 2 weeks (Week 1-2)
- **Effort:** ~40 hours implementation + 20 hours testing
- **Agents:** coderef-context (lead), coderef-dashboard (lead), papertrail (validation)

### Phase 2: Integration
- **Duration:** 2 weeks (Week 3-4)
- **Effort:** ~60 hours implementation + 30 hours testing
- **Agents:** coderef-workflow (lead), coderef-docs (lead), coderef-testing (lead), papertrail (validation)

### Phase 3: Accuracy & Performance
- **Duration:** 6 weeks (Week 5-10)
- **Effort:** ~120 hours implementation + 60 hours testing
- **Agents:** coderef-dashboard (lead), coderef-testing (lead), coderef-workflow (reintegration), coderef-docs (reintegration)

**Total:** 10 weeks, ~220 hours implementation, ~110 hours testing

---

## Next Steps

1. **Review this document** - Confirm session structure and scope
2. **Create session files:**
   - `communication.json` - Agent roster with 3-phase tracking
   - `instructions.json` - Orchestrator + agent instructions with integration focus
3. **Initialize session directory:**
   - `C:\Users\willh\.mcp-servers\coderef\sessions\scanner-context-enhancement\`
4. **Begin Phase 1** - Core enhancements (context + scanner quick wins)

---

**Document Status:** ✅ Ready for session file generation
**Last Updated:** 2026-01-14
