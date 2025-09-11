#!/usr/bin/env python3
"""
A simple command-line dice rolling simulator.

This module provides the core functionality for simulating the roll of a die
with a customizable number of sides.
"""

import secrets


class Die:
    def __init__(self, sides: int = 6) -> None:
        if sides < 1:
            raise ValueError('Number of sides must be at least 1.')
        else:
            self.sides = sides

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
        print(f'🎲 You rolled a: {result}')
    except ValueError as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    main()
