from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="new-",
    version="0.1.0",
    author="Himanshu Kataria",
    description="A simple project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/himanshkataria22-maker/new-",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
