#!/usr/bin/env python3
"""tests for temperature_converter.py"""

import os
import sys

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
    """convert 32F to 0C"""
    # Arrange
    class_under_test = TemperatureConverter()

    # Act
    result = class_under_test.convert_to_celsius(32)

    # Assert
    assert result == 0, "Expected 32°F to convert to 0°C"
