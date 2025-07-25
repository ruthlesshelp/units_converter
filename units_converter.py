#! /usr/bin/env python3
"""
Author: Stephen Ritchie
Date: 2025-07-23
Purpose: Main command-line interface for temperature conversions.
This script provides a command-line interface for converting temperatures.
"""

import os
import sys
import argparse

# Add src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '.', 'src'))

from conversion.temperature_converter import TemperatureConverter

def get_args():
    """Get command-line arguments."""
    parser = argparse.ArgumentParser(
        description='Convert temperatures between Fahrenheit and Celsius.'
    )

    parser.add_argument(
        'value',
        type=int,
        help='Fahrenheit value to convert to Celsius.'
    )
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Main function to handle command-line arguments and perform temperature conversions."""
    args = get_args()
    fahrenheit = args.value

    # Create an instance of TemperatureConverter and perform the conversion
    converter = TemperatureConverter()
    # Convert the Fahrenheit value to Celsius
    celsius = converter.convert_to_celsius(fahrenheit)

    print(f'Converted {fahrenheit}°F to {celsius}°C')


# Ensure the script can be run directly
if __name__ == "__main__":
    # Call the main function of the temperature converter
    main()