import logging
from typing import Optional, Dict, Any

# Initialize loggers for the application
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
    logger.error(message, extra=extra or {}, exc_info=True)


def log_exception(exception: Exception,
                  message: str = "An exception occurred") -> None:
    """
    Log exceptions and traceback.
    """
    logger.exception(f"{message}: {exception}")
