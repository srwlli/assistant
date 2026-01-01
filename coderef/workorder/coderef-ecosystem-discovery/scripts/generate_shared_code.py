#!/usr/bin/env python3
"""
Generate SHARED-CODE.md - Duplicated code analysis
Finds functions/classes with same names across servers
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

def find_duplicates():
    """Find functions/classes with same names across servers"""
    name_to_servers = defaultdict(list)

    for server in SERVERS:
        server_path = MCP_ROOT / server
        elements = load_index(server_path)

        for elem in elements:
            # Skip dependency packages (not our code)
            file_path = elem.get('file', '')
            if any(x in file_path for x in ['.venv', 'node_modules', '__pycache__', 'site-packages']):
                continue

            if elem['type'] in ['function', 'class', 'component']:
                name = elem['name']
                location = f"{server}:{elem['file']}:{elem.get('line', '?')}"
                name_to_servers[name].append(location)

    # Filter for duplicates (appear in 2+ servers)
    duplicates = {name: locs for name, locs in name_to_servers.items() if len(locs) >= 2}
    return duplicates

def generate_markdown(duplicates):
    """Generate SHARED-CODE.md content"""
    lines = [
        "# Shared Code Analysis",
        "",
        "Functions, classes, and components that appear in multiple servers.",
        "",
        f"**Total duplicates found:** {len(duplicates)}",
        "",
        "## Duplicate Inventory",
        "",
        "| Name | Type | Locations | Recommendation |",
        "|------|------|-----------|----------------|"
    ]

    # Sort by number of occurrences (most duplicated first)
    sorted_dupes = sorted(duplicates.items(), key=lambda x: len(x[1]), reverse=True)

    for name, locations in sorted_dupes:
        # Infer type from first location
        elem_type = "function"  # default
        if "Component" in name or name[0].isupper():
            elem_type = "class/component"

        loc_str = "<br>".join(f"`{loc}`" for loc in locations[:3])
        if len(locations) > 3:
            loc_str += f"<br>*+{len(locations)-3} more*"

        # Recommendation based on duplication count
        if len(locations) >= 4:
            recommendation = "🔴 **Move to shared library**"
        elif len(locations) == 3:
            recommendation = "🟡 Consider consolidation"
        else:
            recommendation = "🟢 Acceptable duplication"

        lines.append(f"| `{name}` | {elem_type} | {loc_str} | {recommendation} |")

    # Summary recommendations
    lines.extend([
        "",
        "## Consolidation Recommendations",
        "",
        "### High Priority (4+ duplicates)",
        ""
    ])

    high_priority = [name for name, locs in sorted_dupes if len(locs) >= 4]
    if high_priority:
        for name in high_priority:
            lines.append(f"- `{name}` - Found in {len(duplicates[name])} servers")
    else:
        lines.append("None")

    lines.extend(["", "### Shared Library Candidates", ""])
    lines.append("Consider creating `coderef-shared` package for:")
    lines.append("- Common generators (planning, docs, analysis)")
    lines.append("- Utility functions (path handling, JSON parsing)")
    lines.append("- Shared data models (plan structure, metadata)")

    return "\n".join(lines)

if __name__ == "__main__":
    print("Generating SHARED-CODE.md...")
    duplicates = find_duplicates()
    markdown = generate_markdown(duplicates)

    output_path = Path(__file__).parent.parent / "SHARED-CODE.md"
    output_path.write_text(markdown, encoding='utf-8')

    print(f"✅ Generated {output_path}")
    print(f"   Found {len(duplicates)} duplicated code elements")
