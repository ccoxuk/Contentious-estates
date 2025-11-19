# Contentious Estates

A contentious probate repository enhanced with Memori's memory management and contextual data features for handling contentious probate processes with improved security, workflow automation, and user-specific memory.

## Features

- **Memori Integration**: Advanced memory management for probate case context
- **Persistent Case Memory**: Store and retrieve case-specific metadata across sessions
- **Key Date Management**: Track statutory deadlines and procedural dates
- **Witness & Party Management**: Manage executors, beneficiaries, and involved parties
- **Evidence Management**: Searchable memory for prior disclosures
- **Security & Audit Logging**: Comprehensive logging and secure access

## Installation

```bash
# Clone the repository with submodules
git clone --recursive https://github.com/ccoxuk/Contentious-estates.git
cd Contentious-estates

# Install dependencies
pip install -r requirements.txt

# Initialize the database
python -m contentious_estates.init_db
```

## Usage

```python
from contentious_estates import ContentiousProbateMemory

# Initialize the memory system
memory = ContentiousProbateMemory(
    user_id="case_manager_123",
    case_id="PROB_2024_001"
)

# Store case information
memory.store_case_date("filing_deadline", "2024-12-31")
memory.store_witness("John Doe", role="executor")
memory.store_evidence("Will_Document_v1.pdf", description="Original will")

# Retrieve case context
case_context = memory.get_case_context()
```

## License

MIT License - see LICENSE file for details
