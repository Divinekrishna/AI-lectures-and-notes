# AI Learning Assistant - Usage Guide

## Quick Start

### Prerequisites
```bash
# 1. Install Python 3.11+
# 2. Get OpenAI API key from https://platform.openai.com/api-keys
# 3. Create .env file with your API key
```

### Setup in 3 Steps

**Step 1**: Set up environment
```bash
cd ai_app
cp .env.example .env
# Edit .env and add your OpenAI API key
```

**Step 2**: Install dependencies
```bash
pip install -r requirements.txt
```

**Step 3**: Run the app
```bash
streamlit run app.py
```

## Using Docker

**Step 1**: Build and run
```bash
docker-compose up --build
```

**Step 2**: Open browser
```
http://localhost:8501
```

## Feature Guide

### 📤 Upload Resources
- Click "Upload Resources" in sidebar
- Select files from your computer
- Supported: PDF, TXT, DOCX, MP3, WAV, MP4
- Max file size: 50MB per file

### 🎙️ Lecture Processing
- Select uploaded resource
- Extract text from documents
- Generate AI summaries (requires OpenAI)
- Translate to different languages

### 💬 Chatbot
- Ask questions about your resources
- AI uses context from uploaded materials
- Chat history is maintained in session
- Available 24/7

### 🔍 Resource Finder
- Search for topics across materials
- Get AI recommendations
- Discover related content

## API Keys

### Getting OpenAI API Key
1. Visit https://platform.openai.com/signup
2. Create account and verify email
3. Go to API keys page
4. Create new secret key
5. Copy to `.env` file

### Cost Estimation
- `gpt-3.5-turbo`: ~$0.0005 per 1K tokens
- `gpt-4`: ~$0.03 per 1K tokens
- Monitor usage at https://platform.openai.com/account/billing/overview

## Troubleshooting

### Application won't start
```bash
# Check Python version
python --version  # Should be 3.11+

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall

# Clear cache
streamlit cache clear
streamlit run app.py
```

### File upload not working
- Check file format (PDF, TXT, DOCX, MP3, WAV, MP4)
- Verify file size < 50MB
- Check disk space in uploads folder

### LLM not responding
- Verify API key in .env file
- Check account has credits at openai.com
- Check internet connection
- View Streamlit terminal for error messages

### Docker issues
```bash
# Check Docker is running
docker ps

# View logs
docker-compose logs

# Rebuild from scratch
docker-compose down
docker-compose up --build
```

## Tips & Tricks

1. **Faster Processing**: Use smaller files for quicker results
2. **Better Summaries**: Upload structured documents (PDFs, not images)
3. **Cost Control**: Use `gpt-3.5-turbo` for basic tasks, `gpt-4` for complex analysis
4. **Batch Processing**: Upload multiple resources, then process in bulk
5. **Export Results**: Copy-paste chatbot responses for external use

## Keyboard Shortcuts
- Ctrl+C: Stop Streamlit app
- Ctrl+R: Refresh Streamlit page
- F5: Full page refresh

## Performance

| Operation | Time | Cost |
|-----------|------|------|
| Extract text (PDF) | < 1s | Free |
| Generate summary | 5-10s | ~$0.01 |
| Translate text | 3-5s | ~$0.01 |
| Chat response | 2-5s | ~$0.005 |

## Next Steps
- Customize app appearance (see app.py CSS section)
- Add more file format support
- Integrate with other AI models
- Deploy to cloud (Heroku, AWS, GCP)
