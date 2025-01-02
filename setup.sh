#!/bin/bash

# Update package list
apt-get update

# Install Tesseract OCR and dependencies
apt-get install -y tesseract-ocr libtesseract-dev

# Verify Tesseract installation
if ! command -v tesseract &> /dev/null; then
    echo "Tesseract installation failed. Please check."
    exit 1
else
    echo "Tesseract installed successfully at $(command -v tesseract)."
fi
