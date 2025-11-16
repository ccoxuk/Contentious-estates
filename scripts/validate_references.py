#!/usr/bin/env python3
"""
Reference Validation Script for Contentious Probate Manual & Toolkit

This script validates the integrity of reference documents and their metadata:
- Checks that every PDF has a corresponding metadata file
- Validates metadata YAML schema and required fields
- Verifies source URL accessibility
- Reports missing or malformed entries
- Identifies orphaned files

Usage:
    python scripts/validate_references.py

Exit Codes:
    0: All validations passed
    1: Validation errors found
"""

import os
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple
import re
import yaml
import urllib.request
import urllib.error
from urllib.parse import urlparse


# Configuration
REPO_ROOT = Path(__file__).parent.parent
REFERENCES_DIR = REPO_ROOT / "docs" / "references"
METADATA_DIR = REFERENCES_DIR / "metadata"

REQUIRED_METADATA_FIELDS = [
    "title",
    "type",
    "jurisdiction",
    "date",
    "citation",
    "source_url",
    "filename",
]

VALID_TYPES = [
    "statute",
    "case",
    "form",
    "guidance",
    "practice-direction",
    "procedural-rule",
]

# Terminal colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"


class ValidationError:
    """Represents a validation error"""

    def __init__(self, severity: str, category: str, message: str):
        self.severity = severity  # "error" or "warning"
        self.category = category
        self.message = message

    def __str__(self):
        color = RED if self.severity == "error" else YELLOW
        return f"{color}[{self.severity.upper()}]{RESET} {self.category}: {self.message}"


class ReferenceValidator:
    """Validates reference documents and metadata"""

    def __init__(self):
        self.errors: List[ValidationError] = []
        self.warnings: List[ValidationError] = []

    def add_error(self, category: str, message: str):
        """Add an error to the validation results"""
        error = ValidationError("error", category, message)
        self.errors.append(error)
        print(error)

    def add_warning(self, category: str, message: str):
        """Add a warning to the validation results"""
        warning = ValidationError("warning", category, message)
        self.warnings.append(warning)
        print(warning)

    def find_pdfs(self) -> Dict[str, Path]:
        """Find all PDF files in reference directories"""
        pdfs = {}
        reference_subdirs = [
            "legislation",
            "cases",
            "guidance",
            "procedural-rules",
            "practice-directions",
            "forms",
        ]

        for subdir in reference_subdirs:
            subdir_path = REFERENCES_DIR / subdir
            if subdir_path.exists():
                for pdf_file in subdir_path.glob("*.pdf"):
                    pdfs[pdf_file.stem] = pdf_file

        return pdfs

    def find_metadata_files(self) -> Dict[str, Path]:
        """Find all metadata files"""
        metadata_files = {}
        if METADATA_DIR.exists():
            for md_file in METADATA_DIR.glob("*.md"):
                # Skip README files
                if md_file.name.upper() != "README.MD":
                    metadata_files[md_file.stem] = md_file

        return metadata_files

    def check_pdf_metadata_pairing(
        self, pdfs: Dict[str, Path], metadata_files: Dict[str, Path]
    ) -> None:
        """Check that every PDF has a corresponding metadata file"""
        print(f"\n{BLUE}Checking PDF-metadata pairing...{RESET}")

        # Check for PDFs without metadata
        for pdf_name, pdf_path in pdfs.items():
            if pdf_name not in metadata_files:
                self.add_error(
                    "Missing Metadata",
                    f"PDF '{pdf_path.relative_to(REPO_ROOT)}' has no metadata file",
                )

        # Check for metadata without PDFs (orphaned metadata)
        for meta_name, meta_path in metadata_files.items():
            if meta_name not in pdfs:
                self.add_warning(
                    "Orphaned Metadata",
                    f"Metadata file '{meta_path.relative_to(REPO_ROOT)}' has no corresponding PDF",
                )

    def parse_yaml_frontmatter(self, content: str) -> Tuple[Dict, str]:
        """Parse YAML front matter from markdown content"""
        # Match YAML front matter between --- delimiters
        pattern = r"^---\s*\n(.*?)\n---\s*\n(.*)$"
        match = re.match(pattern, content, re.DOTALL)

        if not match:
            return {}, content

        yaml_content = match.group(1)
        body_content = match.group(2)

        try:
            metadata = yaml.safe_load(yaml_content)
            return metadata or {}, body_content
        except yaml.YAMLError as e:
            raise ValueError(f"Invalid YAML: {e}")

    def validate_metadata_file(self, metadata_path: Path) -> None:
        """Validate a single metadata file"""
        relative_path = metadata_path.relative_to(REPO_ROOT)

        try:
            content = metadata_path.read_text(encoding="utf-8")
        except Exception as e:
            self.add_error("Read Error", f"Cannot read '{relative_path}': {e}")
            return

        # Parse YAML front matter
        try:
            metadata, _ = self.parse_yaml_frontmatter(content)
        except ValueError as e:
            self.add_error("YAML Error", f"'{relative_path}': {e}")
            return

        if not metadata:
            self.add_error(
                "Missing YAML",
                f"'{relative_path}' has no YAML front matter",
            )
            return

        # Check required fields
        for field in REQUIRED_METADATA_FIELDS:
            if field not in metadata or not metadata[field]:
                self.add_error(
                    "Missing Field",
                    f"'{relative_path}' missing required field '{field}'",
                )

        # Validate field types
        if "type" in metadata:
            if metadata["type"] not in VALID_TYPES:
                self.add_error(
                    "Invalid Type",
                    f"'{relative_path}' has invalid type '{metadata['type']}'. "
                    f"Must be one of: {', '.join(VALID_TYPES)}",
                )

        # Validate date format (basic check)
        if "date" in metadata and metadata["date"]:
            date_str = str(metadata["date"])
            if not re.match(r"^\d{4}-\d{2}-\d{2}$", date_str):
                self.add_warning(
                    "Date Format",
                    f"'{relative_path}' date '{date_str}' should be YYYY-MM-DD format",
                )

        # Validate source_url
        if "source_url" in metadata and metadata["source_url"]:
            source_url = metadata["source_url"]
            if not self.is_valid_url(source_url):
                self.add_error(
                    "Invalid URL",
                    f"'{relative_path}' has invalid source_url '{source_url}'",
                )

        # Validate filename references actual PDF
        if "filename" in metadata and metadata["filename"]:
            filename = metadata["filename"]
            expected_stem = metadata_path.stem

            # Check if filename matches metadata file name
            if Path(filename).stem != expected_stem:
                self.add_warning(
                    "Filename Mismatch",
                    f"'{relative_path}' filename '{filename}' doesn't match "
                    f"metadata name '{expected_stem}.md'",
                )

    def is_valid_url(self, url: str) -> bool:
        """Basic URL validation"""
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except Exception:
            return False

    def check_url_accessibility(
        self, metadata_files: Dict[str, Path], check_urls: bool = True
    ) -> None:
        """Check if source URLs are accessible (optional, can be slow)"""
        if not check_urls:
            return

        print(f"\n{BLUE}Checking URL accessibility (this may take a while)...{RESET}")

        for meta_name, meta_path in metadata_files.items():
            try:
                content = meta_path.read_text(encoding="utf-8")
                metadata, _ = self.parse_yaml_frontmatter(content)

                if "source_url" in metadata and metadata["source_url"]:
                    url = metadata["source_url"]
                    if self.is_url_accessible(url):
                        print(f"  {GREEN}✓{RESET} {url}")
                    else:
                        self.add_warning(
                            "Inaccessible URL",
                            f"'{meta_path.relative_to(REPO_ROOT)}' source_url "
                            f"'{url}' is not accessible",
                        )
            except Exception as e:
                continue

    def is_url_accessible(self, url: str, timeout: int = 10) -> bool:
        """Check if a URL is accessible"""
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            response = urllib.request.urlopen(req, timeout=timeout)
            return response.status in [200, 301, 302]
        except Exception:
            return False

    def validate_naming_conventions(self, pdfs: Dict[str, Path]) -> None:
        """Validate file naming conventions"""
        print(f"\n{BLUE}Checking naming conventions...{RESET}")

        # Pattern: lowercase, hyphens, alphanumeric
        valid_pattern = re.compile(r"^[a-z0-9][a-z0-9-]*[a-z0-9]$")

        for pdf_name, pdf_path in pdfs.items():
            if not valid_pattern.match(pdf_name):
                self.add_warning(
                    "Naming Convention",
                    f"'{pdf_path.relative_to(REPO_ROOT)}' doesn't follow "
                    f"kebab-case naming convention",
                )

    def run_validation(self, check_urls: bool = False) -> bool:
        """Run all validations"""
        print(f"{BLUE}{'=' * 60}{RESET}")
        print(f"{BLUE}Reference Validation for Contentious Probate Manual{RESET}")
        print(f"{BLUE}{'=' * 60}{RESET}")

        # Find all files
        print(f"\n{BLUE}Scanning for reference files...{RESET}")
        pdfs = self.find_pdfs()
        metadata_files = self.find_metadata_files()

        print(f"Found {len(pdfs)} PDF files")
        print(f"Found {len(metadata_files)} metadata files")

        if not pdfs and not metadata_files:
            print(f"\n{YELLOW}No reference files found. This is OK for a new repository.{RESET}")
            return True

        # Run validations
        self.check_pdf_metadata_pairing(pdfs, metadata_files)

        print(f"\n{BLUE}Validating metadata files...{RESET}")
        for meta_name, meta_path in metadata_files.items():
            self.validate_metadata_file(meta_path)

        self.validate_naming_conventions(pdfs)

        if check_urls:
            self.check_url_accessibility(metadata_files, check_urls=True)

        # Print summary
        print(f"\n{BLUE}{'=' * 60}{RESET}")
        print(f"{BLUE}Validation Summary{RESET}")
        print(f"{BLUE}{'=' * 60}{RESET}")

        if self.errors:
            print(f"{RED}Errors: {len(self.errors)}{RESET}")
        else:
            print(f"{GREEN}Errors: 0{RESET}")

        if self.warnings:
            print(f"{YELLOW}Warnings: {len(self.warnings)}{RESET}")
        else:
            print(f"{GREEN}Warnings: 0{RESET}")

        if not self.errors and not self.warnings:
            print(f"\n{GREEN}✓ All validations passed!{RESET}")
            return True
        elif not self.errors:
            print(f"\n{GREEN}✓ No errors, but {len(self.warnings)} warnings{RESET}")
            return True
        else:
            print(f"\n{RED}✗ Validation failed with {len(self.errors)} errors{RESET}")
            return False


def main():
    """Main entry point"""
    # Parse command line arguments
    check_urls = "--check-urls" in sys.argv

    validator = ReferenceValidator()
    success = validator.run_validation(check_urls=check_urls)

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
