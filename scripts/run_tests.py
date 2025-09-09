import subprocess
from pathlib import Path

def run_tests():
    """Run tests for all projects."""
    projects_dir = Path("projects")
    for project in projects_dir.iterdir():
        if project.is_dir():
            print(f"Running tests for {project.name}...")
            subprocess.run(["pytest", str(project / "tests")], check=False)

if __name__ == "__main__":
    run_tests()
