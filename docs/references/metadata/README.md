# Metadata Directory

This directory contains YAML-frontmatter metadata files (`.md` format) describing each source document stored in the legal resources manifest.

## Purpose

Metadata files serve multiple purposes:
- Document provenance and authenticity
- Track versions and updates
- Enable search and discovery
- Create relationships between documents
- Maintain data quality and consistency

## File Naming

Metadata files must have the **exact same base filename** as their corresponding source document, with a `.md` extension:

```
[Source file]     docs/references/legislation/20251116-wills-act-1837-legislation-gov-uk-v01.pdf
[Metadata file]   docs/references/metadata/20251116-wills-act-1837-legislation-gov-uk-v01.md
```

## Metadata Structure

Each metadata file must follow this structure:

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

## Required Fields

The following fields are **required** for all metadata files:
- `title` - Official or best-available title
- `type` - Document type from the controlled list
- `date_downloaded` - When you obtained this version
- `source_url` - Where the document was obtained
- `source_authority` - The authoritative source
- `jurisdiction` - Usually "England and Wales"
- `status` - Current legal/practical status

## Optional Fields

The following fields are **recommended** but may not apply to all documents:
- `date_published` - Official publication date (if known)
- `keywords` - For search and categorization
- `notes` - Additional context
- `related_documents` - Cross-references
- Summary section - Brief overview
- Key Provisions section - Important points
- Updates section - Version history

## Template

Use the template file `TEMPLATE-metadata.md` as a starting point for creating new metadata files.

## Best Practices

1. **Accuracy** - Verify all information before recording
2. **Completeness** - Fill in all applicable fields
3. **Consistency** - Use controlled vocabularies for type, status, etc.
4. **Keywords** - Choose meaningful, searchable terms
5. **Cross-referencing** - Link related documents
6. **Updates** - Keep metadata current when documents change
7. **Sources** - Always record the authoritative source

## Validation

Before committing metadata files, verify:
- ✓ Filename matches source document
- ✓ All required fields completed
- ✓ Dates in correct format (YYYY-MM-DD)
- ✓ URLs are valid and accessible
- ✓ Keywords are relevant and specific
- ✓ Related documents exist in the manifest
