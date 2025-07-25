#!/usr/bin/env python3
"""tests for temperature_converter.py"""

import os
import sys
import pytest

file_under_test = os.path.join(os.path.dirname(__file__), '..', 'src', 'conversion', 'temperature_converter.py')

def test_exists():
    """Ensure the script is run from the correct directory"""

    assert os.path.isfile(file_under_test), f'{file_under_test} does not exist. Please run this test from the project root directory.'


# Add src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

# Import the TemperatureConverter class from the conversion module
from conversion.temperature_converter import TemperatureConverter


# --------------------------------------------------
def test_convert_with_32f_expect_0c():
    """
    freezing point of water
    convert 32F to 0C
    """
    # Arrange
    class_under_test = TemperatureConverter()

    # Act
    result = class_under_test.convert_to_celsius(32)

    # Assert
    assert result == 0, "Expected 32°F to convert to 0°C"

def test_convert_with_212f_expect_100c():
    """
    boiling point of water
    convert 212F to 100C
    """
    # Arrange
    class_under_test = TemperatureConverter()

    # Act
    result = class_under_test.convert_to_celsius(212)

    # Assert
    assert result == 100, "Expected 212°F to convert to 100°C"

def test_convert_with_98_6f_expect_37c():
    """
    normal human body temperature
    convert 98.6F to 37C
    """
    # Arrange
    class_under_test = TemperatureConverter()

    # Act
    result = class_under_test.convert_to_celsius(98.6)

    # Assert
    assert result == 37, "Expected 98.6°F to convert to 37°C"

def test_convert_with_minus_40f_expect_minus_40c():
    """
    special case where Fahrenheit and Celsius scales intersect
    """
    # Arrange
    class_under_test = TemperatureConverter()

    # Act
    result = class_under_test.convert_to_celsius(-40)

    # Assert
    assert result == -40, "Expected -40°F to convert to -40°C"

def test_convert_with_0f_expect_minus_17_78c():
    """
    convert 0F to approximately -17.78C
    """
    # Arrange
    class_under_test = TemperatureConverter()

    # Act
    result = class_under_test.convert_to_celsius(0)

    # Assert
    assert result == -17.78, "Expected 0°F to convert to approximately -17.78°C"

def test_convert_with_minus_500f_expect_value_error():
    """
    test for invalid input
    convert -500F should raise ValueError
    """
    # Arrange
    class_under_test = TemperatureConverter()

    # Act
    with pytest.raises(ValueError) as exc_info:
        class_under_test.convert_to_celsius(-500)

    # Assert
    assert str(exc_info.value) == "Temperature below absolute zero is not valid", "Expected ValueError for temperatures below absolute zero"
