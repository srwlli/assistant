#!/usr/bin/env python3
"""
create-coderef-structure.py - Create Universal coderef/ Directory Structure

Creates the standard coderef/ directory structure for any project.
Only creates directories, not files.

Usage:
    python scripts/create-coderef-structure.py [project_path]
    python scripts/create-coderef-structure.py C:/Users/willh/Desktop/projects/my-project
"""

import sys
from pathlib import Path


def create_coderef_structure(project_path: str):
    """
    Create the universal coderef/ directory structure.

    Structure:
    {project}/coderef/
    ├── workorder/
    ├── archived/
    ├── foundation/
    │   └── docs/
    ├── user/
    └── standards/
    """
    project = Path(project_path).resolve()

    if not project.exists():
        print(f"[ERROR] Project path does not exist: {project}")
        sys.exit(1)

    coderef_dir = project / 'coderef'
    print(f"\n[*] Creating coderef/ structure in: {project}")
    print(f"[*] Target directory: {coderef_dir}\n")

    # Define directory structure
    directories = [
        coderef_dir / 'workorder',
        coderef_dir / 'archived',
        coderef_dir / 'foundation' / 'docs',
        coderef_dir / 'user',
        coderef_dir / 'standards',
    ]

    # Create directories
    created = 0
    skipped = 0

    for directory in directories:
        if directory.exists():
            print(f"[SKIP] {directory.relative_to(project)} (already exists)")
            skipped += 1
        else:
            directory.mkdir(parents=True, exist_ok=True)
            print(f"[OK]   {directory.relative_to(project)}")
            created += 1

    # Summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print(f"Created: {created}")
    print(f"Skipped: {skipped}")
    print(f"\nCoderef directory: {coderef_dir}")

    # Print structure
    print("\n" + "="*60)
    print("DIRECTORY STRUCTURE")
    print("="*60)
    print_tree(coderef_dir)


def print_tree(directory: Path, prefix: str = "", max_depth: int = 3, current_depth: int = 0):
    """Print directory tree structure."""
    if current_depth >= max_depth or not directory.exists():
        return

    try:
        items = sorted(directory.iterdir(), key=lambda x: (not x.is_dir(), x.name))
        for i, item in enumerate(items):
            is_last = i == len(items) - 1
            connector = "+-- " if is_last else "|-- "

            if item.is_dir():
                print(f"{prefix}{connector}{item.name}/")
                extension = "    " if is_last else "|   "
                print_tree(item, prefix + extension, max_depth, current_depth + 1)
    except PermissionError:
        pass


if __name__ == "__main__":
    if len(sys.argv) > 1:
        project_path = sys.argv[1]
    else:
        # Interactive mode
        project_path = input("Enter project path: ").strip()
        if not project_path:
            print("Using current directory")
            project_path = "."

    create_coderef_structure(project_path)
