#!/bin/bash

# Update package list
apt-get update

# Install Tesseract OCR
apt-get install -y tesseract-ocr libtesseract-dev

# Verify installation
if ! command -v tesseract &> /dev/null; then
    echo "Tesseract installation failed."
    exit 1
else
    echo "Tesseract installed successfully."
fi
