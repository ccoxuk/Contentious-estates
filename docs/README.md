# Contentious Probate Legal Resources

This repository provides a comprehensive, structured framework for organizing and managing legal resources related to contentious probate practice in England and Wales.

## Overview

The **Contentious Probate Legal Resources Manifest** is a systematic approach to collecting, organizing, and maintaining legal resources including legislation, case law, procedural rules, practice directions, guidance, and forms relevant to contentious probate matters.

## Purpose

This framework serves to:
- Create a centralized repository of contentious probate legal resources
- Maintain consistent organization and naming conventions
- Enable efficient retrieval and reference of materials
- Track versions and updates of legal resources
- Build a knowledge graph of related legal materials
- Support legal research and case preparation

## Structure

```
docs/
└── references/
    ├── README.md (main documentation)
    ├── .gitignore (excludes PDFs and large files)
    ├── legislation/          # Primary and secondary legislation
    ├── procedural-rules/     # CPR and other procedural rules
    ├── practice-directions/  # Practice Directions
    ├── cases/                # Case law and judgments
    ├── guidance/             # Court guides and professional guidance
    ├── professional-standards/ # SRA, BSB standards
    ├── forms/                # Court forms and precedents
    └── metadata/             # YAML metadata for all resources
```

## Quick Start

### Adding a New Resource

1. **Download the resource** from an authoritative source
2. **Name the file** using the convention: `YYYYMMDD-source-slug-v01.ext`
3. **Save to appropriate directory** (legislation, cases, etc.)
4. **Create metadata file** in `metadata/` directory using the template
5. **Fill in all metadata fields** accurately

### Example Workflow

Adding the Wills Act 1837:

```bash
# 1. Download from legislation.gov.uk
# 2. Save as: docs/references/legislation/20251116-wills-act-1837-legislation-gov-uk-v01.pdf
# 3. Create metadata: docs/references/metadata/20251116-wills-act-1837-legislation-gov-uk-v01.md
# 4. Fill in metadata using template
```

## Key Features

### Standardized Naming Convention
All files follow the format: `YYYYMMDD-source-slug-v01.ext`
- Ensures chronological ordering
- Identifies source and version
- Prevents naming conflicts

### Comprehensive Metadata
Each resource has a structured metadata file containing:
- Title and type
- Publication and download dates
- Source URL and authority
- Legal status
- Keywords and relevance
- Related documents

### Organized by Category
Resources are organized into logical categories:
- **Legislation** - Acts and statutory instruments
- **Procedural Rules** - CPR and other rules
- **Practice Directions** - Court practice directions
- **Cases** - Case law and judgments
- **Guidance** - Professional and judicial guidance
- **Professional Standards** - Regulatory standards
- **Forms** - Court forms and templates

### Version Control
- Files are versioned (v01, v02, etc.)
- Metadata tracks updates and amendments
- Historical versions can be retained

## Documentation

Each directory contains:
- **README.md** - Explains the category and usage
- **.gitkeep** - Ensures directory is tracked by git
- Resource files (PDFs, etc.)

The `metadata/` directory contains:
- **README.md** - Metadata guidelines
- **TEMPLATE-metadata.md** - Template for new metadata
- **EXAMPLE-*.md** - Example metadata files
- Metadata files for each resource

## Usage

### For Practitioners
- Quick access to up-to-date legal resources
- Organized by practice area
- Cross-referenced through metadata
- Version tracking for updated materials

### For Researchers
- Systematic organization of materials
- Keyword-based discovery
- Relationship mapping between resources
- Historical version tracking

### For Knowledge Management
- Standardized structure for teams
- Consistent metadata for searchability
- Quality control through validation
- Audit trail of resources

## Best Practices

1. **Use Official Sources** - Always download from authoritative websites
2. **Complete Metadata** - Fill in all required fields
3. **Verify Currency** - Check for latest versions before using
4. **Cross-Reference** - Link related documents in metadata
5. **Regular Updates** - Check for amendments and new resources
6. **Quality Control** - Review metadata for accuracy

## Maintenance

The manifest should be regularly maintained to:
- Add new important resources
- Update existing resources when amended
- Mark superseded materials
- Verify URLs remain valid
- Review and update metadata

## Contributing

When adding resources:
1. Follow naming conventions strictly
2. Use the metadata template
3. Complete all required fields
4. Verify source authenticity
5. Check for existing versions
6. Cross-reference related materials

## Technical Notes

### Git Management
- PDFs and large files are excluded via `.gitignore`
- Metadata and directory structure are version controlled
- Use `.gitkeep` files to preserve empty directories

### File Organization
- One metadata file per source document
- Metadata filename matches source filename (but .md extension)
- All metadata in central `metadata/` directory
- Source files in category-specific directories

## Resources

### Key Websites
- **legislation.gov.uk** - UK legislation
- **judiciary.uk** - Court rules and practice directions
- **BAILII** - Free law reports
- **gov.uk/government/organisations/hm-courts-and-tribunals-service** - Court forms

### Professional Bodies
- **Law Society** - Solicitor guidance
- **Bar Council** - Barrister resources
- **ACTAPS** - Contentious trust and probate specialists

## License

See the repository LICENSE file for terms of use.

## Support

For questions or suggestions about this framework, please open an issue in the repository.

---

**Note**: This is a resource organization framework. Users are responsible for ensuring they use current, authoritative versions of legal materials and comply with copyright and licensing terms of source materials.
