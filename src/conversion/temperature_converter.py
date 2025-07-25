import logging

class TemperatureConverter:
    def __init__(self):
        pass

    def convert_to_celsius(self, fahrenheit: int) -> int:
        celsius = (fahrenheit - 32) * 5 / 9

        logging.debug(f"Converting {fahrenheit}°F to {celsius}°C")
        return celsius
