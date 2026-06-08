#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DevToolbox-CLI — Setup Script
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="devtoolbox-cli",
    version="1.0.0",
    author="gitstq",
    author_email="",
    description="🧰 Lightweight Terminal Developer Utility Engine — Zero Dependencies, Cross-Platform",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gitstq/DevToolbox-CLI",
    py_modules=["main"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "devtoolbox=main:main",
        ],
    },
    keywords="cli developer tools json base64 hash uuid jwt regex utility terminal",
    project_urls={
        "Bug Reports": "https://github.com/gitstq/DevToolbox-CLI/issues",
        "Source": "https://github.com/gitstq/DevToolbox-CLI",
    },
)
