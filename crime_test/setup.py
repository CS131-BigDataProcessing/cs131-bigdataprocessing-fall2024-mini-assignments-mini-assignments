from setuptools import setup, find_packages

setup(
    name="crime_test",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy"
    ],
    author="Lawton Fong",
    description="A package for validating and analyzing crime dataset",
    url="https://github.com/CS131-BigDataProcessing/cs131-bigdataprocessing-fall2024-mini-assignments-mini-assignments/crime_test",
    python_requires=">=3.6"
)