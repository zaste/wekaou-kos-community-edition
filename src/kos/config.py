"""Configuration management for KOS."""

from dataclasses import dataclass, field
from typing import Optional, Dict, Any
import os


@dataclass
class StorageConfig:
    """Storage backend configuration."""
    type: str = "memory"
    host: Optional[str] = None
    port: Optional[int] = None
    database: Optional[str] = None
    user: Optional[str] = None
    password: Optional[str] = None
    options: Dict[str, Any] = field(default_factory=dict)


@dataclass
class APIConfig:
    """API server configuration."""
    enabled: bool = False
    host: str = "0.0.0.0"
    port: int = 8000
    

@dataclass
class ValidationConfig:
    """Validation configuration."""
    oos_enabled: bool = True
    vqf_enabled: bool = True
    strict_mode: bool = False


@dataclass
class Config:
    """Main KOS configuration.
    
    Example:
        >>> config = Config(
        ...     storage="postgres",
        ...     db_host="localhost",
        ...     db_port=5432
        ... )
    """
    
    # Storage configuration
    storage: str = "memory"
    db_host: Optional[str] = None
    db_port: Optional[int] = None
    db_name: Optional[str] = None
    db_user: Optional[str] = None
    db_password: Optional[str] = None
    
    # API configuration
    api_enabled: bool = False
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    
    # Validation configuration
    validation_enabled: bool = True
    strict_mode: bool = False
    
    # Logging
    log_level: str = "INFO"
    
    @classmethod
    def from_env(cls) -> "Config":
        """Create configuration from environment variables.
        
        Returns:
            Config instance with values from environment
        """
        return cls(
            storage=os.getenv("KOS_STORAGE_TYPE", "memory"),
            db_host=os.getenv("KOS_DB_HOST"),
            db_port=int(os.getenv("KOS_DB_PORT", "0")) or None,
            db_name=os.getenv("KOS_DB_NAME"),
            db_user=os.getenv("KOS_DB_USER"),
            db_password=os.getenv("KOS_DB_PASSWORD"),
            api_enabled=os.getenv("KOS_API_ENABLED", "false").lower() == "true",
            api_port=int(os.getenv("KOS_API_PORT", "8000")),
            log_level=os.getenv("KOS_LOG_LEVEL", "INFO"),
        )
