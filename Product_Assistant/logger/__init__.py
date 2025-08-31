"""
Logging Module.

This module provides logging configuration and utilities for the
Ecommerce Product Assistant application. It handles log formatting,
file rotation, and different log levels for development and production.
"""
# logger/__init__.py
from .custom_logger import CustomLogger

# Create a single shared logger instance
GLOBAL_LOGGER = CustomLogger().get_logger("prod_assistant")