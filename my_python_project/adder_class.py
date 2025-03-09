"""
Module containing the AdderClass.
"""

from typing import List


class AdderClass:
    """
    A class that adds numbers from a list.
    """

    def __init__(self, numbers: List[int]) -> None:
        """
        Initialize the AdderClass with a list of numbers.

        Args:
            numbers (List[int]): A list of integers to be added.
        """
        self.numbers = numbers

    def add(self) -> int:
        """
        Add the numbers in the list.

        Returns:
            int: The sum of the numbers in the list.
        """
        return sum(self.numbers)
