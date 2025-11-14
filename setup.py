#!/usr/bin/env python
"""Setup script for KOS Community Edition."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="wekaou-kos-ce",
    version="0.1.0",
    author="WEKAOU Community",
    author_email="community@wekaou.org",
    description="Knowledge Operating System - Community Edition",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zaste/wekaou-kos-community-edition",
    project_urls={
        "Bug Reports": "https://github.com/zaste/wekaou-kos-community-edition/issues",
        "Documentation": "https://github.com/zaste/wekaou-kos-community-edition/docs",
        "Source": "https://github.com/zaste/wekaou-kos-community-edition",
    },
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.9",
    install_requires=[
        "pydantic>=2.0",
        "jsonschema>=4.0",
        "pyyaml>=6.0",
        "click>=8.0",
        "fastapi>=0.100",
        "uvicorn>=0.20",
        "sqlalchemy>=2.0",
        "aiosqlite>=0.19",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=4.0",
            "pytest-asyncio>=0.21",
            "ruff>=0.1",
            "mypy>=1.0",
            "black>=23.0",
            "pre-commit>=3.0",
        ],
        "postgres": [
            "psycopg2-binary>=2.9",
            "asyncpg>=0.29",
        ],
        "mongodb": [
            "motor>=3.3",
            "pymongo>=4.5",
        ],
        "docs": [
            "sphinx>=6.0",
            "sphinx-rtd-theme>=1.3",
            "myst-parser>=2.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "kos=kos.cli:main",
        ],
    },
)
