FROM python:3.9-bullseye
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*
RUN pip install watchdog pytesseract python-docx PyYAML pdf2image
