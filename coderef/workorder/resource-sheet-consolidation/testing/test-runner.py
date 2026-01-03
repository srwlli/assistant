#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test Runner for WO-RESOURCE-SHEET-CONSOLIDATION-001
Executes all 5 test categories and generates results.
"""

import json
import time
import sys
import io
from pathlib import Path
from typing import Dict, List, Any

# Fix Windows console encoding
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Test results storage
results = {
    "workorder_id": "WO-RESOURCE-SHEET-CONSOLIDATION-001-TESTING",
    "execution_date": time.strftime("%Y-%m-%d"),
    "total_tests": 5,
    "tests_passed": 0,
    "tests_failed": 0,
    "critical_requirements": {
        "CR-1": {"name": "Routing", "status": "pending", "threshold": "100%"},
        "CR-2": {"name": "Detection", "status": "pending", "threshold": "80%+"},
        "CR-3": {"name": "Auto-fill", "status": "pending", "threshold": "60-80%"},
        "CR-4": {"name": "Validation", "status": "pending", "threshold": "100%"},
        "CR-5": {"name": "Performance", "status": "pending", "threshold": "<2s"}
    },
    "test_results": []
}

def print_header(title: str):
    """Print formatted test section header"""
    print("\n" + "="*80)
    print(f"  {title}")
    print("="*80 + "\n")

def test_routing() -> Dict[str, Any]:
    """TEST-ROUTING: Verify MCP tool invocation"""
    print_header("TEST 1/5: Routing Validation (CR-1)")

    test_result = {
        "test_id": "TEST-ROUTING",
        "category": "Routing Validation",
        "critical_requirement": "CR-1",
        "status": "manual_verification_required",
        "instructions": [
            "1. Open Claude Code",
            "2. Run: /create-resource-sheet --element-type='custom_hook' --name='useAuth'",
            "3. Check logs for: 'mcp__coderef-docs__generate_resource_sheet'",
            "4. Verify element_type parameter passed through",
            "5. Confirm resource sheet generated"
        ],
        "pass_criteria": "100% of invocations call MCP tool",
        "manual_verification": True,
        "evidence_required": "Screenshot or log showing MCP tool invocation"
    }

    print("This test requires manual verification in Claude Code:")
    for instruction in test_result["instructions"]:
        print(f"  {instruction}")

    print("\n[!] After running the test manually, update results in:")
    print("    testing/detection-results.json")

    return test_result

def test_detection() -> Dict[str, Any]:
    """TEST-DETECTION: Verify element type detection for all 20 types"""
    print_header("TEST 2/5: Element Type Detection (CR-2)")

    # Define all 20 element types from element-type-mapping.json
    element_types = {
        "priority_1": ["top_level_widgets", "stateful_containers", "global_state", "custom_hooks", "api_clients"],
        "priority_2": ["data_models", "utility_modules", "constants", "error_definitions", "type_definitions"],
        "priority_3": ["validation", "middleware", "transformers", "event_handlers", "services"],
        "priority_4": ["configuration", "context_providers", "decorators", "factories", "observers"]
    }

    test_result = {
        "test_id": "TEST-DETECTION",
        "category": "Element Type Detection",
        "critical_requirement": "CR-2",
        "status": "automated_test_needed",
        "element_types_to_test": element_types,
        "total_types": 20,
        "instructions": [
            "1. Import detection_module.py from:",
            "   C:\\Users\\willh\\.mcp-servers\\coderef-docs\\generators\\detection_module.py",
            "2. For each of 20 element types, create test case with:",
            "   - Sample filename (e.g., 'useAuth.ts' for custom_hooks)",
            "   - Sample code snippet",
            "3. Run: result = detect_element_type(filename, code_sample)",
            "4. Record: detected_type, confidence_score, detection_stage",
            "5. Calculate average confidence per priority tier"
        ],
        "pass_criteria": "≥80% average confidence across all 20 types",
        "test_script": "testing/test_detection.py",
        "evidence_file": "testing/detection-results.json"
    }

    print(f"Testing {test_result['total_types']} element types:")
    for priority, types in element_types.items():
        print(f"\n  {priority}: {', '.join(types)}")

    print("\n[>] To execute this test:")
    print("  1. Run: python testing/test_detection.py")
    print("  2. Results will be saved to: testing/detection-results.json")
    print("  3. Review confidence scores (must be >=80% average)")

    return test_result

def test_autofill() -> Dict[str, Any]:
    """TEST-AUTOFILL: Verify graph integration auto-fill rates"""
    print_header("TEST 3/5: Graph Integration Auto-Fill (CR-3)")

    test_result = {
        "test_id": "TEST-AUTOFILL",
        "category": "Graph Integration Auto-Fill",
        "critical_requirement": "CR-3",
        "status": "automated_test_needed",
        "instructions": [
            "1. Import graph-helpers from coderef-system:",
            "   from packages/core/src/analyzer/graph-helpers import *",
            "2. Choose 5 test elements (mix of components, hooks, utilities)",
            "3. For each element, run:",
            "   - getImportsForElement(element_name)",
            "   - getExportsForElement(element_name)",
            "   - getConsumersForElement(element_name)",
            "   - getDependenciesForElement(element_name)",
            "4. Count auto-filled lines vs total section lines",
            "5. Calculate: (auto_filled / total) * 100 per section"
        ],
        "target_rates": {
            "imports": "90%",
            "exports": "95%",
            "consumers": "70%",
            "dependencies": "75%",
            "overall": "60-80%"
        },
        "pass_criteria": "60-80% average completion rate",
        "test_script": "testing/test_autofill.py",
        "evidence_file": "testing/autofill-results.json"
    }

    print("Target auto-fill rates:")
    for section, rate in test_result["target_rates"].items():
        print(f"  {section}: {rate}")

    print("\n[>] To execute this test:")
    print("  1. Run: python testing/test_autofill.py")
    print("  2. Results will be saved to: testing/autofill-results.json")
    print("  3. Review completion rates (must be 60-80% average)")

    return test_result

def test_validation() -> Dict[str, Any]:
    """TEST-VALIDATION: Verify 4-gate validation pipeline"""
    print_header("TEST 4/5: Validation Pipeline (CR-4)")

    test_result = {
        "test_id": "TEST-VALIDATION",
        "category": "Validation Pipeline",
        "critical_requirement": "CR-4",
        "status": "automated_test_needed",
        "instructions": [
            "1. Import validation_pipeline.py from:",
            "   C:\\Users\\willh\\.mcp-servers\\coderef-docs\\generators\\validation_pipeline.py",
            "2. Create 5 test resource sheets:",
            "   - Good sheet (all sections complete)",
            "   - Incomplete sheet (missing purpose/usage)",
            "   - Minimal sheet (only name/type)",
            "   - Edge case 1 (empty sections)",
            "   - Edge case 2 (malformed content)",
            "3. Run: score, result = validate_resource_sheet(sheet)",
            "4. Verify all 4 gates execute correctly"
        ],
        "validation_gates": {
            "gate_1": "Structural integrity (required sections present)",
            "gate_2": "Content completeness (sections not empty)",
            "gate_3": "Quality standards (writing_standards.py)",
            "gate_4": "Auto-fill validation (60%+ from graph)"
        },
        "scoring": {
            "pass": "≥90 points",
            "warn": "70-89 points",
            "reject": "<70 points"
        },
        "pass_criteria": "Good sheets PASS (≥90), bad sheets REJECT (<70)",
        "test_script": "testing/test_validation.py",
        "evidence_file": "testing/validation-results.json"
    }

    print("Testing 4 validation gates:")
    for gate, description in test_result["validation_gates"].items():
        print(f"  {gate}: {description}")

    print("\n[>] To execute this test:")
    print("  1. Run: python testing/test_validation.py")
    print("  2. Results will be saved to: testing/validation-results.json")
    print("  3. Review scores (good >=90, bad <70)")

    return test_result

def test_performance() -> Dict[str, Any]:
    """TEST-PERFORMANCE: Measure end-to-end timing"""
    print_header("TEST 5/5: Performance Benchmarks (CR-5)")

    test_result = {
        "test_id": "TEST-PERFORMANCE",
        "category": "Performance Benchmarks",
        "critical_requirement": "CR-5",
        "status": "automated_test_needed",
        "instructions": [
            "1. Use Python timeit module for 10 iterations",
            "2. Measure end-to-end: /create-resource-sheet → final output",
            "3. Breakdown timing by stage:",
            "   - Detection: <50ms",
            "   - Graph queries: <200ms (4 queries @ <50ms each)",
            "   - Template rendering: <500ms",
            "   - Validation: <100ms",
            "4. Calculate: average, p95, max",
            "5. Verify p95 ≤2000ms"
        ],
        "performance_targets": {
            "detection_ms": 50,
            "graph_queries_ms": 200,
            "template_rendering_ms": 500,
            "validation_ms": 100,
            "total_ms": 2000
        },
        "pass_criteria": "p95 ≤2000ms, average ≤1500ms",
        "test_script": "testing/test_performance.py",
        "evidence_file": "testing/performance-results.json"
    }

    print("Performance targets:")
    for stage, target_ms in test_result["performance_targets"].items():
        print(f"  {stage}: <{target_ms}ms")

    print("\n[>] To execute this test:")
    print("  1. Run: python testing/test_performance.py")
    print("  2. Results will be saved to: testing/performance-results.json")
    print("  3. Review timing (p95 must be <=2000ms)")

    return test_result

def generate_summary(all_results: List[Dict[str, Any]]) -> str:
    """Generate TESTING-SUMMARY.md"""

    summary = f"""# Testing Summary - WO-RESOURCE-SHEET-CONSOLIDATION-001

**Date:** {time.strftime("%Y-%m-%d")}
**Total Tests:** {len(all_results)}
**Status:** In Progress

---

## Test Results

"""

    for i, test in enumerate(all_results, 1):
        summary += f"""
### Test {i}/5: {test['test_id']}
- **Category:** {test['category']}
- **Critical Requirement:** {test['critical_requirement']}
- **Status:** {test['status']}
- **Pass Criteria:** {test['pass_criteria']}

"""
        if 'instructions' in test:
            summary += "**Instructions:**\n"
            for instruction in test['instructions']:
                summary += f"{instruction}\n"
            summary += "\n"

    summary += """
---

## Critical Requirements Status

| Requirement | Target | Status | Result |
|-------------|--------|--------|--------|
| CR-1: Routing | 100% | ⏳ Pending | - |
| CR-2: Detection | 80%+ | ⏳ Pending | - |
| CR-3: Auto-fill | 60-80% | ⏳ Pending | - |
| CR-4: Validation | 100% | ⏳ Pending | - |
| CR-5: Performance | <2s | ⏳ Pending | - |

---

## GO/NO-GO Decision

**Status:** ⏳ Testing in progress

**Decision Framework:**
- ✅ **GO:** All 5 critical requirements PASS
- ❌ **NO-GO:** Any 1 critical requirement FAIL
- ⚠️ **CONDITIONAL GO:** Minor issues only (warnings)

**Recommendation:** TBD (awaiting test results)

---

## Next Steps

1. Execute all 5 test scripts:
   - `python testing/test_detection.py`
   - `python testing/test_autofill.py`
   - `python testing/test_validation.py`
   - `python testing/test_performance.py`
   - Manual verification: TEST-ROUTING

2. Review evidence files:
   - `detection-results.json`
   - `autofill-results.json`
   - `validation-results.json`
   - `performance-results.json`

3. Update this summary with final GO/NO-GO decision

4. Notify orchestrator in parent instructions.json

---

**Testing Agent:** coderef-testing
**Workorder:** WO-RESOURCE-SHEET-CONSOLIDATION-001
"""

    return summary

def main():
    """Main test runner"""
    print("\n" + "="*80)
    print("  WO-RESOURCE-SHEET-CONSOLIDATION-001 - Test Runner")
    print("="*80)

    print("\nThis script will guide you through executing all 5 test categories.")
    print("Some tests are automated, others require manual verification.\n")

    # Run all tests
    test_results = []
    test_results.append(test_routing())
    test_results.append(test_detection())
    test_results.append(test_autofill())
    test_results.append(test_validation())
    test_results.append(test_performance())

    # Save results
    results["test_results"] = test_results

    results_file = Path(__file__).parent / "test-results.json"
    with open(results_file, 'w') as f:
        json.dump(results, f, indent=2)

    print_header("Test Execution Summary")
    print(f"[OK] Test guide generated")
    print(f"[FILE] Results template saved: {results_file}")

    # Generate summary
    summary = generate_summary(test_results)
    summary_file = Path(__file__).parent / "TESTING-SUMMARY.md"
    with open(summary_file, 'w', encoding='utf-8') as f:
        f.write(summary)

    print(f"[FILE] Summary template saved: {summary_file}")

    print("\n" + "="*80)
    print("  Next Steps")
    print("="*80)
    print("\n1. Execute automated tests:")
    print("   - python testing/test_detection.py")
    print("   - python testing/test_autofill.py")
    print("   - python testing/test_validation.py")
    print("   - python testing/test_performance.py")
    print("\n2. Perform manual verification:")
    print("   - TEST-ROUTING in Claude Code")
    print("\n3. Review all results and update TESTING-SUMMARY.md")
    print("\n4. Make GO/NO-GO decision based on critical requirements")
    print("\n5. Notify orchestrator in parent instructions.json")
    print("\n" + "="*80 + "\n")

if __name__ == "__main__":
    main()
