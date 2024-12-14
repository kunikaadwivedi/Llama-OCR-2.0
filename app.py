import streamlit as st
from PIL import Image, ImageOps
from pytesseract import pytesseract, image_to_string
import shutil
import os

# Set the Tesseract executable path
pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'

# Verify Tesseract installation
if shutil.which("tesseract") is None:
    raise FileNotFoundError("Tesseract is not installed or not in PATH. Please install it and try again.")

# Image preprocessing function
def preprocess_image(image):
    image = image.convert("L")  # Convert to grayscale
    image = ImageOps.autocontrast(image)  # Increase contrast
    image = image.resize((int(image.width * 1.5), int(image.height * 1.5)))  # Resize for better OCR
    image = image.point(lambda x: 0 if x < 140 else 255, '1')  # Apply binary threshold
    return image

# Postprocess OCR output
def clean_ocr_output(text):
    return '\n'.join([line.strip() for line in text.splitlines() if line.strip()])

# Page configuration
st.set_page_config(
    page_title="Llama OCR 2.0",
    page_icon="🦙",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for dark theme styling
st.markdown(
    """<style>
    body {
        background-color: #1E1E2F; /* Dark background */
        font-family: 'Poppins', sans-serif;
        color: #FFFFFF; /* White text for readability */
    }
    h1 {
        color: #FF6347; /* Vibrant coral for title */
        font-family: 'Cinzel', serif; /* Elegant serif font */
        text-align: center;
        font-size: 5em;
        letter-spacing: 2px;
        text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.5);
        margin-top: 20px;
        margin-bottom: 20px;
    }
    h3 {
        color: #1E90FF; /* Dodger blue for headings */
        font-size: 2em;
        margin-bottom: 20px;
    }
    p {
        color: #DCDCDC; /* Light gray for text */
        font-size: 1.2em;
    }
    .result-container {
        background-color: #2E2E3E; /* Dark gray container */
        padding: 25px;
        border-radius: 10px;
        border: 2px solid #4682B4; /* Steel blue border */
        box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.5);
    }
    .stButton > button {
        background-color: #FF4500; /* Orange red button */
        color: #FFFFFF; /* White text */
        border-radius: 8px;
        font-size: 1.1em;
        padding: 12px 25px;
        border: none;
        cursor: pointer;
        transition: 0.3s;
    }
    .stButton > button:hover {
        background-color: #FF6347; /* Lighter coral on hover */
    }
    .sidebar .sidebar-content {
        background-color: #2B2B3B; /* Dark sidebar */
        color: #FFFFFF; /* White text in sidebar */
    }
    footer {
        text-align: center;
        margin-top: 30px;
        font-size: 1em;
        color: #87CEFA; /* Light sky blue footer text */
    }
    </style>""",
    unsafe_allow_html=True
)

# Title and description
st.markdown("<h1>🦙 Llama OCR 2.0</h1>", unsafe_allow_html=True)
st.markdown("<p>Extract text from images with enhanced accuracy and readability.</p>", unsafe_allow_html=True)
st.markdown("---")

# Sidebar for file upload
with st.sidebar:
    st.header("Upload Image")
    uploaded_file = st.file_uploader("Choose an image file", type=['png', 'jpg', 'jpeg'])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Extract Text 🔍"):
        with st.spinner("Processing image..."):
            try:
                processed_image = preprocess_image(image)
                st.image(processed_image, caption="Processed Image", use_column_width=True)

                ocr_result = image_to_string(processed_image, lang='eng', config='--psm 6')
                cleaned_result = clean_ocr_output(ocr_result)

                st.markdown(
                    f"""<div class='result-container'>
                    <h3>OCR Results:</h3>
                    <p>{cleaned_result}</p>
                    </div>""", unsafe_allow_html=True
                )
            except Exception as e:
                st.error(f"Error during OCR processing: {e}")
else:
    st.info("Please upload an image to start the OCR process.")

# Footer
st.markdown("<footer>Made with ❤️ using Streamlit | Designed by Kunikaa Dwivedi</footer>", unsafe_allow_html=True)
