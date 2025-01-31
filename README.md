# DocFlow - Automated Document Organization

## Features
- Automatic file categorization
- OCR and text extraction
- Configurable rules engine
- File renaming and organization

## Quick Start
```bash
# Install dependencies
sudo apt-get install tesseract-ocr poppler-utils
pip install docflow

# Run with default config
docflow --daemon
```

## Customization
Edit `config.yaml` to add custom rules:
```yaml
categories:
  Marketing:
    keywords: ["campaign", "brief", "creative"]
```
