"""
Logging Setup Utility

This module provides a standardized way to set up logging across all projects in the CodeOdyssey16 monorepo.
It supports both console and file logging, with configurable log levels and formats.

Features:
- Customizable log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- Support for both console and file logging
- Standardized log format: `%(asctime)s - %(name)s - %(levelname)s - %(message)s`
- Thread-safe logging setup

Usage:
```python
from utils.logging_setup import setup_logging

# Basic setup for console logging
logger = setup_logging(__name__)

# Advanced setup with file logging
logger = setup_logging(__name__, level=logging.DEBUG, log_file="app.log")
"""

import logging


def setup_logging(
    name: str, level: int = logging.INFO, log_file: str | None = None
) -> logging.Logger:
    """
    Set up logging for a module.
    Args:
        name: Name of the logger (typically __name__).
        level: Logging level (default: logging.INFO).
        log_file: Optional path to a log file. If provided, logs will also be written to this file.

    Returns:
        Configured logger instance.

    Example:
        >>> logger = setup_logging(__name__, level=logging.DEBUG, log_file="app.log")
        >>> logger.info("This is an info message")
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if this function is called multiple times for the same logger
    if logger.hasHandlers():
        logger.handlers.clear()

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File handler (if log_file is provided)
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
