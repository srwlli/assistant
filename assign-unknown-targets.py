#!/usr/bin/env python3
"""
Assign 'unknown' target_project to stubs that couldn't be inferred
"""

import json
from pathlib import Path

# Stubs that couldn't be inferred (from previous run)
UNKNOWN_STUBS = [
    "ai-video-gen",
    "coderef-directory-rename",
    "coderef-tracking-api-mvp",
    "connection-to-all-llm",
    "consolidate-project-directories",
    "git-libraries",
    "mcp-config-investigation",
    "mcp-docs-workflow-refactor",
    "mcp-integrations",
    "mcp-usage-tracker",
    "organize-and-consolidate",
    "railway-config",
    "remove-utility-personas",
    "rename-start-feature-command",
    "reorganize-gits-projects",
    "track-and-note-commands",
    "work-order-folder-rename"
]

def assign_unknown():
    """Assign 'unknown' to stubs missing target_project"""
    project_root = Path(__file__).parent
    working_dir = project_root / "coderef" / "working"

    print("Assigning 'unknown' Target Projects")
    print("=" * 60)

    updated = 0

    for stub_name in UNKNOWN_STUBS:
        stub_path = working_dir / stub_name / "stub.json"

        if not stub_path.exists():
            print(f"[SKIP] {stub_name} - stub.json not found")
            continue

        with open(stub_path, 'r', encoding='utf-8') as f:
            stub = json.load(f)

        # Check if already has target_project
        if "target_project" in stub and stub["target_project"]:
            print(f"[SKIP] {stub_name} - already has target: {stub['target_project']}")
            continue

        # Assign 'unknown'
        stub["target_project"] = "unknown"

        with open(stub_path, 'w', encoding='utf-8') as f:
            json.dump(stub, f, indent=2, ensure_ascii=False)

        print(f"[UPDATED] {stub_name} -> unknown")
        updated += 1

    print("\n" + "=" * 60)
    print(f"[COMPLETE] Assigned 'unknown' to {updated} stubs")

if __name__ == "__main__":
    assign_unknown()
