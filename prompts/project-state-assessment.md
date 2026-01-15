# MISSION: Project State Assessment

You are conducting a comprehensive analysis of THIS PROJECT to generate a factual State of the Project report. The project has been scanned with coderef-scanner, producing `.coderef/index.json` and `.coderef/graph.json` files.

## Your Task

Analyze the current project directory and generate an objective, data-driven report documenting the current state of the project. Focus on measurable facts and observable conditions. This is a single-project assessment, not a portfolio comparison.

## Analysis Process

### 1. Pre-Analysis: Verify Data Quality

**CRITICAL - Check for Virtual Environment Pollution (Python projects only):**

Before analyzing Python projects, verify `.coderef/index.json` does NOT include virtual environment files (`.venv/`, `venv/`, `env/`).

If virtual environment detected:
- Flag as **Data Quality Issue** in the report
- Add asterisk (*) to element counts
- Include note: "Element count includes virtual environment dependencies"
- Estimate actual project size separately by excluding .venv paths

**Signs of .venv pollution:**
- Element counts > 100,000
- Paths containing `.venv/`, `venv/`, `site-packages/`

### 2. Extract Git History Data

Run these git commands in the project directory to capture complete history:

```bash
# Get first commit date (project start date)
git log --reverse --format="%ai" | head -1

# Get total commit count
git log --oneline | wc -l

# Get commit activity (last 30 days)
git log --since="30 days ago" --oneline | wc -l

# Get commit activity (last 90 days)
git log --since="90 days ago" --oneline | wc -l

# Get contributors list
git shortlog -sn

# Get last commit details
git log -1 --format="%ai | %s"

# Get current branch
git branch --show-current

# Get uncommitted changes count
git status --short | wc -l
```

**If git commands fail:** Mark as "Unknown" and note "Git history unavailable"

### 3. Use coderef-context MCP Tools

**For each major component/file identified:**

```javascript
// Get complexity metrics for critical files
mcp__coderef-context__coderef_complexity({
  project_path: "/path/to/project",
  element: "MainComponent"  // Replace with actual component name
})

// Analyze dependency patterns
mcp__coderef-context__coderef_query({
  project_path: "/path/to/project",
  query_type: "depends-on",
  target: "CoreService"  // Replace with actual service name
})

// Discover architectural patterns
mcp__coderef-context__coderef_patterns({
  project_path: "/path/to/project",
  limit: 20
})

// Find test coverage gaps
mcp__coderef-context__coderef_coverage({
  project_path: "/path/to/project",
  format: "detailed"
})
```

**Run complexity analysis on at least:**
- Main entry point files
- Top 3 most complex files (by LOC or import count)
- Core business logic files

### 4. Read Critical Files

- README.md or package.json (project description, tech stack)
- CLAUDE.md or documentation (if exists)
- .coderef/index.json (code inventory - verify no .venv pollution)
- .coderef/graph.json (dependency graph)

### 5. Document Observable Facts

- What functionality exists (based on code analysis)
- What tests exist
- What documentation exists
- What dependencies are present
- What patterns are implemented

### 6. Quantify Effort Indicators

- Count of TODO/FIXME comments
- Count of incomplete functions (empty or stub implementations)
- Count of failing tests (if test suite exists)
- Count of outdated dependencies

## Output Format

Generate **PROJECT-STATE-ASSESSMENT.md** in the project's `.coderef/` directory with this structure:

---

# Project State Assessment: [Project Name]

**Analysis Date:** [Date]
**Project Path:** [Absolute path]
**Project Type:** [Web App / CLI Tool / Library / etc.]

## Table of Contents

1. [What This Project Is](#1-what-this-project-is)
2. [Quick Health Check](#2-quick-health-check)
3. [What It Can Do Right Now](#3-what-it-can-do-right-now)
4. [Executive Summary](#4-executive-summary)
5. [Codebase Metrics](#5-codebase-metrics)
6. [Feature Implementation Status](#6-feature-implementation-status)
7. [Testing Status](#7-testing-status)
8. [Documentation Status](#8-documentation-status)
9. [Architecture & Patterns](#9-architecture--patterns)
10. [Version Control Status](#10-version-control-status)
11. [Development Environment](#11-development-environment)
12. [Code Quality Indicators](#12-code-quality-indicators)
13. [Project State Summary](#13-project-state-summary)

---

## 1. What This Project Is

**In Plain English:**

[2-3 paragraph description written for non-technical stakeholders. Answer: What does this do? Who is it for? What problem does it solve?]

Example:
> "This is a web application that helps small businesses track their inventory in real-time. Store owners can scan barcodes, check stock levels, and get alerts when items are running low. It's built for retail shops that need simple, reliable inventory management without complex enterprise software."

**Project Type:** [Web App / Mobile App / CLI Tool / Library / API / Desktop App / etc.]

**Target Users:** [Who uses this? Developers? End users? Internal teams?]

**Primary Purpose:** [One sentence - what's the main goal?]

**Current Stage:** [Prototype / MVP / Beta / Production / Abandoned / Maintenance Mode]

---

## 2. Quick Health Check

### Overall Health Score: [X]/100

**Scoring Breakdown:**

| Category | Score | Rating | Details |
|----------|-------|--------|---------|
| **Code Completeness** | [X]/25 | ⭐⭐⭐⭐☆ | [Brief explanation] |
| **Code Quality** | [X]/20 | ⭐⭐⭐☆☆ | [Brief explanation] |
| **Testing** | [X]/20 | ⭐⭐☆☆☆ | [Brief explanation] |
| **Documentation** | [X]/15 | ⭐⭐⭐⭐⭐ | [Brief explanation] |
| **Active Maintenance** | [X]/20 | ⭐⭐⭐⭐☆ | [Brief explanation] |

**Health Score Calculation:**
- **Code Completeness (25 pts):** Based on implemented features vs TODO comments ratio
- **Code Quality (20 pts):** Based on complexity scores, linting setup, error handling
- **Testing (20 pts):** Based on test coverage % and test file count
- **Documentation (15 pts):** Based on README quality, inline comments, API docs
- **Active Maintenance (20 pts):** Based on recent commits, contributor activity

**Rating Scale:**
- ⭐⭐⭐⭐⭐ (90-100): Excellent
- ⭐⭐⭐⭐☆ (70-89): Good
- ⭐⭐⭐☆☆ (50-69): Fair
- ⭐⭐☆☆☆ (30-49): Needs Work
- ⭐☆☆☆☆ (0-29): Critical Issues

### Traffic Light Status

| Aspect | Status | What This Means |
|--------|--------|-----------------|
| **Can I Run This?** | 🟢 / 🟡 / 🔴 | [Setup complexity - easy/medium/hard] |
| **Is It Actively Developed?** | 🟢 / 🟡 / 🔴 | [Commits in last 30 days: N] |
| **Is It Tested?** | 🟢 / 🟡 / 🔴 | [Test coverage: X%] |
| **Is It Documented?** | 🟢 / 🟡 / 🔴 | [README + docs quality] |
| **Is It Production-Ready?** | 🟢 / 🟡 / 🔴 | [Based on completeness + quality] |

**Legend:**
- 🟢 **Green:** Good to go
- 🟡 **Yellow:** Usable but needs attention
- 🔴 **Red:** Not ready / needs significant work

---

## 3. What It Can Do Right Now

### Functional Features (Working)

**Core Capabilities:**

1. **[Feature Name]** - ✅ Fully Working
   - What it does: [Plain language description]
   - How complete: [X]%
   - Evidence: [File paths or component names]

2. **[Feature Name]** - ✅ Fully Working
   - What it does: [Plain language description]
   - How complete: [X]%
   - Evidence: [File paths or component names]

3. **[Feature Name]** - ⚠️ Partially Working
   - What it does: [Plain language description]
   - How complete: [X]%
   - What's missing: [Specific gaps]
   - Evidence: [TODO comments or missing files]

### Feature Completeness Ranking

| Rank | Feature | Completeness | Status | Priority to Finish |
|------|---------|--------------|--------|-------------------|
| 1 | [Feature] | 95% | ✅ Working | Low |
| 2 | [Feature] | 80% | ⚠️ Partial | Medium |
| 3 | [Feature] | 60% | ⚠️ Partial | High |
| 4 | [Feature] | 30% | 🔴 Incomplete | High |
| 5 | [Feature] | 10% | 🔴 Stub Only | Low |

**Completion Status:**
- ✅ **Working (80-100%):** Feature is usable and mostly complete
- ⚠️ **Partial (40-79%):** Feature exists but has significant gaps
- 🔴 **Incomplete (0-39%):** Feature is stubbed or barely started

### What's Missing (Top Priority Gaps)

1. **[Missing Feature/Component]**
   - Why it matters: [Impact on usability]
   - Effort to complete: [Hours/Days/Weeks estimate]
   - Blockers: [Dependencies or unknowns]

2. **[Missing Feature/Component]**
   - Why it matters: [Impact on usability]
   - Effort to complete: [Hours/Days/Weeks estimate]
   - Blockers: [Dependencies or unknowns]

---

## 4. Executive Summary

**Project Name:** [Name]
**Primary Language:** [Language]
**Tech Stack:** [Languages, frameworks, key dependencies with versions]
**Current Status:** [Active development / Inactive / Maintenance mode]
**Last Activity:** [Date of last commit]

**Key Metrics:**
- Total Lines of Code: [N]
- Total Components/Modules: [N]
- Test Files: [N]
- Test Coverage: [X]% or Unknown
- TODO/FIXME Comments: [N]
- Git Commits: [N]
- Contributors: [N]

---

## 5. Codebase Metrics

**Size:**
- Total Files: [N]
- Total Lines of Code: [N]
- Components/Classes/Modules: [N]
- Functions: [N]

**Complexity:**
- Average Cyclomatic Complexity: [N] (use coderef_complexity tool)
- High Complexity Functions (>10): [List names and scores]
- Maximum Complexity: [N] in [function/file name]
- **Top 3 Most Complex Files:**
  - [file]: Complexity score [N]
  - [file]: Complexity score [N]
  - [file]: Complexity score [N]

**Dependencies:**
- Total Dependencies: [N]
- Outdated Dependencies: [N]
- Security Vulnerabilities: [N] (if detectable)
- Peer Dependencies: [List]

## 6. Feature Implementation Status

**Implemented Features:**
[List based on code analysis - routes, components, services, etc.]
- [Feature name]: [What exists - files, functions, components]
- [Feature name]: [What exists]

**Partially Implemented Features:**
[Features with TODO/FIXME or stub implementations]
- [Feature name]: [What's missing or incomplete]

**Identified Gaps:**
[Based on TODO comments, stub functions, missing tests]
- [Gap description]: [Evidence - file:line]

## 7. Testing Status

**Test Files:** [N]
**Test Suites:** [N]
**Test Cases:** [N]
**Coverage:** [X]% (or "Unknown" if not measurable)

**Test Distribution:**
- Unit Tests: [N]
- Integration Tests: [N]
- E2E Tests: [N]

**Untested Components:** [List components with no associated tests]

## 8. Documentation Status

**README:** [Yes/No] - [Length in lines if exists]
**CLAUDE.md:** [Yes/No]
**API Documentation:** [Yes/No]
**Inline Comments:** [% of functions with comments]
**Architecture Docs:** [Yes/No]

**Documentation Completeness:**
- Setup Instructions: [Present/Missing]
- Usage Examples: [Present/Missing]
- API Reference: [Present/Missing]
- Contribution Guidelines: [Present/Missing]

## 9. Architecture & Patterns

**Detected Patterns:**
[From coderef_patterns tool]
- [Pattern name]: [Usage count]

**Core Systems Present:**
[Based on directory structure and code analysis]
- [System name]: [Status - Implemented/Partial/Missing]
  - Files: [List]
  - Entry points: [List]

**External Integrations:**
[APIs, services, databases]
- [Integration name]: [Config present? Yes/No]

## 10. Version Control Status

**Git Repository:** [Yes/No]
**Total Commits:** [N] (use: git log --oneline | wc -l)
**Contributors:** [N] (use: git shortlog -sn)
  - [Contributor name]: [N] commits
  - [Contributor name]: [N] commits
**Last Commit:** [Date] (use: git log -1 --format="%ai")
**Last Commit Message:** [Message]
**Active Branch:** [Branch name] (use: git branch --show-current)
**Uncommitted Changes:** [Yes/No] - [N] files modified (use: git status --short | wc -l)

**Commit Activity:**
- Last 30 days: [N] commits (use: git log --since="30 days ago" --oneline | wc -l)
- Last 90 days: [N] commits (use: git log --since="90 days ago" --oneline | wc -l)
- First commit: [Date] (use: git log --reverse --format="%ai" | head -1)

## 11. Development Environment

**Configuration Files Present:**
- package.json / requirements.txt / etc: [Yes/No]
- .env / config files: [Yes/No]
- Docker / containerization: [Yes/No]
- CI/CD config: [Yes/No]

**Build System:**
- Build tool: [Tool name or "None detected"]
- Scripts defined: [List from package.json or equivalent]

**Development Dependencies:** [N]

## 12. Code Quality Indicators

**TODO/FIXME Comments:** [N]
**Sample TODOs:**
- [file:line] - [TODO text]
- [file:line] - [TODO text]

**Linting Configuration:** [Present/Missing]
**Formatting Configuration:** [Present/Missing]

**Empty or Stub Functions:** [N]
**Functions with No Error Handling:** [N or "Not analyzed"]

## 13. Project State Summary

**Observable Characteristics:**
- Project started: [Date of first commit - use git log --reverse]
- Active development period: [First commit date] to [Last commit date]
- Inactive since: [Date of last commit]
- Total development time: [Days/months between first and last commit]
- Commit frequency: [Average commits per month]

**Functional Components:**
[What actually works based on code completeness]
- [Component/feature]: [Evidence it's complete]

**Incomplete Components:**
[What has gaps based on TODOs, stubs, missing tests]
- [Component/feature]: [Evidence it's incomplete]

**Critical Files:**
[Most complex or most imported/depended upon]
- [file]: [Complexity score, import count]

---

## Analysis Guidelines

1. **Report only observable facts:** File counts, line numbers, commit dates, test results
2. **Quote TODO comments directly:** Don't interpret intent, show what's written
3. **Use coderef metrics:** Ground all statements in tool outputs or file reads
4. **List, don't summarize:** When listing features/gaps, be specific
5. **Include evidence:** Every claim should reference a file, function, or metric
6. **No speculation:** Don't guess about intended features or future plans
7. **User-friendly language:** Sections 1-3 use plain English for non-technical readers. Sections 4+ can be technical.
8. **Calculate scores objectively:** Use formulas provided for health scores and ratings
9. **NO RECOMMENDATIONS beyond Section 3:** After "What It Can Do", stick to facts only - no strategic advice
10. **Run git commands:** Execute all git history commands from Section 2 for complete timeline data
11. **Run complexity analysis:** Use coderef-context tools on at least 3 critical files
12. **Flag data issues:** Explicitly mark virtual environment pollution, missing git data, or parsing errors

## Project Directory

**Project to analyze:** The current working directory (where this prompt is being executed)

The agent should automatically detect the project path and analyze it without requiring explicit path specification.

---

## Critical Reminders

**BEFORE YOU BEGIN:**

1. ✅ **Detect project path** - Use current working directory, confirm with user if ambiguous
2. ✅ **Write user-friendly intro** - Sections 1-3 must use plain English, avoid jargon
3. ✅ **Calculate health scores** - Use objective formulas for ratings (see Section 2 template)
4. ✅ **Run ALL git commands** from Section 2 - do not mark as "Unknown" without trying
5. ✅ **Check for .venv pollution** in Python projects - flag with asterisks if present
6. ✅ **Run complexity analysis** on at least 3 critical files using coderef-context tools
7. ✅ **Include evidence** - every claim must reference a file, line number, or tool output
8. ✅ **Save output** - Write report to `.coderef/PROJECT-STATE-ASSESSMENT.md` in the project directory

**Example coderef-context tool usage:**

```javascript
// Get complexity metrics
mcp__coderef-context__coderef_complexity({
  project_path: "/path/to/project",
  element: "MainComponent"
})

// Find test coverage
mcp__coderef-context__coderef_coverage({
  project_path: "/path/to/project",
  format: "detailed"
})

// Analyze patterns
mcp__coderef-context__coderef_patterns({
  project_path: "/path/to/project",
  limit: 20
})

// Check dependencies
mcp__coderef-context__coderef_query({
  project_path: "/path/to/project",
  query_type: "depends-on",
  target: "CoreService"
})
```

---

**Begin analysis and generate PROJECT-STATE-ASSESSMENT.md in the `.coderef/` directory with factual reporting only.**
