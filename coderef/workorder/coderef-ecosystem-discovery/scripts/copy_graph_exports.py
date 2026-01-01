#!/usr/bin/env python3
"""
Copy graph.json exports from all servers to workorder exports/ folder
"""

import shutil
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

def copy_graph_exports():
    """Copy graph.json from each server to exports/ folder"""
    output_dir = Path(__file__).parent.parent / "exports"
    output_dir.mkdir(exist_ok=True)

    copied = []
    missing = []

    for server in SERVERS:
        server_path = MCP_ROOT / server
        graph_file = server_path / ".coderef" / "exports" / "graph.json"

        if not graph_file.exists():
            print(f"⚠️ Skipping {server}: graph.json not found")
            missing.append(server)
            continue

        # Create safe filename (replace / with -)
        safe_server_name = server.replace("/", "-")
        dest_file = output_dir / f"graph-{safe_server_name}.json"

        shutil.copy2(graph_file, dest_file)
        copied.append(server)
        print(f"✅ Copied {server} → {dest_file.name}")

    return copied, missing

def generate_readme(copied, missing):
    """Generate README for exports/ folder"""
    lines = [
        "# Graph Exports",
        "",
        "Dependency graphs from all CodeRef MCP servers (JSON format).",
        "",
        "## Available Exports",
        ""
    ]

    for server in sorted(copied):
        safe_name = server.replace("/", "-")
        lines.append(f"- `graph-{safe_name}.json` - {server}")

    if missing:
        lines.extend([
            "",
            "## Missing Exports",
            ""
        ])
        for server in sorted(missing):
            lines.append(f"- {server} (graph.json not found)")

    lines.extend([
        "",
        "## Usage",
        "",
        "These JSON files can be imported into:",
        "- Neo4j (graph database)",
        "- GraphQL schema generators",
        "- Custom analysis tools",
        "- Dependency visualization tools"
    ])

    return "\n".join(lines)

if __name__ == "__main__":
    print("Copying graph.json exports...")
    copied, missing = copy_graph_exports()

    readme_content = generate_readme(copied, missing)
    readme_path = Path(__file__).parent.parent / "exports" / "README.md"
    readme_path.write_text(readme_content, encoding='utf-8')

    print(f"\n✅ Copied {len(copied)} graph exports")
    if missing:
        print(f"⚠️ Missing {len(missing)} exports: {', '.join(missing)}")
    print(f"✅ Generated {readme_path}")
