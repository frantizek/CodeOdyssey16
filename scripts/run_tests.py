"""
Test Runner Script

This script runs tests for all projects in the CodeOdyssey16 monorepo.
It provides a convenient way to execute all tests at once or for specific projects.

Features:
- Runs tests for all projects by default
- Can target specific projects
- Provides clear output for test results

Usage:
```bash
# Run tests for all projects
python scripts/run_tests.py

# Run tests for a specific project
python scripts/run_tests.py project_name
"""

import sys
from pathlib import Path


def run_tests(project_name: str | None = None) -> None:
    """
    Run tests for all projects or a specific project.

    Args:
        project_name: Name of the project to test. If None, tests all projects.
    """
    projects_dir = Path('projects')
    projects_to_test = []

    if project_name:
        # Basic input validation
        if not isinstance(project_name, str) or any(c in project_name for c in '/\\'):
            print('Invalid project name')
            sys.exit(1)

        project_path = projects_dir / project_name
        if project_path.exists():
            projects_to_test.append(project_path)
        else:
            print(f'Project {project_name} not found.')
            sys.exit(1)
    else:
        projects_to_test = [p for p in projects_dir.iterdir() if p.is_dir()]

    for project in projects_to_test:
        print(f'\nRunning tests for {project.name}...')
        test_dir = project / 'tests'

        if test_dir.exists():
            try:
                # Use pytest's programmatic API instead of subprocess
                import pytest

                exit_code = pytest.main([str(test_dir)])
                print(
                    f'Tests completed for {project.name} with return code {exit_code}'
                )
            except ImportError:
                print('Error: pytest is not installed')
                sys.exit(1)
            except Exception as e:
                print(f'Error running tests for {project.name}: {e}')
        else:
            print(f'No tests directory found in {project.name}')


if __name__ == '__main__':
    project_name = sys.argv[1] if len(sys.argv) > 1 else None
    run_tests(project_name)
