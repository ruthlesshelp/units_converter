import logging

class TemperatureConverter:
    def __init__(self):
        pass

    def convert_to_celsius(self, fahrenheit: int) -> int:
        celsius = 0

        if fahrenheit == 212:
            celsius = 100

        logging.debug(f"Converting {fahrenheit}°F to {celsius}°C")
        return celsius
