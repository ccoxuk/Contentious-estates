# Reference Metadata

This directory contains metadata files (`.md` files) for all reference PDFs in the repository.

## Purpose

Metadata files provide structured information about each reference document, enabling:

1. **Automated validation**: Ensuring all PDFs have proper documentation
2. **Reference indexing**: Auto-generating comprehensive reference lists
3. **Source tracking**: Maintaining links to authoritative sources
4. **Version control**: Tracking updates and superseded documents
5. **Cross-referencing**: Linking related materials

## File Naming

Metadata files must have the same base name as their corresponding PDF:

- PDF: `statute-inheritance-act-1975.pdf` (in `/legislation/`)
- Metadata: `statute-inheritance-act-1975.md` (in `/metadata/`)

## Required Schema

Every metadata file must include YAML front matter with these required fields:

```yaml
---
title: "Full Title of Document"
type: "statute|case|form|guidance|practice-direction|procedural-rule"
jurisdiction: "England and Wales|Scotland|Northern Ireland"
date: "YYYY-MM-DD"
citation: "Official citation"
source_url: "https://..."
filename: "corresponding-pdf-filename.pdf"
---
```

### Field Descriptions

- **title**: Full official title of the document
- **type**: Document category (must match one of the approved types)
- **jurisdiction**: Legal jurisdiction where the document applies
- **date**: Publication, enactment, or decision date (ISO 8601 format)
- **citation**: Official legal citation or reference number
- **source_url**: URL to authoritative source (must be accessible)
- **filename**: Name of the corresponding PDF file

## Optional Fields

```yaml
version: "1.0"
status: "current|superseded|draft"
supersedes: "previous-version-filename.pdf"
related_cases: ["case-name-year.pdf"]
related_statutes: ["statute-name-year.pdf"]
keywords: ["keyword1", "keyword2"]
summary: "Brief description of the document"
court: "Supreme Court"
judges: ["Justice Name"]
issuer: "HMCTS"
purpose: "Description of use"
amendments: ["Amendment description"]
```

## Example: Statute Metadata

```yaml
---
title: "Inheritance (Provision for Family and Dependants) Act 1975"
type: "statute"
jurisdiction: "England and Wales"
date: "1975-11-12"
citation: "1975 c. 63"
source_url: "https://www.legislation.gov.uk/ukpga/1975/63"
filename: "statute-inheritance-act-1975.pdf"
version: "as amended 2024"
status: "current"
keywords: ["family provision", "reasonable financial provision", "inheritance"]
summary: "Enables certain categories of people to apply for reasonable financial provision from the estate of a deceased person."
---

# Additional Information

This Act is the primary legislation for family provision claims and contentious probate matters in England and Wales.

## Key Sections

- Section 1: Applications for financial provision
- Section 2: Powers of court to make orders
- Section 3: Matters to which court is to have regard
```

## Example: Case Metadata

```yaml
---
title: "Ilott v Mitson and others"
type: "case"
jurisdiction: "England and Wales"
date: "2017-03-15"
citation: "[2017] UKSC 17"
source_url: "https://www.bailii.org/uk/cases/UKSC/2017/17.html"
filename: "case-ilott-v-mitson-2017.pdf"
court: "Supreme Court"
judges: ["Lord Hughes", "Lady Hale", "Lord Kerr", "Lord Wilson", "Lord Carnwath"]
keywords: ["family provision", "adult child", "reasonable financial provision"]
summary: "Landmark Supreme Court decision on family provision claims by adult children."
related_statutes: ["statute-inheritance-act-1975.pdf"]
---

# Case Summary

The Supreme Court's decision in Ilott v Mitson provides important guidance on the application of the Inheritance Act 1975, particularly regarding claims by adult children.

## Key Principles

1. The test for reasonable financial provision
2. Factors to consider under section 3
3. The balance between testamentary freedom and family provision
```

## Validation

All metadata files are automatically validated by `scripts/validate_references.py` to ensure:

- YAML front matter is properly formatted
- All required fields are present and populated
- Field types are correct (dates, URLs, etc.)
- Source URLs are accessible
- Referenced PDF files exist
- No orphaned metadata files (metadata without corresponding PDF)

## Maintenance

When updating metadata:

1. Preserve the original filename
2. Update version information
3. Mark superseded documents appropriately
4. Test validation before committing
5. Update related cross-references

## Contributing

See [ENGINEERING_PRACTICES.md](../../../.github/ENGINEERING_PRACTICES.md) for detailed guidelines on creating and maintaining metadata files.
