import os
import sys
import pytest
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
    """Check if ValueError is raised for invalid temperature."""
    context.value_error_raised = False
    try:
        context.celsius = context.converter.convert_to_celsius(context.fahrenheit)
    except ValueError:
        context.value_error_raised = True

@then('the result should be {celsius:d} degrees Celsius')
@then('the result should be {celsius:f} degrees Celsius') # Allow float values
def step_then_result(context, celsius):
    assert context.celsius == celsius, f"Expected {celsius}, got {context.celsius}"

@then(u'the ValueError should be raised')
def step_then_value_error(context):
    """Check if ValueError is raised for invalid temperature."""
    assert context.value_error_raised, "ValueError was not raised as expected"