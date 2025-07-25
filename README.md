# Units Converter
A units converter program that is used for training purposes.

## Getting Started

### Using virtual environment venv

Python virtual environments enable you to set up a Python sandbox with its own set of packages separate from the system site-packages in which to work.

#### Create

```bash
$ python -m venv env_dir_name
```

#### Activate

To activate on macOS and Linux.
```bash
$ source env_dir_name/bin/activate
```

To activate on Windows.
```bash
$ env_dir_name\Scripts\activate.bat
```

To activate on Windows with PowerShell.
```bash
$ env_dir_name\Scripts\Activate.ps
```

#### Deactivate

When done, run:
```bash
$ deactivate
```

### Using pip to install pytest

`pip` is the tool used to install Python packages, and it is installed as part of
your Python installation.

Confirm pip version by running:
```bash
$ pip --version
```

You should see:
```bash
pip 24.0 from /Users/ ... /env_dir_name/lib/python3.11/site-packages/pip (python 3.11)
```

Install pytest by running:
```bash
$ pip install pytest
```

Confirm the pytest version by running:
```bash
$ pytest --version
```

You should see:
```bash
pytest 8.1.1
```

## Running the pytest testing framework

Run pytest with the following command:
```bash
$ pytest [options] [file_or_dir] [file_or_dir]
```

Show help message and configuration info:
```bash
$ pytest --help
```

### Commands to run tests

| Command |  Description |
|:--------|:-------------|
| `pytest tests` | Run tests in a directory. |

### Passing test output

Running:
```bash
$ pytest tests
```

Returns:
```bash
(.venv) ruthlesshelp:units_converter$ pytest tests
======================================================= test session starts ========================================================
platform darwin -- Python 3.11.7, pytest-8.4.1, pluggy-1.6.0
rootdir: /Users/.../ruthlesshelp/units_converter
collected 2 items                                                                                                                  

tests/test_temperature_converter.py .F                                                                                       [100%]

============================================================= FAILURES =============================================================
_________________________________________________ test_convert_with_32f_expect_0c __________________________________________________

    def test_convert_with_32f_expect_0c():
        """convert 32F to 0C"""
        # Arrange
        class_under_test = TemperatureConverter()
    
        # Act
>       result = class_under_test.convert_to_celsius(32)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_temperature_converter.py:29: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <conversion.temperature_converter.TemperatureConverter object at 0x1019240d0>, fahrenheit = 32

    def convert_to_celsius(self, fahrenheit: int) -> int:
        # throw a NotImplementedError if the method is not implemented
>       raise NotImplementedError("This method is not implemented.")
E       NotImplementedError: This method is not implemented.

src/conversion/temperature_converter.py:9: NotImplementedError
===================================================== short test summary info ======================================================
FAILED tests/test_temperature_converter.py::test_convert_with_32f_expect_0c - NotImplementedError: This method is not implemented.
=================================================== 1 failed, 1 passed in 0.02s ====================================================
```

### Congratulations!

Congrats, now that you have failing tests, you're ready to started.

## Behavior-Driven Development (BDD) with Behave

This project includes BDD tests using the `behave` framework. BDD tests are written in natural language using the Gherkin syntax.

Install `behave` by running:
```bash
$ pip install behave
```

Confirm the `behave` version by running:
```bash
$ behave --version
```

You should see:
```bash
behave 1.2.6
```

### Running BDD Tests

Run all BDD tests:
```bash
$ behave
```

Run BDD tests with verbose output:
```bash
$ behave -v
```

Run BDD tests with specific tags:
```bash
$ behave --tags=@smoke
```

Using the Makefile:
```bash
$ make bdd           # Run all BDD tests
```

### BDD Test Structure

- **Features**: Located in `features/` directory
  - `temperature_conversion.feature` - Contains scenarios for temperature conversion
- **Step Definitions**: Located in `features/steps/`
  - `temperature_steps.py` - Python code that implements the Gherkin steps
- **Environment**: `features/environment.py` - Setup and teardown hooks
- **Configuration**: `behave.ini` - Behave configuration settings

### Writing New BDD Tests

1. Add scenarios to feature files using Gherkin syntax:
   ```gherkin
   Scenario: Convert room temperature
     Given I have a temperature converter
     When I convert 72 degrees Fahrenheit to Celsius
     Then the result should be 22.22 degrees Celsius
   ```

2. Implement step definitions in Python:
   ```python
   @when('I convert {fahrenheit:f} degrees Fahrenheit to Celsius')
   def step_convert_temperature(context, fahrenheit):
       context.result = context.converter.convert_to_celsius(fahrenheit)
   ```
