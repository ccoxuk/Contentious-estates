# Contentious Probate Legal Resources Manifest

This directory contains a comprehensive, organized framework for managing legal resources related to contentious probate matters in England and Wales.

## Directory Structure

The legal resources are organized into the following categories:

### `legislation/`
Contains primary and secondary legislation relevant to contentious probate, including:
- Wills Act 1837
- Inheritance (Provision for Family and Dependants) Act 1975
- Administration of Estates Act 1925
- Trustee Act 1925
- Other relevant statutes

### `procedural-rules/`
Contains procedural rules governing contentious probate proceedings, including:
- Civil Procedure Rules Part 57 (Probate, Inheritance and Presumption of Death)
- Other relevant CPR parts
- Insolvency Rules (where applicable)

### `practice-directions/`
Contains Practice Directions supplementing the procedural rules, including:
- Practice Direction 57 (Probate and Inheritance)
- Other relevant Practice Directions

### `cases/`
Contains important case law and judgments relating to contentious probate matters, organized by topic and chronologically.

### `guidance/`
Contains guidance notes, best practice documents, and interpretative materials, including:
- Court guides
- Judicial guidance
- Professional body guidance

### `professional-standards/`
Contains professional conduct and regulatory standards, including:
- SRA Standards and Regulations
- Bar Standards Board requirements
- Costs guidance

### `forms/`
Contains court forms, precedents, and templates for contentious probate proceedings.

### `metadata/`
Contains YAML metadata files describing each source document stored in the other directories.

## File Naming Convention

All source files must follow this naming convention:

```
YYYYMMDD-source-slug-v01.ext
```

Where:
- `YYYYMMDD` = Date of download or last version check (e.g., 20251116)
- `source-slug` = Descriptive identifier in kebab-case (e.g., wills-act-1837-legislation-gov-uk)
- `v01` = Version number (increment for updates)
- `ext` = File extension (e.g., pdf, html, txt)

### Examples:
- `20251116-wills-act-1837-legislation-gov-uk-v01.pdf`
- `20251116-cpr-part-57-justice-gov-uk-v01.pdf`
- `20251116-practice-direction-57-v01.pdf`
- `20251116-marley-v-rawlings-2014-uksc-2-bailii-v01.pdf`

## Metadata Files

For each source document, a corresponding metadata file must be created in the `metadata/` directory with the same base filename but with a `.md` extension.

### Metadata File Naming:
```
YYYYMMDD-source-slug-v01.md
```

### Metadata Structure:

```markdown
---
# Source Metadata
title: "Official or best-available title"
type: "Act | Rules | Practice Direction | Case | Guidance | Form | Standard"
date_published: "YYYY-MM-DD"
date_downloaded: "YYYY-MM-DD"
version: "v01"
source_url: "https://..."
source_authority: "e.g., legislation.gov.uk, judiciary.uk, BAILII"
jurisdiction: "England and Wales"
status: "In force | Repealed | Amended | Historical"
relevance: "Brief description of relevance to contentious probate"
keywords:
  - "keyword1"
  - "keyword2"
  - "keyword3"
notes: "Any additional notes about this resource"
related_documents:
  - "YYYYMMDD-related-doc-v01.pdf"
---

# Summary

Brief summary or abstract of the document content.

# Key Provisions

- Key point 1
- Key point 2
- Key point 3

# Updates and Amendments

Record any updates or amendments to this resource.
```

## Metadata Template

A metadata template file is available at `metadata/TEMPLATE-metadata.md` to help you create new metadata entries.

## Usage Guidelines

### Adding a New Resource

1. **Download the source document** to the appropriate directory using the correct naming convention
2. **Create a metadata file** in the `metadata/` directory using the template
3. **Fill in all required metadata fields** accurately
4. **Add keywords and tags** to improve searchability
5. **Link related documents** to create a knowledge graph

### Updating an Existing Resource

1. **Increment the version number** in both filename and metadata (e.g., v01 → v02)
2. **Update the date_downloaded field** in the metadata
3. **Add update notes** in the metadata file
4. **Keep previous versions** for historical reference (optional, based on significance)

### Best Practices

- Always verify URLs and sources before adding documents
- Use official government or court sources where available
- Maintain consistent naming and metadata standards
- Cross-reference related documents in metadata
- Keep metadata files up-to-date with document changes
- Use descriptive keywords for better discoverability

## Maintenance

This manifest should be reviewed and updated regularly to ensure:
- Links remain valid and active
- Documents reflect current law and practice
- New important resources are added promptly
- Outdated or superseded materials are clearly marked

## Contributing

When contributing to this resource collection:
1. Follow the naming conventions strictly
2. Complete all required metadata fields
3. Verify source authenticity and authority
4. Check for existing versions before adding duplicates
5. Use consistent formatting and structure

## License

See the repository LICENSE file for terms of use and distribution of this manifest structure.
