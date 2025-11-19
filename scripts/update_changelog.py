#!/usr/bin/env python3
"""
Changelog Update Script for Contentious Probate Manual & Toolkit

This script maintains a changelog of reference document changes:
- Tracks additions, modifications, and deletions
- Records reference updates
- Timestamps all changes
- Appends to _changelog.md

Usage:
    python scripts/update_changelog.py [--message "Description of changes"]

Output:
    docs/contentious-probate-manual/_changelog.md
"""

import os
import sys
from pathlib import Path
from datetime import datetime
import subprocess
import argparse


# Configuration
REPO_ROOT = Path(__file__).parent.parent
CHANGELOG_FILE = REPO_ROOT / "docs" / "contentious-probate-manual" / "_changelog.md"
REFERENCES_DIR = REPO_ROOT / "docs" / "references"


class ChangelogUpdater:
    """Updates the changelog with reference changes"""

    def __init__(self):
        self.changes = []

    def get_git_changes(self) -> dict:
        """Get changes from git"""
        try:
            # Get list of changed files in docs/references
            result = subprocess.run(
                ["git", "diff", "--name-status", "HEAD~1", "HEAD", "docs/references/"],
                cwd=REPO_ROOT,
                capture_output=True,
                text=True,
            )

            if result.returncode != 0:
                # Probably first commit or no previous commit
                return {"added": [], "modified": [], "deleted": []}

            changes = {"added": [], "modified": [], "deleted": []}

            for line in result.stdout.strip().split("\n"):
                if not line:
                    continue

                parts = line.split("\t")
                if len(parts) < 2:
                    continue

                status = parts[0]
                filepath = parts[1]

                # Skip README files
                if "README.md" in filepath:
                    continue

                # Categorize by status
                if status == "A":
                    changes["added"].append(filepath)
                elif status == "M":
                    changes["modified"].append(filepath)
                elif status == "D":
                    changes["deleted"].append(filepath)

            return changes

        except Exception as e:
            print(f"Warning: Could not get git changes: {e}")
            return {"added": [], "modified": [], "deleted": []}

    def format_change_entry(
        self, change_type: str, files: list, custom_message: str = None
    ) -> str:
        """Format a change entry"""
        if not files:
            return ""

        entry = []

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M UTC")
        entry.append(f"### {timestamp}\n\n")

        if custom_message:
            entry.append(f"{custom_message}\n\n")

        if change_type == "added":
            entry.append(f"**Added** ({len(files)}):\n\n")
        elif change_type == "modified":
            entry.append(f"**Modified** ({len(files)}):\n\n")
        elif change_type == "deleted":
            entry.append(f"**Deleted** ({len(files)}):\n\n")

        for filepath in files:
            filename = Path(filepath).name
            entry.append(f"- `{filename}`\n")

        entry.append("\n---\n\n")

        return "".join(entry)

    def create_changelog_header(self) -> str:
        """Create changelog header"""
        header = []
        header.append("# Changelog\n\n")
        header.append(
            "*This file tracks changes to reference materials in the "
            "Contentious Probate Manual & Toolkit.*\n\n"
        )
        header.append(
            "Changes are recorded automatically when updates are merged to the main branch.\n\n"
        )
        header.append("---\n\n")
        return "".join(header)

    def read_existing_changelog(self) -> str:
        """Read existing changelog content"""
        if CHANGELOG_FILE.exists():
            return CHANGELOG_FILE.read_text(encoding="utf-8")
        return ""

    def update_changelog(self, custom_message: str = None) -> None:
        """Update the changelog"""
        print("=" * 60)
        print("Changelog Updater")
        print("=" * 60)

        print("\nChecking for changes...")
        git_changes = self.get_git_changes()

        total_changes = sum(len(files) for files in git_changes.values())

        if total_changes == 0:
            print("No changes detected in reference files.")
            print("Changelog not updated.")
            return

        print(f"Found {total_changes} changes:")
        print(f"  Added: {len(git_changes['added'])}")
        print(f"  Modified: {len(git_changes['modified'])}")
        print(f"  Deleted: {len(git_changes['deleted'])}")

        print("\nUpdating changelog...")

        # Read existing changelog
        existing_content = self.read_existing_changelog()

        # If no existing changelog, create header
        if not existing_content:
            existing_content = self.create_changelog_header()
        elif not existing_content.startswith("# Changelog"):
            # Add header if missing
            existing_content = self.create_changelog_header() + existing_content

        # Generate new entries
        new_entries = []

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M UTC")
        new_entries.append(f"### {timestamp}\n\n")

        if custom_message:
            new_entries.append(f"**{custom_message}**\n\n")

        if git_changes["added"]:
            new_entries.append(f"**Added** ({len(git_changes['added'])}):\n\n")
            for filepath in git_changes["added"]:
                filename = Path(filepath).name
                new_entries.append(f"- `{filename}`\n")
            new_entries.append("\n")

        if git_changes["modified"]:
            new_entries.append(f"**Modified** ({len(git_changes['modified'])}):\n\n")
            for filepath in git_changes["modified"]:
                filename = Path(filepath).name
                new_entries.append(f"- `{filename}`\n")
            new_entries.append("\n")

        if git_changes["deleted"]:
            new_entries.append(f"**Deleted** ({len(git_changes['deleted'])}):\n\n")
            for filepath in git_changes["deleted"]:
                filename = Path(filepath).name
                new_entries.append(f"- `{filename}`\n")
            new_entries.append("\n")

        new_entries.append("---\n\n")

        # Insert new entries after header
        lines = existing_content.split("\n")
        header_end = 0

        # Find where to insert (after the --- following the header)
        for i, line in enumerate(lines):
            if line.strip() == "---" and i > 0:
                header_end = i + 1
                break

        # Insert new entries
        new_content = (
            "\n".join(lines[: header_end + 1])
            + "\n"
            + "".join(new_entries)
            + "\n".join(lines[header_end + 1 :])
        )

        # Save changelog
        CHANGELOG_FILE.parent.mkdir(parents=True, exist_ok=True)
        CHANGELOG_FILE.write_text(new_content, encoding="utf-8")

        print(f"Updated changelog: {CHANGELOG_FILE.relative_to(REPO_ROOT)}")
        print("\n✓ Changelog update complete!")

    def run(self, custom_message: str = None) -> None:
        """Run the changelog update"""
        self.update_changelog(custom_message)


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="Update changelog with reference changes"
    )
    parser.add_argument(
        "--message", type=str, help="Custom message to include in changelog"
    )

    args = parser.parse_args()

    updater = ChangelogUpdater()
    updater.run(custom_message=args.message)


if __name__ == "__main__":
    main()
