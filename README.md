# AI Learning Assistant Project

[![CI/CD Pipeline](https://github.com/Divinekrishna/AI-lectures-and-notes/workflows/CI%2FCD%20Pipeline/badge.svg)](https://github.com/Divinekrishna/AI-lectures-and-notes/actions)

## Overview
An AI-powered learning application built with Streamlit that allows users to:
- Upload and manage learning resources (PDFs, documents, lectures)
- Process lectures with AI-generated summaries and translations
- Chat with an intelligent assistant about uploaded resources
- Find relevant learning materials based on queries

## 🚀 Automation Features

This project includes comprehensive automation to streamline development and deployment:

### ✅ Automated Setup
- **One-command setup**: `./setup.sh` or `make setup`
- **Environment verification**: Automatic validation of dependencies and configuration
- **Directory initialization**: Auto-creation of required folders

### 🔄 CI/CD Pipeline
- **Automated testing**: Tests run on every push and pull request
- **Code quality checks**: Linting and formatting validation
- **Security scanning**: Dependency vulnerability detection
- **Docker builds**: Automated container image creation

### 🛠️ Development Tools
- **Makefile**: Common tasks automated (test, lint, format, run)
- **Pre-commit hooks**: Code quality checks before every commit
- **Dependency management**: Weekly automated security scans
- **Testing framework**: Comprehensive test suite with coverage reports

## Features
- 🎙️ **Lecture Processing**: Extract text, generate summaries, translate content
- 💬 **AI Chatbot**: Ask questions about your resources using OpenAI LLM
- 📤 **Resource Upload**: Support for PDF, TXT, DOCX, MP3, WAV, MP4 files
- 🌍 **Multi-language Support**: Process content in multiple languages
- 🔍 **Resource Discovery**: Find relevant materials based on search queries
- 🐳 **Docker Support**: Easy deployment with Docker and Docker Compose

## Project Structure
```
ai_app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker configuration
├── docker-compose.yml    # Docker Compose configuration
├── .env.example          # Environment variables template
├── .gitignore            # Git ignore rules
├── README.md             # This file
├── src/
│   └── utils/
│       ├── file_handler.py    # File upload and processing
│       └── llm_handler.py      # OpenAI LLM integration
├── uploads/              # User uploaded resources
└── temp/                 # Temporary files directory
```

## Installation

### Prerequisites
- Python 3.11+
- Docker (optional, for containerized deployment)
- OpenAI API Key

### Quick Setup (Automated)

The easiest way to set up the project is using the automated setup script:

```bash
# Clone the repository (if not already done)
git clone <repository-url>
cd ai_app

# Run automated setup
./setup.sh
```

Or use the Makefile:

```bash
make setup
```

This will automatically:
- Install all Python dependencies
- Create necessary directories
- Set up your .env file
- Verify the environment

### Manual Setup

If you prefer manual setup:

1. **Clone or navigate to project directory**
   ```bash
   cd ai_app
   ```

2. **Create environment file**
   ```bash
   cp .env.example .env
   ```

3. **Add your OpenAI API key to .env**
   ```
   OPENAI_API_KEY=your_key_here
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Create required directories**
   ```bash
   mkdir -p uploads temp
   ```

6. **Verify setup**
   ```bash
   python verify_env.py
   ```

7. **Run the application**
   ```bash
   streamlit run app.py
   # Or use: make run
   ```

   The app will be available at `http://localhost:8501`

## Docker Deployment

### Using Docker Compose (Recommended)

1. **Set your API key in .env**
   ```bash
   echo "OPENAI_API_KEY=your_key_here" > .env
   ```

2. **Start the application**
   ```bash
   docker-compose up --build
   ```

3. **Access the application**
   - Open your browser to `http://localhost:8501`

### Using Docker directly

1. **Build the image**
   ```bash
   docker build -t ai-learning-assistant .
   ```

2. **Run the container**
   ```bash
   docker run -p 8501:8501 \
     -e OPENAI_API_KEY=your_key_here \
     -v $(pwd)/uploads:/app/uploads \
     ai-learning-assistant
   ```

## Usage

### 1. Upload Resources
- Navigate to "📤 Upload Resources" page
- Upload files (PDF, TXT, DOCX, MP3, WAV, MP4)
- Files are stored in the `uploads` directory

### 2. Process Lectures
- Go to "🎙️ Lecture Processing" page
- Select a resource to extract and summarize
- Translate content to different languages

### 3. Chat with Assistant
- Visit "💬 Chatbot" page
- Ask questions about your uploaded resources
- The AI will use context from your materials

### 4. Find Resources
- Use "🔍 Resource Finder" page
- Search for specific topics
- Get AI recommendations for relevant materials

## Configuration

### Environment Variables (.env)
```
OPENAI_API_KEY=your_api_key        # Required: OpenAI API key
UPLOAD_FOLDER=uploads              # Folder for uploaded files
MAX_FILE_SIZE=52428800             # Maximum file size (50MB)
SUPPORTED_FORMATS=pdf,txt,docx,... # Supported file formats
DEFAULT_LANGUAGE=en                # Default language
SUPPORTED_LANGUAGES=en,es,fr,...   # Available languages
```

## API Integration

### OpenAI Integration
The application uses OpenAI's GPT models for:
- Text summarization
- Content translation
- Question answering
- Resource recommendation
- Chat responses

### Supported Models
- `gpt-3.5-turbo` (default, fast and cost-effective)
- `gpt-4` (more advanced, use if available)

## Supported File Formats
- **Documents**: PDF, TXT, DOCX
- **Audio**: MP3, WAV
- **Video**: MP4

## Requirements
- Python 3.11+
- streamlit >= 1.28.1
- openai >= 1.3.0
- langchain >= 0.0.354
- pydub >= 0.25.1
- PyPDF2 >= 3.0.1
- python-dotenv >= 1.0.0

## Troubleshooting

### "OPENAI_API_KEY not found"
- Check your `.env` file exists
- Ensure `OPENAI_API_KEY` is set correctly
- The key should start with `sk-`

### Files not uploading
- Check max file size (default 50MB)
- Verify file format is supported
- Check disk space in uploads folder

### Streamlit app not loading
- Ensure port 8501 is available
- Check Python version is 3.11+
- Reinstall dependencies: `pip install -r requirements.txt --force-reinstall`

## Development

### Development Tools

The project includes comprehensive automation tools:

#### Makefile Commands
```bash
make help          # Show all available commands
make install       # Install dependencies
make setup         # Complete project setup
make verify        # Verify environment
make test          # Run tests
make lint          # Run code linting
make format        # Format code
make clean         # Clean temporary files
make run           # Run the application
make docker-build  # Build Docker image
make docker-run    # Run in Docker
```

#### Pre-commit Hooks

Install pre-commit hooks to automatically check code quality:

```bash
pip install pre-commit
pre-commit install
```

This will run checks on every commit:
- Code formatting (Black)
- Linting (Flake8)
- Security checks (Bandit)
- Import sorting (isort)
- File consistency checks

### Running Tests

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run all tests
make test

# Or use pytest directly
pytest tests/ -v
```

### CI/CD Pipeline

The project includes automated GitHub Actions workflows:

- **CI Pipeline** (`.github/workflows/ci.yml`)
  - Code quality checks (linting, formatting)
  - Automated testing
  - Security scanning
  - Docker image building

- **Dependency Updates** (`.github/workflows/dependency-update.yml`)
  - Weekly dependency security scans
  - Automated vulnerability reporting
  - Outdated package detection

### Adding New Features
1. Create new utility modules in `src/utils/`
2. Add new pages in `app.py` using Streamlit columns/tabs
3. Update requirements.txt with new dependencies
4. Add tests in `tests/` directory
5. Run `make lint` and `make test` before committing
6. Commit changes (pre-commit hooks will run automatically)

## Performance Tips
- Upload files < 10MB for faster processing
- Use `gpt-3.5-turbo` for cost-effective operations
- Clean up old uploads regularly using file handler cleanup method
- Monitor OpenAI API usage for cost control

## Security Considerations
- Never commit `.env` file with API keys to version control
- Use `.gitignore` to prevent accidental exposure
- Rotate API keys regularly
- For production, use secret management tools

## Future Enhancements
- 🎤 Add voice input capability
- 🔊 Text-to-speech functionality
- 📊 Data visualization and analytics
- 🎯 Fine-tuned models for domain-specific tasks
- 👥 User authentication and multi-user support
- 💾 Database integration for persistent storage
- 🚀 Performance optimization with caching

## License
[Add your license here]

## Support
For issues or questions, please [add support contact information]

## Changelog

### v1.0 (2024)
- Initial release
- Basic file upload and processing
- LLM chatbot integration
- Multi-language support
- Docker containerization
