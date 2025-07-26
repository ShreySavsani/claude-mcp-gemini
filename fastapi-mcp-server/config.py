import os
from typing import Optional
from dotenv import load_dotenv

# Load environment variables from .env files in order of precedence
# .env.local (highest priority for local development)
# .env.prod (for production)
# .env (fallback)
load_dotenv('.env.local')
load_dotenv('.env.prod')
load_dotenv('.env')

class ConfigurationError(Exception):
    """Raised when there is a configuration error."""
    pass

class Config:
    """Application configuration management."""
    
    def __init__(self):
        self._google_api_key: Optional[str] = None
        self._app_host: str = "0.0.0.0"
        self._app_port: int = 8000
        self._app_debug: bool = False
        self._log_level: str = "INFO"
        
        self._load_config()
        self._validate_required_config()
    
    def _load_config(self) -> None:
        """Load configuration from environment variables."""
        self._google_api_key = os.getenv("GOOGLE_API_KEY")
        self._app_host = os.getenv("APP_HOST", "0.0.0.0")
        self._app_port = int(os.getenv("APP_PORT", "8000"))
        self._app_debug = os.getenv("APP_DEBUG", "false").lower() == "true"
        self._log_level = os.getenv("LOG_LEVEL", "INFO").upper()
    
    def _validate_required_config(self) -> None:
        """Validate that all required configuration is present."""
        if not self._google_api_key:
            raise ConfigurationError(
                "GOOGLE_API_KEY environment variable is required. "
                "Please set it in your .env file or environment variables."
            )
    
    @property
    def google_api_key(self) -> str:
        """Get the Google API key."""
        if not self._google_api_key:
            raise ConfigurationError("Google API key is not configured")
        return self._google_api_key
    
    @property
    def app_host(self) -> str:
        """Get the application host."""
        return self._app_host
    
    @property
    def app_port(self) -> int:
        """Get the application port."""
        return self._app_port
    
    @property
    def app_debug(self) -> bool:
        """Get the application debug mode."""
        return self._app_debug
    
    @property
    def log_level(self) -> str:
        """Get the logging level."""
        return self._log_level

# Global configuration instance
config = Config()