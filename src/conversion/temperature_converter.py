import logging

class TemperatureConverter:
    def __init__(self):
        pass

    def convert_to_celsius(self, fahrenheit: int) -> int:
        if fahrenheit < -459.67:
            raise ValueError("Temperature below absolute zero is not valid")

        celsius = (fahrenheit - 32) * 5 / 9
        celsius = round(celsius, 2)

        logging.debug(f"Converting {fahrenheit}°F to {celsius}°C")
        return celsius
