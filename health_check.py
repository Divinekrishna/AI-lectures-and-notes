#!/usr/bin/env python3
"""
Health check script for AI Learning Assistant
Can be used for monitoring and automated health checks
"""
import sys
import os
from pathlib import Path

def check_health():
    """Perform basic health checks."""
    checks_passed = True
    
    # Check critical files exist
    critical_files = ['app.py', 'file_handler.py', 'llm_handler.py', '.env']
    for file in critical_files:
        if not Path(file).exists():
            print(f"❌ Critical file missing: {file}")
            checks_passed = False
    
    # Check directories exist
    critical_dirs = ['uploads', 'temp']
    for directory in critical_dirs:
        if not Path(directory).exists():
            print(f"❌ Critical directory missing: {directory}")
            checks_passed = False
    
    # Check API key is configured (but don't expose it)
    if not os.getenv('OPENAI_API_KEY'):
        print("❌ OPENAI_API_KEY not configured")
        checks_passed = False
    
    if checks_passed:
        print("✅ Health check passed")
        return 0
    else:
        print("❌ Health check failed")
        return 1

if __name__ == "__main__":
    sys.exit(check_health())
