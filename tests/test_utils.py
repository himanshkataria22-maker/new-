"""
Test suite for the utils module.

This module contains unit tests for the utility functions
to ensure they work as expected.
"""

import unittest
from src.utils import greet, format_version


class TestUtils(unittest.TestCase):
    """Test cases for utility functions."""

    def test_greet(self):
        """Test the greet function."""
        result = greet("World")
        self.assertEqual(result, "Hello, World! Welcome to the new- project.")
        
        result = greet("")
        self.assertEqual(result, "Hello, ! Welcome to the new- project.")

    def test_format_version(self):
        """Test the format_version function."""
        result = format_version("1.0.0")
        self.assertEqual(result, "v1.0.0")
        
        result = format_version("0.1")
        self.assertEqual(result, "v0.1")


if __name__ == "__main__":
    unittest.main()
