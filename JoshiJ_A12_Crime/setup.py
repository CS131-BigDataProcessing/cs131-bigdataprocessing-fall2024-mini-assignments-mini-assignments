# setup.py

from setuptools import setup, find_packages

setup(
    name="crime_test",
    version="1.0.0",
    author="Your Name",
    description="A package for validating and calculating crime statistics",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy"
    ]
)

