# Engineering Practices for Contentious Probate Manual & Toolkit

## Overview

This document establishes the engineering practices, standards, and guidelines for maintaining the Contentious Probate Manual & Toolkit repository. All contributors must adhere to these practices to ensure consistency, maintainability, and compliance with procedural standards.

## Repository Goals

1. **Documentation Excellence**: Maintain comprehensive, accurate, and up-to-date legal documentation for contentious probate matters
2. **Automation**: Implement automated validation, reference management, and quality checks
3. **Compliance**: Meet audit and procedural compliance standards for legal documentation
4. **Maintainability**: Ensure all outputs are deterministic and well-documented

## Directory Structure

The repository follows a strict organizational structure:

```
/docs/contentious-probate-manual/    # Main manual documentation
/docs/templates/contentious-probate/ # Document templates
/docs/admin/contentious-probate-file/ # Administrative documents
/docs/references/legislation/        # Legislative references (PDF + metadata)
/docs/references/cases/              # Case law references (PDF + metadata)
/docs/references/guidance/           # Official guidance documents
/docs/references/procedural-rules/   # Court procedural rules
/docs/references/practice-directions/ # Practice directions
/docs/references/forms/              # Court forms and templates
/docs/references/metadata/           # Reference metadata files
/scripts/                            # Automation and validation scripts
/.github/workflows/                  # GitHub Actions workflows
```

## File Naming Conventions

### Reference Documents (PDFs)

- Use kebab-case for all filenames
- Include year or version where applicable
- Format: `{type}-{title}-{year}.pdf`
- Examples:
  - `statute-inheritance-act-1975.pdf`
  - `case-ilott-v-mitson-2017.pdf`
  - `form-n1-claim-form.pdf`

### Metadata Files

- Every PDF must have a corresponding `.md` metadata file
- Metadata files must be placed in `/docs/references/metadata/`
- Use same base name as PDF: `{pdf-basename}.md`
- Examples:
  - `statute-inheritance-act-1975.md`
  - `case-ilott-v-mitson-2017.md`

### Markdown Documentation

- Use descriptive, lowercase names with hyphens
- Prefix special files with underscore: `_changelog.md`, `_references-and-authorities.md`
- Keep names concise but clear

## Metadata Standards

All reference metadata files must include YAML front matter with the following fields:

```yaml
---
title: "Full Title of Document"
type: "statute|case|form|guidance|practice-direction|procedural-rule"
jurisdiction: "England and Wales|Scotland|Northern Ireland"
date: "YYYY-MM-DD"
citation: "Official citation"
source_url: "https://..."
filename: "corresponding-pdf-filename.pdf"
version: "1.0"
status: "current|superseded|draft"
---
```

### Required Fields

- `title`: Full official title
- `type`: Document category (must match approved types)
- `jurisdiction`: Legal jurisdiction
- `date`: Publication or decision date
- `citation`: Official legal citation
- `source_url`: Authoritative source URL
- `filename`: Associated PDF filename

### Optional Fields

- `version`: Document version number
- `status`: Current status of document
- `supersedes`: Previous version reference
- `related_cases`: Array of related case citations
- `related_statutes`: Array of related statute citations
- `keywords`: Array of searchable terms
- `summary`: Brief description

## Validation Requirements

### Automated Checks

All commits must pass the following automated validations:

1. **Reference Validation** (`validate_references.py`)
   - Every PDF has corresponding metadata file
   - Metadata files are properly formatted
   - Required YAML fields are present
   - Source URLs are accessible (not 404)
   - File references are valid

2. **Structure Validation** (`validate-structure.yml` workflow)
   - Directory structure is intact
   - Naming conventions are followed
   - No orphaned files exist

3. **Style Validation** (`.editorconfig` and `.markdownlint.yml`)
   - No trailing whitespace
   - Consistent line endings (LF)
   - Maximum line length compliance
   - Heading structure consistency
   - Relative link validation

### Manual Review Requirements

- All legal content must be reviewed by qualified personnel
- References must be verified against authoritative sources
- Changes to templates require legal review
- Major structural changes require approval

## Automation Scripts

### validate_references.py

Validates reference integrity:
- Checks PDF-metadata pairing
- Validates metadata schema
- Verifies source URL accessibility
- Reports missing or malformed entries

### generate_reference_index.py

Generates comprehensive reference index:
- Reads all metadata files
- Categorizes by type
- Sorts chronologically or alphabetically
- Outputs to `_references-and-authorities.md`
- Updates automatically on merge to main

### update_changelog.py

Maintains change log:
- Tracks additions/modifications/deletions
- Records reference updates
- Timestamps all changes
- Outputs to `_changelog.md`

## GitHub Workflows

### On Push/Pull Request

1. **validate-references.yml**: Runs reference validation
2. **validate-structure.yml**: Checks directory structure and naming
3. **markdown-lint.yml**: Enforces markdown style rules

### On Merge to Main

1. **generate-index.yml**: Auto-generates reference index
2. **update-changelog.yml**: Updates changelog with new changes

## Contribution Guidelines

### Before Committing

1. Run local validation: `python scripts/validate_references.py`
2. Check markdown formatting: Follow `.markdownlint.yml` rules
3. Verify metadata completeness
4. Test any script changes locally

### Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

Examples:
```
feat(references): add Inheritance Act 1975 statute and metadata
fix(validation): correct URL checking logic in validate_references.py
docs(manual): update section 3.2 on standing to bring claims
```

### Pull Request Requirements

- Clear description of changes
- All validation checks passing
- Metadata files included for any new PDFs
- No breaking changes to existing references
- Documentation updated if needed

## Quality Standards

### Documentation

- Clear, professional language
- Proper legal citation format
- Cross-references properly linked
- No broken internal links
- Consistent terminology

### Code

- Python 3.8+ compatible
- Type hints where applicable
- Comprehensive error handling
- Clear function documentation
- Follow PEP 8 style guide

### Testing

- Test new scripts with sample data
- Verify workflows in PR before merge
- Check edge cases
- Validate error handling

## Versioning

- Semantic versioning for scripts: MAJOR.MINOR.PATCH
- Date-based versioning for manual: YYYY.MM
- Document version in metadata
- Track superseded versions

## Security Considerations

- Do not commit sensitive client information
- Redact personal data from case examples
- Use only publicly available references
- Verify source authenticity
- Regular security audits of automation scripts

## Maintenance Responsibilities

### Regular Tasks

- Monthly: Review and update references
- Quarterly: Audit metadata accuracy
- Annually: Comprehensive manual review
- As needed: Update automation scripts

### Issue Tracking

- Use GitHub Issues for tracking
- Label issues appropriately: `bug`, `enhancement`, `documentation`
- Link issues to PRs
- Close issues when resolved

## Support and Questions

For questions or clarifications on these practices:
1. Check existing documentation first
2. Review closed issues and PRs
3. Open a new issue with `question` label
4. Tag relevant maintainers

## Review and Updates

This document is reviewed and updated as needed. Significant changes require discussion and approval from repository maintainers.

---

**Last Updated**: 2025-11-16
**Version**: 1.0
