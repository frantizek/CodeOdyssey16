import logging
from typing import Optional

def setup_logging(name: str, level: int = logging.INFO, log_file: Optional[str] = None) -> logging.Logger:
    """Set up logging for a module.

    Args:
        name: Name of the logger.
        level: Logging level.
        log_file: Optional path to a log file.

    Returns:
        Configured logger.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File handler
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
