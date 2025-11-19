"""
Memory Manager for Contentious Probate Cases

This module provides the main interface for managing case-specific memory,
including key dates, witness data, evidence management, and case context.
"""

import logging
from datetime import datetime
from typing import Optional, Dict, Any, List
from pathlib import Path
import json

from .memori_integration import create_memori_integration, MemoriIntegration
from .models import CaseMetadata, KeyDate, Witness, Evidence
from .audit_logger import AuditLogger


logger = logging.getLogger(__name__)


class ContentiousProbateMemory:
    """
    Main memory management class for contentious probate cases.
    
    Integrates Memori for persistent storage and retrieval of case-specific
    information across user sessions.
    """
    
    def __init__(
        self,
        user_id: str,
        case_id: str,
        database_url: Optional[str] = None,
        enable_audit: bool = True
    ):
        """
        Initialize the probate memory manager.
        
        Args:
            user_id: Unique identifier for the user
            case_id: Unique identifier for the probate case
            database_url: Optional database URL for Memori storage
            enable_audit: Enable audit logging
        """
        self.user_id = user_id
        self.case_id = case_id
        
        # Create unique session identifier
        session_id = f"{user_id}_{case_id}"
        
        # Initialize Memori integration
        self.memori = create_memori_integration(
            user_id=session_id,
            database_url=database_url,
            memory_filters={
                "case_id": case_id,
                "user_id": user_id
            }
        )
        
        # Initialize audit logger
        self.audit_logger = AuditLogger(enabled=enable_audit) if enable_audit else None
        
        # In-memory cache for current session
        self._case_metadata = CaseMetadata(case_id=case_id, user_id=user_id)
        
        logger.info(f"ContentiousProbateMemory initialized for case: {case_id}")
        
        if self.audit_logger:
            self.audit_logger.log_event(
                "MEMORY_INIT",
                user_id=user_id,
                case_id=case_id,
                details="Memory manager initialized"
            )
    
    def store_case_date(
        self,
        date_type: str,
        date_value: str,
        description: Optional[str] = None
    ) -> bool:
        """
        Store a key date for the case.
        
        Args:
            date_type: Type of date (e.g., 'filing_deadline', 'hearing_date')
            date_value: ISO format date string
            description: Optional description
            
        Returns:
            True if stored successfully
        """
        try:
            key_date = KeyDate(
                date_type=date_type,
                date_value=date_value,
                description=description
            )
            
            self._case_metadata.key_dates[date_type] = key_date
            
            # Store in Memori (when available, uses stub for now)
            self._store_in_memory("key_date", key_date.to_dict())
            
            if self.audit_logger:
                self.audit_logger.log_event(
                    "STORE_DATE",
                    user_id=self.user_id,
                    case_id=self.case_id,
                    details=f"Stored date: {date_type} = {date_value}"
                )
            
            logger.info(f"Stored key date: {date_type} = {date_value}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to store case date: {e}")
            return False
    
    def store_witness(
        self,
        name: str,
        role: str,
        contact: Optional[str] = None,
        notes: Optional[str] = None
    ) -> bool:
        """
        Store witness/party information.
        
        Args:
            name: Name of the witness/party
            role: Role (e.g., 'executor', 'beneficiary', 'witness')
            contact: Optional contact information
            notes: Optional notes
            
        Returns:
            True if stored successfully
        """
        try:
            witness = Witness(
                name=name,
                role=role,
                contact=contact,
                notes=notes
            )
            
            self._case_metadata.witnesses.append(witness)
            
            # Store in Memori
            self._store_in_memory("witness", witness.to_dict())
            
            if self.audit_logger:
                self.audit_logger.log_event(
                    "STORE_WITNESS",
                    user_id=self.user_id,
                    case_id=self.case_id,
                    details=f"Stored witness: {name} ({role})"
                )
            
            logger.info(f"Stored witness: {name} ({role})")
            return True
            
        except Exception as e:
            logger.error(f"Failed to store witness: {e}")
            return False
    
    def store_evidence(
        self,
        file_name: str,
        description: str,
        evidence_type: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None
    ) -> bool:
        """
        Store evidence information.
        
        Args:
            file_name: Name of the evidence file
            description: Description of the evidence
            evidence_type: Type of evidence (e.g., 'will', 'disclosure', 'affidavit')
            metadata: Additional metadata
            
        Returns:
            True if stored successfully
        """
        try:
            evidence = Evidence(
                file_name=file_name,
                description=description,
                evidence_type=evidence_type,
                metadata=metadata or {}
            )
            
            self._case_metadata.evidence.append(evidence)
            
            # Store in Memori
            self._store_in_memory("evidence", evidence.to_dict())
            
            if self.audit_logger:
                self.audit_logger.log_event(
                    "STORE_EVIDENCE",
                    user_id=self.user_id,
                    case_id=self.case_id,
                    details=f"Stored evidence: {file_name}"
                )
            
            logger.info(f"Stored evidence: {file_name}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to store evidence: {e}")
            return False
    
    def get_case_context(self) -> Dict[str, Any]:
        """
        Retrieve complete case context.
        
        Returns:
            Dictionary containing all case information
        """
        context = {
            "case_id": self.case_id,
            "user_id": self.user_id,
            "key_dates": {k: v.to_dict() for k, v in self._case_metadata.key_dates.items()},
            "witnesses": [w.to_dict() for w in self._case_metadata.witnesses],
            "evidence": [e.to_dict() for e in self._case_metadata.evidence],
            "metadata": self._case_metadata.additional_metadata
        }
        
        if self.audit_logger:
            self.audit_logger.log_event(
                "GET_CONTEXT",
                user_id=self.user_id,
                case_id=self.case_id,
                details="Retrieved case context"
            )
        
        return context
    
    def search_evidence(self, query: str) -> List[Dict[str, Any]]:
        """
        Search evidence by description or metadata.
        
        Args:
            query: Search query string
            
        Returns:
            List of matching evidence items
        """
        results = []
        query_lower = query.lower()
        
        for evidence in self._case_metadata.evidence:
            if (query_lower in evidence.description.lower() or
                query_lower in evidence.file_name.lower() or
                (evidence.evidence_type and query_lower in evidence.evidence_type.lower())):
                results.append(evidence.to_dict())
        
        if self.audit_logger:
            self.audit_logger.log_event(
                "SEARCH_EVIDENCE",
                user_id=self.user_id,
                case_id=self.case_id,
                details=f"Searched evidence with query: {query}, found {len(results)} results"
            )
        
        logger.info(f"Evidence search for '{query}' returned {len(results)} results")
        return results
    
    def get_upcoming_dates(self, days_ahead: int = 30) -> List[Dict[str, Any]]:
        """
        Get upcoming key dates within specified timeframe.
        
        Args:
            days_ahead: Number of days to look ahead
            
        Returns:
            List of upcoming key dates
        """
        from datetime import datetime, timedelta
        
        now = datetime.now()
        cutoff = now + timedelta(days=days_ahead)
        upcoming = []
        
        for date_type, key_date in self._case_metadata.key_dates.items():
            try:
                date_obj = datetime.fromisoformat(key_date.date_value)
                if now <= date_obj <= cutoff:
                    upcoming.append(key_date.to_dict())
            except (ValueError, AttributeError):
                # Skip invalid dates
                continue
        
        # Sort by date
        upcoming.sort(key=lambda x: x.get('date_value', ''))
        
        logger.info(f"Found {len(upcoming)} upcoming dates within {days_ahead} days")
        return upcoming
    
    def _store_in_memory(self, data_type: str, data: Dict[str, Any]) -> bool:
        """
        Internal method to store data in Memori.
        
        Args:
            data_type: Type of data being stored
            data: Data dictionary to store
            
        Returns:
            True if stored successfully
        """
        try:
            # When Memori is available, this will use the actual storage
            # For now, it's a placeholder that maintains the interface
            if self.memori and self.memori.is_enabled():
                # Would use: self.memori.get_memory_tool().store(...)
                logger.debug(f"Stored {data_type} in memory (stub mode)")
            return True
        except Exception as e:
            logger.error(f"Failed to store in memory: {e}")
            return False
    
    def close(self):
        """Clean up and close the memory manager"""
        if self.memori:
            self.memori.disable()
        
        if self.audit_logger:
            self.audit_logger.log_event(
                "MEMORY_CLOSE",
                user_id=self.user_id,
                case_id=self.case_id,
                details="Memory manager closed"
            )
        
        logger.info(f"ContentiousProbateMemory closed for case: {self.case_id}")
