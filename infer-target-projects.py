#!/usr/bin/env python3
"""
Target Project Inference Script
Scans all stubs and intelligently assigns target_project based on feature context
"""

import json
import os
from pathlib import Path
from typing import Dict, Optional

# Project inference rules
PROJECT_KEYWORDS = {
    "coderef-dashboard": ["dashboard", "widget", "ui", "frontend", "tracking-widget"],
    "assistant": ["orchestrator", "assistant", "terminal", "workorder-handoff", "stub-"],
    "scriptboard": ["scriptboard", "clipboard", "companion"],
    "gridiron": ["gridiron", "nfl", "franchise", "team-page"],
    "scrapper": ["scrapper", "scraping", "data-collection"],
    "noted": ["noted", "notes", "markdown"],
    "coderef-workflow": ["workflow", "create-plan", "execute-plan", "deliverables", "archive-feature"],
    "coderef-docs": ["docs", "documentation", "foundation-docs", "standards", "changelog"],
    "coderef-context": ["coderef-context", "context", "analysis", "complexity"],
    "personas-mcp": ["persona", "agent", "role-context"],
    "coderef-mcp": ["coderef-mcp", "coderef-system"],
    "multi-tenant": ["multi-tenant", "saas", "business-dash"],
    "app-documents": ["app-documents", "documents"]
}

def infer_target_project(feature_name: str, description: str) -> Optional[str]:
    """
    Infer target project based on feature name and description
    Returns project name or None if can't infer
    """
    text = f"{feature_name} {description}".lower()

    # Check each project's keywords
    matches = {}
    for project, keywords in PROJECT_KEYWORDS.items():
        score = sum(1 for keyword in keywords if keyword in text)
        if score > 0:
            matches[project] = score

    if not matches:
        return None

    # Return project with highest score
    return max(matches.items(), key=lambda x: x[1])[0]

def scan_and_infer():
    """Scan all stubs and infer missing target_project fields"""
    project_root = Path(__file__).parent
    working_dir = project_root / "coderef" / "working"

    if not working_dir.exists():
        print(f"[ERROR] Working directory not found: {working_dir}")
        return

    # Find all stubs
    stub_files = []
    for item in working_dir.iterdir():
        if item.is_dir():
            stub_file = item / "stub.json"
            if stub_file.exists():
                stub_files.append(stub_file)

    print(f"Target Project Inference")
    print("=" * 60)
    print(f"\nFound {len(stub_files)} stubs\n")

    missing_count = 0
    inferred_count = 0
    skipped_count = 0

    updates = []

    for stub_path in stub_files:
        with open(stub_path, 'r', encoding='utf-8') as f:
            stub = json.load(f)

        feature_name = stub.get("feature_name", stub_path.parent.name)
        has_target = "target_project" in stub and stub["target_project"]

        if has_target:
            # Already has target_project
            continue

        missing_count += 1

        # Infer target project
        description = stub.get("description", "")
        inferred = infer_target_project(feature_name, description)

        if inferred:
            stub["target_project"] = inferred

            # Save updated stub
            with open(stub_path, 'w', encoding='utf-8') as f:
                json.dump(stub, f, indent=2, ensure_ascii=False)

            rel_path = stub_path.relative_to(project_root)
            print(f"[INFERRED] {feature_name}")
            print(f"  File: {rel_path}")
            print(f"  Target: {inferred}")
            print()

            inferred_count += 1
            updates.append({
                "feature": feature_name,
                "target": inferred
            })
        else:
            print(f"[SKIPPED] {feature_name}")
            print(f"  Reason: Could not infer target project")
            print(f"  Description: {description[:80]}...")
            print()
            skipped_count += 1

    # Summary
    print("=" * 60)
    print(f"[COMPLETE] Target Project Inference:")
    print(f"  - Total stubs: {len(stub_files)}")
    print(f"  - Already had target: {len(stub_files) - missing_count}")
    print(f"  - Missing target: {missing_count}")
    print(f"  - Inferred successfully: {inferred_count}")
    print(f"  - Could not infer: {skipped_count}")

    if updates:
        print(f"\n[UPDATES] {inferred_count} stubs updated:")
        for update in updates:
            print(f"  - {update['feature']} → {update['target']}")

if __name__ == "__main__":
    scan_and_infer()
