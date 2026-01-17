"""
Tests for FileHandler class
"""
import os
import tempfile
from pathlib import Path
import pytest
from file_handler import FileHandler


class TestFileHandler:
    """Test cases for FileHandler class."""

    @pytest.fixture
    def file_handler(self):
        """Create a FileHandler instance with a temporary directory."""
        with tempfile.TemporaryDirectory() as temp_dir:
            handler = FileHandler(upload_folder=temp_dir)
            yield handler

    @pytest.fixture
    def sample_text_file(self):
        """Create a sample text file."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            f.write("This is a test file.\nWith multiple lines.\n")
            temp_path = f.name
        yield temp_path
        # Cleanup
        if os.path.exists(temp_path):
            os.remove(temp_path)

    def test_is_supported_format_valid(self, file_handler):
        """Test that supported formats are recognized."""
        assert file_handler.is_supported_format("document.pdf") is True
        assert file_handler.is_supported_format("text.txt") is True
        assert file_handler.is_supported_format("doc.docx") is True
        assert file_handler.is_supported_format("audio.mp3") is True
        assert file_handler.is_supported_format("video.mp4") is True

    def test_is_supported_format_invalid(self, file_handler):
        """Test that unsupported formats are rejected."""
        assert file_handler.is_supported_format("image.jpg") is False
        assert file_handler.is_supported_format("archive.zip") is False
        assert file_handler.is_supported_format("executable.exe") is False

    def test_extract_text_from_file_txt(self, file_handler, sample_text_file):
        """Test text extraction from a .txt file."""
        text = file_handler.extract_text_from_file(sample_text_file)
        assert "This is a test file" in text
        assert len(text) > 0

    def test_get_file_size_mb(self, file_handler, sample_text_file):
        """Test file size calculation."""
        size = file_handler.get_file_size_mb(sample_text_file)
        assert size > 0
        assert size < 1  # Should be less than 1 MB for a small test file

    def test_upload_folder_creation(self):
        """Test that upload folder is created if it doesn't exist."""
        with tempfile.TemporaryDirectory() as temp_dir:
            upload_path = os.path.join(temp_dir, "new_uploads")
            handler = FileHandler(upload_folder=upload_path)
            assert os.path.exists(upload_path)
