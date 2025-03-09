"""
Unit tests for the main module.
"""

from typing import Any
from my_python_project.main import main

def test_main(capfd: Any) -> None:
    """Test the main function output."""
    main()
    out, _ = capfd.readouterr()
    assert out == "Hello, World!\n"

# Add more test cases as needed
