# Reference Materials

This directory contains authoritative legal references used throughout the Contentious Probate Manual.

## Directory Structure

```
/references/
├── legislation/          # Statutes and statutory instruments
├── cases/               # Case law and judgments
├── guidance/            # Official guidance documents
├── procedural-rules/    # Court procedural rules (CPR, etc.)
├── practice-directions/ # Practice directions
├── forms/              # Court forms and templates
└── metadata/           # Metadata files for all references
```

## Reference Management

### PDF Documents

Each reference document is stored as a PDF in its appropriate category subdirectory:

- `legislation/`: Acts of Parliament, statutory instruments
- `cases/`: Reported judgments and decisions
- `guidance/`: Official guidance from courts, regulators
- `procedural-rules/`: Civil Procedure Rules and court-specific rules
- `practice-directions/`: Practice directions and protocols
- `forms/`: Standard court forms

### Metadata Files

Every PDF must have a corresponding metadata file in `/metadata/` with:

- YAML front matter containing required fields
- Document classification and categorization
- Source URL and accessibility information
- Related references and cross-links
- Version and status information

See [ENGINEERING_PRACTICES.md](../../.github/ENGINEERING_PRACTICES.md) for metadata schema requirements.

## Validation

All reference materials are automatically validated to ensure:

1. **PDF-Metadata Pairing**: Every PDF has a corresponding `.md` metadata file
2. **Schema Compliance**: Metadata contains all required fields
3. **URL Accessibility**: Source URLs are valid and accessible
4. **Naming Conventions**: Files follow established naming standards
5. **Cross-Reference Integrity**: Links between documents are valid

Validation runs automatically on every push via GitHub Actions.

## Adding New References

To add a new reference:

1. **Obtain the PDF**: Download from authoritative source
2. **Name the file**: Follow naming conventions (kebab-case, include year/version)
3. **Place in correct directory**: Based on document type
4. **Create metadata file**: In `/metadata/` with same base name
5. **Complete YAML fields**: Include all required metadata
6. **Verify source URL**: Ensure it's accessible
7. **Test locally**: Run `python scripts/validate_references.py`
8. **Submit PR**: With both PDF and metadata file

## Reference Types

### Legislation

- Acts of Parliament
- Statutory instruments
- Delegated legislation
- Historical statutes

Format: `statute-{title}-{year}.pdf`

Example: `statute-inheritance-act-1975.pdf`

### Cases

- Court of Appeal decisions
- High Court judgments
- Supreme Court rulings
- First instance decisions

Format: `case-{short-title}-{year}.pdf`

Example: `case-ilott-v-mitson-2017.pdf`

### Forms

- Court forms (N-series, etc.)
- Application forms
- Standard templates

Format: `form-{number}-{title}.pdf`

Example: `form-n1-claim-form.pdf`

### Guidance

- Official guidance documents
- Practice notes
- Procedural guidance

Format: `guidance-{issuer}-{title}-{year}.pdf`

Example: `guidance-hmcts-probate-claims-2024.pdf`

### Practice Directions

- CPR practice directions
- Court-specific directions
- Protocol amendments

Format: `pd-{number}-{title}.pdf`

Example: `pd-57ac-probate-claims.pdf`

### Procedural Rules

- Civil Procedure Rules
- Court-specific rules
- Rule amendments

Format: `rules-{title}-{year}.pdf`

Example: `rules-cpr-part-57-2024.pdf`

## Auto-Generated Index

The comprehensive reference index (`_references-and-authorities.md`) is automatically generated from metadata files and is located in `/docs/contentious-probate-manual/`.

This index is regenerated automatically on merge to main branch.

## Maintenance

Regular maintenance tasks:

- **Monthly**: Check for updated versions of key references
- **Quarterly**: Verify source URLs remain accessible
- **Annually**: Comprehensive review of all references
- **As needed**: Add new references as they become relevant

## Contributing

When contributing references:

1. Verify document authenticity and authority
2. Use official versions from authoritative sources
3. Include complete and accurate metadata
4. Test validation before submitting PR
5. Document any special considerations

For detailed guidelines, see [ENGINEERING_PRACTICES.md](../../.github/ENGINEERING_PRACTICES.md).
