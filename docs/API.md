# API Documentation

## ContentionsProbateMemory

Main class for managing case-specific memory in contentious probate applications.

### Initialization

```python
from contentious_estates import ContentiousProbateMemory

memory = ContentiousProbateMemory(
    user_id="case_manager_123",
    case_id="PROB_2024_001",
    database_url="sqlite:///contentious_memory.db",  # optional
    enable_audit=True  # optional, default True
)
```

### Methods

#### store_case_date()

Store a key date for the case.

```python
memory.store_case_date(
    date_type="filing_deadline",
    date_value="2024-12-31T00:00:00",
    description="Deadline to file probate application"
)
```

**Parameters:**
- `date_type` (str): Type of date (e.g., 'filing_deadline', 'hearing_date')
- `date_value` (str): ISO format date string
- `description` (str, optional): Human-readable description

**Returns:** `bool` - True if successful

---

#### store_witness()

Store information about a witness or party.

```python
memory.store_witness(
    name="John Smith",
    role="executor",
    contact="john.smith@example.com",
    notes="Primary executor of the estate"
)
```

**Parameters:**
- `name` (str): Name of the witness/party
- `role` (str): Role (e.g., 'executor', 'beneficiary', 'witness')
- `contact` (str, optional): Contact information
- `notes` (str, optional): Additional notes

**Returns:** `bool` - True if successful

---

#### store_evidence()

Store evidence or documentation information.

```python
memory.store_evidence(
    file_name="Last_Will_Testament.pdf",
    description="Last will and testament",
    evidence_type="will",
    metadata={"pages": 12, "signed": True}
)
```

**Parameters:**
- `file_name` (str): Name of the evidence file
- `description` (str): Description of the evidence
- `evidence_type` (str, optional): Type (e.g., 'will', 'disclosure', 'affidavit')
- `metadata` (dict, optional): Additional metadata

**Returns:** `bool` - True if successful

---

#### get_case_context()

Retrieve the complete case context.

```python
context = memory.get_case_context()
```

**Returns:** `dict` - Dictionary containing:
- `case_id`: Case identifier
- `user_id`: User identifier
- `key_dates`: Dictionary of key dates
- `witnesses`: List of witnesses/parties
- `evidence`: List of evidence items
- `metadata`: Additional metadata

---

#### search_evidence()

Search evidence by description or metadata.

```python
results = memory.search_evidence("will")
```

**Parameters:**
- `query` (str): Search query string

**Returns:** `list` - List of matching evidence items

---

#### get_upcoming_dates()

Get upcoming key dates within a specified timeframe.

```python
upcoming = memory.get_upcoming_dates(days_ahead=30)
```

**Parameters:**
- `days_ahead` (int): Number of days to look ahead (default: 30)

**Returns:** `list` - List of upcoming key dates, sorted by date

---

#### close()

Clean up and close the memory manager.

```python
memory.close()
```

---

## Query Templates and Retrieval System

Advanced querying capabilities for case data.

### Initialization

```python
from contentious_estates.query_templates import create_retrieval_system

retrieval = create_retrieval_system()
```

### Available Query Templates

#### date_range

Search for events/dates within a specified range.

```python
results = retrieval.execute_query(
    'date_range',
    memory,
    days_ahead=60
)
```

#### witness_search

Search for witnesses by role or name.

```python
results = retrieval.execute_query(
    'witness_search',
    memory,
    role='executor'
)
```

#### evidence_search

Search evidence by type, description, or metadata.

```python
results = retrieval.execute_query(
    'evidence_search',
    memory,
    evidence_type='will'
)
```

#### case_context

Retrieve complete case context.

```python
context = retrieval.execute_query(
    'case_context',
    memory,
    include_sections=['key_dates', 'witnesses']
)
```

### Custom Query Templates

Create and register custom query templates:

```python
from contentious_estates.query_templates import QueryTemplate

class CustomQuery(QueryTemplate):
    def __init__(self):
        super().__init__("custom", "Custom query description")
    
    def execute(self, memory_manager, **kwargs):
        # Your custom query logic
        return results

retrieval.register_template(CustomQuery())
```

---

## Audit Logging

Security and compliance logging.

### Initialization

```python
from contentious_estates.audit_logger import AuditLogger

audit = AuditLogger(
    log_file="audit.log",
    enabled=True
)
```

### Methods

#### log_event()

Log a general audit event.

```python
audit.log_event(
    event_type="CASE_UPDATED",
    user_id="user123",
    case_id="case456",
    details="Updated case information",
    metadata={"field": "value"}
)
```

#### log_access()

Log access to a resource.

```python
audit.log_access(
    user_id="user123",
    case_id="case456",
    resource="case_data",
    action="READ"
)
```

#### log_security_event()

Log a security-related event.

```python
audit.log_security_event(
    event_type="UNAUTHORIZED_ACCESS",
    user_id="user123",
    case_id="case456",
    severity="WARNING",
    details="Attempted access to restricted case"
)
```

---

## Configuration

Environment variables for configuration:

```bash
# Database
DATABASE_URL=sqlite:///contentious_memory.db

# Memori settings
MEMORI_AUTO_INGEST=true
MEMORI_CONSCIOUS_INGEST=true

# Audit settings
AUDIT_ENABLED=true
AUDIT_LOG_FILE=audit.log

# Security
ENABLE_ENCRYPTION=false
SECRET_KEY=your-secret-key

# Logging
LOG_LEVEL=INFO
```

---

## Error Handling

All methods return boolean success indicators or raise appropriate exceptions:

```python
try:
    success = memory.store_case_date("deadline", "2024-12-31")
    if not success:
        print("Failed to store date")
except Exception as e:
    print(f"Error: {e}")
```

---

## Thread Safety

The current implementation is not thread-safe. For multi-threaded applications, use appropriate locking mechanisms:

```python
import threading

lock = threading.Lock()

with lock:
    memory.store_case_date("deadline", "2024-12-31")
```
