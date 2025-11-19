"""
Query Templates and Retrieval Systems

This module provides templated queries and retrieval methods for
searching and accessing case context and memory.
"""

from typing import Dict, Any, List, Optional, Callable
from datetime import datetime, timedelta
import logging


logger = logging.getLogger(__name__)


class QueryTemplate:
    """Base class for query templates"""
    
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
    
    def execute(self, memory_manager, **kwargs) -> Any:
        """Execute the query template"""
        raise NotImplementedError


class DateRangeQuery(QueryTemplate):
    """Query template for date range searches"""
    
    def __init__(self):
        super().__init__(
            "date_range",
            "Search for events/dates within a specified range"
        )
    
    def execute(
        self,
        memory_manager,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        days_ahead: Optional[int] = None
    ) -> List[Dict[str, Any]]:
        """
        Execute date range query.
        
        Args:
            memory_manager: ContentiousProbateMemory instance
            start_date: ISO format start date
            end_date: ISO format end date
            days_ahead: Alternative to end_date - number of days from now
            
        Returns:
            List of matching dates
        """
        if days_ahead:
            return memory_manager.get_upcoming_dates(days_ahead)
        
        # More complex date filtering would go here
        context = memory_manager.get_case_context()
        return context.get('key_dates', {})


class WitnessQuery(QueryTemplate):
    """Query template for witness searches"""
    
    def __init__(self):
        super().__init__(
            "witness_search",
            "Search for witnesses by role or name"
        )
    
    def execute(
        self,
        memory_manager,
        role: Optional[str] = None,
        name_pattern: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Execute witness query.
        
        Args:
            memory_manager: ContentiousProbateMemory instance
            role: Filter by role
            name_pattern: Filter by name pattern
            
        Returns:
            List of matching witnesses
        """
        context = memory_manager.get_case_context()
        witnesses = context.get('witnesses', [])
        
        results = []
        for witness in witnesses:
            if role and witness.get('role', '').lower() != role.lower():
                continue
            if name_pattern and name_pattern.lower() not in witness.get('name', '').lower():
                continue
            results.append(witness)
        
        return results


class EvidenceQuery(QueryTemplate):
    """Query template for evidence searches"""
    
    def __init__(self):
        super().__init__(
            "evidence_search",
            "Search evidence by type, description, or metadata"
        )
    
    def execute(
        self,
        memory_manager,
        evidence_type: Optional[str] = None,
        query: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Execute evidence query.
        
        Args:
            memory_manager: ContentiousProbateMemory instance
            evidence_type: Filter by evidence type
            query: Search query string
            
        Returns:
            List of matching evidence items
        """
        if query:
            results = memory_manager.search_evidence(query)
            if evidence_type:
                results = [e for e in results if e.get('evidence_type') == evidence_type]
            return results
        
        context = memory_manager.get_case_context()
        evidence = context.get('evidence', [])
        
        if evidence_type:
            evidence = [e for e in evidence if e.get('evidence_type') == evidence_type]
        
        return evidence


class CaseContextQuery(QueryTemplate):
    """Query template for full case context retrieval"""
    
    def __init__(self):
        super().__init__(
            "case_context",
            "Retrieve complete case context"
        )
    
    def execute(
        self,
        memory_manager,
        include_sections: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        Execute case context query.
        
        Args:
            memory_manager: ContentiousProbateMemory instance
            include_sections: List of sections to include (None = all)
            
        Returns:
            Case context dictionary
        """
        context = memory_manager.get_case_context()
        
        if include_sections:
            filtered_context = {}
            for section in include_sections:
                if section in context:
                    filtered_context[section] = context[section]
            return filtered_context
        
        return context


class RetrievalSystem:
    """
    Main retrieval system for querying case memory.
    
    Provides a unified interface for executing different query templates
    and retrieving case-specific information.
    """
    
    def __init__(self):
        """Initialize the retrieval system with available query templates"""
        self.templates: Dict[str, QueryTemplate] = {
            'date_range': DateRangeQuery(),
            'witness_search': WitnessQuery(),
            'evidence_search': EvidenceQuery(),
            'case_context': CaseContextQuery()
        }
        
        logger.info("RetrievalSystem initialized with templates: " +
                   ", ".join(self.templates.keys()))
    
    def execute_query(
        self,
        template_name: str,
        memory_manager,
        **kwargs
    ) -> Any:
        """
        Execute a query template.
        
        Args:
            template_name: Name of the query template
            memory_manager: ContentiousProbateMemory instance
            **kwargs: Template-specific parameters
            
        Returns:
            Query results
        """
        if template_name not in self.templates:
            raise ValueError(f"Unknown query template: {template_name}")
        
        template = self.templates[template_name]
        logger.info(f"Executing query template: {template_name}")
        
        try:
            results = template.execute(memory_manager, **kwargs)
            logger.info(f"Query '{template_name}' completed successfully")
            return results
        except Exception as e:
            logger.error(f"Query '{template_name}' failed: {e}")
            raise
    
    def register_template(self, template: QueryTemplate):
        """
        Register a custom query template.
        
        Args:
            template: QueryTemplate instance to register
        """
        self.templates[template.name] = template
        logger.info(f"Registered custom template: {template.name}")
    
    def list_templates(self) -> List[Dict[str, str]]:
        """
        List all available query templates.
        
        Returns:
            List of template descriptions
        """
        return [
            {
                "name": name,
                "description": template.description
            }
            for name, template in self.templates.items()
        ]


def create_retrieval_system() -> RetrievalSystem:
    """
    Factory function to create a retrieval system.
    
    Returns:
        Initialized RetrievalSystem instance
    """
    return RetrievalSystem()
