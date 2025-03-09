"""
Unit tests for the AdderClass.
"""

from my_python_project.adder_class import AdderClass


def test_adder_class() -> None:
    """
    Test the AdderClass and its add method.

    Returns:
        None
    """
    numbers = [1, 2, 3, 4, 5]
    adder = AdderClass(numbers)
    result = adder.add()
    assert result == 15

# Add more test cases as needed
