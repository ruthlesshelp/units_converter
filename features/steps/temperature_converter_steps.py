import os
import sys
from behave import given, when, then

# Add src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from conversion.temperature_converter import TemperatureConverter

@given('I have a temperature converter')
def step_given_temperature_converter(context):
    """Initialize the temperature converter."""
    context.converter = TemperatureConverter()

@when('I convert {fahrenheit:d} degrees Fahrenheit to Celsius')
@when('I convert {fahrenheit:f} degrees Fahrenheit to Celsius')
def step_when_convert_fahrenheit_to_celsius(context, fahrenheit):
    """Convert the given Fahrenheit temperature to Celsius."""
    context.fahrenheit = fahrenheit
    context.celsius = context.converter.convert_to_celsius(fahrenheit)

@then('the result should be {celsius:d} degrees Celsius')
def step_then_result(context, celsius):
    assert context.celsius == celsius, f"Expected {celsius}, got {context.celsius}"
