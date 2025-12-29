import os
import PyPDF2
from pathlib import Path
from typing import Optional, List

class FileHandler:
    """Handle file operations for uploaded resources."""
    
    SUPPORTED_FORMATS = {
        'pdf': 'application/pdf',
        'txt': 'text/plain',
        'docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        'mp3': 'audio/mpeg',
        'wav': 'audio/wav',
        'mp4': 'video/mp4'
    }
    
    def __init__(self, upload_folder: str = 'uploads'):
        self.upload_folder = upload_folder
        Path(upload_folder).mkdir(exist_ok=True)
    
    def save_uploaded_file(self, uploaded_file, subfolder: str = '') -> Optional[str]:
        """Save uploaded file to disk and return file path."""
        try:
            subfolder_path = os.path.join(self.upload_folder, subfolder) if subfolder else self.upload_folder
            Path(subfolder_path).mkdir(parents=True, exist_ok=True)
            
            file_path = os.path.join(subfolder_path, uploaded_file.name)
            with open(file_path, 'wb') as f:
                f.write(uploaded_file.getbuffer())
            return file_path
        except Exception as e:
            print(f"Error saving file: {e}")
            return None
    
    def extract_text_from_pdf(self, pdf_path: str) -> str:
        """Extract text from PDF file."""
        try:
            text = ""
            with open(pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                for page in pdf_reader.pages:
                    text += page.extract_text()
            return text
        except Exception as e:
            print(f"Error extracting text from PDF: {e}")
            return ""
    
    def extract_text_from_file(self, file_path: str) -> str:
        """Extract text from supported file formats."""
        file_ext = Path(file_path).suffix.lower().strip('.')
        
        if file_ext == 'pdf':
            return self.extract_text_from_pdf(file_path)
        elif file_ext == 'txt':
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    return f.read()
            except Exception as e:
                print(f"Error reading text file: {e}")
                return ""
        else:
            return ""
    
    def is_supported_format(self, filename: str) -> bool:
        """Check if file format is supported."""
        ext = Path(filename).suffix.lower().strip('.')
        return ext in self.SUPPORTED_FORMATS
    
    def get_file_size_mb(self, file_path: str) -> float:
        """Get file size in MB."""
        return os.path.getsize(file_path) / (1024 * 1024)
    
    def cleanup_old_files(self, folder: str, max_age_hours: int = 24):
        """Remove files older than specified hours."""
        import time
        current_time = time.time()
        for file in Path(folder).glob('*'):
            if file.is_file():
                file_age = (current_time - file.stat().st_mtime) / 3600
                if file_age > max_age_hours:
                    file.unlink()
