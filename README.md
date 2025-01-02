# 🦙 Llama OCR 2.0

Llama OCR 2.0 is a powerful Optical Character Recognition (OCR) application built with Streamlit and Tesseract. It allows you to extract text from images with ease and accuracy.

---

## Features
- **Upload Images**: Supports PNG, JPG, and JPEG formats.
- **Image Preprocessing**: Automatically enhances images for better OCR results.
- **Dynamic Tesseract Detection**: Automatically detects the Tesseract OCR installation path.

---

## Installation and Setup

### Prerequisites
1. **Tesseract OCR** must be installed on your system.
   - For Linux: `apt-get install tesseract-ocr`
   - For macOS: `brew install tesseract`
   - For Windows: [Download and install Tesseract OCR](https://github.com/tesseract-ocr/tesseract).

2. Python 3.8+ with the following libraries:
   - `streamlit`
   - `pytesseract`
   - `Pillow`

### Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/llama-ocr-2.0.git
   cd llama-ocr-2.0
