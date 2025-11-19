"""
Unit Tests for Contentious Estates Memory Management
"""

import unittest
from datetime import datetime, timedelta
from contentious_estates import ContentiousProbateMemory
from contentious_estates.query_templates import create_retrieval_system
from contentious_estates.models import KeyDate, Witness, Evidence


class TestMemoryManager(unittest.TestCase):
    """Test the ContentiousProbateMemory class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.memory = ContentiousProbateMemory(
            user_id="test_user",
            case_id="TEST_CASE_001",
            enable_audit=False
        )
    
    def test_initialization(self):
        """Test memory manager initialization"""
        self.assertIsNotNone(self.memory)
        self.assertEqual(self.memory.user_id, "test_user")
        self.assertEqual(self.memory.case_id, "TEST_CASE_001")
    
    def test_store_case_date(self):
        """Test storing key dates"""
        result = self.memory.store_case_date(
            "filing_deadline",
            "2025-12-31T00:00:00",
            "Test deadline"
        )
        self.assertTrue(result)
        
        context = self.memory.get_case_context()
        self.assertIn("filing_deadline", context["key_dates"])
    
    def test_store_witness(self):
        """Test storing witness information"""
        result = self.memory.store_witness(
            "Test Witness",
            role="executor",
            contact="test@example.com"
        )
        self.assertTrue(result)
        
        context = self.memory.get_case_context()
        self.assertEqual(len(context["witnesses"]), 1)
        self.assertEqual(context["witnesses"][0]["name"], "Test Witness")
    
    def test_store_evidence(self):
        """Test storing evidence"""
        result = self.memory.store_evidence(
            "test_document.pdf",
            description="Test evidence document",
            evidence_type="will"
        )
        self.assertTrue(result)
        
        context = self.memory.get_case_context()
        self.assertEqual(len(context["evidence"]), 1)
        self.assertEqual(context["evidence"][0]["file_name"], "test_document.pdf")
    
    def test_get_case_context(self):
        """Test retrieving case context"""
        # Add some data
        self.memory.store_case_date("test_date", "2025-12-31T00:00:00")
        self.memory.store_witness("Test Person", role="witness")
        self.memory.store_evidence("test.pdf", description="Test")
        
        context = self.memory.get_case_context()
        
        self.assertEqual(context["case_id"], "TEST_CASE_001")
        self.assertEqual(context["user_id"], "test_user")
        self.assertIn("key_dates", context)
        self.assertIn("witnesses", context)
        self.assertIn("evidence", context)
    
    def test_search_evidence(self):
        """Test evidence searching"""
        self.memory.store_evidence(
            "will_v1.pdf",
            description="Last will and testament",
            evidence_type="will"
        )
        self.memory.store_evidence(
            "contract.pdf",
            description="Employment contract",
            evidence_type="disclosure"
        )
        
        results = self.memory.search_evidence("will")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["file_name"], "will_v1.pdf")
    
    def test_get_upcoming_dates(self):
        """Test getting upcoming dates"""
        # Add a future date
        future_date = (datetime.now() + timedelta(days=15)).isoformat()
        self.memory.store_case_date("future_deadline", future_date)
        
        # Add a past date
        past_date = (datetime.now() - timedelta(days=15)).isoformat()
        self.memory.store_case_date("past_deadline", past_date)
        
        upcoming = self.memory.get_upcoming_dates(days_ahead=30)
        self.assertEqual(len(upcoming), 1)
        self.assertEqual(upcoming[0]["date_type"], "future_deadline")


class TestModels(unittest.TestCase):
    """Test data models"""
    
    def test_key_date_creation(self):
        """Test KeyDate model"""
        key_date = KeyDate(
            date_type="deadline",
            date_value="2025-12-31T00:00:00",
            description="Test deadline"
        )
        self.assertEqual(key_date.date_type, "deadline")
        self.assertIsNotNone(key_date.created_at)
        
        data = key_date.to_dict()
        self.assertIn("date_type", data)
        self.assertIn("date_value", data)
    
    def test_witness_creation(self):
        """Test Witness model"""
        witness = Witness(
            name="John Doe",
            role="executor",
            contact="john@example.com"
        )
        self.assertEqual(witness.name, "John Doe")
        self.assertEqual(witness.role, "executor")
        
        data = witness.to_dict()
        self.assertIn("name", data)
        self.assertIn("role", data)
    
    def test_evidence_creation(self):
        """Test Evidence model"""
        evidence = Evidence(
            file_name="test.pdf",
            description="Test document",
            evidence_type="will"
        )
        self.assertEqual(evidence.file_name, "test.pdf")
        
        data = evidence.to_dict()
        self.assertIn("file_name", data)
        self.assertIn("description", data)


class TestQueryTemplates(unittest.TestCase):
    """Test query template system"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.memory = ContentiousProbateMemory(
            user_id="test_user",
            case_id="TEST_QUERY_001",
            enable_audit=False
        )
        self.retrieval = create_retrieval_system()
    
    def test_retrieval_system_initialization(self):
        """Test retrieval system setup"""
        templates = self.retrieval.list_templates()
        self.assertGreater(len(templates), 0)
    
    def test_witness_query(self):
        """Test witness search query template"""
        self.memory.store_witness("Test Executor", role="executor")
        self.memory.store_witness("Test Beneficiary", role="beneficiary")
        
        results = self.retrieval.execute_query(
            'witness_search',
            self.memory,
            role='executor'
        )
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["role"], "executor")
    
    def test_evidence_query(self):
        """Test evidence search query template"""
        self.memory.store_evidence("will.pdf", "Last will", evidence_type="will")
        self.memory.store_evidence("contract.pdf", "Contract", evidence_type="disclosure")
        
        results = self.retrieval.execute_query(
            'evidence_search',
            self.memory,
            evidence_type='will'
        )
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["evidence_type"], "will")
    
    def test_case_context_query(self):
        """Test case context query template"""
        self.memory.store_case_date("test_date", "2025-12-31T00:00:00")
        
        context = self.retrieval.execute_query(
            'case_context',
            self.memory
        )
        self.assertIn("case_id", context)
        self.assertEqual(context["case_id"], "TEST_QUERY_001")


if __name__ == '__main__':
    unittest.main()
