# Contentious Probate Manual & Toolkit

A comprehensive documentation system and reference library for contentious probate matters in
England and Wales.

[![Validate References](https://github.com/ccoxuk/Contentious-estates/actions/workflows/validate-references.yml/badge.svg)](https://github.com/ccoxuk/Contentious-estates/actions/workflows/validate-references.yml)
[![Validate Structure](https://github.com/ccoxuk/Contentious-estates/actions/workflows/validate-structure.yml/badge.svg)](https://github.com/ccoxuk/Contentious-estates/actions/workflows/validate-structure.yml)
[![Markdown Lint](https://github.com/ccoxuk/Contentious-estates/actions/workflows/markdown-lint.yml/badge.svg)](https://github.com/ccoxuk/Contentious-estates/actions/workflows/markdown-lint.yml)

## Overview

This repository provides:

- **Comprehensive Manual**: Detailed guidance on contentious probate matters
- **Reference Library**: Organized collection of legislation, case law, and procedural materials
- **Document Templates**: Reusable templates for common contentious probate documents
- **Automation Tools**: Scripts for validating, indexing, and maintaining reference materials
- **Quality Assurance**: Automated validation and style enforcement

## Repository Structure

```
contentious-estates/
├── docs/
│   ├── contentious-probate-manual/    # Main manual documentation
│   ├── templates/contentious-probate/ # Document templates
│   ├── admin/contentious-probate-file/ # Administrative documents
│   └── references/                     # Reference materials library
│       ├── legislation/                # Statutes and statutory instruments
│       ├── cases/                      # Case law and judgments
│       ├── guidance/                   # Official guidance documents
│       ├── procedural-rules/           # Court procedural rules
│       ├── practice-directions/        # Practice directions
│       ├── forms/                      # Court forms
│       └── metadata/                   # Reference metadata files
├── scripts/                            # Automation scripts
│   ├── validate_references.py          # Reference validation
│   ├── generate_reference_index.py     # Index generation
│   └── update_changelog.py             # Changelog maintenance
├── .github/
│   ├── workflows/                      # GitHub Actions workflows
│   └── ENGINEERING_PRACTICES.md        # Engineering guidelines
├── .editorconfig                       # Editor configuration
├── .markdownlint.yml                   # Markdown linting rules
└── requirements.txt                    # Python dependencies
```

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Git

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ccoxuk/Contentious-estates.git
   cd Contentious-estates
   ```

2. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

#### Validate References

Check that all PDF references have corresponding metadata and that metadata is properly formatted:

```bash
python scripts/validate_references.py
```

To also check URL accessibility (slower):

```bash
python scripts/validate_references.py --check-urls
```

#### Generate Reference Index

Create a comprehensive index of all reference materials:

```bash
python scripts/generate_reference_index.py
```

This generates `docs/contentious-probate-manual/_references-and-authorities.md`

#### Update Changelog

Record changes to reference materials:

```bash
python scripts/update_changelog.py
```

With a custom message:

```bash
python scripts/update_changelog.py --message "Updated inheritance act materials"
```

## Adding References

To add a new reference document:

1. **Add the PDF**: Place it in the appropriate directory:
   - Legislation → `docs/references/legislation/`
   - Cases → `docs/references/cases/`
   - Forms → `docs/references/forms/`
   - Guidance → `docs/references/guidance/`
   - Practice Directions → `docs/references/practice-directions/`
   - Procedural Rules → `docs/references/procedural-rules/`

2. **Name the file**: Use kebab-case naming:
   - Statutes: `statute-{title}-{year}.pdf`
   - Cases: `case-{short-title}-{year}.pdf`
   - Forms: `form-{number}-{title}.pdf`

3. **Create metadata**: Create a corresponding `.md` file in `docs/references/metadata/` with
   the same base name

4. **Complete YAML front matter**: Include all required fields:

   ```yaml
   ---
   title: "Full Document Title"
   type: "statute|case|form|guidance|practice-direction|procedural-rule"
   jurisdiction: "England and Wales"
   date: "YYYY-MM-DD"
   citation: "Official citation"
   source_url: "https://authoritative-source.url"
   filename: "corresponding-pdf-filename.pdf"
   ---
   ```

5. **Validate**: Run validation before committing:

   ```bash
   python scripts/validate_references.py
   ```

6. **Commit**: Create a pull request with both the PDF and metadata file

## Automation

The repository includes several GitHub Actions workflows:

### On Push/Pull Request

- **validate-references**: Validates reference integrity
- **validate-structure**: Checks directory structure and naming conventions
- **markdown-lint**: Enforces markdown style rules

### On Merge to Main

- **generate-index**: Auto-generates reference index
- **update-changelog**: Updates changelog with changes

## Documentation Standards

### File Naming

- Use lowercase letters, numbers, and hyphens only
- No spaces in filenames
- Include year or version where applicable
- Examples:
  - `statute-inheritance-act-1975.pdf`
  - `case-ilott-v-mitson-2017.pdf`
  - `form-n1-claim-form.pdf`

### Metadata Requirements

Every PDF must have a corresponding metadata file with:

- **Required fields**: title, type, jurisdiction, date, citation, source_url, filename
- **YAML front matter**: Properly formatted and validated
- **Accurate information**: Verified against authoritative sources
- **Working URLs**: Source URLs must be accessible

### Markdown Style

- Maximum line length: 100 characters (documentation), 120 (code blocks)
- Consistent heading structure
- No trailing whitespace
- Unix line endings (LF)
- See `.markdownlint.yml` for complete rules

## Contributing

We welcome contributions! Please:

1. Read [ENGINEERING_PRACTICES.md](.github/ENGINEERING_PRACTICES.md)
2. Fork the repository
3. Create a feature branch
4. Make your changes following our standards
5. Run validation scripts
6. Submit a pull request

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
fix(validation): correct URL checking logic
docs(manual): update section on standing to bring claims
```

## Quality Assurance

All contributions are automatically validated for:

- ✓ Reference integrity (PDF-metadata pairing)
- ✓ Metadata schema compliance
- ✓ Directory structure
- ✓ Naming conventions
- ✓ Markdown style
- ✓ Working source URLs

## Testing

The repository includes test data:

- Sample PDFs in `docs/references/`
- Corresponding metadata in `docs/references/metadata/`
- Generated index in `docs/contentious-probate-manual/_references-and-authorities.md`

These demonstrate the expected structure and can be used to test the automation scripts.

## Maintenance

Regular maintenance tasks:

- **Monthly**: Review and update references for legislative changes
- **Quarterly**: Verify source URLs remain accessible
- **Annually**: Comprehensive review of all materials
- **As needed**: Add new references as they become relevant

## Support

For questions or issues:

1. Check existing documentation
2. Review [ENGINEERING_PRACTICES.md](.github/ENGINEERING_PRACTICES.md)
3. Search existing issues
4. Open a new issue with details

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Legislation from [legislation.gov.uk](https://www.legislation.gov.uk/)
- Case law from [BAILII](https://www.bailii.org/)
- Court forms from [HMCTS](https://www.gov.uk/government/organisations/hm-courts-and-tribunals-service)

## Version

**Current Version**: 1.0.0
**Last Updated**: 2025-11-16

---

For detailed engineering practices and guidelines, see
[ENGINEERING_PRACTICES.md](.github/ENGINEERING_PRACTICES.md)
