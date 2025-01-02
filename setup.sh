#!/bin/bash

# Update package list
apt-get update

# Install Tesseract OCR and its dependencies
apt-get install -y tesseract-ocr libtesseract-dev

# Verify installation
echo "Checking Tesseract installation..."
command -v tesseract || { echo "Tesseract installation failed."; exit 1; }

# Print the Tesseract version for confirmation
tesseract --version
