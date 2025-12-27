# The Coderef System: Context, Workflows, and Docs

## Overview

The coderef system is a unified MCP ecosystem for AI agents to understand, plan, and execute work on codebases. It answers three fundamental questions:

1. **coderef-context:** "What exists in this code and what matters?"
2. **coderef-workflow:** "How should we organize work based on what exists?"
3. **coderef-docs:** "What should agents/humans read as reference?"

---

## 1. coderef-context: Deep Code Analysis

### Purpose
Scan a codebase and generate **structured context** that agents use to make decisions, estimate effort, and avoid pitfalls.

### What It Analyzes

```typescript
// Input: Codebase directory
const sourceDir = "C:\\Users\\willh\\Desktop\\projects\\my-app";

// Output: Deep analysis JSON
{
  // 1. Code inventory
  files: 287,
  functions: 3420,
  classes: 145,
  tests: 892,

  // 2. Dependencies and relationships
  external_deps: ["express", "react", "mongoose"],
  internal_modules: ["auth", "api", "ui"],
  call_graph: {...},

  // 3. Patterns discovered (auto)
  patterns: {
    error_handling: "try/catch + logger.error()",
    api_calls: "axios wrapper",
    state_management: "Redux",
    testing: "Jest + Supertest"
  },

  // 4. Code health metrics
  complexity: {
    average_cyclomatic: 4.2,
    hotspots: ["auth/middleware.ts", "api/handlers.ts"],
    maintainability_index: 72
  },

  // 5. Technology stack detected
  stack: {
    language: "TypeScript",
    framework: "Express + React",
    database: "MongoDB",
    testing: "Jest"
  }
}
```

### 6 Phases (Progressive Enhancement)

#### Phase 1: Complexity Scoring
**What:** Score effort for any feature based on related code

**Output:**
```json
{
  "feature": "Add email notifications",
  "related_modules": ["email", "queue", "templates"],
  "complexity": "medium",
  "effort_hours": "8-12",
  "confidence": 0.87
}
```

**How agents use it:** "This feature is medium complexity, estimate 8-12 hours"

---

#### Phase 2: Task-Specific Context
**What:** Generate context specific to a task description

**Input:** "Implement user authentication with JWT and refresh tokens"

**Output:**
```json
{
  "task": "Implement user authentication with JWT and refresh tokens",

  "related_functions": [
    "authenticateUser()",
    "generateToken()",
    "verifyToken()",
    "refreshAccessToken()"
  ],

  "related_files": [
    "src/auth/strategies.ts",
    "src/auth/middleware.ts",
    "src/auth/jwt.utils.ts",
    "tests/auth.test.ts"
  ],

  "complexity_estimate": "medium (10 hours)",

  "risk_level": "high (affects login flow)",

  "examples": [
    {
      "file": "src/auth/strategies.ts",
      "code": "export const jwtStrategy = new JwtStrategy(...)",
      "relevance": "Shows how JWT is currently implemented"
    }
  ],

  "gotchas": [
    "Must handle token expiration gracefully",
    "Refresh tokens need separate storage (not httpOnly)",
    "CORS must allow credentials: true",
    "Session cleanup when user logs out"
  ],

  "test_pattern": "Mock JWT library, test both success and expiration cases",

  "dependencies": [
    "jsonwebtoken library",
    "express middleware pattern",
    "MongoDB user model"
  ],

  "confidence": 0.92
}
```

**How agents use it:**
- "Here's what's already implemented, here are examples"
- "This is high risk, watch out for: X, Y, Z"
- "Here's how to test it"

---

#### Phase 3: Edge Case Detection
**What:** Identify edge cases and potential bugs in related code

**Output:**
```json
{
  "task": "Implement user authentication with JWT",

  "edge_cases": [
    {
      "case": "Token expires during request processing",
      "impact": "User gets logged out mid-transaction",
      "solution": "Check token validity before starting long operations"
    },
    {
      "case": "Refresh token stolen",
      "impact": "Attacker can impersonate user indefinitely",
      "solution": "Implement refresh token rotation + blacklist"
    },
    {
      "case": "Multiple simultaneous login requests",
      "impact": "Race condition creating multiple sessions",
      "solution": "Lock user record during authentication"
    }
  ],

  "security_issues": [
    {
      "issue": "JWT stored in localStorage (XSS vulnerable)",
      "severity": "high",
      "fix": "Use httpOnly cookies instead"
    }
  ]
}
```

**How agents use it:** "These are the pitfalls to watch for—test these scenarios"

---

#### Phase 4: Test Pattern Analysis
**What:** Extract testing patterns from existing code

**Output:**
```json
{
  "task": "Implement user authentication",

  "test_patterns": [
    {
      "pattern": "Mock JWT library",
      "example": "jest.mock('jsonwebtoken', () => ({...}))",
      "used_in": ["tests/auth.test.ts"]
    },
    {
      "pattern": "Supertest for API endpoints",
      "example": "request(app).post('/auth/login').send({...})",
      "used_in": ["tests/api/auth.test.ts"]
    },
    {
      "pattern": "Test both success and failure paths",
      "example": "describe('login', () => { it('succeeds'); it('fails with wrong password'); })",
      "used_in": ["tests/auth.test.ts"]
    }
  ],

  "test_coverage_target": "95%",
  "critical_paths_to_test": [
    "Successful login flow",
    "Token expiration",
    "Invalid credentials",
    "Refresh token rotation"
  ]
}
```

**How agents use it:** "Follow these test patterns; aim for 95% coverage; test these critical paths"

---

#### Phase 5: Code Example Extraction
**What:** Pull relevant code examples from the codebase

**Output:**
```json
{
  "task": "Implement user authentication",

  "examples": [
    {
      "title": "Existing JWT strategy",
      "file": "src/auth/strategies.ts",
      "lines": "42-65",
      "code": "export const jwtStrategy = new JwtStrategy({...})",
      "explanation": "Shows how JWT is configured in passport.js"
    },
    {
      "title": "Token generation utility",
      "file": "src/auth/jwt.utils.ts",
      "lines": "10-25",
      "code": "export function generateToken(payload) {...}",
      "explanation": "Reuse this pattern for generating JWT tokens"
    },
    {
      "title": "API route with auth middleware",
      "file": "src/api/routes/protected.ts",
      "lines": "5-20",
      "code": "router.get('/profile', authenticate, (req, res) => {...})",
      "explanation": "Shows how to protect routes with JWT middleware"
    }
  ]
}
```

**How agents use it:** Copy-paste patterns, understand existing conventions

---

#### Phase 6: Agentic Output Formatting
**What:** Format all context as JSON optimized for AI agent consumption

**Output:**
```json
{
  "metadata": {
    "task": "Implement user authentication with JWT",
    "analysis_timestamp": "2025-12-23T19:30:00Z",
    "codebase_version": "abc123def",
    "confidence_overall": 0.92
  },

  "context": {
    "what_exists": {
      "current_auth": "Session-based (outdated)",
      "related_modules": ["auth", "user", "session"],
      "tech_stack": ["Express", "Passport", "MongoDB"]
    },

    "complexity": {
      "effort": "10-12 hours",
      "risk": "high",
      "difficulty": "medium"
    },

    "examples": [...],
    "gotchas": [...],
    "edge_cases": [...]
  },

  "actions": {
    "files_to_modify": [
      "src/auth/strategies.ts",
      "src/auth/jwt.utils.ts",
      "src/api/middleware.ts"
    ],

    "files_to_create": [
      "src/auth/jwt.config.ts",
      "tests/auth.integration.test.ts"
    ],

    "test_strategy": "Unit test token generation, integration test login flow, e2e test full auth flow",

    "validation_checklist": [
      "[ ] Token expires correctly",
      "[ ] Refresh token works",
      "[ ] Invalid tokens rejected",
      "[ ] CORS credentials enabled",
      "[ ] Tests pass at 95%+ coverage"
    ]
  }
}
```

**How agents use it:** This is the complete task brief, ready to implement

---

## 2. coderef-workflow: Intelligent Planning & Orchestration

### Purpose
Use context from coderef-context to create plans, assign work, track progress, and validate completion.

### How It Works

```
Step 1: Gather Requirements
  ↓
Step 2: Analyze Codebase (calls coderef-context)
  ↓
Step 3: Generate Plan
  ↓
Step 4: Break Into Tasks
  ↓
Step 5: Embed Context Into Each Task
  ↓
Step 6: Assign to Agents
  ↓
Step 7: Track Execution
  ↓
Step 8: Validate Completion
```

### Example: Create Plan with Embedded Context

**Input: Feature Requirements**
```json
{
  "feature": "User Authentication System",
  "goal": "Replace session-based auth with JWT + refresh tokens",
  "requirements": [
    "Implement JWT token generation",
    "Implement JWT verification",
    "Implement refresh token rotation",
    "Add HTTP-only cookie support",
    "Add comprehensive tests"
  ],
  "constraints": [
    "Must not break existing sessions during migration",
    "Backward compatible for 1 week",
    "Must pass security audit"
  ]
}
```

**Process:**
```typescript
// Step 1: Get codebase analysis
const analysis = await coderefContext.analyze(sourceDir);
// Returns: tech stack, existing patterns, complexity

// Step 2: For each requirement, get task-specific context
const tasks = [];
for (const req of requirements) {
  const taskContext = await coderefContext.generateTaskContext(
    sourceDir,
    req
  );
  // Returns: effort estimate, examples, gotchas, test patterns

  tasks.push({
    requirement: req,
    context: taskContext,
    effort: taskContext.complexity_estimate,
    risk: taskContext.risk_level
  });
}

// Step 3: Create plan with embedded context
const plan = await coderefWorkflow.createPlan(
  feature,
  analysis,
  tasks,
  constraints
);
```

**Output: plan.json (with context embedded)**
```json
{
  "workorder_id": "WO-AUTH-SYSTEM-001",
  "feature": "User Authentication System",
  "created_at": "2025-12-23T19:30:00Z",

  "sections": {
    "1_executive_summary": {
      "goal": "Replace session-based auth with JWT...",
      "effort_total": "48-60 hours",
      "risk_level": "high",
      "complexity": "medium-high"
    },

    "2_current_state": {
      "what_exists": "Session-based authentication using express-session",
      "tech_stack": ["Express", "Passport", "MongoDB"],
      "patterns": ["Middleware-based auth checks", "Database session store"],
      "gotchas": [
        "Sessions are stored in DB (read on every request)",
        "No refresh token concept",
        "Hard to scale across multiple servers"
      ]
    },

    "3_target_state": {
      "what_we_build": "JWT-based authentication with refresh tokens",
      "technology": ["jsonwebtoken", "httpOnly cookies"],
      "benefits": [
        "Stateless authentication (scalable)",
        "Refresh tokens allow long sessions",
        "Better for mobile/SPA"
      ]
    },

    "4_dependencies": [
      "jsonwebtoken library",
      "bcryptjs for password hashing",
      "Redis for refresh token blacklist (optional)"
    ],

    "5_tasks": [
      {
        "id": "AUTH-001",
        "title": "Implement JWT token generation",
        "description": "Create utility to generate access + refresh tokens",

        "context_embedded": {
          "what_exists": "generateToken() in jwt.utils.ts - modify this",
          "complexity": "low (4 hours)",
          "risk": "low",
          "examples": [
            "Check src/auth/jwt.utils.ts lines 10-25"
          ],
          "gotchas": [
            "Token payload must include user ID and role",
            "Access token: 15min expiry, Refresh: 7 days",
            "Use RS256 (asymmetric) for better security"
          ],
          "test_pattern": "Mock jsonwebtoken, test token contains expected claims"
        },

        "files_to_modify": ["src/auth/jwt.utils.ts"],
        "effort": "4 hours",
        "assigned_to": "agent_1"
      },

      {
        "id": "AUTH-002",
        "title": "Implement JWT verification middleware",
        "description": "Create middleware to verify JWT tokens in requests",

        "context_embedded": {
          "what_exists": "authenticate() middleware exists - extend it",
          "complexity": "low (3 hours)",
          "risk": "low",
          "examples": [
            "Check src/api/middleware.ts lines 5-20 for pattern"
          ],
          "gotchas": [
            "Extract token from Authorization header",
            "Handle expired tokens gracefully",
            "Return 401 for invalid tokens"
          ],
          "test_pattern": "Test with valid token, expired token, no token, malformed token"
        },

        "files_to_modify": ["src/api/middleware.ts"],
        "files_to_create": ["src/auth/verifyJwt.ts"],
        "effort": "3 hours",
        "assigned_to": "agent_1"
      },

      {
        "id": "AUTH-003",
        "title": "Implement refresh token rotation",
        "description": "Allow clients to refresh expired access tokens",

        "context_embedded": {
          "complexity": "medium (6 hours)",
          "risk": "high (security-critical)",
          "gotchas": [
            "Refresh tokens must be stored securely (httpOnly cookies)",
            "Old refresh tokens should be invalidated (prevent replay attacks)",
            "Implement rotation: new request = new refresh token",
            "Consider token blacklist for logout"
          ],
          "edge_cases": [
            "What if refresh token is stolen?",
            "What if user logs out but has valid refresh token?",
            "What if client makes concurrent refresh requests?"
          ],
          "test_pattern": "Test refresh flow, test with expired access token, test with invalid refresh token"
        },

        "files_to_modify": ["src/auth/jwt.utils.ts"],
        "files_to_create": ["src/api/routes/auth/refresh.ts"],
        "effort": "6 hours",
        "assigned_to": "agent_2"
      },

      {
        "id": "AUTH-004",
        "title": "Add HTTP-only cookie support",
        "description": "Store refresh tokens in httpOnly cookies (not localStorage)",

        "context_embedded": {
          "complexity": "low (3 hours)",
          "risk": "low (security improvement)",
          "gotchas": [
            "CORS must allow credentials: true",
            "SameSite=Strict to prevent CSRF",
            "Domain/Path must match your API"
          ],
          "test_pattern": "Test cookie is set, test cookie is sent in requests, test CORS headers"
        },

        "files_to_modify": ["src/api/routes/auth/login.ts"],
        "effort": "3 hours",
        "assigned_to": "agent_2"
      },

      {
        "id": "AUTH-005",
        "title": "Add comprehensive tests",
        "description": "Test all auth flows with >95% coverage",

        "context_embedded": {
          "complexity": "medium (8 hours)",
          "risk": "low (testing is safe)",
          "test_pattern": [
            "Mock jsonwebtoken",
            "Use Supertest for API testing",
            "Test both success and failure paths",
            "Test edge cases: expired tokens, stolen tokens, etc"
          ],
          "critical_paths": [
            "Login succeeds with valid credentials",
            "Login fails with wrong password",
            "Access token verified successfully",
            "Expired access token rejected",
            "Refresh token works",
            "Token rotation happens",
            "Stolen refresh token detected"
          ]
        },

        "files_to_create": ["tests/auth.unit.test.ts", "tests/auth.integration.test.ts"],
        "effort": "8 hours",
        "assigned_to": "agent_3"
      }
    ],

    "6_timeline": [
      {"phase": "Phase 1: Setup", "tasks": ["AUTH-001"], "duration": "1 day"},
      {"phase": "Phase 2: Implementation", "tasks": ["AUTH-002", "AUTH-003", "AUTH-004"], "duration": "2 days"},
      {"phase": "Phase 3: Testing", "tasks": ["AUTH-005"], "duration": "1 day"},
      {"phase": "Phase 4: Migration", "tasks": [], "duration": "1 day"}
    ],

    "7_risks": [
      {
        "risk": "Breaking existing sessions during migration",
        "mitigation": "Keep old session code for 1 week, run in parallel"
      },
      {
        "risk": "Security vulnerabilities in token handling",
        "mitigation": "Security audit before deployment, test edge cases"
      }
    ],

    "8_success_criteria": [
      "All tests pass (>95% coverage)",
      "Authentication works end-to-end",
      "Refresh tokens rotate correctly",
      "Security audit passed",
      "No performance degradation"
    ]
  }
}
```

### Key Innovation: Context Embedded in Tasks

Each task contains:
- ✅ What already exists (no need to reinvent)
- ✅ Complexity estimate (avoid surprises)
- ✅ Risk level (plan accordingly)
- ✅ Code examples (copy-paste ready)
- ✅ Gotchas (avoid bugs)
- ✅ Test patterns (know how to validate)
- ✅ Edge cases (think ahead)

**Agents don't need to explore the codebase.** The plan is self-contained.

---

## 3. coderef-docs: Automated Reference Documentation

### Purpose
Generate and maintain reference documentation that agents use while implementing.

### What It Generates

```
README.md
├── Installation
├── Quick Start
├── API Overview
└── Configuration

ARCHITECTURE.md
├── System Design
├── Module Relationships
├── Data Flow
└── Design Decisions

API.md
├── Endpoints
├── Request/Response Examples
├── Error Codes
└── Authentication

SCHEMA.md
├── Data Models
├── Relationships
├── Validation Rules
└── Constraints

STANDARDS.md (generated by coderef-context)
├── UI Standards (buttons, forms, modals)
├── Behavior Standards (error handling, loading)
└── UX Patterns (navigation, permissions)
```

### Example: Auto-Generated API.md

```markdown
# API Reference

## Authentication

### POST /auth/login
Authenticate a user with email and password.

**Request:**
```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

**Response (Success):**
```json
{
  "accessToken": "eyJhbGciOiJIUzI1NiIs...",
  "refreshToken": "eyJhbGciOiJIUzI1NiIs...",
  "user": {
    "id": "507f1f77bcf86cd799439011",
    "email": "user@example.com",
    "role": "user"
  }
}
```

**Response (Error - 401):**
```json
{
  "error": "Invalid credentials",
  "message": "Email or password is incorrect"
}
```

**Related Code:**
- Implementation: src/api/routes/auth/login.ts
- Test: tests/auth.integration.test.ts

---

## Related Patterns

This endpoint follows the authentication pattern documented in STANDARDS.md:
- Error handling: [Error Standards](#error-handling)
- Security: [JWT Standards](#jwt-authentication)
```

### How coderef-docs Uses Context

```typescript
// coderef-docs receives standards from coderef-context
const standards = await coderefContext.discoverStandards(sourceDir);

// Example standards discovered:
standards = {
  "api_error_pattern": "{ error: string, message: string }",
  "auth_pattern": "JWT in Authorization header",
  "response_format": "{ data, meta, error }"
}

// Embed into generated docs
const apiMd = generateApiMd(endpoints);
// Add: "This API follows the error pattern: {...}"
// Add: "Authentication uses: JWT tokens..."
// Add: "Response format: {...}"

// Generate standards documents
await writeMarkdown('STANDARDS.md', standards);
```

---

## How They Work Together

### The Flow

```
┌─────────────────────────────────────────────────────────┐
│ 1. Orchestrator creates workorder with requirements     │
└──────────────────┬──────────────────────────────────────┘
                   │
                   ↓
┌─────────────────────────────────────────────────────────┐
│ 2. coderef-context analyzes codebase                    │
│    - Outputs: context.json, discovered standards        │
└──────────────────┬──────────────────────────────────────┘
                   │
    ┌──────────────┼──────────────┐
    │              │              │
    ↓              ↓              ↓
┌────────────┐ ┌──────────┐ ┌──────────┐
│coderef-    │ │coderef-  │ │coderef-  │
│workflow    │ │docs      │ │testing   │
└────────────┘ └──────────┘ └──────────┘
    │              │              │
    ├─ Uses ctx    ├─ Uses stds   ├─ Uses patterns
    │              │              │
    ↓              ↓              ↓
Creates plan   Generates docs  Creates tests
with embedded  (README, API,    (unit, integration,
context        SCHEMA, etc)     e2e)
    │              │              │
    ↓              ↓              ↓
Assigns to ──── Agents read ──── Agents
agents        while implementing validate
              and testing
```

---

## Key Insights

### Why This Works

1. **Single Source of Truth:** coderef-context analyzes once, outputs used by workflow, docs, testing
2. **Context Embedded:** Tasks have all needed context (no exploration needed)
3. **Documentation Auto-Generated:** Stays in sync with code patterns
4. **Progressive Disclosure:** Agents get details when they need them (in task context)
5. **Decoupled:** Each system can be updated independently

### What Agents Get

| System | Agents Get |
|--------|-----------|
| **coderef-context** | Understanding of codebase, complexity, gotchas |
| **coderef-workflow** | Plan with embedded context for each task |
| **coderef-docs** | Reference docs while implementing |

### Why It's Better Than Old Approach

**Old:**
- Agent explores codebase (slow, error-prone)
- Agent finds patterns by trial & error
- Agent discovers gotchas the hard way (bugs)
- Documentation is outdated (not used)

**New:**
- Context is pre-generated (fast)
- Patterns are discovered automatically
- Gotchas are documented in task
- Docs are auto-generated from code analysis

---

## Real-World Example

**Task: "Add email notifications feature"**

### What Agent Gets (from coderef-workflow plan)

```json
{
  "task": "Add email notifications when user completes profile",

  "complexity": "medium (12 hours)",
  "risk": "medium (touches email service)",

  "context": {
    "what_exists": [
      "Email service: Sendgrid (configured, working)",
      "Events system: EventEmitter pattern in place",
      "User model: Has email field"
    ],

    "examples": [
      "Check src/services/email/sendWelcome.ts for pattern",
      "Check src/events/userCreated.ts for event pattern"
    ],

    "gotchas": [
      "Email sending is async (don't await)",
      "Handle bounced emails (track failures)",
      "Test with fake email service (don't send real emails)"
    ],

    "test_pattern": "Mock Sendgrid, emit event, verify email sent"
  }
}
```

### What Agent Reads (from coderef-docs)

- **ARCHITECTURE.md:** How email service integrates
- **STANDARDS.md:** Email error handling standards
- **API.md:** Event service API

### Agent Implements

Agent has:
- Context about existing email system
- Examples to copy from
- Gotchas to avoid
- Test patterns to follow
- Reference docs to consult

**Result:** Fast, confident implementation with fewer bugs.

---

## Summary

**coderef-context** = AI's eyes on the codebase
- Analyzes once
- Outputs structured knowledge
- Feeds context and standards

**coderef-workflow** = AI's brain for planning
- Uses context to create plans
- Embeds context in tasks
- Assigns work intelligently

**coderef-docs** = AI's reference library
- Generated from code analysis
- Auto-discovers patterns and standards
- Keeps documentation in sync

**Together:** AI agents (personas or humans) have everything they need to implement features correctly, efficiently, and safely.
