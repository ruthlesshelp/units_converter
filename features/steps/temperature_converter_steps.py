import os
import sys
from behave import given, when, then

# Add src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from conversion.temperature_converter import TemperatureConverter

@given('I have a temperature of {fahrenheit:d} Fahrenheit')
def step_given_temperature(context, fahrenheit):
    context.fahrenheit = fahrenheit

@when('I convert it to Celsius')
def step_when_convert(context):
    converter = TemperatureConverter()
    context.celsius = converter.convert_to_celsius(context.fahrenheit)

@then('the result should be {expected:d} Celsius')
def step_then_result(context, expected):
    assert context.celsius == expected, f"Expected {expected}, got {context.celsius}"
