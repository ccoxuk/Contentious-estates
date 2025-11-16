"""
Tests for Memori Integration Module
"""

import unittest
from contentious_estates.memori_integration import (
    MemoriConfig,
    MemoriIntegration,
    create_memori_integration
)


class TestMemoriConfig(unittest.TestCase):
    """Test MemoriConfig class"""
    
    def test_default_config(self):
        """Test default configuration values"""
        config = MemoriConfig()
        self.assertEqual(config.database_url, "sqlite:///contentious_memory.db")
        self.assertTrue(config.auto_ingest)
        self.assertTrue(config.conscious_ingest)
    
    def test_custom_config(self):
        """Test custom configuration"""
        config = MemoriConfig(
            database_url="postgresql://localhost/test",
            auto_ingest=False
        )
        self.assertEqual(config.database_url, "postgresql://localhost/test")
        self.assertFalse(config.auto_ingest)


class TestMemoriIntegration(unittest.TestCase):
    """Test MemoriIntegration class"""
    
    def test_initialization(self):
        """Test basic initialization"""
        integration = MemoriIntegration(user_id="test_user")
        self.assertEqual(integration.user_id, "test_user")
        self.assertIsNotNone(integration.config)
    
    def test_initialize_method(self):
        """Test initialize method"""
        integration = MemoriIntegration(user_id="test_user")
        result = integration.initialize()
        self.assertTrue(result)
    
    def test_enable_method(self):
        """Test enable method"""
        integration = MemoriIntegration(user_id="test_user")
        result = integration.enable()
        self.assertTrue(result)
        self.assertTrue(integration.is_enabled())
    
    def test_disable_method(self):
        """Test disable method"""
        integration = MemoriIntegration(user_id="test_user")
        integration.enable()
        result = integration.disable()
        self.assertTrue(result)
        self.assertFalse(integration.is_enabled())
    
    def test_factory_function(self):
        """Test create_memori_integration factory"""
        integration = create_memori_integration(user_id="test_user")
        self.assertIsNotNone(integration)
        self.assertTrue(integration.is_enabled())


if __name__ == '__main__':
    unittest.main()
