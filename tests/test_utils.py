import unittest
from src.utils import greet, format_version


class TestUtils(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("World"), "Hello, World!")

    def test_format_version(self):
        self.assertEqual(format_version("1.0.0"), "v1.0.0")


if __name__ == "__main__":
    unittest.main()
