"""
Configuration Management for Contentious Estates

Handles configuration loading from environment variables and config files.
"""

import os
from pathlib import Path
from typing import Optional
from dataclasses import dataclass


@dataclass
class Config:
    """Configuration settings for the contentious estates system"""
    
    # Database settings
    DATABASE_URL: str = "sqlite:///contentious_memory.db"
    
    # Memori settings
    MEMORI_AUTO_INGEST: bool = True
    MEMORI_CONSCIOUS_INGEST: bool = True
    
    # Audit settings
    AUDIT_ENABLED: bool = True
    AUDIT_LOG_FILE: str = "audit.log"
    
    # Security settings
    ENABLE_ENCRYPTION: bool = False
    SECRET_KEY: Optional[str] = None
    
    # Logging settings
    LOG_LEVEL: str = "INFO"
    
    @classmethod
    def from_env(cls) -> 'Config':
        """Load configuration from environment variables"""
        return cls(
            DATABASE_URL=os.getenv("DATABASE_URL", cls.DATABASE_URL),
            MEMORI_AUTO_INGEST=os.getenv("MEMORI_AUTO_INGEST", "true").lower() == "true",
            MEMORI_CONSCIOUS_INGEST=os.getenv("MEMORI_CONSCIOUS_INGEST", "true").lower() == "true",
            AUDIT_ENABLED=os.getenv("AUDIT_ENABLED", "true").lower() == "true",
            AUDIT_LOG_FILE=os.getenv("AUDIT_LOG_FILE", cls.AUDIT_LOG_FILE),
            ENABLE_ENCRYPTION=os.getenv("ENABLE_ENCRYPTION", "false").lower() == "true",
            SECRET_KEY=os.getenv("SECRET_KEY"),
            LOG_LEVEL=os.getenv("LOG_LEVEL", cls.LOG_LEVEL)
        )


# Global config instance
config = Config.from_env()
