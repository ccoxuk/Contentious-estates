"""
Tests for Audit Logger Module
"""

import unittest
import os
import json
import logging
from contentious_estates.audit_logger import AuditLogger, SecureTraceLogger


class TestAuditLogger(unittest.TestCase):
    """Test AuditLogger class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.test_log_file = "/tmp/test_audit.log"
        if os.path.exists(self.test_log_file):
            os.remove(self.test_log_file)
        
        # Clear any existing handlers
        audit_logger = logging.getLogger("contentious_estates.audit")
        audit_logger.handlers.clear()
    
    def tearDown(self):
        """Clean up test files"""
        if os.path.exists(self.test_log_file):
            os.remove(self.test_log_file)
        
        # Clear handlers
        audit_logger = logging.getLogger("contentious_estates.audit")
        audit_logger.handlers.clear()
    
    def test_initialization(self):
        """Test audit logger initialization"""
        logger = AuditLogger(log_file=self.test_log_file)
        self.assertTrue(logger.enabled)
        self.assertEqual(logger.log_file, self.test_log_file)
    
    def test_log_event(self):
        """Test logging an event"""
        logger = AuditLogger(log_file=self.test_log_file)
        logger.log_event(
            "TEST_EVENT",
            user_id="test_user",
            case_id="test_case",
            details="Test event details"
        )
        
        # Flush handlers to ensure data is written
        for handler in logger.audit_logger.handlers:
            handler.flush()
        
        # Check if log file was created and contains the event
        self.assertTrue(os.path.exists(self.test_log_file))
        with open(self.test_log_file, 'r') as f:
            content = f.read()
            self.assertIn("TEST_EVENT", content)
            self.assertIn("test_user", content)
    
    def test_log_access(self):
        """Test logging access events"""
        logger = AuditLogger(log_file=self.test_log_file)
        logger.log_access(
            user_id="test_user",
            case_id="test_case",
            resource="case_data",
            action="READ"
        )
        
        # Flush handlers to ensure data is written
        for handler in logger.audit_logger.handlers:
            handler.flush()
        
        with open(self.test_log_file, 'r') as f:
            content = f.read()
            self.assertIn("ACCESS_READ", content)
    
    def test_log_security_event(self):
        """Test logging security events"""
        logger = AuditLogger(log_file=self.test_log_file)
        logger.log_security_event(
            "UNAUTHORIZED_ACCESS",
            user_id="test_user",
            case_id="test_case",
            severity="WARNING"
        )
        
        # Flush handlers to ensure data is written
        for handler in logger.audit_logger.handlers:
            handler.flush()
        
        with open(self.test_log_file, 'r') as f:
            content = f.read()
            self.assertIn("SECURITY_UNAUTHORIZED_ACCESS", content)
            self.assertIn("WARNING", content)
    
    def test_disabled_logger(self):
        """Test that disabled logger doesn't create files"""
        logger = AuditLogger(log_file=self.test_log_file, enabled=False)
        logger.log_event(
            "TEST_EVENT",
            user_id="test_user",
            case_id="test_case"
        )
        
        # File should not be created when logger is disabled
        self.assertFalse(os.path.exists(self.test_log_file))


class TestSecureTraceLogger(unittest.TestCase):
    """Test SecureTraceLogger class"""
    
    def test_initialization(self):
        """Test trace logger initialization"""
        logger = SecureTraceLogger()
        self.assertIsNotNone(logger.logger)
    
    def test_trace_method(self):
        """Test trace logging method"""
        logger = SecureTraceLogger()
        # Should not raise any exceptions
        logger.trace("Test trace message", key="value")
    
    def test_trace_error_method(self):
        """Test error trace logging"""
        logger = SecureTraceLogger()
        try:
            raise ValueError("Test error")
        except ValueError as e:
            # Should not raise any exceptions
            logger.trace_error("Test error occurred", e)


if __name__ == '__main__':
    unittest.main()
