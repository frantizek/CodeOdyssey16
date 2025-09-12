#!/usr/bin/env python3
"""
A simple command-line dice rolling simulator.

This module provides the core functionality for simulating the roll of a die
with a customizable number of sides.
"""

import secrets
from dataclasses import dataclass
from typing import Self


@dataclass
class Die:
    """A dataclass representing a die with a customizable number of sides."""

    sides: int = 6

    def __post_init__(self) -> None:
        """
        Validates the Die's attributes after initialization.
        """
        if self.sides < 1:
            raise ValueError('Number of sides must be at least 1.')

    def roll(self) -> int:
        """Simulates rolling a single die with a given number of sides.

        Uses the cryptographically secure 'secrets' module for number generation.

        Args:
            sides: The number of sides on the die. Must be a positive integer.
                   Defaults to 6.

        Returns:
            An integer representing the result of the roll, between 1 and 'sides'.

        Raises:
            ValueError: If the number of sides is less than 1.
        """
        return secrets.randbelow(self.sides) + 1

    @classmethod
    def from_string(cls: type[Self], dice_string: str) -> Self:
        """
        Creates a Die instance from a string format (e.g., 'D6', 'd20').
        """
        if not dice_string:
            raise ValueError('Input string cannot be empty.')
        dice_string = dice_string.strip().upper()
        if not dice_string.startswith('D') or not dice_string[1:].isdigit():
            raise ValueError("Invalid dice format. Must be like 'D6' or 'D20'.")
        number_of_sides = int(dice_string[1:])
        return cls(sides=number_of_sides)


def main() -> None:
    """
    Main entry point for the dice simulator application.

    This function simulates rolling a standard 6-sided die, provides
    visual feedback, and prints the result to the console.
    """
    print('Rolling the die...')
    # Simple "animation" for user experience
    try:
        d = Die()
        result = d.roll()
        print(f' 🎲  You rolled a: {result}')
    except ValueError as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    main()
