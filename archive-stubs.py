#!/usr/bin/env python3
"""
Archive Stubs - Identify and move ~35 old/obsolete stubs to archived folder.

Archival Criteria:
1. Test/Example stubs - Contains "test", "example", "stub-location" in name
2. Already completed - Work documented as done
3. Obsolete/superseded - Old ideas no longer relevant
4. Low priority + old - Created before 2025-12 AND priority is low/medium
5. Duplicates - Similar feature names or descriptions

Conservative approach: Only archive clear candidates.
"""

import json
import os
import shutil
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Tuple

WORKING_DIR = Path(r"C:\Users\willh\Desktop\assistant\coderef\working")
ARCHIVE_DIR = Path(r"C:\Users\willh\Desktop\assistant\coderef\archived")

# Ensure archive directory exists
ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)

class ArchiveAnalysis:
    def __init__(self):
        self.stubs: Dict[str, Dict] = {}
        self.candidates: Dict[str, Tuple[str, str]] = {}  # {name: (reason, stub_id)}
        self.archive_report = []

    def load_stubs(self) -> int:
        """Load all stub.json files from working directory."""
        count = 0
        for stub_dir in WORKING_DIR.iterdir():
            if not stub_dir.is_dir():
                continue

            stub_file = stub_dir / "stub.json"
            if not stub_file.exists():
                continue

            try:
                with open(stub_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.stubs[stub_dir.name] = data
                    count += 1
            except Exception as e:
                print(f"Warning: Failed to read {stub_file}: {e}")

        return count

    def is_test_example(self, name: str, data: Dict) -> bool:
        """Check if stub is a test/example."""
        keywords = ["test", "example", "stub-location"]
        name_lower = name.lower()

        for keyword in keywords:
            if keyword in name_lower:
                return True

        # Check description for test indicators
        desc = data.get("description", "").lower()
        if any(k in desc for k in ["test ", "testing ", "example ", "verify stub"]):
            if "test" in name_lower or "example" in name_lower:
                return True

        return False

    def is_completed(self, data: Dict) -> bool:
        """Check if stub is marked as completed."""
        status = data.get("status", "").lower()
        if status in ["completed", "done", "archived"]:
            return True

        # Check if workorder completed
        context = data.get("context", {})
        if isinstance(context, dict):
            if context.get("status") in ["completed", "done"]:
                return True

        return False

    def is_obsolete_name(self, name: str) -> bool:
        """Check if name indicates obsolete/superseded work."""
        obsolete_keywords = [
            "deprecated",
            "remove-",
            "delete-",
            "redundant-",
            "duplicate-",
            "old-",
            "legacy-",
            "unused-",
            "stale-",
            "archived-",
            "deprecated-",
        ]

        name_lower = name.lower()
        for keyword in obsolete_keywords:
            if keyword in name_lower:
                return True

        return False

    def is_low_priority_old(self, data: Dict) -> bool:
        """Check if stub is low/medium priority AND created before 2025-12-20."""
        priority = data.get("priority", "").lower()
        if priority not in ["low", "medium"]:
            return False

        created = data.get("created", "")
        try:
            created_date = datetime.strptime(created, "%Y-%m-%d")
            # Archive if created before mid-December 2025 (gives 2-week buffer)
            if created_date < datetime(2025, 12, 20):
                return True
        except:
            pass

        return False

    def is_vague_exploration(self, name: str, data: Dict) -> bool:
        """Check if stub is vague exploration/brainstorm with no clear scope."""
        status = data.get("status", "").lower()
        if status not in ["brainstorming", "exploration", "research"]:
            return False

        # Very vague stubs without clear direction
        vague_keywords = [
            "ideas",
            "audit",
            "review",
            "investigation",
            "analysis",
            "improvements",
            "research",
        ]

        name_lower = name.lower()
        for keyword in vague_keywords:
            if keyword in name_lower:
                return True

        # Check description length - very short descriptions indicate incomplete planning
        description = data.get("description", "").strip()
        if status == "brainstorming" and len(description) < 50:
            return True

        return False

    def is_infrastructure_utility(self, name: str, data: Dict) -> bool:
        """Check if stub is infrastructure/utility without active priority."""
        category = data.get("category", "").lower()
        priority = data.get("priority", "").lower()
        status = data.get("status", "").lower()

        # Infrastructure/utility stubs with low/medium priority in planning stage
        if category in ["infrastructure", "utility", "refactor", "cleanup"]:
            if priority in ["low", "medium"] and status == "planning":
                # But exclude recent ones (less than 1 week old)
                created = data.get("created", "")
                try:
                    created_date = datetime.strptime(created, "%Y-%m-%d")
                    if created_date < datetime(2026, 1, 6):  # Older than 1 week from 2026-01-13
                        return True
                except:
                    pass

        return False

    def is_duplicate(self, name: str, data: Dict) -> bool:
        """Check if stub might be a duplicate of another active stub."""
        # List of clearly duplicate/related stubs
        duplicate_groups = [
            # Directory rename stubs (multiple versions)
            (["coderef-directory-rename", "work-order-folder-rename"], "Directory structure refactoring"),
            (["rename-execute-plan-to-align-plan", "rename-start-feature-command"], "Command renaming"),
            (["scanner-output-validation", "scanner-python-detection", "scanner-script-path-config"], "Scanner configuration"),
            (["websocket-live-update-test", "scriptboard-endpoints-test"], "Scriptboard testing"),
            (["test-and-fix-emojis", "test-stub-example", "testing-brief-entry-point"], "Testing infrastructure"),
            (["mcp-docs-workflow-refactor", "consolidate-foundation-docs-workflow"], "Docs consolidation"),
        ]

        for group, reason in duplicate_groups:
            if name in group and len(group) > 1:
                # Return True only if there are other stubs in this group with higher priority
                other_stubs = [s for s in group if s != name]
                if other_stubs:
                    for other in other_stubs:
                        if other in self.stubs:
                            other_data = self.stubs[other]
                            # Archive if other has higher or equal priority and created earlier/same time
                            other_priority = {"critical": 0, "high": 1, "medium": 2, "low": 3}.get(
                                other_data.get("priority", "low").lower(), 3
                            )
                            our_priority = {"critical": 0, "high": 1, "medium": 2, "low": 3}.get(
                                data.get("priority", "low").lower(), 3
                            )
                            if other_priority <= our_priority:
                                return True

        return False

    def analyze(self) -> None:
        """Analyze all stubs and identify archival candidates."""
        print(f"Analyzing {len(self.stubs)} stubs...\n")

        for name, data in sorted(self.stubs.items()):
            stub_id = data.get("stub_id", "UNKNOWN")
            reason = None

            # Check criteria in order (most specific to least specific)
            if self.is_test_example(name, data):
                reason = "TEST/EXAMPLE"
            elif self.is_completed(data):
                reason = "COMPLETED"
            elif self.is_obsolete_name(name):
                reason = "OBSOLETE_NAME"
            elif self.is_duplicate(name, data):
                reason = "DUPLICATE"
            elif self.is_vague_exploration(name, data):
                reason = "VAGUE_EXPLORATION"
            elif self.is_infrastructure_utility(name, data):
                reason = "INFRA_UTILITY_LOW"
            elif self.is_low_priority_old(data):
                reason = "LOW_PRIORITY_OLD"

            if reason:
                self.candidates[name] = (reason, stub_id)

    def archive(self) -> None:
        """Move identified stubs to archive directory."""
        if not self.candidates:
            print("No archival candidates identified.")
            return

        print(f"\nArchiving {len(self.candidates)} stubs:\n")
        print("-" * 80)

        archived_count = 0
        failed = []

        for name, (reason, stub_id) in sorted(self.candidates.items()):
            src_dir = WORKING_DIR / name
            dst_dir = ARCHIVE_DIR / name

            try:
                # Move directory
                if dst_dir.exists():
                    shutil.rmtree(dst_dir)

                shutil.move(str(src_dir), str(dst_dir))
                archived_count += 1

                status = "[OK]"
                print(f"{status:15} | {stub_id:12} | {reason:20} | {name}")

                self.archive_report.append({
                    "stub_id": stub_id,
                    "name": name,
                    "reason": reason,
                    "archived": True,
                    "timestamp": datetime.now().isoformat()
                })

            except Exception as e:
                failed.append((name, str(e)))
                print(f"[FAIL]          | {stub_id:12} | {reason:20} | {name}")
                print(f"  Error: {e}\n")

        print("-" * 80)
        print(f"\nArchival Summary:")
        print(f"  Successfully archived: {archived_count}/{len(self.candidates)}")
        print(f"  Failed: {len(failed)}/{len(self.candidates)}")

        if failed:
            print(f"\nFailed archives:")
            for name, error in failed:
                print(f"  - {name}: {error}")

    def generate_report(self) -> str:
        """Generate a detailed report of archived stubs."""
        report = []
        report.append("=" * 80)
        report.append("STUB ARCHIVAL REPORT")
        report.append("=" * 80)
        report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append(f"Total stubs archived: {len(self.archive_report)}\n")

        # Group by reason
        by_reason = {}
        for item in self.archive_report:
            reason = item["reason"]
            if reason not in by_reason:
                by_reason[reason] = []
            by_reason[reason].append(item)

        for reason in sorted(by_reason.keys()):
            items = by_reason[reason]
            report.append(f"\n{reason} ({len(items)} stubs)")
            report.append("-" * 80)

            for item in sorted(items, key=lambda x: x["stub_id"]):
                report.append(f"  {item['stub_id']:12} | {item['name']}")

        report.append("\n" + "=" * 80)
        report.append("ARCHIVAL CRITERIA REFERENCE")
        report.append("=" * 80)
        report.append("""
1. TEST/EXAMPLE
   - Name contains: test, example, stub-location
   - Purpose: Validation stubs for workflow testing

2. COMPLETED
   - Status marked as: completed, done, archived
   - Purpose: Work is finished, no longer needed

3. OBSOLETE_NAME
   - Name contains: deprecated, remove-, delete-, legacy-, unused-, etc.
   - Purpose: Old approaches no longer relevant

4. LOW_PRIORITY_OLD
   - Priority: low or medium
   - Created: before 2025-12-01
   - Purpose: Old backlog items with low urgency

5. DUPLICATE
   - Similar stubs in same functional area
   - Purpose: Consolidation - keep best version, archive redundant
        """)

        return "\n".join(report)

    def save_report(self) -> None:
        """Save report to file."""
        report_path = WORKING_DIR.parent / "ARCHIVAL_REPORT.txt"
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(self.generate_report())
        print(f"\nReport saved to: {report_path}")


def main():
    """Main execution."""
    print("\n" + "=" * 80)
    print("ARCHIVE STUBS - Conservative Identification & Archival")
    print("=" * 80)
    print(f"Working directory: {WORKING_DIR}")
    print(f"Archive directory: {ARCHIVE_DIR}\n")

    analysis = ArchiveAnalysis()

    # Load all stubs
    stub_count = analysis.load_stubs()
    print(f"Loaded {stub_count} stubs")

    # Analyze candidates
    analysis.analyze()
    print(f"Identified {len(analysis.candidates)} archival candidates (conservative)\n")

    if len(analysis.candidates) == 0:
        print("No candidates identified. Exiting.")
        return

    # List candidates before archiving
    print("ARCHIVAL CANDIDATES:")
    print("-" * 80)
    for name, (reason, stub_id) in sorted(analysis.candidates.items()):
        print(f"{stub_id:12} | {reason:20} | {name}")
    print("-" * 80 + "\n")

    # Archive stubs
    analysis.archive()

    # Generate and save report
    analysis.save_report()

    print("\n" + "=" * 80)
    print("ARCHIVAL COMPLETE")
    print("=" * 80)


if __name__ == "__main__":
    main()
