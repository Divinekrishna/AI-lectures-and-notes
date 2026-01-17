# Contributing to AI Learning Assistant

Thank you for your interest in contributing! This document provides guidelines and workflows for contributing to the project.

## 🚀 Getting Started

### Setting Up Your Development Environment

1. **Fork and clone the repository**
   ```bash
   git clone https://github.com/your-username/AI-lectures-and-notes.git
   cd AI-lectures-and-notes
   ```

2. **Run automated setup**
   ```bash
   ./setup.sh
   # Or use: make setup
   ```

3. **Install development dependencies**
   ```bash
   pip install -r requirements-dev.txt
   ```

4. **Install pre-commit hooks**
   ```bash
   pre-commit install
   ```

## 🔄 Development Workflow

### 1. Create a Feature Branch
```bash
git checkout -b feature/your-feature-name
```

### 2. Make Your Changes

Follow these guidelines:
- Write clear, self-documenting code
- Add comments for complex logic
- Update documentation as needed
- Add tests for new functionality

### 3. Run Automated Checks

Before committing, ensure your code passes all checks:

```bash
# Format code
make format

# Run linting
make lint

# Run tests
make test

# Verify environment
make verify
```

### 4. Commit Your Changes

Pre-commit hooks will automatically run when you commit:

```bash
git add .
git commit -m "feat: add your feature description"
```

Use conventional commit messages:
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `test:` - Adding or updating tests
- `refactor:` - Code refactoring
- `chore:` - Maintenance tasks

### 5. Push and Create Pull Request

```bash
git push origin feature/your-feature-name
```

Then create a pull request on GitHub.

## 📋 Code Standards

### Python Style Guide
- Follow PEP 8 guidelines
- Use Black for code formatting (line length: 120)
- Use isort for import sorting
- Maximum line length: 120 characters

### Testing
- Write unit tests for new functions
- Maintain or improve code coverage
- Use meaningful test names
- Test edge cases and error conditions

### Documentation
- Update README.md for user-facing changes
- Add docstrings to functions and classes
- Comment complex algorithms
- Update QUICKSTART.md for setup changes

## 🧪 Testing

### Running Tests
```bash
# Run all tests
make test

# Run specific test file
pytest tests/test_file_handler.py -v

# Run with coverage report
pytest tests/ -v --cov=. --cov-report=html
```

### Writing Tests
- Place tests in the `tests/` directory
- Name test files as `test_*.py`
- Name test functions as `test_*`
- Use fixtures for common setup
- Mock external API calls

## 🔒 Security

### Security Best Practices
- Never commit API keys or secrets
- Use environment variables for sensitive data
- Run `bandit` for security checks: `make lint`
- Check dependencies: `safety check`

### Reporting Security Issues
If you discover a security vulnerability, please email the maintainers directly instead of opening a public issue.

## 📝 Pull Request Process

1. **Ensure CI passes**: All GitHub Actions checks must pass
2. **Update documentation**: Reflect your changes in docs
3. **Add tests**: New features need test coverage
4. **Follow conventions**: Use conventional commit messages
5. **Request review**: Wait for maintainer review

### Pull Request Checklist
- [ ] Code follows project style guidelines
- [ ] Tests added and passing
- [ ] Documentation updated
- [ ] Pre-commit hooks pass
- [ ] CI/CD pipeline passes
- [ ] No merge conflicts
- [ ] Commit messages follow conventions

## 🏗️ Project Structure

```
ai_app/
├── .github/
│   └── workflows/         # CI/CD pipeline definitions
├── tests/                 # Test files
├── uploads/              # User uploaded files (gitignored)
├── temp/                 # Temporary files (gitignored)
├── app.py                # Main Streamlit application
├── file_handler.py       # File operations
├── llm_handler.py        # LLM integration
├── verify_env.py         # Environment validation
├── setup.sh              # Automated setup script
├── Makefile              # Task automation
├── requirements.txt      # Production dependencies
├── requirements-dev.txt  # Development dependencies
└── .pre-commit-config.yaml  # Pre-commit hooks
```

## 🤝 Code Review Process

### For Contributors
- Respond to review comments promptly
- Make requested changes in new commits
- Ask questions if feedback is unclear
- Be patient and respectful

### For Reviewers
- Be constructive and specific
- Explain the reasoning behind suggestions
- Approve when changes meet standards
- Test the changes locally when possible

## 🐛 Bug Reports

When reporting bugs, include:
- Python version
- Operating system
- Steps to reproduce
- Expected behavior
- Actual behavior
- Error messages/logs
- Screenshots (if applicable)

## 💡 Feature Requests

For feature requests, describe:
- The problem you're trying to solve
- Your proposed solution
- Alternative solutions considered
- Why this feature benefits users

## 📚 Resources

- [Python Style Guide (PEP 8)](https://pep8.org/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [GitHub Flow](https://guides.github.com/introduction/flow/)
- [Streamlit Documentation](https://docs.streamlit.io/)

## 🎯 Quick Reference

### Common Commands
```bash
make help          # Show all commands
make setup         # Setup environment
make test          # Run tests
make lint          # Run linting
make format        # Format code
make run           # Run application
make clean         # Clean temporary files
```

### Debugging
```bash
# Run with verbose logging
streamlit run app.py --logger.level=debug

# Check environment
python verify_env.py

# Test Docker build
make docker-build
```

## ❓ Questions?

If you have questions:
1. Check existing issues and discussions
2. Review documentation
3. Ask in pull request comments
4. Contact maintainers

---

Thank you for contributing to AI Learning Assistant! 🎉
