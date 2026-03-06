.PHONY: help install dev run clean lint test

# Default target
help:
	@echo "Available targets:"
	@echo "  make install      - Create virtual environment and install dependencies"
	@echo "  make dev          - Run development server"
	@echo "  make run          - Run the agent"
	@echo "  make clean        - Remove virtual environment and cache files"
	@echo "  make lint         - Run code linting"
	@echo "  make test         - Run tests"

# Create virtual environment and install dependencies
install:
	python3 -m venv venv
	. venv/bin/activate && pip install --upgrade pip
	. venv/bin/activate && pip install -r requirements.txt

# Run development server
dev:
	. venv/bin/activate && python -m app.client.agent

# Run the agent
run-mcp:
	. venv/bin/activate && python -m app.client.agent

# Clean up
clean:
	rm -rf venv
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +

# Run linting
lint:
	. venv/bin/activate && python -m pylint app/

# Run tests
test:
	. venv/bin/activate && python -m pytest
