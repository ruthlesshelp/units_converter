"""
Environment setup for behave BDD tests.
This file contains hooks that run before/after scenarios and features.
"""

import logging
import sys
import os

# Add src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))


def before_all(context):
    """Setup that runs before all tests."""
    # Configure logging for tests
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    context.logger = logging.getLogger('behave_tests')
    context.logger.info("Starting BDD test suite")


def before_feature(context, feature):
    """Setup that runs before each feature."""
    context.logger.info(f"Starting feature: {feature.name}")


def before_scenario(context, scenario):
    """Setup that runs before each scenario."""
    context.logger.info(f"Starting scenario: {scenario.name}")
    # Clear any previous state
    context.converter = None
    context.result = None
    context.error = None


def after_scenario(context, scenario):
    """Cleanup that runs after each scenario."""
    if scenario.status == "failed":
        context.logger.error(f"Scenario failed: {scenario.name}")
    else:
        context.logger.info(f"Scenario passed: {scenario.name}")


def after_feature(context, feature):
    """Cleanup that runs after each feature."""
    context.logger.info(f"Finished feature: {feature.name}")


def after_all(context):
    """Cleanup that runs after all tests."""
    context.logger.info("Finished BDD test suite")
