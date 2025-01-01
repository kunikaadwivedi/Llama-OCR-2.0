import os
import streamlit as st
from PIL import Image, ImageOps
from pytesseract import pytesseract, image_to_string

# Ensure Tesseract path is correctly set
TESSERACT_PATH = "/usr/bin/tesseract"  # Default path for Linux environments

# Check if Tesseract is installed
if os.path.exists(TESSERACT_PATH):
    pytesseract.tesseract_cmd = TESSERACT_PATH
else:
    st.error("Tesseract is not installed or accessible in the expected path. Please check the setup.")

# Image preprocessing function
def preprocess_image(image):
    """Preprocess the image to improve OCR accuracy."""
    image = image.convert("L")  # Convert to grayscale
    image = ImageOps.autocontrast(image)  # Increase contrast
    image = image.resize((int(image.width * 1.5), int(image.height * 1.5)))  # Resize for better OCR
    image = image.point(lambda x: 0 if x < 140 else 255, '1')  # Apply binary threshold
    return image

# Postprocess OCR output
def clean_ocr_output(text):
    """Clean the OCR output by removing unnecessary lines and whitespace."""
    return '\n'.join([line.strip() for line in text.splitlines() if line.strip()])

# Page configuration
st.set_page_config(
    page_title="Llama OCR 2.0",
    page_icon="🦙",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title and description
st.markdown("<h1>🦙 Llama OCR 2.0</h1>", unsafe_allow_html=True)
st.markdown("<p>Upload an image to extract text with high accuracy. Supports PNG, JPG, and JPEG formats.</p>", unsafe_allow_html=True)
st.markdown("---")

# Sidebar for file upload
with st.sidebar:
    st.header("Upload Image")
    st.write("Supported formats: PNG, JPG, JPEG. Ensure the image is clear for best results.")
    uploaded_file = st.file_uploader("Choose an image file", type=['png', 'jpg', 'jpeg'])

# Main functionality
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Extract Text 🔍"):
        with st.spinner("Processing image..."):
            try:
                # Preprocess the image
                processed_image = preprocess_image(image)
                st.image(processed_image, caption="Processed Image", use_column_width=True)

                # Perform OCR
                ocr_result = image_to_string(processed_image, lang='eng', config='--psm 6')
                cleaned_result = clean_ocr_output(ocr_result)

                # Display OCR results
                if cleaned_result.strip():
                    st.markdown(
                        f"""<div style='background-color: #1E1E1E; padding: 20px; border-radius: 10px; border: 2px solid #64B5F6;'>
                        <h3 style='color: #2196F3;'>OCR Results:</h3>
                        <p style='color: #B0BEC5;'>{cleaned_result}</p>
                        </div>""",
                        unsafe_allow_html=True
                    )
                else:
                    st.warning("No text detected in the uploaded image. Please try with a clearer image.")

            except Exception as e:
                st.error(f"Error during OCR processing: {e}")
else:
    st.info("Please upload an image to start the OCR process.")

# Footer
st.markdown("<footer style='text-align: center; margin-top: 20px; font-size: 0.9em; color: #90CAF9;'>Made with ❤️ using Streamlit | Designed by Kunikaa Dwivedi</footer>", unsafe_allow_html=True)
