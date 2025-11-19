# Memori Submodule Integration Guide

## Overview

This document describes how Memori is integrated into the Contentious Estates repository as a git submodule, providing direct access to its core functionality.

## Adding Memori as a Submodule

To add Memori as a git submodule, the repository maintainer should run:

```bash
# Add Memori as a submodule
git submodule add https://github.com/mem0ri/mem0ri.git memori

# Initialize and update the submodule
git submodule init
git submodule update

# Commit the submodule addition
git add .gitmodules memori
git commit -m "Add Memori as a submodule"
```

## Cloning with Submodules

When cloning this repository, use the `--recursive` flag to automatically clone submodules:

```bash
git clone --recursive https://github.com/ccoxuk/Contentious-estates.git
```

If you already cloned without `--recursive`, initialize the submodules:

```bash
git submodule init
git submodule update
```

## Updating Memori Submodule

To update to the latest version of Memori:

```bash
cd memori
git pull origin main
cd ..
git add memori
git commit -m "Update Memori submodule"
```

## Memori Requirements

Ensure Memori's dependencies are installed:

```bash
# Install from the submodule
pip install -e memori/

# Or install from requirements
pip install -r memori/requirements.txt
```

## Integration Architecture

The Contentious Estates system integrates Memori through:

1. **memori_integration.py**: Core wrapper for Memori initialization
2. **memory_manager.py**: High-level API using Memori for case data
3. **Fallback Mode**: System runs with stub implementation if Memori is unavailable

## Stub Mode

If Memori is not available (not installed or import fails), the system operates in "stub mode":
- All operations succeed but use in-memory storage only
- Suitable for development and testing
- Warning logs indicate stub mode is active

## Production Setup

For production deployment:

1. Ensure Memori submodule is properly initialized
2. Install Memori dependencies
3. Configure database connection in environment variables
4. Enable audit logging and security features

## Environment Variables

```bash
# Database configuration for Memori
DATABASE_URL=sqlite:///contentious_memory.db

# Memori-specific settings
MEMORI_AUTO_INGEST=true
MEMORI_CONSCIOUS_INGEST=true

# Audit and security
AUDIT_ENABLED=true
AUDIT_LOG_FILE=audit.log
```

## Troubleshooting

### Submodule Not Found

If the memori directory is empty after cloning:

```bash
git submodule update --init --recursive
```

### Import Errors

If you get "No module named 'memori'" errors:

```bash
# Check submodule status
git submodule status

# Reinstall Memori
pip install -e memori/
```

### Updating Dependencies

After updating the Memori submodule, reinstall its dependencies:

```bash
pip install --upgrade -e memori/
```
