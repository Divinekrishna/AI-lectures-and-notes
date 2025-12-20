#!/usr/bin/env python3
"""
Script to update .env.example from .env (excluding sensitive values)
Helps keep the template in sync with actual configuration
"""
import re
from pathlib import Path

def sanitize_value(key, value):
    """Replace actual values with placeholders for example file."""
    sensitive_keywords = ['KEY', 'SECRET', 'TOKEN', 'PASSWORD', 'CREDENTIAL']
    
    if any(keyword in key.upper() for keyword in sensitive_keywords):
        # Replace actual keys/secrets with placeholder
        return f"your_{key.lower()}_here"
    
    # Keep other values as they might be useful defaults
    return value

def update_env_example():
    """Update .env.example from .env file."""
    env_file = Path('.env')
    example_file = Path('.env.example')
    
    if not env_file.exists():
        print("❌ .env file not found")
        return 1
    
    print("📝 Updating .env.example from .env...")
    
    # Read .env file
    with open(env_file, 'r') as f:
        env_lines = f.readlines()
    
    # Process lines
    example_lines = []
    for line in env_lines:
        line = line.strip()
        
        # Skip empty lines and comments
        if not line or line.startswith('#'):
            example_lines.append(line + '\n')
            continue
        
        # Parse key=value
        if '=' in line:
            key, value = line.split('=', 1)
            sanitized_value = sanitize_value(key, value)
            example_lines.append(f"{key}={sanitized_value}\n")
        else:
            example_lines.append(line + '\n')
    
    # Write to .env.example
    with open(example_file, 'w') as f:
        f.writelines(example_lines)
    
    print(f"✅ Updated {example_file}")
    print(f"⚠️  Please review {example_file} to ensure no sensitive data was included")
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(update_env_example())
