from pathlib import Path


def create_project(project_name: str) -> None:
    """Create a new project directory with standard structure."""
    base_path = Path(f"projects/{project_name}")
    paths = [
        base_path / "src" / project_name,
        base_path / "tests",
        base_path / "docs",
    ]

    for path in paths:
        path.mkdir(parents=True, exist_ok=True)

    # Create initial files
    (base_path / "README.md").touch()
    (base_path / "requirements.txt").touch()
    (base_path / "src" / project_name / "__init__.py").touch()
    (base_path / "tests" / "__init__.py").touch()

    print(f"Project {project_name} created at {base_path}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python setup_project.py <project_name>")
        sys.exit(1)
    create_project(sys.argv[1])
