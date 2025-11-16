#!/usr/bin/env python3
"""
Reference Index Generator for Contentious Probate Manual & Toolkit

This script generates a comprehensive reference index from metadata files:
- Reads all metadata files
- Categorizes references by type
- Sorts chronologically or alphabetically
- Generates formatted markdown output
- Creates _references-and-authorities.md in the manual directory

Usage:
    python scripts/generate_reference_index.py

Output:
    docs/contentious-probate-manual/_references-and-authorities.md
"""

import os
import sys
from pathlib import Path
from typing import Dict, List
from datetime import datetime
import re
import yaml


# Configuration
REPO_ROOT = Path(__file__).parent.parent
METADATA_DIR = REPO_ROOT / "docs" / "references" / "metadata"
OUTPUT_FILE = REPO_ROOT / "docs" / "contentious-probate-manual" / "_references-and-authorities.md"

TYPE_LABELS = {
    "statute": "Legislation",
    "case": "Case Law",
    "form": "Court Forms",
    "guidance": "Official Guidance",
    "practice-direction": "Practice Directions",
    "procedural-rule": "Procedural Rules",
}

TYPE_ORDER = [
    "statute",
    "case",
    "procedural-rule",
    "practice-direction",
    "guidance",
    "form",
]


class ReferenceIndexGenerator:
    """Generates comprehensive reference index"""

    def __init__(self):
        self.references: Dict[str, List[Dict]] = {
            ref_type: [] for ref_type in TYPE_ORDER
        }

    def parse_yaml_frontmatter(self, content: str) -> Dict:
        """Parse YAML front matter from markdown content"""
        pattern = r"^---\s*\n(.*?)\n---\s*\n(.*)$"
        match = re.match(pattern, content, re.DOTALL)

        if not match:
            return {}

        yaml_content = match.group(1)

        try:
            metadata = yaml.safe_load(yaml_content)
            return metadata or {}
        except yaml.YAMLError:
            return {}

    def load_metadata_files(self) -> None:
        """Load all metadata files"""
        if not METADATA_DIR.exists():
            print(f"Warning: Metadata directory not found: {METADATA_DIR}")
            return

        for md_file in METADATA_DIR.glob("*.md"):
            # Skip README files
            if md_file.name.upper() == "README.MD":
                continue

            try:
                content = md_file.read_text(encoding="utf-8")
                metadata = self.parse_yaml_frontmatter(content)

                if not metadata:
                    continue

                # Get reference type
                ref_type = metadata.get("type", "")
                if ref_type in self.references:
                    metadata["_filename"] = md_file.name
                    self.references[ref_type].append(metadata)

            except Exception as e:
                print(f"Warning: Error reading {md_file}: {e}")

    def sort_references(self) -> None:
        """Sort references within each category"""
        # Sort statutes and rules by title
        for ref_type in ["statute", "procedural-rule"]:
            self.references[ref_type].sort(key=lambda x: x.get("title", ""))

        # Sort cases by date (most recent first), then by title
        self.references["case"].sort(
            key=lambda x: (x.get("date", "9999-99-99"), x.get("title", "")),
            reverse=True,
        )

        # Sort other types by title
        for ref_type in ["practice-direction", "guidance", "form"]:
            self.references[ref_type].sort(key=lambda x: x.get("title", ""))

    def format_reference_entry(self, ref: Dict) -> str:
        """Format a single reference entry"""
        title = ref.get("title", "Untitled")
        citation = ref.get("citation", "")
        date = ref.get("date", "")
        source_url = ref.get("source_url", "")
        filename = ref.get("filename", "")

        # Build the entry
        entry = f"### {title}\n\n"

        if citation:
            entry += f"**Citation**: {citation}\n\n"

        if date:
            entry += f"**Date**: {date}\n\n"

        if filename:
            # Create relative path to PDF
            ref_type = ref.get("type", "")
            type_dirs = {
                "statute": "legislation",
                "case": "cases",
                "form": "forms",
                "guidance": "guidance",
                "practice-direction": "practice-directions",
                "procedural-rule": "procedural-rules",
            }
            subdir = type_dirs.get(ref_type, "")
            if subdir:
                entry += f"**Document**: [PDF](../references/{subdir}/{filename})\n\n"

        if source_url:
            entry += f"**Source**: [{source_url}]({source_url})\n\n"

        # Add optional fields
        if "summary" in ref and ref["summary"]:
            entry += f"{ref['summary']}\n\n"

        # Add related references
        if "related_statutes" in ref and ref["related_statutes"]:
            entry += "**Related Legislation**: "
            entry += ", ".join(ref["related_statutes"])
            entry += "\n\n"

        if "related_cases" in ref and ref["related_cases"]:
            entry += "**Related Cases**: "
            entry += ", ".join(ref["related_cases"])
            entry += "\n\n"

        entry += "---\n\n"

        return entry

    def generate_index(self) -> str:
        """Generate the complete index"""
        output = []

        # Header
        output.append("# References and Authorities\n\n")
        output.append(
            f"*Auto-generated on {datetime.now().strftime('%Y-%m-%d at %H:%M UTC')}*\n\n"
        )
        output.append(
            "This document provides a comprehensive index of all reference materials "
            "used in the Contentious Probate Manual & Toolkit.\n\n"
        )

        # Table of contents
        output.append("## Table of Contents\n\n")
        for ref_type in TYPE_ORDER:
            if self.references[ref_type]:
                label = TYPE_LABELS.get(ref_type, ref_type.title())
                count = len(self.references[ref_type])
                anchor = label.lower().replace(" ", "-")
                output.append(f"- [{label}](#{anchor}) ({count})\n")
        output.append("\n")

        # Generate sections
        for ref_type in TYPE_ORDER:
            refs = self.references[ref_type]
            if not refs:
                continue

            label = TYPE_LABELS.get(ref_type, ref_type.title())
            output.append(f"## {label}\n\n")

            for ref in refs:
                output.append(self.format_reference_entry(ref))

        # Footer
        output.append("---\n\n")
        output.append(
            "*This file is automatically generated. Do not edit manually. "
            "To update, run `python scripts/generate_reference_index.py` or merge to main branch.*\n"
        )

        return "".join(output)

    def save_index(self, content: str) -> None:
        """Save the generated index"""
        OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
        OUTPUT_FILE.write_text(content, encoding="utf-8")
        print(f"Generated reference index: {OUTPUT_FILE.relative_to(REPO_ROOT)}")

    def run(self) -> None:
        """Run the index generation"""
        print("=" * 60)
        print("Reference Index Generator")
        print("=" * 60)

        print("\nLoading metadata files...")
        self.load_metadata_files()

        # Count total references
        total = sum(len(refs) for refs in self.references.values())
        print(f"Found {total} references")

        if total == 0:
            print("\nNo references found. Generating empty index.")

        print("\nSorting references...")
        self.sort_references()

        print("Generating index...")
        content = self.generate_index()

        print("Saving index...")
        self.save_index(content)

        print("\n✓ Index generation complete!")


def main():
    """Main entry point"""
    generator = ReferenceIndexGenerator()
    generator.run()


if __name__ == "__main__":
    main()
