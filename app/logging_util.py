import logging
from typing import Optional, Dict, Any

# Initialize logger for the application
logger = logging.getLogger("uicheckapp")


def log_info(message: str, extra: Optional[Dict[str, Any]] = None) -> None:
    """
    Log information messages.
    """
    logger.info(message, extra=extra or {})


def log_debug(message: str, extra: Optional[Dict[str, Any]] = None) -> None:
    """
    Log debug messages.
    """
    logger.debug(message, extra=extra or {})


def log_error(message: str, extra: Optional[Dict[str, Any]] = None) -> None:
    """
    Log error messages with additional exception information if present.
    """
    # Log error messages; exc_info is not used here
    logger.error(message, extra=extra or {})


def log_exception(exception: Exception, message: str = "An exception occurred") -> None:
    """
    Log exceptions and traceback.
    """
    # Use logger.exception for logging exceptions
    logger.exception(f"{message}: {exception}")
