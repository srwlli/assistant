#!/usr/bin/env python3
"""
Generate PATTERNS-ANALYSIS.md - Pattern inconsistency detection
Compares patterns.json files across servers
"""

import json
from pathlib import Path
from collections import defaultdict

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

def load_patterns(server_path):
    """Load patterns.json from .coderef/reports/"""
    patterns_file = server_path / ".coderef" / "reports" / "patterns.json"
    if not patterns_file.exists():
        return {}

    with open(patterns_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data if isinstance(data, dict) else {}

def analyze_patterns():
    """Compare patterns across servers"""
    all_patterns = {}

    for server in SERVERS:
        server_path = MCP_ROOT / server
        patterns = load_patterns(server_path)
        all_patterns[server] = patterns

    return all_patterns

def compare_error_handling(all_patterns):
    """Compare error handling patterns"""
    error_patterns = {}

    for server, patterns in all_patterns.items():
        if 'error_handling' in patterns:
            error_patterns[server] = patterns['error_handling']

    return error_patterns

def compare_logging(all_patterns):
    """Compare logging patterns"""
    logging_patterns = {}

    for server, patterns in all_patterns.items():
        if 'logging' in patterns:
            logging_patterns[server] = patterns['logging']

    return logging_patterns

def compare_validation(all_patterns):
    """Compare validation patterns"""
    validation_patterns = {}

    for server, patterns in all_patterns.items():
        if 'validation' in patterns:
            validation_patterns[server] = patterns['validation']

    return validation_patterns

def generate_markdown(all_patterns):
    """Generate PATTERNS-ANALYSIS.md content"""
    lines = [
        "# Code Patterns Analysis",
        "",
        "Comparison of error handling, logging, and validation patterns across servers.",
        "",
        "## Pattern Coverage by Server",
        "",
        "| Server | Error Handling | Logging | Validation |",
        "|--------|----------------|---------|------------|"
    ]

    for server in SERVERS:
        patterns = all_patterns.get(server, {})
        has_error = "✅" if 'error_handling' in patterns else "❌"
        has_logging = "✅" if 'logging' in patterns else "❌"
        has_validation = "✅" if 'validation' in patterns else "❌"

        lines.append(f"| {server} | {has_error} | {has_logging} | {has_validation} |")

    # Error Handling Patterns
    lines.extend([
        "",
        "## Error Handling Patterns",
        ""
    ])

    error_patterns = compare_error_handling(all_patterns)
    if error_patterns:
        lines.append("| Server | Pattern Type | Count |")
        lines.append("|--------|--------------|-------|")

        for server, patterns in sorted(error_patterns.items()):
            pattern_type = patterns.get('type', 'Unknown')
            count = patterns.get('count', 0)
            lines.append(f"| {server} | {pattern_type} | {count} |")
    else:
        lines.append("No error handling patterns detected.")

    # Logging Patterns
    lines.extend([
        "",
        "## Logging Patterns",
        ""
    ])

    logging_patterns = compare_logging(all_patterns)
    if logging_patterns:
        lines.append("| Server | Logger Type | Count |")
        lines.append("|--------|-------------|-------|")

        for server, patterns in sorted(logging_patterns.items()):
            logger_type = patterns.get('type', 'Unknown')
            count = patterns.get('count', 0)
            lines.append(f"| {server} | {logger_type} | {count} |")
    else:
        lines.append("No logging patterns detected.")

    # Validation Patterns
    lines.extend([
        "",
        "## Validation Patterns",
        ""
    ])

    validation_patterns = compare_validation(all_patterns)
    if validation_patterns:
        lines.append("| Server | Validation Type | Count |")
        lines.append("|--------|-----------------|-------|")

        for server, patterns in sorted(validation_patterns.items()):
            validation_type = patterns.get('type', 'Unknown')
            count = patterns.get('count', 0)
            lines.append(f"| {server} | {validation_type} | {count} |")
    else:
        lines.append("No validation patterns detected.")

    # Standardization Recommendations
    lines.extend([
        "",
        "## Standardization Recommendations",
        "",
        "### Error Handling",
        "- Standardize exception types across servers",
        "- Use consistent error message formatting",
        "- Implement common error recovery strategies",
        "",
        "### Logging",
        "- Adopt unified logging framework (e.g., Python `logging`)",
        "- Standardize log levels (DEBUG, INFO, WARNING, ERROR)",
        "- Consistent log message structure",
        "",
        "### Validation",
        "- Create shared validation utilities",
        "- Use common schema validation (e.g., JSON Schema)",
        "- Standardize input sanitization patterns"
    ])

    return "\n".join(lines)

if __name__ == "__main__":
    print("Generating PATTERNS-ANALYSIS.md...")
    all_patterns = analyze_patterns()
    markdown = generate_markdown(all_patterns)

    output_path = Path(__file__).parent.parent / "PATTERNS-ANALYSIS.md"
    output_path.write_text(markdown, encoding='utf-8')

    print(f"✅ Generated {output_path}")
    print(f"   Analyzed {len(all_patterns)} servers")
