.PHONY: help install test lint format clean build docs

help:
	@echo "Automotive Claude Code - Available Commands"
	@echo ""
	@echo "Setup:"
	@echo "  make install    - Install Python dependencies"
	@echo "  make dev        - Install development dependencies"
	@echo ""
	@echo "Development:"
	@echo "  make format     - Format code with black"
	@echo "  make lint       - Run linters (ruff, mypy)"
	@echo "  make test       - Run all tests"
	@echo "  make coverage   - Run tests with coverage report"
	@echo ""
	@echo "Tools:"
	@echo "  make detect-tools   - Detect installed automotive tools"
	@echo "  make list-adapters  - List all tool adapters"
	@echo ""
	@echo "Documentation:"
	@echo "  make docs       - Build documentation"
	@echo "  make docs-serve - Serve documentation locally"
	@echo ""
	@echo "Cleanup:"
	@echo "  make clean      - Remove build artifacts"
	@echo "  make clean-all  - Remove all generated files"

install:
	pip install -r requirements.txt

dev:
	pip install -r requirements.txt
	pip install -e .

format:
	black tools/ skills/ agents/ commands/ tests/
	ruff check --fix tools/ skills/ agents/ commands/ tests/

lint:
	ruff check tools/ skills/ agents/ commands/ tests/
	mypy tools/ --strict

test:
	pytest tests/ -v

coverage:
	pytest tests/ --cov=tools --cov=skills --cov=agents --cov-report=html --cov-report=term-missing

detect-tools:
	python -m tools.detectors.tool_detector

list-adapters:
	python -m tools.tool_router --list

docs:
	mkdocs build

docs-serve:
	mkdocs serve

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.coverage" -delete
	rm -rf build/ dist/ *.egg-info/ .pytest_cache/ .mypy_cache/ .ruff_cache/ htmlcov/

clean-all: clean
	rm -rf venv/ .venv/ ENV/ env/
	find . -type f -name "*.log" -delete
