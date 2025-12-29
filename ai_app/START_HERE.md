# 🚀 AI Learning Assistant - Quick Start Guide

## ✅ Setup Complete!

Your project is fully configured and ready to run.

## 📁 Project Structure

```
ai_app/
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies (installed ✅)
├── .env                        # API key configured ✅
├── src/
│   └── utils/
│       ├── file_handler.py     # File operations
│       └── llm_handler.py      # OpenAI LLM integration
├── uploads/                    # User uploaded resources
└── temp/                       # Temporary files
```

## 🎯 How to Run

### Option 1: Run Locally (Recommended for Development)

```powershell
# Navigate to project
cd c:\Users\losha\Project\ai_app

# Activate virtual environment
& c:/Users/losha/Project/.venv/Scripts/Activate.ps1

# Run Streamlit app
c:/Users/losha/Project/.venv/Scripts/python.exe -m streamlit run app.py
```

The app will open automatically at: **http://localhost:8501**

### Option 2: Run with Docker

```powershell
cd c:\Users\losha\Project\ai_app

# Build and run
docker-compose up --build

# Access at http://localhost:8501
```

## 🎨 Features Available

### 🏠 Home
- Overview of all features
- Getting started guide

### 📤 Upload Resources
- Upload PDFs, documents, audio, video
- Supported formats: PDF, TXT, DOCX, MP3, WAV, MP4
- Max file size: 50MB

### 🎙️ Lecture Processing
- Extract text from PDFs
- Generate AI summaries
- Translate to multiple languages

### 💬 Chatbot
- Ask questions about your resources
- AI-powered responses using OpenAI
- Context-aware answers from uploaded materials

### 🔍 Resource Finder
- Search across all materials
- AI recommendations
- Find relevant resources

## 🔑 API Key Status

✅ OpenAI API Key configured in `.env`

## 🛠️ Troubleshooting

### App won't start
```powershell
# Reinstall dependencies
c:/Users/losha/Project/.venv/Scripts/python.exe -m pip install -r requirements.txt --force-reinstall

# Clear Streamlit cache
c:/Users/losha/Project/.venv/Scripts/python.exe -m streamlit cache clear
```

### Import errors
```powershell
# Verify virtual environment is activated
& c:/Users/losha/Project/.venv/Scripts/Activate.ps1

# Check installed packages
c:/Users/losha/Project/.venv/Scripts/python.exe -m pip list
```

### API key issues
- Check `.env` file has `OPENAI_API_KEY=sk-...`
- Verify key is valid at https://platform.openai.com/api-keys
- Check API usage/billing at https://platform.openai.com/account/billing

## 📊 Cost Monitoring

- GPT-3.5-turbo: ~$0.0005 per 1K tokens (default model)
- Monitor usage: https://platform.openai.com/account/billing/overview
- Set spending limits in OpenAI dashboard

## 🔒 Security Notes

- ⚠️ **Never commit `.env` to Git** (already in `.gitignore`)
- 🔑 Treat API keys as passwords
- 🔄 Rotate keys if exposed
- 🚫 Don't share keys in chat/email

## 🎓 Next Steps

1. **Start the app** using Option 1 above
2. **Upload a test PDF** in the Upload Resources page
3. **Try the chatbot** - ask questions about your materials
4. **Process a lecture** - extract and summarize content
5. **Find resources** - search across materials

## 📚 Documentation

- Full docs: `README.md`
- Quick guide: `QUICKSTART.md`
- Docker setup: `docker-compose.yml`

## 💡 Tips

- **Smaller files** = faster processing
- **Structured PDFs** work best (not scanned images)
- **Use GPT-3.5-turbo** for cost-effective operations
- **Clean up old uploads** regularly to save disk space

## 🆘 Need Help?

- Check error messages in terminal
- Review Streamlit logs
- Verify Python version: `python --version` (3.11+ recommended)
- Check virtual environment is active (you'll see `(.venv)` in prompt)

---

**Ready to start?** Run the command below:

```powershell
cd c:\Users\losha\Project\ai_app; & c:/Users/losha/Project/.venv/Scripts/Activate.ps1; c:/Users/losha/Project/.venv/Scripts/python.exe -m streamlit run app.py
```

This will:
1. Navigate to project
2. Activate virtual environment
3. Start Streamlit app
4. Open browser at http://localhost:8501

🎉 **Your AI Learning Assistant is ready!**
