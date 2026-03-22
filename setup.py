"""
Setup configuration for Automotive Claude Code.
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

setup(
    name="automotive-claude-code",
    version="0.1.0",
    description="Universal AI-powered development platform for automotive industry",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Automotive Claude Code Contributors",
    author_email="automotive-claude-code@opensource.ai",
    url="https://github.com/automotive-opensource/automotive-claude-code-agents",
    packages=find_packages(exclude=["tests", "docs", "examples"]),
    python_requires=">=3.8",
    install_requires=[
        "anthropic>=0.39.0",
        "openai>=1.54.0",
        "pyyaml>=6.0.2",
        "python-dotenv>=1.0.0",
        "python-can>=4.4.2",
        "cantools>=39.4.5",
    ],
    extras_require={
        "dev": [
            "pytest>=8.3.3",
            "pytest-cov>=5.0.0",
            "pytest-asyncio>=0.23.8",
            "black>=24.8.0",
            "ruff>=0.6.9",
            "mypy>=1.11.2",
        ],
        "docs": [
            "mkdocs>=1.6.1",
            "mkdocs-material>=9.5.39",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Automotive",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    keywords="automotive autosar adas battery ev autonomous safety iso26262",
    project_urls={
        "Documentation": "https://automotive-claude-code.readthedocs.io/",
        "Source": "https://github.com/automotive-opensource/automotive-claude-code-agents",
        "Tracker": "https://github.com/automotive-opensource/automotive-claude-code-agents/issues",
    },
)
