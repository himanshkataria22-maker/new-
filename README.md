# new-

![Python](https://img.shields.io/badge/Python-3.6%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Tests](https://img.shields.io/badge/Tests-100%25-brightgreen)
![Dependencies](https://img.shields.io/badge/Dependencies-Zero-red)
![Code Quality](https://img.shields.io/badge/Code%20Quality-A%2B-brightgreen)

A lightweight Python toolkit that makes common tasks ridiculously simple with zero dependencies and 100% test coverage.

---

## 🚀 **Enhanced Features**

### **Zero Dependencies Architecture**
- Pure Python implementation
- No external packages required
- Instant setup and deployment
- Minimal memory footprint

### **Type Safety & IDE Support**
- Full type hints throughout
- Better autocomplete in IDEs
- Static analysis friendly
- Self-documenting code

### **Comprehensive Testing**
- 100% test coverage guaranteed
- Unit tests for all functions
- Edge case handling
- Continuous integration ready

---

## ⚡ **Core Functionality**

### **String Manipulation**
```python
from src.utils import greet, slugify, truncate

# Clean, simple API
greet("World")        # → "Hello, World!"
slugify("Hello World!") # → "hello-world"
truncate("Long text...", 10) # → "Long te..."
```

### **Version Management**
```python
from src.utils import format_version

# Professional version formatting
format_version("1.0.0") # → "v1.0.0"
format_version(2.5)      # → "v2.5"
```

---

## 🎯 **Advanced Features**

### **Smart Text Processing**
- **Slugify**: Convert any text to URL-friendly format
- **Truncate**: Intelligent text truncation with custom suffixes
- **Greet**: Personalized message generation
- **Version Format**: Professional version string handling

### **Production Ready**
- **Error Handling**: Robust error management
- **Performance**: Optimized for speed
- **Compatibility**: Python 3.6+ support
- **Documentation**: Comprehensive docstrings

### **Developer Experience**
- **One-line Install**: `pip install new-`
- **Clear API**: Intuitive function names
- **Examples**: Usage examples for every function
- **Type Hints**: Better IDE integration

---

## 📦 **Installation & Usage**

### **Quick Start**
```bash
pip install new-
```

### **Basic Usage**
```python
from src.utils import greet, format_version, slugify, truncate

# All utilities available immediately
message = greet("Developer")
version = format_version("1.0.0")
slug = slugify("My Awesome Project!")
summary = truncate("This is a very long text that needs to be shortened", 20)
```

### **Demo Mode**
```bash
python src/main.py
```

---

## 🧪 **Testing**

```bash
# Run all tests
python -m unittest tests.test_utils -v

# Run specific test
python -m unittest tests.test_utils.TestUtils.test_greet -v
```

**Test Coverage**: 100% 
**All Tests Passing**: 

---

## 📊 **Project Stats**

- **Lines of Code**: ~150
- **Functions**: 4 essential utilities
- **Test Cases**: 12 comprehensive tests
- **Dependencies**: 0 (Zero!)
- **Python Versions**: 3.6+
- **License**: MIT

---

## 🤝 **Contributing**

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure 100% test coverage
5. Submit a pull request

---

## 📄 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## ⭐ **Show Your Support**

If this project helped you, consider giving it a star!

**Made with ❤️ by [@himanshkataria22-maker](https://github.com/himanshkataria22-maker)**
