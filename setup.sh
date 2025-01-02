#!/bin/bash

# Update the package list
apt-get update

# Install Tesseract OCR and dependencies
apt-get install -y tesseract-ocr libtesseract-dev

# Verify Tesseract installation
echo "Checking Tesseract installation..."
command -v tesseract || { echo "Tesseract installation failed."; exit 1; }

# Print Tesseract version and confirm path
tesseract --version
