# CodeRef Scripts Reference

**Complete inventory of all scripts in the CodeRef ecosystem**

**Last Updated:** 2025-12-31

---

## Structure Creators

| Script | Description | Location |
|--------|-------------|----------|
| **create-coderef-structure.py** | Create `coderef/` directory structure (workorder/, archived/, foundation/, user/, standards/) | `assistant/scripts/` |
| **scan-all.py** | Generate minimal `.coderef/` structure (2-3 files: index.json, context.md) | `coderef-system/scripts/` |
| **populate-coderef.py** | Generate complete `.coderef/` structure (all 16 files: reports/, diagrams/, exports/) | `coderef-system/scripts/` |

---

## Documentation Generators

| Script | Description | Location |
|--------|-------------|----------|
| **generate_docs.py** | Generate foundation docs from `.coderef/` data (README, ARCHITECTURE, API, SCHEMA, COMPONENTS) | `.coderef/` (per-project) |
| **foundation_generator.py** | Generate foundation docs (traditional approach - reads source files directly) | `coderef-workflow/generators/` & `coderef-docs/generators/` |
| **coderef_foundation_generator.py** | Generate foundation docs (hybrid approach - uses `.coderef/` data + source analysis) | `coderef-workflow/generators/` & `coderef-docs/generators/` |
| **enhance-standards.py** | Generate UI/behavior/UX standards using `.coderef/` data (COMPONENT-INDEX, UI-STANDARDS, BEHAVIOR-STANDARDS, UX-PATTERNS) | `coderef-system/scripts/` |
| **standards_generator.py** | Generate standards (MCP tool integration with .coderef/ fast path) | `coderef-workflow/generators/` |
| **diagram-generator.py** | Generate visual diagrams from codebase structure (Mermaid/DOT) | `coderef-system/scripts/` |
| **mermaid_formatter.py** | Format Mermaid diagrams | `coderef-workflow/generators/` |

---

## Data Processing

| Script | Description | Location |
|--------|-------------|----------|
| **parse_coderef_data.py** | Preprocess large index files (summarizes .coderef/index.json for large codebases) | `coderef-system/packages/` (149 LOC) & `coderef-system/scripts/` (492 LOC) |
| **extract-context.py** | Extract context from files | `coderef-system/scripts/` |
| **extractors.py** | Extract data from existing documentation | `coderef-docs/` |
| **export_processor.py** | Export coderef data to JSON/JSON-LD/Mermaid formats | `coderef-context/processors/` |

---

## Validation & Quality

| Script | Description | Location |
|--------|-------------|----------|
| **validate-docs.py** | Validate generated documentation (completeness, accuracy, cross-refs, broken links, markdown, diagrams) | `coderef-system/scripts/` |
| **validate-stubs.py** | Validate stub.json files against schema | `assistant/` |
| **plan_validator.py** | Validate implementation plans (0-100 score) | `coderef-workflow/generators/` |
| **plan_format_validator.py** | Validate plan format | `coderef-workflow/helpers/` |
| **schema_validator.py** | Validate schemas | `coderef-workflow/helpers/` |
| **validation.py** | General validation helpers | `coderef-workflow/helpers/` |

---

## Planning & Workflow

| Script | Description | Location |
|--------|-------------|----------|
| **planning_analyzer.py** | Analyze project for planning (discovers foundation docs, standards, patterns) | `coderef-workflow/generators/` |
| **planning_generator.py** | Generate 10-section implementation plans | `coderef-workflow/generators/` |
| **quick_plan_generator.py** | Quick planning workflow | `coderef-personas/src/generators/` |
| **interactive_plan_executor.py** | Execute plans interactively | `coderef-personas/src/executors/` |
| **plan_execution_tracker.py** | Track plan execution progress | `coderef-personas/src/trackers/` |
| **changelog_generator.py** | Auto-detect git changes and generate changelog entries | `coderef-workflow/generators/` |
| **quickref_generator.py** | Interactive quickref workflow (interview-based guide generation) | `coderef-workflow/generators/` |
| **handoff_generator.py** | Generate agent handoff context files | `coderef-workflow/generators/` |
| **risk_generator.py** | Risk assessment across 5 dimensions | `coderef-workflow/generators/` |
| **audit_generator.py** | Audit all plans in workorder/ directory | `coderef-workflow/generators/` |
| **consistency_checker.py** | Check code against established standards | `coderef-workflow/generators/` |
| **review_formatter.py** | Generate plan review reports | `coderef-workflow/generators/` |
| **features_inventory_generator.py** | Generate feature inventory from workorder/ and archived/ | `coderef-workflow/generators/` |
| **todo_list_generator.py** | Generate TodoWrite task lists from plans | `coderef-personas/src/generators/` |

---

## Personas & Agents

| Script | Description | Location |
|--------|-------------|----------|
| **persona_manager.py** | Persona activation and management | `coderef-personas/src/` |
| **persona_generator.py** | Create custom personas | `coderef-personas/src/` |

---

## Testing

| Script | Description | Location |
|--------|-------------|----------|
| **test_runner.py** | Run tests and analyze results | `coderef-testing/src/` |
| **framework_detector.py** | Detect testing framework (pytest/jest/vitest/etc) | `coderef-testing/src/` |
| **result_analyzer.py** | Parse test results | `coderef-testing/src/` |
| **proof_generator.py** | Generate completion proof | `coderef-testing/src/` |
| **test_scan_all.py** | Test suite for scan-all.py | `coderef-system/scripts/` |

---

## Build & Utilities

| Script | Description | Location |
|--------|-------------|----------|
| **build-exe.py** | Build standalone executable using PyInstaller | `coderef-system/scripts/` |
| **update_lloyd.py** | Update Lloyd persona | `coderef-personas/build_scripts/` |
| **build_phase2.py** | Build phase 2 | `coderef-personas/build_scripts/` |
| **build_phase3.py** | Build phase 3 | `coderef-personas/build_scripts/` |
| **create_research_scout.py** | Create research scout persona | `coderef-personas/build_scripts/` |
| **scan-emojis.py** | Scan for emoji usage in codebase | `coderef-system/scripts/` |
| **remove-emojis.py** | Remove emoji characters from files | `assistant/scripts/` |
| **scan-gui.py** | GUI wrapper for CodeRef scanner | `coderef-system/scripts/` |
| **scan-all-fixed.py** | Fixed version of scan-all.py | `coderef-system/scripts/` |
| **cli_utils.py** | CLI helper utilities | `coderef-docs/` |

---

## MCP Server Core

| Script | Description | Location |
|--------|-------------|----------|
| **server.py** (coderef-context) | Code Intelligence MCP server entry point | `coderef-context/` |
| **server.py** (coderef-workflow) | Planning & Orchestration MCP server entry point | `coderef-workflow/` |
| **server.py** (coderef-docs) | Documentation MCP server entry point | `coderef-docs/` |
| **server.py** (coderef-personas) | Expert Agents MCP server entry point | `coderef-personas/` |
| **server.py** (coderef-testing) | Test Automation MCP server entry point | `coderef-testing/` |
| **tool_handlers.py** | All 28 MCP tool implementations | `coderef-workflow/` |

---

## Helpers & Support

| Script | Description | Location |
|--------|-------------|----------|
| **base_generator.py** | Base class for all generator scripts | `coderef-workflow/generators/` |
| **handler_helpers.py** | Handler helper functions | `coderef-workflow/helpers/` |
| **handler_decorators.py** | Handler decorators | `coderef-workflow/helpers/` |
| **uds_helpers.py** | Universal Documentation Standards helpers | `coderef-workflow/helpers/` |
| **logger_config.py** | Logging configuration | `coderef-workflow/helpers/` |
| **error_responses.py** | Error response handling | `coderef-workflow/helpers/` |
| **constants.py** | Constants definitions | `coderef-workflow/helpers/` |

---

**Total Scripts:** 50+

**Base Paths:**
- `assistant/` = `C:\Users\willh\Desktop\assistant\`
- `coderef-system/` = `C:\Users\willh\Desktop\projects\coderef-system\`
- `coderef-context/` = `C:\Users\willh\.mcp-servers\coderef-context\`
- `coderef-workflow/` = `C:\Users\willh\.mcp-servers\coderef-workflow\`
- `coderef-docs/` = `C:\Users\willh\.mcp-servers\coderef-docs\`
- `coderef-personas/` = `C:\Users\willh\.mcp-servers\coderef-personas\`
- `coderef-testing/` = `C:\Users\willh\.mcp-servers\coderef-testing\`
