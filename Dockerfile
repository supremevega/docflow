FROM python:3.9-slim
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*
COPY . /app
WORKDIR /app
RUN pip install .
CMD ["docflow", "--daemon"]
