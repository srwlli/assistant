#!/usr/bin/env python3
"""
Generate ECOSYSTEM-ARCHITECTURE.mmd - Visual ecosystem diagram
Combines dependency data into single Mermaid diagram
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

def build_dependency_graph():
    """Build dependency graph for Mermaid"""
    dependencies = defaultdict(set)

    for server in SERVERS:
        server_path = MCP_ROOT / server
        elements = load_index(server_path)

        if not elements:
            continue

        imports = extract_imports(elements)

        # Find cross-server dependencies
        for imp in imports:
            for target_server in SERVERS:
                if target_server != server and target_server.replace("/", "-") in imp:
                    dependencies[server].add(target_server)

    return dependencies

def generate_mermaid(dependencies):
    """Generate Mermaid diagram"""
    lines = [
        "graph TD",
        "    %% CodeRef Ecosystem Architecture",
        ""
    ]

    # Define nodes
    node_styles = {
        "coderef-context": "context[Context<br/>Code Intelligence]",
        "coderef-docs": "docs[Docs<br/>Documentation]",
        "coderef-personas": "personas[Personas<br/>Expert Agents]",
        "coderef-workflow": "workflow[Workflow<br/>Planning & Orchestration]",
        "coderef-testing": "testing[Testing<br/>Test Automation]",
        "papertrail": "papertrail[Papertrail<br/>Audit Trail]",
        "archived/coderef-mcp": "archived[Archived<br/>Legacy MCP]"
    }

    for server, style in node_styles.items():
        lines.append(f"    {style}")

    lines.append("")

    # Add dependencies
    for from_server, to_servers in sorted(dependencies.items()):
        from_id = from_server.replace("/", "-").replace("coderef-", "")
        for to_server in sorted(to_servers):
            to_id = to_server.replace("/", "-").replace("coderef-", "")
            lines.append(f"    {from_id} --> {to_id}")

    # Styling
    lines.extend([
        "",
        "    %% Styling",
        "    classDef core fill:#4CAF50,stroke:#2E7D32,color:#fff",
        "    classDef support fill:#2196F3,stroke:#1565C0,color:#fff",
        "    classDef archived fill:#9E9E9E,stroke:#616161,color:#fff",
        "",
        "    class context,docs,workflow core",
        "    class personas,testing,papertrail support",
        "    class archived archived"
    ])

    return "\n".join(lines)

def generate_markdown(mermaid_diagram, dependencies):
    """Generate complete markdown file"""
    lines = [
        "# CodeRef Ecosystem Architecture",
        "",
        "Visual representation of all 7 MCP servers and their dependencies.",
        "",
        "```mermaid",
        mermaid_diagram,
        "```",
        "",
        "## Legend",
        "",
        "- **Core Servers** (Green): Primary functionality - context, docs, workflow",
        "- **Support Servers** (Blue): Secondary features - personas, testing, papertrail",
        "- **Archived** (Gray): Legacy/deprecated servers",
        "",
        "## Dependency Summary",
        ""
    ]

    total_deps = sum(len(targets) for targets in dependencies.values())
    lines.append(f"- **Total Dependencies:** {total_deps}")
    lines.append(f"- **Servers with Dependencies:** {len(dependencies)}")
    lines.append("")

    for server in sorted(dependencies.keys()):
        targets = sorted(dependencies[server])
        lines.append(f"- **{server}** → {', '.join(targets)}")

    return "\n".join(lines)

if __name__ == "__main__":
    print("Generating ECOSYSTEM-ARCHITECTURE.mmd...")
    dependencies = build_dependency_graph()
    mermaid = generate_mermaid(dependencies)
    markdown = generate_markdown(mermaid, dependencies)

    output_path = Path(__file__).parent.parent / "ECOSYSTEM-ARCHITECTURE.md"
    output_path.write_text(markdown, encoding='utf-8')

    print(f"✅ Generated {output_path}")
    print(f"   {len(SERVERS)} servers, {sum(len(t) for t in dependencies.values())} dependencies")
