"""
Audit Logger for Contentious Probate System

Provides comprehensive audit logging for security, compliance, and
tracking of all operations on case data.
"""

import logging
from datetime import datetime, timezone
from typing import Optional, Dict, Any
import json
from pathlib import Path


logger = logging.getLogger(__name__)


class AuditLogger:
    """
    Audit logging system for tracking all operations.
    
    Logs all access and modifications to case data with timestamps,
    user information, and operation details.
    """
    
    def __init__(
        self,
        log_file: Optional[str] = None,
        enabled: bool = True
    ):
        """
        Initialize the audit logger.
        
        Args:
            log_file: Path to audit log file (default: audit.log)
            enabled: Whether audit logging is enabled
        """
        self.enabled = enabled
        self.log_file = log_file or "audit.log"
        
        if self.enabled:
            self._setup_logger()
    
    def _setup_logger(self):
        """Configure the audit logger with file handler"""
        self.audit_logger = logging.getLogger("contentious_estates.audit")
        self.audit_logger.setLevel(logging.INFO)
        
        # Don't add handlers if they already exist
        if self.audit_logger.handlers:
            return
        
        # Create file handler
        fh = logging.FileHandler(self.log_file)
        fh.setLevel(logging.INFO)
        
        # Create formatter
        formatter = logging.Formatter(
            '%(asctime)s - AUDIT - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        fh.setFormatter(formatter)
        
        # Add handler
        self.audit_logger.addHandler(fh)
    
    def log_event(
        self,
        event_type: str,
        user_id: str,
        case_id: str,
        details: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None
    ):
        """
        Log an audit event.
        
        Args:
            event_type: Type of event (e.g., 'STORE_DATE', 'GET_CONTEXT')
            user_id: User performing the action
            case_id: Case being accessed/modified
            details: Human-readable details
            metadata: Additional structured metadata
        """
        if not self.enabled:
            return
        
        audit_entry = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "event_type": event_type,
            "user_id": user_id,
            "case_id": case_id,
            "details": details,
            "metadata": metadata or {}
        }
        
        # Log as JSON for easy parsing
        self.audit_logger.info(json.dumps(audit_entry))
    
    def log_access(
        self,
        user_id: str,
        case_id: str,
        resource: str,
        action: str = "READ"
    ):
        """
        Log access to a resource.
        
        Args:
            user_id: User accessing the resource
            case_id: Case being accessed
            resource: Resource being accessed
            action: Type of access (READ, WRITE, DELETE)
        """
        self.log_event(
            f"ACCESS_{action}",
            user_id=user_id,
            case_id=case_id,
            details=f"{action} access to {resource}"
        )
    
    def log_security_event(
        self,
        event_type: str,
        user_id: str,
        case_id: str,
        severity: str = "INFO",
        details: Optional[str] = None
    ):
        """
        Log a security-related event.
        
        Args:
            event_type: Type of security event
            user_id: User involved
            case_id: Case involved
            severity: Severity level (INFO, WARNING, CRITICAL)
            details: Event details
        """
        self.log_event(
            f"SECURITY_{event_type}",
            user_id=user_id,
            case_id=case_id,
            details=details,
            metadata={"severity": severity}
        )


class SecureTraceLogger:
    """
    Runtime trace logger for debugging and monitoring.
    
    Provides clean, secure logging of runtime operations.
    """
    
    def __init__(self, log_level: int = logging.INFO):
        """
        Initialize trace logger.
        
        Args:
            log_level: Logging level
        """
        self.logger = logging.getLogger("contentious_estates.trace")
        self.logger.setLevel(log_level)
        
        # Console handler
        ch = logging.StreamHandler()
        ch.setLevel(log_level)
        
        formatter = logging.Formatter(
            '%(asctime)s - TRACE - %(name)s - %(levelname)s - %(message)s'
        )
        ch.setFormatter(formatter)
        
        if not self.logger.handlers:
            self.logger.addHandler(ch)
    
    def trace(self, message: str, **kwargs):
        """Log a trace message"""
        if kwargs:
            message = f"{message} | {json.dumps(kwargs)}"
        self.logger.info(message)
    
    def trace_error(self, message: str, error: Exception):
        """Log an error trace"""
        self.logger.error(f"{message}: {str(error)}", exc_info=True)
