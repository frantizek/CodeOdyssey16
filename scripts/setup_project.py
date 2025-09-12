#!/usr/bin/env python3
"""
Project setup script to create a standardized Python project structure.

This script creates a new project directory with a predefined structure,
including source, test, and documentation directories, along with initial
files like README.md and requirements.txt. It ensures compatibility with
common Python linters (e.g., flake8, pylint, mypy) and follows PEP 8 style
guidelines.

Improvements:
- Checks if the project directory already exists to prevent accidental overwrites.

Usage:
    python setup_project.py <project_name>

Example:
    python setup_project.py my_new_project
"""

import logging
import sys
from pathlib import Path

# Configure logging for better output handling
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)
logger = logging.getLogger(__name__)


def validate_project_name(project_name: str) -> bool:
    """
    Validate the project name to ensure it follows Python package naming conventions.

    Args:
        project_name (str): The name of the project to validate.

    Returns:
        bool: True if the project name is valid, False otherwise.

    Notes:
        - Project name should contain only letters, numbers, hyphens, or underscores.
        - Must not start with a number or special character.
        - Must not be empty.
    """
    if not project_name:
        logger.error('Project name cannot be empty')
        return False
    if not project_name.replace('-', '_').isidentifier():
        logger.error(
            "Invalid project name: '%s'. Use letters, numbers, hyphens, or underscores, "
            "and ensure it doesn't start with a number.",
            project_name,
        )
        return False
    return True


def create_project(project_name: str, base_dir: str = 'projects') -> Path | None:
    """
    Create a new project directory with a standard Python project structure.

    Args:
        project_name (str): The name of the project to create.
        base_dir (str, optional): The base directory to create the project in.
            Defaults to "projects".

    Returns:
        Optional[Path]: The Path object for the project directory if created,
            None if creation fails or if the directory already exists.

    Creates:
        - projects/<project_name>/src/<project_name>/
        - projects/<project_name>/tests/
        - projects/<project_name>/docs/
        - README.md, requirements.txt, and __init__.py files

    Improvement:
        - If the project directory exists, logs a warning and skips creation to avoid overwrites.
    """
    # Validate project name
    if not validate_project_name(project_name):
        return None

    # Define base path for the project
    base_path = Path(base_dir) / project_name

    # Check if project already exists to prevent overwrite
    if base_path.exists():
        logger.warning(
            "Project '%s' already exists at %s. Skipping creation to avoid overwriting existing files. "
            'If you want to recreate, delete the directory first.',
            project_name,
            base_path,
        )
        return None

    # Define directory structure
    paths = [
        base_path / 'src' / project_name,
        base_path / 'tests',
        base_path / 'docs',
    ]

    try:
        # Create directories
        for path in paths:
            path.mkdir(parents=True, exist_ok=True)
            logger.debug('Created directory: %s', path)

        # Create initial files
        initial_files = [
            (
                base_path / 'README.md',
                f'# {project_name}\n\nProject description goes here.',
            ),
            (base_path / 'requirements.txt', ''),
            (
                base_path / 'src' / project_name / '__init__.py',
                f'"""{project_name} package."""',
            ),
            (
                base_path / 'tests' / '__init__.py',
                f'"""Test suite for {project_name}."""',
            ),
        ]

        for file_path, content in initial_files:
            file_path.write_text(content, encoding='utf-8')
            logger.debug('Created file: %s', file_path)

        logger.info("Project '%s' created successfully at %s", project_name, base_path)
        print('\n--- Next Steps ---')
        print(f'1. Navigate to your project directory: cd {base_path}')
        print('2. Add project-specific dependencies to requirements.txt')
        print('3. Install them: uv pip install -r requirements.txt')
        print(f'4. Start developing in: {base_path / "src"}')
        print('------------------')
        return base_path

    except PermissionError as e:
        logger.error('Permission denied while creating project: %s', e)
        return None
    except OSError as e:
        logger.error('Failed to create project structure: %s', e)
        return None


def main() -> None:
    """
    Main entry point for the script.

    Expects a single command-line argument for the project name.
    Exits with status code 1 if the usage is incorrect or project creation fails.
    """
    if len(sys.argv) != 2:
        logger.error('Usage: python %s <project_name>', sys.argv[0])
        sys.exit(1)

    project_name = sys.argv[1]
    result = create_project(project_name)
    if result is None:
        sys.exit(1)


if __name__ == '__main__':
    main()
