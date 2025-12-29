# 🔄 How to Change LLM Provider

This guide shows you how to switch API keys or use different LLM providers.

## 📝 Quick Reference

| Provider | Setup Time | Cost | Best For |
|----------|------------|------|----------|
| **OpenAI** (GPT-3.5/4) | 2 min | Pay-per-use | General purpose, reliable |
| **Anthropic** (Claude) | 2 min | Pay-per-use | Long context, reasoning |
| **Google** (Gemini) | 2 min | Free tier + paid | Multimodal, free testing |
| **Local** (Ollama) | 10 min | Free | Privacy, no internet needed |

---

## 🔑 Change OpenAI API Key

**Option 1: Edit .env file**
```powershell
cd c:\Users\losha\Project\ai_app
notepad .env
```

Update the line:
```
OPENAI_API_KEY=sk-your-new-key-here
```

**Option 2: One-line command**
```powershell
cd c:\Users\losha\Project\ai_app
Set-Content .\.env -Value (Get-Content .\.env | ForEach-Object { $_ -replace 'OPENAI_API_KEY=.*', 'OPENAI_API_KEY=sk-your-new-key' })
```

Restart the app - done!

---

## 🤖 Switch to Different OpenAI Model

In `.env`, change the model:

```env
OPENAI_MODEL=gpt-4
```

**Available models:**
- `gpt-3.5-turbo` - Fast, cheap ($0.0005/1K tokens) ✅ Default
- `gpt-4` - Smarter ($0.03/1K tokens)
- `gpt-4-turbo-preview` - Faster GPT-4
- `gpt-4o` - Newest, multimodal

---

## 🌐 Switch to Anthropic (Claude)

### 1. Get Anthropic API Key
- Sign up: https://console.anthropic.com/
- Generate key: https://console.anthropic.com/settings/keys

### 2. Install package
```powershell
c:/Users/losha/Project/.venv/Scripts/python.exe -m pip install anthropic
```

### 3. Update .env
```env
LLM_PROVIDER=anthropic
ANTHROPIC_API_KEY=sk-ant-your-key-here
ANTHROPIC_MODEL=claude-3-sonnet-20240229
```

**Models:**
- `claude-3-haiku-20240307` - Fastest, cheapest
- `claude-3-sonnet-20240229` - Balanced ✅ Recommended
- `claude-3-opus-20240229` - Most capable

### 4. Use new handler
```powershell
# Replace the handler file
Copy-Item src/utils/llm_handler_multi.py src/utils/llm_handler.py -Force
```

Restart app!

---

## 🔍 Switch to Google (Gemini)

### 1. Get Google API Key
- Sign up: https://makersuite.google.com/app/apikey
- Free tier: 60 requests/minute

### 2. Install package
```powershell
c:/Users/losha/Project/.venv/Scripts/python.exe -m pip install google-generativeai
```

### 3. Update .env
```env
LLM_PROVIDER=google
GOOGLE_API_KEY=your-google-key-here
GOOGLE_MODEL=gemini-pro
```

**Models:**
- `gemini-pro` - Text only ✅ Recommended
- `gemini-pro-vision` - Multimodal (images)

### 4. Use new handler
```powershell
Copy-Item src/utils/llm_handler_multi.py src/utils/llm_handler.py -Force
```

---

## 💻 Use Local LLM (Ollama)

Run models locally - no API key needed!

### 1. Install Ollama
- Download: https://ollama.ai/download
- Install and start Ollama app

### 2. Download a model
```powershell
ollama pull llama2
# or: ollama pull mistral, codellama, etc.
```

### 3. Update .env
```env
LLM_PROVIDER=local
LOCAL_MODEL_URL=http://localhost:11434
LOCAL_MODEL_NAME=llama2
```

### 4. Use new handler
```powershell
Copy-Item src/utils/llm_handler_multi.py src/utils/llm_handler.py -Force
```

**Popular models:**
- `llama2` - Meta's LLaMA 2
- `mistral` - Fast, efficient
- `codellama` - Code generation
- `gemma` - Google's open model

---

## 🔄 Easy Provider Switch

I've created a multi-provider handler. To activate:

```powershell
cd c:\Users\losha\Project\ai_app
Copy-Item src/utils/llm_handler_multi.py src/utils/llm_handler.py -Force
```

Then just change `LLM_PROVIDER` in `.env`:
- `openai` - GPT models (default)
- `anthropic` - Claude models
- `google` - Gemini models
- `local` - Ollama/local models

---

## 🧪 Test Configuration

After changing provider:

```powershell
cd c:\Users\losha\Project\ai_app
c:/Users/losha/Project/.venv/Scripts/python.exe test_api.py
```

Should show: ✅ API call successful!

---

## 💡 Tips

**Cost Comparison (per 1M tokens):**
- OpenAI GPT-3.5: $0.50
- OpenAI GPT-4: $30
- Anthropic Claude Haiku: $0.25
- Google Gemini: Free (rate limited)
- Local: $0 (one-time hardware cost)

**When to use what:**
- **Quick chats** → GPT-3.5 or Gemini
- **Long documents** → Claude (200K context)
- **No internet** → Local Ollama
- **Best quality** → GPT-4 or Claude Opus

---

## 🆘 Troubleshooting

**Provider not working?**
```powershell
# Check which provider is active
c:/Users/losha/Project/.venv/Scripts/python.exe -c "import os; from dotenv import load_dotenv; load_dotenv(); print('Provider:', os.getenv('LLM_PROVIDER', 'openai'))"
```

**Missing package?**
```powershell
# Install all provider packages
c:/Users/losha/Project/.venv/Scripts/python.exe -m pip install openai anthropic google-generativeai
```

**API key not loading?**
- Check `.env` file exists
- No spaces around `=` sign
- API key in quotes if it contains special characters
- Restart the app after changes

---

Want me to set up a specific provider now? Just tell me which one!
