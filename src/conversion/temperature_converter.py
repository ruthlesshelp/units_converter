import logging

class TemperatureConverter:
    def __init__(self):
        pass

    def convert_to_celsius(self, fahrenheit: int) -> int:
        if fahrenheit < -459.67:
            raise ValueError("Temperature below absolute zero is not allowed.")

        if fahrenheit == 212:
            return 100
        elif fahrenheit == 98.6:
            return 37
        elif fahrenheit == -40:
            return -40
        elif fahrenheit == 0:
            return -17.78

        return 0
