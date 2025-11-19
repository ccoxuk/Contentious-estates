"""
Memori Integration Module

This module provides the core integration with Memori for managing
contentious probate case memory, including initialization, configuration,
and memory tool creation.
"""

import logging
from typing import Optional, Dict, Any
from pathlib import Path

# Note: Memori will be added as a submodule
# For now, we create a compatible interface
try:
    from memori import Memori, create_memory_tool
    MEMORI_AVAILABLE = True
except ImportError:
    MEMORI_AVAILABLE = False
    logging.warning("Memori not available - running in stub mode")


logger = logging.getLogger(__name__)


class MemoriConfig:
    """Configuration for Memori integration"""
    
    def __init__(
        self,
        database_url: str = "sqlite:///contentious_memory.db",
        auto_ingest: bool = True,
        conscious_ingest: bool = True,
        memory_filters: Optional[Dict[str, Any]] = None
    ):
        self.database_url = database_url
        self.auto_ingest = auto_ingest
        self.conscious_ingest = conscious_ingest
        self.memory_filters = memory_filters or {}


class MemoriIntegration:
    """
    Core Memori integration for contentious probate cases.
    
    This class initializes and manages Memori instances for persistent
    memory across user sessions.
    """
    
    def __init__(
        self,
        user_id: str,
        config: Optional[MemoriConfig] = None
    ):
        """
        Initialize Memori integration.
        
        Args:
            user_id: Unique identifier for the user/case session
            config: Configuration options for Memori
        """
        self.user_id = user_id
        self.config = config or MemoriConfig()
        self.memori_instance = None
        self.memory_tool = None
        self._enabled = False
        
        logger.info(f"Initializing MemoriIntegration for user: {user_id}")
        
    def initialize(self) -> bool:
        """
        Initialize the Memori instance with configured settings.
        
        Returns:
            True if initialization successful, False otherwise
        """
        try:
            if not MEMORI_AVAILABLE:
                logger.warning("Memori not available - creating stub instance")
                self._create_stub_instance()
                return True
                
            # Initialize a Memori instance for a probate application space
            self.memori_instance = Memori(
                database_connect=self.config.database_url,
                auto_ingest=self.config.auto_ingest,
                conscious_ingest=self.config.conscious_ingest,
                user_id=self.user_id,
                memory_filters=self.config.memory_filters
            )
            
            logger.info(f"Memori instance created for user: {self.user_id}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to initialize Memori: {e}")
            return False
    
    def enable(self) -> bool:
        """
        Enable the Memori instance and create memory tools.
        
        Returns:
            True if enabled successfully, False otherwise
        """
        try:
            if not self.memori_instance:
                if not self.initialize():
                    return False
            
            if MEMORI_AVAILABLE:
                self.memori_instance.enable()
                self.memory_tool = create_memory_tool(self.memori_instance)
            
            self._enabled = True
            logger.info(f"Memori enabled for user: {self.user_id}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to enable Memori: {e}")
            return False
    
    def disable(self) -> bool:
        """
        Disable the Memori instance.
        
        Returns:
            True if disabled successfully, False otherwise
        """
        try:
            if MEMORI_AVAILABLE and self.memori_instance:
                self.memori_instance.disable()
            
            self._enabled = False
            logger.info(f"Memori disabled for user: {self.user_id}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to disable Memori: {e}")
            return False
    
    def is_enabled(self) -> bool:
        """Check if Memori is currently enabled"""
        return self._enabled
    
    def get_memory_tool(self):
        """Get the memory tool for case recall and navigation"""
        if not self._enabled:
            raise RuntimeError("Memori not enabled. Call enable() first.")
        return self.memory_tool
    
    def _create_stub_instance(self):
        """Create a stub instance when Memori is not available"""
        self.memori_instance = {
            "database_url": self.config.database_url,
            "user_id": self.user_id,
            "stub": True
        }
        logger.info("Created stub Memori instance")


def create_memori_integration(
    user_id: str,
    database_url: Optional[str] = None,
    **kwargs
) -> MemoriIntegration:
    """
    Factory function to create and initialize a MemoriIntegration instance.
    
    Args:
        user_id: Unique identifier for the user/case session
        database_url: Optional database URL (defaults to sqlite)
        **kwargs: Additional configuration options
    
    Returns:
        Initialized MemoriIntegration instance
    """
    config = MemoriConfig(
        database_url=database_url or "sqlite:///contentious_memory.db",
        **kwargs
    )
    
    integration = MemoriIntegration(user_id, config)
    integration.initialize()
    integration.enable()
    
    return integration
