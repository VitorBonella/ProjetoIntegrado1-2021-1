"""
Módulo de realização do build
"""
from setuptools import setup, find_packages

setup(
    name="app-cafe2020",
    version="0.9.0",
    description="APP DO CAFE",
    packages=find_packages(exclude="venv"),
    include_package_data=True,
    install_requires=[req.strip for req in open("requirements.txt").readlines()]
)
