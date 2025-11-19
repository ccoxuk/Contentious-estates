# Scripts

This directory contains automation and validation scripts for the Contentious Probate Manual & Toolkit.

## Available Scripts

### validate_references.py

**Purpose**: Validates reference document integrity

**Features**:
- Checks that every PDF has a corresponding metadata file
- Validates metadata YAML schema
- Verifies all required fields are present
- Tests source URL accessibility
- Reports missing or malformed entries
- Identifies orphaned files

**Usage**:
```bash
python scripts/validate_references.py
```

**Exit Codes**:
- 0: All validations passed
- 1: Validation errors found

### generate_reference_index.py

**Purpose**: Generates comprehensive reference index

**Features**:
- Reads all metadata files
- Categorizes references by type
- Sorts chronologically or alphabetically
- Generates formatted markdown output
- Creates `_references-and-authorities.md` in manual directory

**Usage**:
```bash
python scripts/generate_reference_index.py
```

### update_changelog.py

**Purpose**: Maintains change log

**Features**:
- Tracks additions, modifications, and deletions
- Records reference updates
- Timestamps all changes
- Appends to `_changelog.md`

**Usage**:
```bash
python scripts/update_changelog.py
```

## Requirements

All scripts require Python 3.8 or higher.

Install dependencies:
```bash
pip install -r requirements.txt
```

## Development

When modifying scripts:

1. Follow PEP 8 style guidelines
2. Include type hints
3. Add comprehensive error handling
4. Update documentation
5. Test with sample data
6. Verify GitHub Actions integration

## Testing

Test scripts locally before committing:

```bash
# Validate references
python scripts/validate_references.py

# Generate index
python scripts/generate_reference_index.py

# Update changelog
python scripts/update_changelog.py
```

## Integration

These scripts are integrated with GitHub Actions workflows:

- `validate-references.yml`: Runs on every push/PR
- `generate-index.yml`: Runs on merge to main
- `update-changelog.yml`: Runs on merge to main

See `.github/workflows/` for workflow definitions.

## Contributing

See [ENGINEERING_PRACTICES.md](../.github/ENGINEERING_PRACTICES.md) for detailed guidelines.
