#!/usr/bin/env python3
"""
Generate REFACTOR-TARGETS.md - High-complexity code analysis
Aggregates complexity metrics from all servers
"""

import json
from pathlib import Path

# Server paths
MCP_ROOT = Path("C:/Users/willh/.mcp-servers")
SERVERS = [
    "coderef-context",
    "coderef-docs",
    "coderef-personas",
    "coderef-workflow",
    "coderef-testing",
    "papertrail",
    "archived/coderef-mcp"
]

def load_complexity_report(server_path):
    """Load complexity report from .coderef/reports/"""
    complexity_file = server_path / ".coderef" / "reports" / "complexity.json"
    if not complexity_file.exists():
        return []

    with open(complexity_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data.get('functions', [])

def find_high_complexity():
    """Find functions with high cyclomatic/cognitive complexity"""
    high_complexity = []

    for server in SERVERS:
        server_path = MCP_ROOT / server
        functions = load_complexity_report(server_path)

        for func in functions:
            cyclomatic = func.get('cyclomatic_complexity', 0)
            cognitive = func.get('cognitive_complexity', 0)

            # Filter: cyclomatic >15 OR cognitive >20
            if cyclomatic > 15 or cognitive > 20:
                high_complexity.append({
                    'server': server,
                    'name': func['name'],
                    'file': func['file'],
                    'line': func.get('line', '?'),
                    'cyclomatic': cyclomatic,
                    'cognitive': cognitive,
                    'severity': calculate_severity(cyclomatic, cognitive)
                })

    return sorted(high_complexity, key=lambda x: x['severity'], reverse=True)

def calculate_severity(cyclomatic, cognitive):
    """Calculate severity score (0-100)"""
    # Weighted average: cyclomatic (40%), cognitive (60%)
    return int((cyclomatic * 0.4) + (cognitive * 0.6))

def generate_markdown(targets):
    """Generate REFACTOR-TARGETS.md content"""
    lines = [
        "# Refactor Targets - High Complexity Code",
        "",
        "Functions with cyclomatic complexity >15 or cognitive complexity >20.",
        "",
        f"**Total targets found:** {len(targets)}",
        "",
        "## High-Complexity Functions",
        "",
        "| Severity | Server | Function | File:Line | Cyclomatic | Cognitive |",
        "|----------|--------|----------|-----------|------------|-----------|"
    ]

    for target in targets:
        severity_icon = "🔴" if target['severity'] > 40 else "🟡" if target['severity'] > 25 else "🟢"
        location = f"{target['file']}:{target['line']}"

        lines.append(
            f"| {severity_icon} {target['severity']} | {target['server']} | "
            f"`{target['name']}` | `{location}` | {target['cyclomatic']} | {target['cognitive']} |"
        )

    # Refactoring recommendations
    lines.extend([
        "",
        "## Refactoring Recommendations",
        "",
        "### Critical Priority (Severity >40)",
        ""
    ])

    critical = [t for t in targets if t['severity'] > 40]
    if critical:
        for target in critical:
            lines.append(f"- **{target['server']}**: `{target['name']}` - Consider breaking into smaller functions")
    else:
        lines.append("None")

    lines.extend([
        "",
        "### High Priority (Severity 25-40)",
        ""
    ])

    high = [t for t in targets if 25 < t['severity'] <= 40]
    if high:
        for target in high:
            lines.append(f"- **{target['server']}**: `{target['name']}` - Refactor for clarity")
    else:
        lines.append("None")

    lines.extend([
        "",
        "## Common Patterns to Simplify",
        "",
        "- Extract nested conditionals into helper functions",
        "- Replace complex if-else chains with pattern matching",
        "- Move validation logic to dedicated validators",
        "- Extract file I/O operations into utility modules",
        "- Simplify error handling with context managers"
    ])

    return "\n".join(lines)

if __name__ == "__main__":
    print("Generating REFACTOR-TARGETS.md...")
    targets = find_high_complexity()
    markdown = generate_markdown(targets)

    output_path = Path(__file__).parent.parent / "REFACTOR-TARGETS.md"
    output_path.write_text(markdown, encoding='utf-8')

    print(f"✅ Generated {output_path}")
    print(f"   Found {len(targets)} high-complexity functions")
