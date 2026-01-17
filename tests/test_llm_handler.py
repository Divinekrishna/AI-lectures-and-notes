"""
Tests for LLMHandler class
"""
import os
import pytest
from unittest.mock import Mock, patch
from llm_handler import LLMHandler


class TestLLMHandler:
    """Test cases for LLMHandler class."""

    def test_init_without_api_key(self):
        """Test that LLMHandler raises error without API key."""
        with patch.dict(os.environ, {}, clear=True):
            with pytest.raises(ValueError, match="OPENAI_API_KEY not found"):
                LLMHandler()

    @patch.dict(os.environ, {"OPENAI_API_KEY": "test-key-123"})
    @patch('llm_handler.OpenAI')
    def test_init_with_api_key(self, mock_openai):
        """Test that LLMHandler initializes with API key."""
        handler = LLMHandler()
        assert handler.api_key == "test-key-123"
        mock_openai.assert_called_once_with(api_key="test-key-123")

    @patch.dict(os.environ, {"OPENAI_API_KEY": "test-key-123"})
    @patch('llm_handler.OpenAI')
    def test_chat_success(self, mock_openai):
        """Test successful chat completion."""
        # Mock the OpenAI client response
        mock_client = Mock()
        mock_response = Mock()
        mock_response.choices = [Mock(message=Mock(content="Test response"))]
        mock_client.chat.completions.create.return_value = mock_response
        mock_openai.return_value = mock_client

        handler = LLMHandler()
        messages = [{"role": "user", "content": "Hello"}]
        response = handler.chat(messages)

        assert response == "Test response"
        mock_client.chat.completions.create.assert_called_once()

    @patch.dict(os.environ, {"OPENAI_API_KEY": "test-key-123"})
    @patch('llm_handler.OpenAI')
    def test_generate_text(self, mock_openai):
        """Test text generation."""
        mock_client = Mock()
        mock_response = Mock()
        mock_response.choices = [Mock(message=Mock(content="Generated text"))]
        mock_client.chat.completions.create.return_value = mock_response
        mock_openai.return_value = mock_client

        handler = LLMHandler()
        result = handler.generate_text("Generate something")

        assert result == "Generated text"

    @patch.dict(os.environ, {"OPENAI_API_KEY": "test-key-123"})
    @patch('llm_handler.OpenAI')
    def test_summarize(self, mock_openai):
        """Test text summarization."""
        mock_client = Mock()
        mock_response = Mock()
        mock_response.choices = [Mock(message=Mock(content="Summary text"))]
        mock_client.chat.completions.create.return_value = mock_response
        mock_openai.return_value = mock_client

        handler = LLMHandler()
        result = handler.summarize("Long text to summarize")

        assert result == "Summary text"

    @patch.dict(os.environ, {"OPENAI_API_KEY": "test-key-123"})
    @patch('llm_handler.OpenAI')
    def test_translate(self, mock_openai):
        """Test text translation."""
        mock_client = Mock()
        mock_response = Mock()
        mock_response.choices = [Mock(message=Mock(content="Texto traducido"))]
        mock_client.chat.completions.create.return_value = mock_response
        mock_openai.return_value = mock_client

        handler = LLMHandler()
        result = handler.translate("Hello", "Spanish")

        assert result == "Texto traducido"
