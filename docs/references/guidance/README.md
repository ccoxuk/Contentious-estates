# Official Guidance

This directory contains official guidance documents from courts, regulators, and professional bodies.

## Types of Guidance

- HMCTS guidance on probate claims
- Law Society practice notes
- Bar Council guidance
- Court service guidance
- Professional conduct guidance

## File Naming

Format: `guidance-{issuer}-{title}-{year}.pdf`

Examples:
- `guidance-hmcts-probate-claims-2024.pdf`
- `guidance-law-society-contentious-probate-2023.pdf`

## Metadata

Each PDF must have a corresponding metadata file in `/docs/references/metadata/`.

Required metadata fields:
- `title`: Full title of guidance
- `type`: "guidance"
- `jurisdiction`: Applicable jurisdiction
- `date`: Publication date
- `citation`: Reference number if applicable
- `source_url`: Official source URL
- `filename`: PDF filename
- `issuer`: Organization that issued the guidance

Optional fields:
- `status`: "current", "superseded", "draft"
- `supersedes`: Previous version reference
- `summary`: Brief description
