"""
Example Usage of Contentious Estates Memory System

This script demonstrates how to use the Memori-integrated memory management
system for contentious probate cases.
"""

import logging
from datetime import datetime, timedelta
from contentious_estates import ContentiousProbateMemory
from contentious_estates.query_templates import create_retrieval_system


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


def main():
    """Main example demonstrating the system usage"""
    
    print("=" * 80)
    print("Contentious Estates - Memory Management System Example")
    print("=" * 80)
    print()
    
    # Initialize the memory system for a specific case
    print("1. Initializing memory system...")
    memory = ContentiousProbateMemory(
        user_id="case_manager_001",
        case_id="PROB_2025_001",
        enable_audit=True
    )
    print("   ✓ Memory system initialized")
    print()
    
    # Store key dates
    print("2. Storing key dates...")
    memory.store_case_date(
        "filing_deadline",
        (datetime.now() + timedelta(days=45)).isoformat(),
        "Deadline to file probate application"
    )
    memory.store_case_date(
        "hearing_date",
        (datetime.now() + timedelta(days=60)).isoformat(),
        "Initial court hearing"
    )
    memory.store_case_date(
        "disclosure_deadline",
        (datetime.now() + timedelta(days=30)).isoformat(),
        "Deadline for disclosure of documents"
    )
    print("   ✓ Stored 3 key dates")
    print()
    
    # Store witness information
    print("3. Storing witness/party information...")
    memory.store_witness(
        "John Smith",
        role="executor",
        contact="john.smith@example.com",
        notes="Primary executor of the estate"
    )
    memory.store_witness(
        "Jane Doe",
        role="beneficiary",
        contact="jane.doe@example.com",
        notes="Primary beneficiary, daughter of deceased"
    )
    memory.store_witness(
        "Dr. Robert Brown",
        role="witness",
        contact="r.brown@example.com",
        notes="Witnessed the signing of the will"
    )
    print("   ✓ Stored 3 witnesses/parties")
    print()
    
    # Store evidence
    print("4. Storing evidence documents...")
    memory.store_evidence(
        "Last_Will_Testament_2024.pdf",
        description="Last will and testament dated December 2024",
        evidence_type="will",
        metadata={"pages": 12, "signed": True}
    )
    memory.store_evidence(
        "Medical_Records_2024.pdf",
        description="Medical records establishing mental capacity",
        evidence_type="disclosure",
        metadata={"pages": 45, "date_range": "2024-01 to 2024-12"}
    )
    memory.store_evidence(
        "Property_Valuation.pdf",
        description="Professional valuation of estate property",
        evidence_type="disclosure",
        metadata={"property_value": 450000}
    )
    print("   ✓ Stored 3 evidence documents")
    print()
    
    # Retrieve case context
    print("5. Retrieving case context...")
    context = memory.get_case_context()
    print(f"   ✓ Case ID: {context['case_id']}")
    print(f"   ✓ Key dates: {len(context['key_dates'])}")
    print(f"   ✓ Witnesses: {len(context['witnesses'])}")
    print(f"   ✓ Evidence: {len(context['evidence'])}")
    print()
    
    # Search evidence
    print("6. Searching evidence...")
    results = memory.search_evidence("will")
    print(f"   ✓ Found {len(results)} evidence items matching 'will':")
    for evidence in results:
        print(f"     - {evidence['file_name']}")
    print()
    
    # Get upcoming dates
    print("7. Checking upcoming dates (next 60 days)...")
    upcoming = memory.get_upcoming_dates(days_ahead=60)
    print(f"   ✓ Found {len(upcoming)} upcoming dates:")
    for date in upcoming:
        print(f"     - {date['date_type']}: {date['date_value'][:10]}")
        print(f"       {date['description']}")
    print()
    
    # Use retrieval system
    print("8. Using advanced retrieval system...")
    retrieval = create_retrieval_system()
    
    # List available templates
    templates = retrieval.list_templates()
    print(f"   ✓ Available query templates: {len(templates)}")
    for template in templates:
        print(f"     - {template['name']}: {template['description']}")
    print()
    
    # Execute witness query
    print("9. Querying witnesses by role...")
    executors = retrieval.execute_query(
        'witness_search',
        memory,
        role='executor'
    )
    print(f"   ✓ Found {len(executors)} executor(s):")
    for executor in executors:
        print(f"     - {executor['name']} ({executor['contact']})")
    print()
    
    # Close the memory system
    print("10. Closing memory system...")
    memory.close()
    print("   ✓ Memory system closed, audit logs saved")
    print()
    
    print("=" * 80)
    print("Example completed successfully!")
    print("Check 'audit.log' for detailed audit trail")
    print("=" * 80)


if __name__ == "__main__":
    main()
