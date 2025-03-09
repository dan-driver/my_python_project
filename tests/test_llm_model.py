"""
Unit tests for the llm_model module.
"""

import subprocess
import sys
from my_python_project.llm_model import ask_gpt2


def test_ask_gpt2() -> None:
    """
    Test the ask_gpt2 function to check if the response includes the word eggs.

    Returns:
        None
    """
    question = "How many eggs are there in a dozen eggs?"
    answer = ask_gpt2(question)
    assert "eggs" in answer


def test_main_as_script() -> None:
    """
    Test running the llm_model module as a script
    and check if the response includes the word eggs.

    Returns:
        None
    """
    result = subprocess.run(
        [sys.executable, "-m", "my_python_project.llm_model"],
        capture_output=True,
        text=True,
        check=True
    )
    assert "eggs" in result.stdout
    assert not result.returncode

# Add more test cases as needed
