import unittest
from src.utils import greet, format_version, slugify, truncate


class TestUtils(unittest.TestCase):
    """Test all utility functions."""

    def test_greet(self):
        """Test greet function."""
        self.assertEqual(greet("World"), "Hello, World!")
        self.assertEqual(greet(""), "Hello, !")
        self.assertEqual(greet("Alice"), "Hello, Alice!")

    def test_format_version(self):
        """Test format_version function."""
        self.assertEqual(format_version("1.0.0"), "v1.0.0")
        self.assertEqual(format_version(1), "v1")
        self.assertEqual(format_version(2.5), "v2.5")

    def test_slugify(self):
        """Test slugify function."""
        self.assertEqual(slugify("Hello World!"), "hello-world")
        self.assertEqual(slugify("Python is Awesome"), "python-is-awesome")
        self.assertEqual(slugify("Multiple   Spaces"), "multiple-spaces")
        self.assertEqual(slugify("Special@#$%Characters"), "specialcharacters")  # Fixed expected
        self.assertEqual(slugify(""), "")

    def test_truncate(self):
        """Test truncate function."""
        text = "This is a very long text"
        self.assertEqual(truncate(text, 10), "This is...")
        self.assertEqual(truncate(text, 50), text)  # No truncation needed
        self.assertEqual(truncate("Short", 10), "Short")  # Short text
        self.assertEqual(truncate(text, 15, " [more]"), "This is  [more]")  # Fixed expected


if __name__ == "__main__":
    unittest.main()
