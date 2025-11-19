# Procedural Rules

This directory contains court procedural rules relevant to contentious probate.

## Key Rules

- Civil Procedure Rules (CPR) Part 57 - Probate and Inheritance
- CPR Part 8 - Alternative Procedure for Claims
- CPR Part 44 - Costs
- Family Procedure Rules (where applicable)

## File Naming

Format: `rules-{title}-{year}.pdf`

Examples:
- `rules-cpr-part-57-2024.pdf`
- `rules-cpr-part-8-2024.pdf`

## Metadata

Each PDF must have a corresponding metadata file in `/docs/references/metadata/`.

Required metadata fields:
- `title`: Full title (e.g., "Civil Procedure Rules Part 57")
- `type`: "procedural-rule"
- `jurisdiction`: "England and Wales" (typically)
- `date`: Last update date
- `citation`: Official citation
- `source_url`: justice.gov.uk or official source
- `filename`: PDF filename

Optional fields:
- `version`: Version number
- `status`: "current", "superseded"
- `amendments`: List of recent amendments
