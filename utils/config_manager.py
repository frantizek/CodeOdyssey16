"""
Configuration Manager Utility

This module provides utilities for managing configuration settings across projects.
It supports loading configurations from environment variables and JSON files,
with validation and type conversion.

Features:
- Load configurations from environment variables
- Load configurations from JSON files
- Validate required configurations
- Type conversion (string to int, bool, etc.)
- Support for default values

Usage:
```python
from utils.config_manager import ConfigManager

# Load from environment variables
config = ConfigManager.from_env(
    required=["DB_HOST", "DB_PORT"],
    optional={"DB_USER": "default_user", "DB_PASS": ""}
)

# Load from JSON file
config = ConfigManager.from_json("config.json")

# Access configuration values
db_host = config.get("DB_HOST")
"""

import json
import os
from typing import Any


class ConfigManager:
    """
    A utility class for managing application configurations.
    Attributes:
        config (Dict[str, Any]): Dictionary holding the configuration values.
    """

    def __init__(self, config: dict[str, Any]):
        """
        Initialize the ConfigManager with a configuration dictionary.

        Args:
            config: Dictionary of configuration values.
        """
        self.config = config

    @classmethod
    def from_env(
        cls, required: list | None = None, optional: dict | None = None
    ) -> 'ConfigManager':
        """
        Create a ConfigManager instance from environment variables.

        Args:
            required: List of required environment variable names.
            optional: Dictionary of optional environment variables with default values.

        Returns:
            ConfigManager instance.

        Raises:
            ValueError: If any required environment variable is missing.
        """
        config = {}

        # Process required variables
        if required:
            for var in required:
                if var not in os.environ:
                    raise ValueError(f'Required environment variable {var} not set')
                config[var] = os.environ[var]

        # Process optional variables
        if optional:
            for var, default in optional.items():
                config[var] = os.environ.get(var, default)

        return cls(config)

    @classmethod
    def from_json(cls, file_path: str) -> 'ConfigManager':
        """
        Create a ConfigManager instance from a JSON file.

        Args:
            file_path: Path to the JSON configuration file.

        Returns:
            ConfigManager instance.

        Raises:
            FileNotFoundError: If the JSON file does not exist.
            json.JSONDecodeError: If the JSON file is not valid.
        """
        with open(file_path) as f:
            config = json.load(f)
        return cls(config)

    def get(self, key: str, default: Any = None) -> Any:
        """
        Get a configuration value by key.

        Args:
            key: The configuration key.
            default: Default value to return if the key is not found.

        Returns:
            The configuration value or the default value if the key is not found.
        """
        return self.config.get(key, default)

    def get_int(self, key: str, default: int = 0) -> int:
        """
        Get a configuration value as an integer.

        Args:
            key: The configuration key.
            default: Default integer value to return if the key is not found or cannot be converted.

        Returns:
            The configuration value as an integer.
        """
        value = self.config.get(key)
        if value is None:
            return default

        try:
            return int(value)
        except (ValueError, TypeError):
            return default

    def get_bool(self, key: str, default: Any = None) -> bool:
        """
        Get a configuration value as a boolean.

        Args:
            key: The configuration key.
            default: Default value to return if the key is not found or cannot be converted to bool.

        Returns:
            The configuration value as a boolean.
        """
        value = self.config.get(key, default)
        if isinstance(value, str):
            return value.lower() in ('true', '1', 'yes')
        return bool(value)
