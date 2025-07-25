Feature: Temperature conversion

  Scenario: Convert Fahrenheit to Celsius
    Given I have a temperature of 32 Fahrenheit
    When I convert it to Celsius
    Then the result should be 0 Celsius
