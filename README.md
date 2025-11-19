# Contentious Probate Legal Resources

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive, structured framework for organizing and managing legal resources related to contentious probate practice in England and Wales.

## Overview

This repository provides a systematic approach to collecting, organizing, and maintaining legal resources including:
- Legislation (Wills Act 1837, Administration of Estates Act 1925, etc.)
- Civil Procedure Rules (Part 57, etc.)
- Practice Directions
- Case law and judgments
- Guidance and best practice documents
- Professional standards
- Court forms and precedents

## Quick Start

### Structure

```
docs/
└── references/
    ├── legislation/          # Acts and statutory instruments
    ├── procedural-rules/     # CPR Part 57 and other rules
    ├── practice-directions/  # Practice Directions
    ├── cases/                # Case law
    ├── guidance/             # Court guides and guidance
    ├── professional-standards/ # SRA, BSB standards
    ├── forms/                # Court forms and templates
    └── metadata/             # YAML metadata files
```

### File Naming Convention

All files follow the standardized format:
```
YYYYMMDD-source-slug-v01.ext
```

**Example:**
```
20251116-wills-act-1837-legislation-gov-uk-v01.pdf
20251116-cpr-part-57-justice-gov-uk-v01.pdf
```

### Adding Resources

1. Download the resource from an authoritative source
2. Save with the correct naming convention to the appropriate directory
3. Create a metadata file in `docs/references/metadata/`
4. Use the template at `docs/references/metadata/TEMPLATE-metadata.md`

### Metadata Structure

Each resource must have a corresponding metadata file with YAML frontmatter:

```yaml
---
title: "Official title"
type: "Act | Rules | Practice Direction | Case | Guidance | Form | Standard"
date_downloaded: "YYYY-MM-DD"
source_url: "https://..."
source_authority: "legislation.gov.uk"
jurisdiction: "England and Wales"
status: "In force | Repealed | Amended"
keywords:
  - "keyword1"
  - "keyword2"
---
```

## Documentation

- **[Main Documentation](docs/README.md)** - Overview and detailed usage guide
- **[References Guide](docs/references/README.md)** - Complete manifest documentation
- **[Metadata Guide](docs/references/metadata/README.md)** - Metadata creation guidelines

### Category-Specific Guides

- [Legislation](docs/references/legislation/README.md)
- [Procedural Rules](docs/references/procedural-rules/README.md)
- [Practice Directions](docs/references/practice-directions/README.md)
- [Cases](docs/references/cases/README.md)
- [Guidance](docs/references/guidance/README.md)
- [Professional Standards](docs/references/professional-standards/README.md)
- [Forms](docs/references/forms/README.md)

## Examples

The repository includes example metadata files demonstrating best practices:

1. **[Wills Act 1837](docs/references/metadata/EXAMPLE-20251116-wills-act-1837-legislation-gov-uk-v01.md)** - Legislation example
2. **[CPR Part 57](docs/references/metadata/EXAMPLE-20251116-cpr-part-57-justice-gov-uk-v01.md)** - Procedural rules example

## Key Features

✅ **Standardized Organization** - Consistent directory structure and naming
✅ **Comprehensive Metadata** - Rich metadata for search and discovery
✅ **Version Control** - Track updates and amendments
✅ **Cross-Referencing** - Link related documents
✅ **Quality Standards** - Validation and best practices

## Best Practices

1. Always use official, authoritative sources
2. Complete all required metadata fields
3. Follow naming conventions strictly
4. Cross-reference related documents
5. Keep resources up-to-date
6. Document amendments and updates

## Contributing

Contributions are welcome! When adding resources:
- Follow the file naming convention
- Use the metadata template
- Complete all required fields
- Verify source authenticity
- Document your additions clearly

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Resources

### Official Sources

- **[legislation.gov.uk](https://www.legislation.gov.uk)** - UK legislation
- **[judiciary.uk](https://www.judiciary.uk)** - Court rules and practice directions
- **[BAILII](https://www.bailii.org)** - Free law reports
- **[HMCTS](https://www.gov.uk/government/organisations/hm-courts-and-tribunals-service)** - Court forms

### Professional Bodies

- **[Law Society](https://www.lawsociety.org.uk)** - Solicitor guidance
- **[Bar Council](https://www.barcouncil.org.uk)** - Barrister resources
- **[ACTAPS](https://www.actaps.com)** - Contentious trust and probate specialists

## Support

For questions, issues, or suggestions, please open an issue in this repository.

---

**Note**: This is a resource organization framework. Users are responsible for ensuring they use current, authoritative versions of legal materials and comply with all applicable copyright and licensing terms.
