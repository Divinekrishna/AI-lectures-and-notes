"""
Test script to diagnose OpenAI API issues
"""
import os
import sys
from dotenv import load_dotenv

# Load environment
load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
print(f"API Key present: {bool(api_key)}")
print(f"Key starts with 'sk-': {str(api_key).startswith('sk-') if api_key else False}")
print(f"Key length: {len(api_key) if api_key else 0}")

# Test OpenAI import
try:
    from openai import OpenAI
    print("✅ OpenAI module imported successfully")
except ImportError as e:
    print(f"❌ Failed to import OpenAI: {e}")
    sys.exit(1)

# Test API connection
try:
    client = OpenAI(api_key=api_key)
    print("✅ OpenAI client created successfully")
    
    # Test simple API call
    print("\nTesting API call...")
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Say 'Hello' in one word."}],
        max_tokens=10
    )
    print(f"✅ API call successful!")
    print(f"Response: {response.choices[0].message.content}")
    
except Exception as e:
    print(f"❌ API Error: {type(e).__name__}")
    print(f"   Message: {str(e)}")
    
    # Check for common issues
    if "401" in str(e) or "Unauthorized" in str(e):
        print("\n🔍 Issue: Invalid API key")
        print("   - Check your key at https://platform.openai.com/api-keys")
        print("   - Ensure there are no extra spaces or quotes")
        print("   - Try generating a new key")
    elif "429" in str(e) or "rate_limit" in str(e):
        print("\n🔍 Issue: Rate limit or quota exceeded")
        print("   - Check your usage at https://platform.openai.com/account/billing")
        print("   - You may need to add payment method or wait")
    elif "timeout" in str(e).lower():
        print("\n🔍 Issue: Connection timeout")
        print("   - Check your internet connection")
        print("   - Try again in a moment")
    else:
        print("\n🔍 Unexpected error - see message above")
