#!/usr/bin/env python3
"""
Environment verification script.
Validates that all required environment variables and dependencies are properly configured.
"""
import os
import sys
from pathlib import Path

def check_env_variable(var_name, required=True):
    """Check if an environment variable is set."""
    value = os.getenv(var_name)
    if value:
        # Don't print the actual key value for security
        if 'KEY' in var_name or 'SECRET' in var_name or 'TOKEN' in var_name:
            print(f"✓ {var_name} is set")
        else:
            print(f"✓ {var_name}={value}")
        return True
    else:
        if required:
            print(f"✗ {var_name} is NOT set (required)")
            return False
        else:
            print(f"⚠ {var_name} is NOT set (optional)")
            return True

def check_directory(dir_path):
    """Check if a directory exists."""
    if Path(dir_path).exists():
        print(f"✓ Directory {dir_path} exists")
        return True
    else:
        print(f"✗ Directory {dir_path} does NOT exist")
        return False

def check_file(file_path):
    """Check if a file exists."""
    if Path(file_path).exists():
        print(f"✓ File {file_path} exists")
        return True
    else:
        print(f"✗ File {file_path} does NOT exist")
        return False

def main():
    """Main verification function."""
    print("=" * 60)
    print("Environment Verification")
    print("=" * 60)
    
    all_checks_passed = True
    
    # Check required environment variables
    print("\n📋 Checking Environment Variables:")
    all_checks_passed &= check_env_variable('OPENAI_API_KEY', required=True)
    check_env_variable('UPLOAD_FOLDER', required=False)
    check_env_variable('MAX_FILE_SIZE', required=False)
    check_env_variable('DEFAULT_LANGUAGE', required=False)
    
    # Check required directories
    print("\n📁 Checking Directories:")
    upload_folder = os.getenv('UPLOAD_FOLDER', 'uploads')
    check_directory(upload_folder)
    check_directory('temp')
    
    # Check required files
    print("\n📄 Checking Files:")
    all_checks_passed &= check_file('.env')
    check_file('requirements.txt')
    check_file('app.py')
    
    # Check Python dependencies
    print("\n📦 Checking Python Dependencies:")
    try:
        import streamlit
        print(f"✓ streamlit {streamlit.__version__}")
    except ImportError:
        print("✗ streamlit is NOT installed")
        all_checks_passed = False
    
    try:
        import openai
        print(f"✓ openai {openai.__version__}")
    except ImportError:
        print("✗ openai is NOT installed")
        all_checks_passed = False
    
    try:
        import PyPDF2
        print(f"✓ PyPDF2 installed")
    except ImportError:
        print("✗ PyPDF2 is NOT installed")
        all_checks_passed = False
    
    # Summary
    print("\n" + "=" * 60)
    if all_checks_passed:
        print("✅ All checks passed! Environment is ready.")
        return 0
    else:
        print("❌ Some checks failed. Please fix the issues above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
