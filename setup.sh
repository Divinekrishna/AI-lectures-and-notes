#!/bin/bash
# Setup script for AI Learning Assistant
# This script automates the initial setup process

set -e

echo "================================================"
echo "AI Learning Assistant - Setup Script"
echo "================================================"
echo ""

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check Python version
echo "🔍 Checking Python version..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
    echo -e "${GREEN}✓ Python $PYTHON_VERSION found${NC}"
else
    echo -e "${RED}✗ Python 3 is not installed${NC}"
    echo "Please install Python 3.11 or higher"
    exit 1
fi

# Check if pip is available
echo ""
echo "🔍 Checking pip..."
if command -v pip3 &> /dev/null; then
    echo -e "${GREEN}✓ pip is available${NC}"
else
    echo -e "${RED}✗ pip is not available${NC}"
    exit 1
fi

# Create virtual environment (optional but recommended)
echo ""
read -p "Do you want to create a virtual environment? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "🔧 Creating virtual environment..."
    python3 -m venv venv
    echo -e "${GREEN}✓ Virtual environment created${NC}"
    echo -e "${YELLOW}⚠️  To activate it, run: source venv/bin/activate${NC}"
    
    # Activate virtual environment
    source venv/bin/activate
fi

# Install dependencies
echo ""
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt
echo -e "${GREEN}✓ Dependencies installed${NC}"

# Create necessary directories
echo ""
echo "📁 Creating necessary directories..."
mkdir -p uploads
mkdir -p temp
echo -e "${GREEN}✓ Directories created${NC}"

# Setup .env file
echo ""
if [ ! -f .env ]; then
    echo "📄 Creating .env file from template..."
    cp .env.example .env
    echo -e "${GREEN}✓ .env file created${NC}"
    echo -e "${YELLOW}⚠️  Please edit .env and add your OPENAI_API_KEY${NC}"
    
    read -p "Do you want to enter your OpenAI API key now? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        read -p "Enter your OpenAI API key: " api_key
        if [ ! -z "$api_key" ]; then
            sed -i.bak "s/your_openai_api_key_here/$api_key/" .env
            rm .env.bak 2>/dev/null || true
            echo -e "${GREEN}✓ API key saved to .env${NC}"
        fi
    fi
else
    echo -e "${YELLOW}⚠️  .env file already exists, skipping${NC}"
fi

# Verify environment
echo ""
echo "🔍 Verifying environment setup..."
python3 verify_env.py

# Summary
echo ""
echo "================================================"
echo -e "${GREEN}✅ Setup Complete!${NC}"
echo "================================================"
echo ""
echo "Next steps:"
echo "1. Make sure your OPENAI_API_KEY is set in .env"
echo "2. Run the application with: streamlit run app.py"
echo "   Or use: make run"
echo ""
echo "For more commands, run: make help"
echo ""
