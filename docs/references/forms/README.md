# Court Forms

This directory contains standard court forms used in contentious probate proceedings.

## Common Forms

- N1 - Claim Form
- N208 - Acknowledgment of Service
- N244 - Application Notice
- N260 - Statement of Costs
- Probate-specific forms

## File Naming

Format: `form-{number}-{title}.pdf`

Examples:
- `form-n1-claim-form.pdf`
- `form-n208-acknowledgment-of-service.pdf`
- `form-n244-application-notice.pdf`

## Metadata

Each PDF must have a corresponding metadata file in `/docs/references/metadata/`.

Required metadata fields:
- `title`: Full form title
- `type`: "form"
- `jurisdiction`: "England and Wales" (typically)
- `date`: Form version date
- `citation`: Form number (e.g., "N1")
- `source_url`: HMCTS or justice.gov.uk URL
- `filename`: PDF filename

Optional fields:
- `version`: Version number/date
- `status`: "current", "superseded"
- `purpose`: Brief description of when to use
- `related_rules`: Associated CPR rules
