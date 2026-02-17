#!/usr/bin/env python3
"""
new- - Essential Python utilities

A lightweight toolkit that makes common tasks ridiculously simple.
"""

from utils import greet, format_version, slugify, truncate


def demo():
    """Quick demo of all utilities."""
    print("new- - Essential Python Utilities")
    print("=" * 40)
    
    # Demo greet
    print(f"greet('World'): {greet('World')}")
    
    # Demo format_version
    print(f"format_version('1.0.0'): {format_version('1.0.0')}")
    
    # Demo slugify
    print(f"slugify('Hello World!'): {slugify('Hello World!')}")
    
    # Demo truncate
    long_text = "This is a very long text that needs to be truncated"
    print(f"truncate('{long_text}', 20): {truncate(long_text, 20)}")


def main():
    """Main entry point."""
    demo()
    return 0


if __name__ == "__main__":
    exit(main())
