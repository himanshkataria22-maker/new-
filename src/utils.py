"""
Utility functions for the new- project.

This module contains common utility functions that can be
used across different parts of the application.
"""

def greet(name: str) -> str:
    """
    Generate a greeting message.
    
    Args:
        name (str): The name to greet
        
    Returns:
        str: A greeting message
    """
    return f"Hello, {name}! Welcome to the new- project."

def format_version(version: str) -> str:
    """
    Format version string for display.
    
    Args:
        version (str): Raw version string
        
    Returns:
        str: Formatted version string
    """
    return f"v{version}"
