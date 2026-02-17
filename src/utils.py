"""
Essential utilities for everyday Python development.
"""

from typing import Union


def greet(name: str) -> str:
    """
    Generate a friendly greeting.
    
    Args:
        name: Name to greet
        
    Returns:
        Personalized greeting message
        
    Example:
        >>> greet("Alice")
        'Hello, Alice!'
    """
    return f"Hello, {name}!"


def format_version(version: Union[str, int, float]) -> str:
    """
    Format version with 'v' prefix.
    
    Args:
        version: Version number (1.0, "2.3", 3, etc.)
        
    Returns:
        Version string with 'v' prefix
        
    Example:
        >>> format_version("1.0.0")
        'v1.0.0'
    """
    return f"v{version}"


def slugify(text: str) -> str:
    """
    Convert text to URL-friendly slug.
    
    Args:
        text: Text to convert
        
    Returns:
        URL-friendly slug
        
    Example:
        >>> slugify("Hello World!")
        'hello-world'
    """
    import re
    # Convert to lowercase and replace spaces with hyphens
    slug = re.sub(r'\s+', '-', text.lower())
    # Remove special characters except hyphens
    slug = re.sub(r'[^a-z0-9-]', '', slug)
    # Remove multiple consecutive hyphens
    slug = re.sub(r'-+', '-', slug)
    return slug.strip('-')


def truncate(text: str, max_length: int = 50, suffix: str = "...") -> str:
    """
    Truncate text to specified length.
    
    Args:
        text: Text to truncate
        max_length: Maximum length before truncation
        suffix: Suffix to add when truncated
        
    Returns:
        Truncated text
        
    Example:
        >>> truncate("This is a very long text", 10)
        'This is...'
    """
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix
