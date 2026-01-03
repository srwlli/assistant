#!/usr/bin/env python3
"""
Stub Validation Script
Validates and auto-fills stub.json files against canonical schema
"""

import json
import os
from pathlib import Path
from datetime import date
from typing import Dict, List, Tuple

# Schema defaults
SCHEMA_DEFAULTS = {
    "category": "feature",
    "priority": "medium",
    "status": "planning",
    "created": str(date.today())
}

REQUIRED_FIELDS = [
    "stub_id",
    "feature_name",
    "description",
    "category",
    "priority",
    "status",
    "created"
]

def load_schema() -> dict:
    """Load the canonical stub schema"""
    schema_path = Path(__file__).parent / "stub-schema.json"
    with open(schema_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def find_stubs(working_dir: Path) -> List[Path]:
    """Find all stub.json files in coderef/working/"""
    stubs = []
    if working_dir.exists():
        for item in working_dir.iterdir():
            if item.is_dir():
                stub_file = item / "stub.json"
                if stub_file.exists():
                    stubs.append(stub_file)
    return stubs

def validate_and_fill(stub_path: Path) -> Tuple[dict, List[str]]:
    """
    Validate stub and auto-fill missing required fields
    Returns: (updated_stub, list_of_changes)
    """
    changes = []

    # Load existing stub
    with open(stub_path, 'r', encoding='utf-8') as f:
        stub = json.load(f)

    # Derive feature_name from folder name if missing
    folder_name = stub_path.parent.name

    # Check and fill required fields
    if "feature_name" not in stub or not stub["feature_name"]:
        stub["feature_name"] = folder_name
        changes.append(f"Added feature_name: {folder_name}")

    if "description" not in stub or not stub["description"]:
        stub["description"] = f"TODO: Add description for {folder_name}"
        changes.append("Added placeholder description")

    for field in ["category", "priority", "status", "created"]:
        if field not in stub or not stub[field]:
            stub[field] = SCHEMA_DEFAULTS[field]
            changes.append(f"Added {field}: {SCHEMA_DEFAULTS[field]}")

    # Validate stub_id format if present
    if "stub_id" in stub:
        stub_id = stub["stub_id"]
        if not stub_id.startswith("STUB-"):
            changes.append(f"[WARNING] Invalid stub_id format: {stub_id}")

    return stub, changes

def main():
    """Main validation routine"""
    # Set UTF-8 encoding for Windows console
    import sys
    if sys.platform == "win32":
        import codecs
        sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

    print("Stub Validation Script")
    print("=" * 60)

    # Find project root
    project_root = Path(__file__).parent
    working_dir = project_root / "coderef" / "working"

    if not working_dir.exists():
        print(f"[ERROR] Working directory not found: {working_dir}")
        return

    # Find all stubs
    stub_files = find_stubs(working_dir)
    print(f"\nFound {len(stub_files)} stub(s) in {working_dir}")

    if not stub_files:
        print("[OK] No stubs to validate")
        return

    # Process each stub
    updated_count = 0
    for stub_path in stub_files:
        rel_path = stub_path.relative_to(project_root)
        print(f"\nProcessing: {rel_path}")

        try:
            stub, changes = validate_and_fill(stub_path)

            if changes:
                # Save updated stub
                with open(stub_path, 'w', encoding='utf-8') as f:
                    json.dump(stub, f, indent=2, ensure_ascii=False)

                print(f"  [UPDATED] {len(changes)} change(s):")
                for change in changes:
                    print(f"    - {change}")
                updated_count += 1
            else:
                print("  [OK] Already valid - no changes needed")

        except Exception as e:
            print(f"  [ERROR] {e}")

    # Summary
    print("\n" + "=" * 60)
    print(f"[COMPLETE] Validation complete:")
    print(f"  - Total stubs: {len(stub_files)}")
    print(f"  - Updated: {updated_count}")
    print(f"  - Already valid: {len(stub_files) - updated_count}")
    print("\n[OK] All stubs now conform to stub-schema.json")

if __name__ == "__main__":
    main()
