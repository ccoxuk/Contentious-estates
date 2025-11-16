"""
Data Models for Contentious Probate Cases

This module defines the data structures for case metadata, including
key dates, witnesses, and evidence.
"""

from typing import Optional, Dict, Any, List
from datetime import datetime
from dataclasses import dataclass, field


@dataclass
class KeyDate:
    """Represents a key date in a probate case"""
    date_type: str
    date_value: str  # ISO format date string
    description: Optional[str] = None
    created_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation"""
        return {
            "date_type": self.date_type,
            "date_value": self.date_value,
            "description": self.description,
            "created_at": self.created_at
        }


@dataclass
class Witness:
    """Represents a witness or party in a probate case"""
    name: str
    role: str  # e.g., 'executor', 'beneficiary', 'witness'
    contact: Optional[str] = None
    notes: Optional[str] = None
    created_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation"""
        return {
            "name": self.name,
            "role": self.role,
            "contact": self.contact,
            "notes": self.notes,
            "created_at": self.created_at
        }


@dataclass
class Evidence:
    """Represents evidence or documentation in a probate case"""
    file_name: str
    description: str
    evidence_type: Optional[str] = None  # e.g., 'will', 'disclosure', 'affidavit'
    metadata: Dict[str, Any] = field(default_factory=dict)
    created_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation"""
        return {
            "file_name": self.file_name,
            "description": self.description,
            "evidence_type": self.evidence_type,
            "metadata": self.metadata,
            "created_at": self.created_at
        }


@dataclass
class CaseMetadata:
    """Complete metadata for a contentious probate case"""
    case_id: str
    user_id: str
    key_dates: Dict[str, KeyDate] = field(default_factory=dict)
    witnesses: List[Witness] = field(default_factory=list)
    evidence: List[Evidence] = field(default_factory=list)
    additional_metadata: Dict[str, Any] = field(default_factory=dict)
    created_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    updated_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation"""
        return {
            "case_id": self.case_id,
            "user_id": self.user_id,
            "key_dates": {k: v.to_dict() for k, v in self.key_dates.items()},
            "witnesses": [w.to_dict() for w in self.witnesses],
            "evidence": [e.to_dict() for e in self.evidence],
            "additional_metadata": self.additional_metadata,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
