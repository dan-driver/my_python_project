from typing import List

from setuptools import setup, find_packages

def parse_requirements(filename: str) -> List[str]:
    """Parse a requirements file into a list of dependencies."""
    with open(filename, 'r', encoding='utf-8') as file:
        return [
            line.strip() for line in file
            if line.strip() and not line.startswith('#')
        ]

setup(
    name="my-python-project",
    version="0.1.0",
    description="A sample Python project",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=parse_requirements('requirements.txt'),
)
