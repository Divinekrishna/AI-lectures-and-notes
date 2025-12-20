# Makefile for AI Learning Assistant
# Automates common development and deployment tasks

.PHONY: help install setup test lint format clean run docker-build docker-run verify

# Default target
help:
	@echo "AI Learning Assistant - Makefile Commands"
	@echo "=========================================="
	@echo "make install      - Install Python dependencies"
	@echo "make setup        - Complete setup (install + create dirs + verify)"
	@echo "make verify       - Verify environment configuration"
	@echo "make test         - Run tests"
	@echo "make lint         - Run code linting"
	@echo "make format       - Format code with black"
	@echo "make clean        - Clean temporary files and caches"
	@echo "make run          - Run the Streamlit application"
	@echo "make docker-build - Build Docker image"
	@echo "make docker-run   - Run application in Docker"
	@echo "make docker-stop  - Stop Docker containers"

# Install dependencies
install:
	@echo "📦 Installing Python dependencies..."
	pip install -r requirements.txt
	@echo "✅ Dependencies installed successfully"

# Complete setup
setup: install
	@echo "🔧 Setting up project structure..."
	mkdir -p uploads temp
	@if [ ! -f .env ]; then \
		echo "📄 Creating .env file from template..."; \
		cp .env.example .env; \
		echo "⚠️  Please edit .env and add your OPENAI_API_KEY"; \
	fi
	@echo "✅ Setup complete!"
	@make verify

# Verify environment
verify:
	@echo "🔍 Verifying environment..."
	python verify_env.py

# Run tests (placeholder for future implementation)
test:
	@echo "🧪 Running tests..."
	@if [ -d tests ]; then \
		python -m pytest tests/ -v; \
	else \
		echo "⚠️  No tests directory found. Skipping tests."; \
	fi

# Lint code
lint:
	@echo "🔍 Running code linting..."
	@if command -v flake8 > /dev/null; then \
		flake8 app.py file_handler.py llm_handler.py --max-line-length=120 --ignore=E501,W503; \
	else \
		echo "⚠️  flake8 not installed. Run: pip install flake8"; \
	fi

# Format code
format:
	@echo "✨ Formatting code..."
	@if command -v black > /dev/null; then \
		black app.py file_handler.py llm_handler.py --line-length=120; \
	else \
		echo "⚠️  black not installed. Run: pip install black"; \
	fi

# Clean temporary files
clean:
	@echo "🧹 Cleaning temporary files..."
	find . -type d -name "__pycache__" -exec rm -r {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	find . -type f -name "*.pyo" -delete 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -r {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -r {} + 2>/dev/null || true
	rm -rf build dist .eggs
	@echo "✅ Cleanup complete"

# Run the application
run:
	@echo "🚀 Starting Streamlit application..."
	@make verify
	streamlit run app.py

# Build Docker image
docker-build:
	@echo "🐳 Building Docker image..."
	docker build -t ai-learning-assistant:latest .
	@echo "✅ Docker image built successfully"

# Run Docker container
docker-run:
	@echo "🐳 Starting Docker container..."
	docker-compose up -d
	@echo "✅ Application running at http://localhost:8501"

# Stop Docker containers
docker-stop:
	@echo "🛑 Stopping Docker containers..."
	docker-compose down
	@echo "✅ Docker containers stopped"

# Development dependencies
dev-install:
	@echo "📦 Installing development dependencies..."
	pip install flake8 black pytest pytest-cov
	@echo "✅ Development dependencies installed"
