Feature: Fahrenheit to Celsius Conversion
  As a user
  I want to convert temperatures between Fahrenheit and Celsius
  So that I can work with different temperature scales

  Scenario Outline: Convert Fahrenheit to Celsius
    Given I have a temperature converter
    When I convert <fahrenheit> degrees Fahrenheit to Celsius
    Then the result should be <celsius> degrees Celsius

    Examples:
      | fahrenheit | celsius | reason                  |
      | 32         | 0       | freezing point of water |
      | 212        | 100     | boiling point of water  |
