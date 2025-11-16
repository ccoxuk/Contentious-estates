# Contentious Estates - Developer Guide

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/ccoxuk/Contentious-estates.git
cd Contentious-estates

# Install the package
pip install -e .

# Run the example
python examples/basic_usage.py
```

### Basic Usage

```python
from contentious_estates import ContentiousProbateMemory

# Initialize memory for a case
memory = ContentiousProbateMemory(
    user_id="case_manager_001",
    case_id="PROB_2025_001"
)

# Store case information
memory.store_case_date("filing_deadline", "2025-12-31T00:00:00")
memory.store_witness("John Doe", role="executor")
memory.store_evidence("will.pdf", description="Last will and testament")

# Retrieve case context
context = memory.get_case_context()
print(f"Case has {len(context['witnesses'])} witnesses")

# Clean up
memory.close()
```

## Architecture

### Core Components

1. **memori_integration.py**: Wrapper for Memori initialization and management
2. **memory_manager.py**: High-level API for case data management
3. **models.py**: Data models for cases, dates, witnesses, and evidence
4. **query_templates.py**: Advanced query and retrieval system
5. **audit_logger.py**: Security and compliance logging
6. **config.py**: Configuration management

### Data Flow

```
User Application
    ↓
ContentiousProbateMemory (memory_manager.py)
    ↓
MemoriIntegration (memori_integration.py)
    ↓
Memori (submodule - when available)
    ↓
Database (SQLite/PostgreSQL/etc.)
```

## Development Workflow

### Setting Up Development Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode with dev dependencies
pip install -e ".[dev]"

# Run tests
python -m unittest discover tests/
```

### Code Style

The project follows PEP 8 guidelines. Use tools for consistency:

```bash
# Format code
black contentious_estates/

# Check style
flake8 contentious_estates/
```

### Running Tests

```bash
# Run all tests
python -m unittest discover tests/ -v

# Run specific test file
python -m unittest tests.test_memory_manager -v

# Run specific test class
python -m unittest tests.test_memory_manager.TestMemoryManager -v

# Run specific test
python -m unittest tests.test_memory_manager.TestMemoryManager.test_store_case_date -v
```

### Adding New Features

1. **Create feature branch**
   ```bash
   git checkout -b feature/new-feature
   ```

2. **Implement feature**
   - Add code in appropriate module
   - Follow existing patterns and conventions
   - Add docstrings to all public methods

3. **Add tests**
   - Create/update test file in `tests/`
   - Ensure all edge cases are covered
   - Aim for high test coverage

4. **Update documentation**
   - Update API.md if adding public API
   - Update README.md if changing usage
   - Add examples if applicable

5. **Run tests**
   ```bash
   python -m unittest discover tests/
   ```

6. **Commit and push**
   ```bash
   git add .
   git commit -m "Add new feature"
   git push origin feature/new-feature
   ```

## Extending the System

### Custom Query Templates

Create custom query templates for specialized searches:

```python
from contentious_estates.query_templates import QueryTemplate

class DeadlineQuery(QueryTemplate):
    def __init__(self):
        super().__init__(
            "deadline_check",
            "Check for approaching deadlines"
        )
    
    def execute(self, memory_manager, threshold_days=7):
        """Find deadlines within threshold"""
        upcoming = memory_manager.get_upcoming_dates(threshold_days)
        return [d for d in upcoming if 'deadline' in d['date_type']]

# Register the template
from contentious_estates.query_templates import create_retrieval_system

retrieval = create_retrieval_system()
retrieval.register_template(DeadlineQuery())

# Use it
results = retrieval.execute_query('deadline_check', memory, threshold_days=14)
```

### Custom Data Models

Extend the data models for specific use cases:

```python
from contentious_estates.models import Evidence
from dataclasses import dataclass
from typing import Optional

@dataclass
class CourtEvidence(Evidence):
    """Extended evidence model with court-specific fields"""
    exhibit_number: Optional[str] = None
    admitted_date: Optional[str] = None
    objection_status: Optional[str] = None
```

### Integration with Other Systems

Integrate with document management systems:

```python
class DocumentManagerIntegration:
    def __init__(self, memory, doc_manager):
        self.memory = memory
        self.doc_manager = doc_manager
    
    def store_document(self, file_path, description, evidence_type):
        """Store document in both systems"""
        # Upload to document manager
        doc_id = self.doc_manager.upload(file_path)
        
        # Store reference in memory
        self.memory.store_evidence(
            file_name=file_path,
            description=description,
            evidence_type=evidence_type,
            metadata={"doc_manager_id": doc_id}
        )
```

## Database Configuration

### SQLite (Default)

```python
memory = ContentiousProbateMemory(
    user_id="user",
    case_id="case",
    database_url="sqlite:///contentious_memory.db"
)
```

### PostgreSQL

```python
memory = ContentiousProbateMemory(
    user_id="user",
    case_id="case",
    database_url="postgresql://user:password@localhost/contentious_db"
)
```

### MySQL

```python
memory = ContentiousProbateMemory(
    user_id="user",
    case_id="case",
    database_url="mysql://user:password@localhost/contentious_db"
)
```

## Performance Considerations

### Caching

The system uses in-memory caching for the current session. For high-volume applications, consider implementing Redis caching:

```python
import redis

cache = redis.Redis(host='localhost', port=6379, db=0)

def get_cached_context(case_id):
    """Get context from cache or database"""
    cached = cache.get(f"case:{case_id}")
    if cached:
        return json.loads(cached)
    
    # Fetch from database
    context = memory.get_case_context()
    
    # Cache for 1 hour
    cache.setex(f"case:{case_id}", 3600, json.dumps(context))
    return context
```

### Batch Operations

For bulk data loading:

```python
def bulk_import_witnesses(memory, witnesses_data):
    """Import multiple witnesses efficiently"""
    for witness_data in witnesses_data:
        memory.store_witness(**witness_data)
    
    # Commit in batch if using database transactions
```

## Troubleshooting

### Common Issues

**Issue: "No module named 'memori'"**

Solution: The system runs in stub mode when Memori is not available. This is expected for development. To use full Memori functionality, add it as a submodule:

```bash
git submodule add https://github.com/mem0ri/mem0ri.git memori
git submodule update --init
pip install -e memori/
```

**Issue: Audit logs not being written**

Solution: Check file permissions and ensure audit logging is enabled:

```python
memory = ContentiousProbateMemory(
    user_id="user",
    case_id="case",
    enable_audit=True  # Ensure this is True
)

# Check audit logger
if memory.audit_logger:
    print("Audit logging is enabled")
```

**Issue: Database connection errors**

Solution: Verify database URL and ensure the database is accessible:

```python
import sqlalchemy

# Test connection
engine = sqlalchemy.create_engine("sqlite:///test.db")
try:
    connection = engine.connect()
    print("Connection successful")
    connection.close()
except Exception as e:
    print(f"Connection failed: {e}")
```

## Best Practices

### 1. Always Close Memory Instances

```python
memory = ContentiousProbateMemory(user_id="user", case_id="case")
try:
    # Use memory
    memory.store_case_date("date", "2025-12-31")
finally:
    memory.close()
```

Or use context manager pattern (if implemented):

```python
with ContentiousProbateMemory(user_id="user", case_id="case") as memory:
    memory.store_case_date("date", "2025-12-31")
```

### 2. Use Type Hints

```python
from typing import Dict, List, Optional

def process_case_data(
    memory: ContentiousProbateMemory,
    case_data: Dict[str, Any]
) -> bool:
    """Process case data with type hints"""
    return memory.store_case_date(**case_data)
```

### 3. Handle Errors Gracefully

```python
def safe_store_witness(memory, name, role):
    """Safely store witness with error handling"""
    try:
        return memory.store_witness(name=name, role=role)
    except Exception as e:
        logger.error(f"Failed to store witness {name}: {e}")
        return False
```

### 4. Use Structured Logging

```python
import logging

logger = logging.getLogger(__name__)

def process_case(memory, case_id):
    logger.info(f"Processing case {case_id}")
    try:
        context = memory.get_case_context()
        logger.info(f"Retrieved context for case {case_id}")
        return context
    except Exception as e:
        logger.error(f"Error processing case {case_id}", exc_info=True)
        raise
```

## Contributing

See CONTRIBUTING.md for guidelines on contributing to this project.

## License

MIT License - see LICENSE file for details.
