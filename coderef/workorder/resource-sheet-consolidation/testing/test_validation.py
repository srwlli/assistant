"""
TEST-VALIDATION: Test 4-gate validation pipeline

Workorder: WO-RESOURCE-SHEET-CONSOLIDATION-001-TESTING
Category: Category 4 - Validation Pipeline
Test Count: 5 test cases
Critical Requirement: CR-4 - 100% error detection (4-gate pipeline)
"""

import sys
import json
from pathlib import Path

# Add coderef-docs to path
sys.path.insert(0, str(Path("C:/Users/willh/.mcp-servers/coderef-docs")))

from generators.validation_pipeline import ValidationPipeline


def create_test_sheets():
    """Create 5 test resource sheets with varying quality levels."""
    return [
        # Test 1: Excellent sheet (should PASS with high score)
        {
            "name": "excellent-sheet",
            "description": "Complete resource sheet with all sections",
            "expected_score_range": (85, 100),
            "expected_status": "pass",
            "content": """
Agent: Claude
Date: 2026-01-03
Task: DOCUMENT

# useAuth — Authoritative Documentation

## Executive Summary
This hook provides authentication state management with type safety and persistence. It manages user login, logout, and session validation. Primary use case is protected routes and user identity.

## Audience & Intent
- **Markdown:** Architecture truth
- **Code:** Runtime behavior
- **Schema:** Type contracts

## Architecture Overview
Custom hook that wraps authentication API with React state management. Integrates with AuthProvider context and localStorage for session persistence.

## State Ownership
| State | Owner | Type | Persistence | Source of Truth |
|-------|-------|------|-------------|-----------------|
| user | useAuth | Domain | localStorage | AuthProvider |
| isAuthenticated | useAuth | Domain | none | Computed from user |
| loading | useAuth | UI | none | Hook state |

**Precedence Rules:** Server state always wins over local cache.

## Behaviors & Events
- **User behaviors:** Login button click, logout action
- **System behaviors:** Token refresh, session timeout

## Event & Callback Contracts
| Event | Trigger | Payload | Side Effects |
|-------|---------|---------|--------------|
| onLogin | User submits credentials | `{ email, password }` | Fetches user, stores token |
| onLogout | User clicks logout | none | Clears localStorage, redirects |

## Testing Strategy
- **Must-Cover Scenarios:** Login flow, logout flow, session refresh, token expiry
- **Explicitly Not Tested:** Password reset (separate flow)

## Common Pitfalls
- Token refresh race conditions
- Stale user data after logout
- Missing cleanup on unmount

#### Checklist
- [ ] Side effects
- [ ] Cleanup guarantees
- [ ] Dependency array
- [ ] Return contract
- [ ] Stale closure bugs
- [ ] Composition patterns
- [ ] Testing approach
- [ ] Performance gotchas
            """
        },

        # Test 2: Good sheet with minor issues (should WARN)
        {
            "name": "good-sheet-with-warnings",
            "description": "Complete but has hedging language",
            "expected_score_range": (70, 84),
            "expected_status": "warn",
            "content": """
Agent: Claude
Date: 2026-01-03
Task: DOCUMENT

# useLocalStorage — Documentation

## Executive Summary
This hook might want to provide localStorage access. It should probably manage persistent state. Primary use case is user preferences.

## Architecture Overview
Custom hook that wraps localStorage API.

## State Ownership
| State | Owner | Type | Source of Truth |
|-------|-------|------|-----------------|
| value | useLocalStorage | Local | localStorage |

## Behaviors
- onChange: Maybe updates localStorage
- onMount: Perhaps hydrates from storage

## Testing Strategy
Some tests needed.

## Common Pitfalls
Serialization errors could occur.
            """
        },

        # Test 3: Incomplete sheet (should REJECT - missing sections)
        {
            "name": "incomplete-sheet",
            "description": "Missing critical sections",
            "expected_score_range": (40, 69),
            "expected_status": "reject",
            "content": """
Agent: Claude
Date: 2026-01-03
Task: DOCUMENT

# SomeComponent

## Executive Summary
This component does something.

TODO: Add more documentation
            """
        },

        # Test 4: Empty sheet (should REJECT - minimal content)
        {
            "name": "empty-sheet",
            "description": "Barely any content",
            "expected_score_range": (0, 39),
            "expected_status": "reject",
            "content": """
# MyComponent

TODO: Document this component
            """
        },

        # Test 5: No metadata (should REJECT - missing header)
        {
            "name": "no-metadata-sheet",
            "description": "Missing agent/date/task metadata",
            "expected_score_range": (30, 60),
            "expected_status": "reject",
            "content": """
# useFeature — Documentation

## Executive Summary
Hook for feature flags. Provides boolean flag state. Use for A/B testing.

## Architecture Overview
Wraps feature flag service.

## State Ownership
| State | Owner | Type |
|-------|-------|------|
| enabled | useFeature | Domain |

## Testing Strategy
Test flag toggling.
            """
        }
    ]


def run_validation_tests():
    """Execute validation tests for all 5 test sheets."""
    pipeline = ValidationPipeline()
    test_sheets = create_test_sheets()

    results = []
    gate_pass_counts = {f"gate_{i}": 0 for i in range(1, 5)}

    print("=" * 80)
    print("TEST-VALIDATION: 4-Gate Validation Pipeline - 5 Test Cases")
    print("=" * 80)
    print()

    for i, test_sheet in enumerate(test_sheets, 1):
        name = test_sheet["name"]
        description = test_sheet["description"]
        content = test_sheet["content"]
        expected_range = test_sheet["expected_score_range"]
        expected_status = test_sheet["expected_status"]

        # Run validation
        validation_result = pipeline.validate(content, "custom_hooks")

        # Check if result matches expectations
        score_in_range = expected_range[0] <= validation_result.overall_score <= expected_range[1]
        status_correct = validation_result.status == expected_status
        test_passed = score_in_range and status_correct

        # Count gate passes
        for j, gate in enumerate(validation_result.gate_results, 1):
            if gate.passed:
                gate_pass_counts[f"gate_{j}"] += 1

        # Extract gate results
        gate_results = {}
        issues_found = []
        for gate in validation_result.gate_results:
            gate_num = gate.gate_name.split(":")[0].replace("Gate ", "")
            gate_results[f"gate_{gate_num}_pass"] = gate.passed
            gate_results[f"gate_{gate_num}_score"] = gate.score
            issues_found.extend(gate.failures)
            issues_found.extend(gate.warnings)

        # Record result
        test_result = {
            "test_number": i,
            "sheet_name": name,
            "description": description,
            "overall_score": validation_result.overall_score,
            "expected_range": list(expected_range),
            "expected_status": expected_status,
            "actual_status": validation_result.status,
            **gate_results,
            "final_result": validation_result.status.upper(),
            "issues_found": issues_found[:5],  # Limit to first 5 issues
            "score_in_range": score_in_range,
            "status_correct": status_correct,
            "pass": test_passed
        }
        results.append(test_result)

        # Print result
        status = "[PASS]" if test_passed else "[FAIL]"
        print(f"{status} Test {i}/5: {name}")
        print(f"  Description: {description}")
        print(f"  Score: {validation_result.overall_score}/100 (expected {expected_range[0]}-{expected_range[1]})")
        print(f"  Status: {validation_result.status.upper()} (expected {expected_status.upper()})")
        print(f"  Gate Results:")
        for gate in validation_result.gate_results:
            gate_status = "PASS" if gate.passed else "FAIL"
            print(f"    [{gate_status}] {gate.gate_name}: {gate.score}/100 ({gate.checks_passed}/{gate.checks_total} checks)")
        if not test_passed:
            print(f"  ISSUE: Expected {expected_status} with score {expected_range[0]}-{expected_range[1]}, got {validation_result.status} with {validation_result.overall_score}")
        print()

    # Calculate statistics
    pass_count = sum(1 for r in results if r["pass"])
    pass_rate = (pass_count / len(test_sheets)) * 100

    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total Tests: {len(test_sheets)}")
    print(f"Passed: {pass_count}/{len(test_sheets)} ({pass_rate:.1f}%)")
    print()
    print("Gate Performance:")
    for gate_num in range(1, 5):
        key = f"gate_{gate_num}"
        count = gate_pass_counts[key]
        print(f"  Gate {gate_num}: {count}/{len(test_sheets)} sheets passed ({count/len(test_sheets)*100:.1f}%)")
    print()

    # Critical requirement check
    cr4_pass = pass_rate == 100  # All tests must pass
    print(f"CR-4 Critical Requirement (100% error detection): {'PASS' if cr4_pass else 'FAIL'}")
    print(f"  Requirement: All validation tests pass (correct scores and status)")
    print(f"  Actual: {pass_count}/{len(test_sheets)} tests passed ({pass_rate:.1f}%)")
    print("=" * 80)

    # Save results
    output = {
        "test_id": "TEST-VALIDATION",
        "category": "Category 4: Validation Pipeline",
        "test_count": len(test_sheets),
        "pass_count": pass_count,
        "pass_rate": round(pass_rate, 1),
        "gate_performance": {
            f"gate_{i}": {
                "pass_count": gate_pass_counts[f"gate_{i}"],
                "pass_rate": round((gate_pass_counts[f"gate_{i}"] / len(test_sheets)) * 100, 1)
            }
            for i in range(1, 5)
        },
        "cr4_pass": cr4_pass,
        "overall_status": "pass" if cr4_pass else "fail",
        "test_results": results
    }

    # Write results
    output_file = Path(__file__).parent / "validation-results.json"
    with open(output_file, 'w') as f:
        json.dump(output, f, indent=2)

    print(f"\nResults saved to: {output_file}")

    return output


if __name__ == "__main__":
    results = run_validation_tests()
