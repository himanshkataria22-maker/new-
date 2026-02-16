# API Documentation

This document provides information about the API and functions available in the new- project.

## Modules

### utils.py

Utility functions that can be used across the application.

#### Functions

##### `greet(name: str) -> str`

Generates a greeting message for the given name.

**Parameters:**
- `name` (str): The name to greet

**Returns:**
- str: A formatted greeting message

**Example:**
```python
from src.utils import greet

message = greet("Alice")
print(message)  # Output: Hello, Alice! Welcome to the new- project.
```

##### `format_version(version: str) -> str`

Formats a version string by adding a 'v' prefix.

**Parameters:**
- `version` (str): The raw version string

**Returns:**
- str: The formatted version string with 'v' prefix

**Example:**
```python
from src.utils import format_version

formatted = format_version("1.0.0")
print(formatted)  # Output: v1.0.0
```

### main.py

Main entry point for the application.

#### Functions

##### `main() -> int`

Main function that runs the application.

**Returns:**
- int: Exit code (0 for success)

**Example:**
```python
if __name__ == "__main__":
    exit(main())
```
