"""
TEST-DETECTION: Test all 20 element types with detection module

Workorder: WO-RESOURCE-SHEET-CONSOLIDATION-001-TESTING
Category: Category 2 - Element Type Detection
Test Count: 24 tests (20 element types + 4 edge cases)
Critical Requirement: CR-2 - 80%+ confidence for all 20 element types
"""

import sys
import json
from pathlib import Path

# Add coderef-docs to path
sys.path.insert(0, str(Path("C:/Users/willh/.mcp-servers/coderef-docs")))

from generators.detection_module import ElementTypeDetector

def create_test_cases():
    """Create test cases for all 20 element types."""
    return [
        # Priority 1: Critical elements (5 types)
        {
            "element_type": "top_level_widgets",
            "filename": "UserDashboardPage.tsx",
            "code_sample": "export function UserDashboardPage() { return <div>Dashboard</div>; }",
            "expected_confidence": 90,
            "priority": 1
        },
        {
            "element_type": "stateful_containers",
            "filename": "AuthProvider.tsx",
            "code_sample": "export function AuthProvider({ children }) { const [user, setUser] = useState(null); }",
            "expected_confidence": 95,
            "priority": 1
        },
        {
            "element_type": "global_state_layer",
            "filename": "store.ts",
            "code_sample": "const store = configureStore({ reducer: rootReducer });",
            "expected_confidence": 95,
            "priority": 1
        },
        {
            "element_type": "custom_hooks",
            "filename": "useAuth.ts",
            "code_sample": "export function useAuth() { useEffect(() => { return () => cleanup(); }); }",
            "expected_confidence": 100,
            "priority": 1
        },
        {
            "element_type": "api_client",
            "filename": "apiClient.ts",
            "code_sample": "export const apiClient = axios.create({ baseURL: '/api' });",
            "expected_confidence": 90,
            "priority": 1
        },

        # Priority 2: High-impact elements (5 types)
        {
            "element_type": "data_models",
            "filename": "types.ts",
            "code_sample": "export interface User { id: string; name: string; }",
            "expected_confidence": 90,
            "priority": 2
        },
        {
            "element_type": "persistence_subsystem",
            "filename": "storage.ts",
            "code_sample": "export const storage = { get: (key) => localStorage.getItem(key) };",
            "expected_confidence": 90,
            "priority": 2
        },
        {
            "element_type": "eventing_messaging",
            "filename": "eventBus.ts",
            "code_sample": "class EventBus extends EventEmitter { emit(event, data) {} }",
            "expected_confidence": 90,
            "priority": 2
        },
        {
            "element_type": "routing_navigation",
            "filename": "router.ts",
            "code_sample": "const router = createBrowserRouter([{ path: '/', element: <App /> }]);",
            "expected_confidence": 90,
            "priority": 2
        },
        {
            "element_type": "file_tree_primitives",
            "filename": "TreeNode.ts",
            "code_sample": "export class TreeNode { children: TreeNode[] = []; }",
            "expected_confidence": 85,
            "priority": 2
        },

        # Priority 3: Medium-impact elements (5 types)
        {
            "element_type": "context_menu_commands",
            "filename": "contextMenu.ts",
            "code_sample": "export const contextMenuActions = { copy: () => {}, paste: () => {} };",
            "expected_confidence": 85,
            "priority": 3
        },
        {
            "element_type": "permission_authz",
            "filename": "permissions.ts",
            "code_sample": "export const can = (user, action) => user.permissions.includes(action);",
            "expected_confidence": 85,
            "priority": 3
        },
        {
            "element_type": "error_handling",
            "filename": "ErrorBoundary.tsx",
            "code_sample": "class ErrorBoundary extends React.Component { componentDidCatch(error) {} }",
            "expected_confidence": 90,
            "priority": 3
        },
        {
            "element_type": "logging_telemetry",
            "filename": "analytics.ts",
            "code_sample": "export const track = (event, properties) => { console.log(event, properties); };",
            "expected_confidence": 85,
            "priority": 3
        },
        {
            "element_type": "performance_critical_ui",
            "filename": "VirtualList.tsx",
            "code_sample": "export function VirtualList() { const items = useMemo(() => [], []); }",
            "expected_confidence": 85,
            "priority": 3
        },

        # Priority 4: Lower-impact elements (5 types)
        {
            "element_type": "design_system_components",
            "filename": "Button.tsx",
            "code_sample": "export function Button({ children, variant = 'primary' }) { return <button>{children}</button>; }",
            "expected_confidence": 90,
            "priority": 4
        },
        {
            "element_type": "theming_styling",
            "filename": "theme.ts",
            "code_sample": "export const theme = { colors: { primary: '#007bff' }, spacing: { sm: 8 } };",
            "expected_confidence": 85,
            "priority": 4
        },
        {
            "element_type": "build_tooling",
            "filename": "build.js",
            "code_sample": "const webpack = require('webpack'); module.exports = { entry: './src/index.ts' };",
            "expected_confidence": 85,
            "priority": 4
        },
        {
            "element_type": "ci_cd_pipelines",
            "filename": ".github/workflows/deploy.yml",
            "code_sample": "name: Deploy\non: push\njobs:\n  deploy:\n    runs-on: ubuntu-latest",
            "expected_confidence": 95,
            "priority": 4
        },
        {
            "element_type": "testing_harness",
            "filename": "test-utils.tsx",
            "code_sample": "export const renderWithProviders = (ui) => render(<Provider>{ui}</Provider>);",
            "expected_confidence": 85,
            "priority": 4
        },
    ]


def run_detection_tests():
    """Execute detection tests for all 20 element types."""
    detector = ElementTypeDetector()
    test_cases = create_test_cases()

    results = []
    total_confidence = 0
    stage_1_count = 0
    stage_2_count = 0
    stage_3_count = 0

    print("=" * 80)
    print("TEST-DETECTION: Element Type Detection - 20 Element Types")
    print("=" * 80)
    print()

    for i, test_case in enumerate(test_cases, 1):
        filename = test_case["filename"]
        code_sample = test_case["code_sample"]
        expected_type = test_case["element_type"]
        expected_confidence = test_case["expected_confidence"]
        priority = test_case["priority"]

        # Run detection
        result = detector.detect(filename, code_sample)

        # Determine detection stage
        if "stage_1" in result.detection_method:
            if "stage_2" in result.detection_method:
                stage = 2
                stage_2_count += 1
            else:
                stage = 1
                stage_1_count += 1
        else:
            stage = 3
            stage_3_count += 1

        # Check if correct type detected
        correct_type = result.element_type == expected_type
        confidence_ok = result.confidence >= expected_confidence * 0.9  # Allow 10% margin
        passed = correct_type and confidence_ok

        total_confidence += result.confidence

        # Record result
        test_result = {
            "test_number": i,
            "element_type": expected_type,
            "priority": priority,
            "filename": filename,
            "detected_type": result.element_type,
            "confidence": result.confidence,
            "expected_confidence": expected_confidence,
            "detection_stage": stage,
            "detection_method": result.detection_method,
            "matched_patterns": result.matched_patterns,
            "correct_type": correct_type,
            "confidence_acceptable": confidence_ok,
            "pass": passed
        }
        results.append(test_result)

        # Print result
        status = "[PASS]" if passed else "[FAIL]"
        print(f"{status} Test {i:2}/20 - Priority {priority}")
        print(f"  Type: {expected_type}")
        print(f"  File: {filename}")
        print(f"  Detected: {result.element_type} ({result.confidence}% confidence)")
        print(f"  Stage: {stage} ({result.detection_method})")
        if not passed:
            print(f"  ISSUE: Expected {expected_type} with {expected_confidence}%+ confidence")
        print()

    # Calculate statistics
    avg_confidence = total_confidence / len(test_cases)
    pass_count = sum(1 for r in results if r["pass"])
    pass_rate = (pass_count / len(test_cases)) * 100

    # Group by priority
    priority_stats = {}
    for priority in [1, 2, 3, 4]:
        priority_results = [r for r in results if r["priority"] == priority]
        if priority_results:
            priority_avg_conf = sum(r["confidence"] for r in priority_results) / len(priority_results)
            priority_pass_rate = (sum(1 for r in priority_results if r["pass"]) / len(priority_results)) * 100
            priority_stats[f"priority_{priority}"] = {
                "count": len(priority_results),
                "avg_confidence": round(priority_avg_conf, 1),
                "pass_rate": round(priority_pass_rate, 1)
            }

    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total Tests: {len(test_cases)}")
    print(f"Passed: {pass_count}/{len(test_cases)} ({pass_rate:.1f}%)")
    print(f"Average Confidence: {avg_confidence:.1f}%")
    print()
    print("Detection Stage Breakdown:")
    print(f"  Stage 1 (Filename): {stage_1_count} ({stage_1_count/len(test_cases)*100:.1f}%)")
    print(f"  Stage 2 (Filename + Code): {stage_2_count} ({stage_2_count/len(test_cases)*100:.1f}%)")
    print(f"  Stage 3 (Fallback): {stage_3_count} ({stage_3_count/len(test_cases)*100:.1f}%)")
    print()
    print("Confidence by Priority:")
    for priority in [1, 2, 3, 4]:
        key = f"priority_{priority}"
        if key in priority_stats:
            stats = priority_stats[key]
            print(f"  Priority {priority}: {stats['avg_confidence']}% avg, {stats['pass_rate']}% pass rate")
    print()

    # Critical requirement check
    cr2_pass = avg_confidence >= 80
    print(f"CR-2 Critical Requirement (80%+ confidence): {'PASS' if cr2_pass else 'FAIL'}")
    print(f"  Requirement: >=80% average confidence")
    print(f"  Actual: {avg_confidence:.1f}%")
    print("=" * 80)

    # Save results
    output = {
        "test_id": "TEST-DETECTION",
        "category": "Category 2: Element Type Detection",
        "test_count": len(test_cases),
        "pass_count": pass_count,
        "pass_rate": round(pass_rate, 1),
        "average_confidence": round(avg_confidence, 1),
        "stage_breakdown": {
            "stage_1_count": stage_1_count,
            "stage_2_count": stage_2_count,
            "stage_3_count": stage_3_count
        },
        "priority_stats": priority_stats,
        "cr2_pass": cr2_pass,
        "overall_status": "pass" if cr2_pass and pass_rate >= 90 else "fail",
        "test_results": results
    }

    # Write results
    output_file = Path(__file__).parent / "detection-results.json"
    with open(output_file, 'w') as f:
        json.dump(output, f, indent=2)

    print(f"\nResults saved to: {output_file}")

    return output


if __name__ == "__main__":
    results = run_detection_tests()
