# Automation Guide

This document describes all automation features available in the AI Learning Assistant project.

## Table of Contents
- [Quick Start](#quick-start)
- [Automated Setup](#automated-setup)
- [Development Automation](#development-automation)
- [CI/CD Pipeline](#cicd-pipeline)
- [Pre-commit Hooks](#pre-commit-hooks)
- [Dependency Management](#dependency-management)
- [Docker Automation](#docker-automation)

## Quick Start

### First-Time Setup
```bash
# Clone the repository
git clone <repository-url>
cd ai_app

# Run automated setup (installs dependencies, creates dirs, verifies env)
./setup.sh

# Or use Makefile
make setup
```

### Daily Development
```bash
# Run the application
make run

# Run tests
make test

# Check code quality
make lint

# Format code
make format
```

## Automated Setup

### Setup Script (`setup.sh`)

The setup script automates initial project configuration:

**What it does:**
- ✅ Checks Python version
- ✅ Offers to create virtual environment
- ✅ Installs dependencies
- ✅ Creates required directories (uploads, temp)
- ✅ Creates .env from template
- ✅ Optionally saves API key
- ✅ Verifies environment

**Usage:**
```bash
./setup.sh
```

**Interactive prompts:**
- Create virtual environment? (y/n)
- Enter OpenAI API key? (y/n)

### Environment Verification (`verify_env.py`)

Validates your development environment:

**What it checks:**
- ✅ Environment variables (OPENAI_API_KEY, etc.)
- ✅ Required directories exist
- ✅ Required files exist
- ✅ Python dependencies installed

**Usage:**
```bash
python verify_env.py
# Or: make verify
```

**Exit codes:**
- 0 = All checks passed
- 1 = Some checks failed

## Development Automation

### Makefile

The Makefile provides convenient commands for common tasks:

#### Available Commands

| Command | Description |
|---------|-------------|
| `make help` | Show all available commands |
| `make install` | Install Python dependencies |
| `make setup` | Complete project setup |
| `make verify` | Verify environment |
| `make test` | Run test suite |
| `make lint` | Run code linting |
| `make format` | Format code with Black |
| `make clean` | Clean temporary files |
| `make run` | Run the application |
| `make docker-build` | Build Docker image |
| `make docker-run` | Run in Docker |
| `make docker-stop` | Stop Docker containers |
| `make dev-install` | Install dev dependencies |

#### Examples

```bash
# Install and verify
make install
make verify

# Development cycle
make format    # Format code
make lint      # Check code quality
make test      # Run tests
make run       # Start app

# Clean up
make clean     # Remove temp files
```

## CI/CD Pipeline

### GitHub Actions Workflows

#### CI/CD Pipeline (`.github/workflows/ci.yml`)

**Triggers:**
- Push to `main` or `develop`
- Pull requests to `main` or `develop`

**Jobs:**

1. **Lint** - Code Quality Checks
   - Black formatter check
   - Flake8 linting
   - Runs on Python 3.11

2. **Test** - Run Tests
   - Pytest with coverage
   - Coverage reports uploaded to Codecov
   - Creates test directories

3. **Security** - Security Scan
   - Safety check for dependencies
   - Bandit security linter
   - Uploads security reports

4. **Build Docker** - Build Docker Image
   - Docker image build
   - Image testing
   - Caching enabled

**Status:**
Check CI status in pull requests or the Actions tab

#### Dependency Update (`.github/workflows/dependency-update.yml`)

**Triggers:**
- Weekly (Monday 9:00 AM UTC)
- Manual trigger (`workflow_dispatch`)

**What it does:**
- Checks for outdated packages
- Runs security scans
- Creates issues for vulnerabilities
- Uploads dependency reports

**Artifacts:**
- `outdated.txt` - List of outdated packages
- `safety-report.json` - Security vulnerabilities

## Pre-commit Hooks

### Installation

```bash
pip install pre-commit
pre-commit install
```

### What Gets Checked

When you run `git commit`, these checks run automatically:

1. **General File Checks**
   - Trailing whitespace removal
   - End-of-file fixing
   - YAML/JSON validation
   - Large file detection (>10MB)
   - Merge conflict detection

2. **Python Formatting**
   - Black (120 char line length)
   - Import sorting (isort)

3. **Python Linting**
   - Flake8 code analysis

4. **Security**
   - Bandit security checks

5. **Docker**
   - Hadolint Dockerfile linting

### Manual Run

```bash
# Run on all files
pre-commit run --all-files

# Run specific hook
pre-commit run black --all-files
```

### Skip Hooks (Not Recommended)

```bash
git commit --no-verify
```

## Dependency Management

### Automated Security Scanning

**Weekly Scans:**
- Every Monday at 9:00 AM UTC
- Checks for vulnerabilities
- Creates GitHub issues if found

**Manual Scan:**
```bash
# Check for vulnerabilities
pip install safety
safety check

# Check for outdated packages
pip list --outdated
```

### Updating Dependencies

```bash
# Update a single package
pip install --upgrade package-name

# Update all packages (careful!)
pip install --upgrade -r requirements.txt

# After updating, test thoroughly
make test
```

### Development Dependencies

```bash
# Install dev dependencies
pip install -r requirements-dev.txt
# Or: make dev-install

# Includes: pytest, black, flake8, bandit, etc.
```

## Docker Automation

### Building Images

```bash
# Build image
make docker-build

# Or manually
docker build -t ai-learning-assistant:latest .
```

### Running Containers

```bash
# Start with docker-compose
make docker-run

# Or manually
docker-compose up -d

# Check status
docker-compose ps

# View logs
docker-compose logs -f
```

### Health Checks

The Docker container includes health checks:
- Endpoint: `http://localhost:8501/_stcore/health`
- Interval: 30 seconds
- Timeout: 10 seconds
- Retries: 3

### Stopping Containers

```bash
make docker-stop

# Or manually
docker-compose down
```

## Testing Automation

### Running Tests

```bash
# All tests
make test

# Specific test file
pytest tests/test_file_handler.py -v

# With coverage
pytest tests/ -v --cov=. --cov-report=html

# Watch mode (requires pytest-watch)
ptw tests/
```

### Test Structure

```
tests/
├── __init__.py
├── test_file_handler.py    # FileHandler tests
└── test_llm_handler.py      # LLMHandler tests
```

### Adding New Tests

1. Create test file: `tests/test_your_module.py`
2. Write test functions: `def test_something():`
3. Run tests: `make test`
4. Check coverage: open `htmlcov/index.html`

## Continuous Integration

### What Happens on PR

1. **Automated checks run:**
   - Code formatting validation
   - Linting
   - Tests
   - Security scans
   - Docker build

2. **Status checks appear:**
   - ✅ All checks passed → Ready to merge
   - ❌ Checks failed → Review errors

3. **Review process:**
   - Fix any issues
   - Push updates
   - Checks run again

### Local CI Simulation

Run the same checks locally before pushing:

```bash
# Format code
make format

# Run linting
make lint

# Run tests
make test

# Verify environment
make verify

# Pre-commit checks
pre-commit run --all-files
```

## Troubleshooting

### Setup Issues

```bash
# Verify Python version
python3 --version  # Should be 3.11+

# Check environment
python verify_env.py

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Pre-commit Issues

```bash
# Update hooks
pre-commit autoupdate

# Reinstall hooks
pre-commit install --install-hooks

# Clean and retry
pre-commit clean
pre-commit run --all-files
```

### Docker Issues

```bash
# Clean Docker cache
docker system prune -a

# Rebuild from scratch
docker-compose down
docker-compose up --build

# Check logs
docker-compose logs -f ai-app
```

### CI/CD Issues

- **Check Actions tab** in GitHub
- **Review logs** for failed jobs
- **Run locally** to reproduce issues
- **Check permissions** for GitHub Actions

## Best Practices

### Before Committing

```bash
make format    # Format code
make lint      # Check quality
make test      # Run tests
make verify    # Verify env
```

### Before Pushing

```bash
# Ensure all tests pass
make test

# Check CI will succeed
pre-commit run --all-files

# Verify Docker still works
make docker-build
```

### Regular Maintenance

- **Weekly:** Review dependency updates
- **Monthly:** Update dependencies
- **After updates:** Run full test suite
- **Before releases:** Full CI/CD check

## Additional Resources

- [CONTRIBUTING.md](CONTRIBUTING.md) - Development workflow
- [README.md](README.md) - Project overview
- [QUICKSTART.md](QUICKSTART.md) - Quick start guide
- [GitHub Actions Docs](https://docs.github.com/en/actions)
- [Pre-commit Docs](https://pre-commit.com/)

## Support

If automation fails:
1. Check error messages
2. Review this guide
3. Check GitHub Actions logs
4. Consult CONTRIBUTING.md
5. Open an issue with details

---

**Remember:** Automation is here to help! If it's causing problems, review the docs or ask for help.
