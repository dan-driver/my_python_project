"""
Unit tests for the main module.
"""

import subprocess
import sys
from typing import Any
from my_python_project.main import main


def test_main(capfd: Any) -> None:
    """
    Test the main function output.

    Args:
        capfd (Any): The capture fixture provided by pytest to capture
          stdout and stderr.

    Returns:
        None
    """
    main()
    out, _ = capfd.readouterr()
    assert out == "Hello, World!\n"


def test_main_as_script() -> None:
    """
    Test running the main module as a script.

    Returns:
        None
    """
    result = subprocess.run(
        [sys.executable, "-m", "my_python_project.main"],
        capture_output=True,
        text=True,
        check=True
    )
    assert result.stdout == "Hello, World!\n"
    assert not result.returncode

# Add more test cases as needed
