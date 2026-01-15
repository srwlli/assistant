#!/usr/bin/env python3
"""
Stub Migration Script
Fixes common validation issues in stub.json files:
1. Convert "status": "stub" → "status": "planning"
2. Fix date format: ISO 8601 → YYYY-MM-DD
3. Assign missing stub_id values
4. Fix invalid categories to valid enums
"""

import json
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple

# Valid enums per schema
VALID_STATUSES = ['planning', 'ready', 'blocked', 'promoted', 'abandoned']
VALID_CATEGORIES = ['feature', 'enhancement', 'bugfix', 'infrastructure', 'documentation', 'refactor', 'research']

# Category mapping for invalid values
CATEGORY_MAPPING = {
    'idea': 'feature',
    'improvement': 'enhancement',
    'persona': 'feature',
    'test': 'infrastructure',
    'investigation': 'research',
    'config': 'infrastructure',
    'utility': 'infrastructure',
    'system': 'infrastructure'
}

def extract_date_from_iso8601(iso_date: str) -> str:
    """Extract YYYY-MM-DD from ISO 8601 timestamp."""
    try:
        # Handle formats like "2025-12-28T06:37:00Z" or "2025-12-28T06:37:00"
        match = re.match(r'(\d{4}-\d{2}-\d{2})', iso_date)
        if match:
            return match.group(1)

        # Try parsing as datetime
        dt = datetime.fromisoformat(iso_date.replace('Z', '+00:00'))
        return dt.strftime('%Y-%m-%d')
    except:
        # If parsing fails, return today's date
        return datetime.now().strftime('%Y-%m-%d')

def get_next_stub_id() -> Tuple[str, int]:
    """Read projects.md and get the next STUB-ID."""
    projects_md = Path(r'C:\Users\willh\Desktop\assistant\projects.md')

    if not projects_md.exists():
        return "STUB-084", 84  # Default if file doesn't exist

    content = projects_md.read_text(encoding='utf-8')

    # Find "Next STUB-ID: STUB-XXX"
    match = re.search(r'Next STUB-ID: STUB-(\d{3})', content)
    if match:
        next_id = int(match.group(1))
        return f"STUB-{next_id:03d}", next_id

    return "STUB-084", 84  # Default

def update_projects_md(new_next_id: int):
    """Update the Next STUB-ID counter in projects.md."""
    projects_md = Path(r'C:\Users\willh\Desktop\assistant\projects.md')

    if not projects_md.exists():
        return

    content = projects_md.read_text(encoding='utf-8')

    # Update the counter
    updated = re.sub(
        r'Next STUB-ID: STUB-\d{3}',
        f'Next STUB-ID: STUB-{new_next_id:03d}',
        content
    )

    # Update timestamp
    updated = re.sub(
        r'Last updated: \d{4}-\d{2}-\d{2}',
        f'Last updated: {datetime.now().strftime("%Y-%m-%d")}',
        updated
    )

    projects_md.write_text(updated, encoding='utf-8')

def migrate_stub(stub_path: Path, stub_id_counter: List[int]) -> Dict[str, List[str]]:
    """
    Migrate a single stub.json file.
    Returns dict of changes made.
    """
    changes = {
        'status_fixed': [],
        'date_fixed': [],
        'stub_id_added': [],
        'category_fixed': [],
        'errors': []
    }

    try:
        # Read stub
        stub = json.loads(stub_path.read_text(encoding='utf-8'))
        modified = False

        # Fix 1: Status "stub" → "planning"
        if stub.get('status') == 'stub':
            stub['status'] = 'planning'
            changes['status_fixed'].append(f"Changed 'stub' → 'planning'")
            modified = True

        # Fix 2: Date format (created field)
        if 'created' in stub:
            created = stub['created']
            # Check if it's ISO 8601 format (contains 'T' or 'Z')
            if 'T' in created or 'Z' in created:
                new_date = extract_date_from_iso8601(created)
                stub['created'] = new_date
                changes['date_fixed'].append(f"Fixed date: {created} → {new_date}")
                modified = True

        # Fix 3: Missing stub_id
        if 'stub_id' not in stub or not stub['stub_id']:
            next_id = f"STUB-{stub_id_counter[0]:03d}"
            stub['stub_id'] = next_id
            changes['stub_id_added'].append(f"Added stub_id: {next_id}")
            stub_id_counter[0] += 1
            modified = True

        # Fix 4: Invalid categories
        if 'category' in stub:
            category = stub['category']
            if category not in VALID_CATEGORIES:
                if category in CATEGORY_MAPPING:
                    new_category = CATEGORY_MAPPING[category]
                    stub['category'] = new_category
                    changes['category_fixed'].append(f"Remapped '{category}' → '{new_category}'")
                    modified = True
                else:
                    # Default to 'feature' for unknown categories
                    stub['category'] = 'feature'
                    changes['category_fixed'].append(f"Unknown category '{category}' → 'feature'")
                    modified = True

        # Save if modified
        if modified:
            stub_path.write_text(json.dumps(stub, indent=2), encoding='utf-8')

    except Exception as e:
        changes['errors'].append(str(e))

    return changes

def main():
    """Main migration function."""
    print("=" * 80)
    print("STUB MIGRATION SCRIPT")
    print("=" * 80)
    print()

    # Get starting stub_id counter
    next_stub_str, next_stub_num = get_next_stub_id()
    print(f"Starting stub_id counter: {next_stub_str}")
    print()

    # Use list to pass by reference
    stub_id_counter = [next_stub_num]

    # Find all stub.json files
    working_dir = Path(r'C:\Users\willh\Desktop\assistant\coderef\working')
    stub_files = list(working_dir.glob('**/stub.json'))

    print(f"Found {len(stub_files)} stub.json files")
    print()

    # Track overall stats
    total_changes = {
        'status_fixed': 0,
        'date_fixed': 0,
        'stub_id_added': 0,
        'category_fixed': 0,
        'errors': 0,
        'files_modified': 0
    }

    detailed_log = []

    # Migrate each stub
    for stub_path in stub_files:
        feature_name = stub_path.parent.name
        changes = migrate_stub(stub_path, stub_id_counter)

        # Check if any changes were made
        has_changes = any(changes[k] for k in ['status_fixed', 'date_fixed', 'stub_id_added', 'category_fixed'])

        if has_changes:
            total_changes['files_modified'] += 1
            log_entry = [f"\n{feature_name}:"]

            for change_type in ['status_fixed', 'date_fixed', 'stub_id_added', 'category_fixed']:
                if changes[change_type]:
                    total_changes[change_type] += len(changes[change_type])
                    for change in changes[change_type]:
                        log_entry.append(f"  - {change}")

            detailed_log.extend(log_entry)

        if changes['errors']:
            total_changes['errors'] += len(changes['errors'])
            detailed_log.append(f"\n{feature_name}: ERROR - {changes['errors'][0]}")

    # Update projects.md with new counter
    if stub_id_counter[0] > next_stub_num:
        update_projects_md(stub_id_counter[0])
        print(f"Updated projects.md: Next STUB-ID -> STUB-{stub_id_counter[0]:03d}")
        print()

    # Print summary
    print("=" * 80)
    print("MIGRATION SUMMARY")
    print("=" * 80)
    print(f"Files modified: {total_changes['files_modified']}/{len(stub_files)}")
    print(f"Status values fixed: {total_changes['status_fixed']}")
    print(f"Date formats fixed: {total_changes['date_fixed']}")
    print(f"Stub IDs added: {total_changes['stub_id_added']}")
    print(f"Categories fixed: {total_changes['category_fixed']}")
    print(f"Errors encountered: {total_changes['errors']}")
    print()

    # Print detailed log
    if detailed_log:
        print("=" * 80)
        print("DETAILED CHANGES")
        print("=" * 80)
        for line in detailed_log:
            print(line)
        print()

    # Save report
    report_path = Path(r'C:\Users\willh\Desktop\assistant\STUB_MIGRATION_REPORT.txt')
    report_lines = [
        "STUB MIGRATION REPORT",
        "=" * 80,
        f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"Total stubs: {len(stub_files)}",
        f"Files modified: {total_changes['files_modified']}",
        "",
        "Changes:",
        f"  - Status values fixed ('stub' → 'planning'): {total_changes['status_fixed']}",
        f"  - Date formats fixed (ISO 8601 → YYYY-MM-DD): {total_changes['date_fixed']}",
        f"  - Stub IDs added: {total_changes['stub_id_added']}",
        f"  - Categories remapped: {total_changes['category_fixed']}",
        f"  - Errors: {total_changes['errors']}",
        "",
        "Stub ID Counter:",
        f"  - Before: STUB-{next_stub_num:03d}",
        f"  - After: STUB-{stub_id_counter[0]:03d}",
        f"  - IDs assigned: {stub_id_counter[0] - next_stub_num}",
        "",
        "=" * 80,
        "DETAILED CHANGES",
        "=" * 80,
    ]
    report_lines.extend(detailed_log)

    report_path.write_text('\n'.join(report_lines), encoding='utf-8')
    print(f"Report saved to: {report_path}")
    print()
    print("[DONE] Migration complete!")

if __name__ == '__main__':
    main()
