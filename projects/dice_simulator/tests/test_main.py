"""
Tests for the dice_simulator main module.
"""

# Standard library imports
from unittest.mock import Mock, patch

import pytest
from dice_simulator.main import Die

# Third-party imports
# Local application imports


def test_roll_dice_with_default_sides() -> None:
    """
    Tests that roll() returns a value within the default range [1, 6].
    """
    for _ in range(100):  # Run multiple times to increase confidence
        d = Die()
        result = d.roll()
        assert 1 <= result <= 6


def test_roll_dice_with_custom_sides() -> None:
    """
    Tests that roll() with a custom side count returns a valid number.
    """
    sides = 20
    for _ in range(100):
        d = Die(sides)
        result = d.roll()
        assert 1 <= result <= sides


def test_roll_dice_raises_error_for_invalid_sides() -> None:
    """
    Tests that Die constructor raises a ValueError for sides less than 1.
    """
    with pytest.raises(ValueError, match='Number of sides must be at least 1.'):
        Die(0)
    with pytest.raises(ValueError, match='Number of sides must be at least 1.'):
        Die(-5)


@patch('secrets.randbelow')
def test_roll_dice_is_deterministic_with_mock(mock_randbelow: Mock) -> None:
    """
    Tests that the roll() method correctly uses secrets.randbelow.
    This test uses mocking to control the random number generator, making the
    test deterministic and repeatable.
    """
    # Configure the mock to return a specific value (e.g., 4)
    mock_randbelow.return_value = 4

    # Test with default 6-sided die
    d = Die()
    result = d.roll()

    # Assert that secrets.randbelow was called correctly
    mock_randbelow.assert_called_once_with(6)
    # Assert that our function correctly added 1 to the result
    assert result == 5


@patch('secrets.randbelow')
def test_roll_dice_with_custom_sides_is_deterministic(mock_randbelow: Mock) -> None:
    """
    Tests that roll() with custom sides correctly uses secrets.randbelow.
    """
    # Configure the mock to return a specific value
    mock_randbelow.return_value = 9

    # Test with 20-sided die
    sides = 20
    d = Die(sides)
    result = d.roll()

    # Assert that secrets.randbelow was called with the correct number of sides
    mock_randbelow.assert_called_once_with(sides)
    # Assert that our function correctly added 1 to the result
    assert result == 10
