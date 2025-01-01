#!/bin/bash

# Update package list
apt-get update

# Install Tesseract OCR and its dependencies
apt-get install -y tesseract-ocr libtesseract-dev

# Check Tesseract installation
if command -v tesseract &> /dev/null; then
    echo "Tesseract installed successfully."
else
    echo "Tesseract installation failed."
    exit 1
fi
