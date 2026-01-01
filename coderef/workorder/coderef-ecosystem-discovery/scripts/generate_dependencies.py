#!/usr/bin/env python3
"""
Generate DEPENDENCIES.md - Cross-server import matrix
Extracts import statements from all 7 servers' index.json files
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

def load_index(server_path):
    """Load index.json from server's .coderef directory"""
    index_file = server_path / ".coderef" / "index.json"
    if not index_file.exists():
        print(f"⚠️ Skipping {server_path.name}: index.json not found")
        return []

    with open(index_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def extract_imports(elements):
    """Extract all import statements from elements"""
    imports = set()
    for elem in elements:
        if 'imports' in elem and elem['imports']:
            imports.update(elem['imports'])
    return imports

def build_dependency_matrix():
    """Build cross-server dependency matrix"""
    matrix = defaultdict(lambda: defaultdict(list))

    for server in SERVERS:
        server_path = MCP_ROOT / server
        elements = load_index(server_path)

        if not elements:
            continue

        imports = extract_imports(elements)

        # Filter for cross-server imports
        for imp in imports:
            for target_server in SERVERS:
                if target_server != server and target_server.replace("/", "-") in imp:
                    matrix[server][target_server].append(imp)

    return matrix

def generate_markdown(matrix):
    """Generate DEPENDENCIES.md content"""
    lines = [
        "# Cross-Server Dependencies",
        "",
        "Generated from `.coderef/index.json` files across all 7 CodeRef MCP servers.",
        "",
        "## Import Matrix",
        "",
        "| From Server | To Server | Import Statements |",
        "|-------------|-----------|-------------------|"
    ]

    for from_server in sorted(matrix.keys()):
        for to_server in sorted(matrix[from_server].keys()):
            imports = matrix[from_server][to_server]
            import_str = ", ".join(f"`{i}`" for i in imports[:3])
            if len(imports) > 3:
                import_str += f" (+{len(imports)-3} more)"

            lines.append(f"| {from_server} | {to_server} | {import_str} |")

    # Detect circular dependencies
    lines.extend(["", "## Circular Dependencies", ""])
    circular = []
    for from_srv in matrix:
        for to_srv in matrix[from_srv]:
            if to_srv in matrix and from_srv in matrix[to_srv]:
                if (to_srv, from_srv) not in circular:
                    circular.append((from_srv, to_srv))

    if circular:
        for srv_a, srv_b in circular:
            lines.append(f"⚠️ **{srv_a} ↔ {srv_b}** (circular)")
    else:
        lines.append("None detected ✅")

    return "\n".join(lines)

if __name__ == "__main__":
    print("Generating DEPENDENCIES.md...")
    matrix = build_dependency_matrix()
    markdown = generate_markdown(matrix)

    output_path = Path(__file__).parent.parent / "DEPENDENCIES.md"
    output_path.write_text(markdown, encoding='utf-8')

    print(f"✅ Generated {output_path}")
    print(f"   Found {len(matrix)} servers with dependencies")
