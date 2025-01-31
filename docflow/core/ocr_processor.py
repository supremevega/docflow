from datetime import datetime
import pytesseract
from pdf2image import convert_from_path
from docx import Document
import logging

logger = logging.getLogger(__name__)

class OCRProcessor:
    def __init__(self, config):
        self.config = config
        
    def extract_text(self, file_path):
        try:
            if file_path.lower().endswith(('.png', '.jpg', '.jpeg')):
                return self._image_to_text(file_path)
            elif file_path.lower().endswith('.pdf'):
                return self._pdf_to_text(file_path)
            elif file_path.lower().endswith(('.doc', '.docx')):
                return self._docx_to_text(file_path)
        except Exception as e:
            logger.error(f"OCR failed for {file_path}: {str(e)}")
            return None

    def _image_to_text(self, path):
        return pytesseract.image_to_string(path)

    def _pdf_to_text(self, path):
        images = convert_from_path(path)
        text = '\n'.join(pytesseract.image_to_string(image) for image in images)
        return text

    def _docx_to_text(self, path):
        doc = Document(path)
        return '\n'.join([para.text for para in doc.paragraphs])
