import logging

class TemperatureConverter:
    def __init__(self):
        pass

    def convert_to_celsius(self, fahrenheit: float) -> float:
        if fahrenheit < -459.67:
            raise ValueError("Temperature below absolute zero is not allowed.")

        # Convert Fahrenheit to Celsius using the formula
        celsius: float = (fahrenheit - 32) * 5.0 / 9.0

        # Round to two decimal places for consistency
        return round(celsius, 2)
