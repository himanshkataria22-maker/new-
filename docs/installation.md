# Installation Guide

This guide will help you install and set up the new- project on your system.

## Prerequisites

- Python 3.8 or higher
- Git
- pip (Python package installer)

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/himanshkataria22-maker/new-.git
cd new-
```

### 2. Create a Virtual Environment (Recommended)

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install the Package in Development Mode

```bash
pip install -e .
```

## Development Setup

For development, you may want to install additional dependencies:

```bash
pip install -e ".[dev]"
```

This will install:
- pytest for testing
- black for code formatting
- flake8 for linting

## Verify Installation

Run the main script to verify the installation:

```bash
python src/main.py
```

You should see the welcome message if everything is installed correctly.

## Next Steps

- Read the [API Documentation](api.md) to learn about available functions
- Check the [Contributing Guide](../CONTRIBUTING.md) to learn how to contribute
- Run the tests to ensure everything is working:
  
  ```bash
  python -m pytest tests/
  ```
