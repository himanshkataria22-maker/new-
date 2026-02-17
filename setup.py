from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="new-",
    version="1.0.0",
    author="Himanshu Kataria",
    description="Essential Python utilities that make common tasks ridiculously simple",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/himanshkataria22-maker/new-",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    python_requires=">=3.6",
    keywords="utilities, toolkit, simple, essential",
    project_urls={
        "Bug Reports": "https://github.com/himanshkataria22-maker/new-/issues",
        "Source": "https://github.com/himanshkataria22-maker/new-",
    },
)
