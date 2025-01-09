import shutil
import streamlit as st
from PIL import Image
from pytesseract import pytesseract, image_to_string

# Streamlit page configuration
st.set_page_config(page_title="Llama OCR", page_icon="🦙", layout="wide")

# Dynamically detect Tesseract executable path
TESSERACT_PATH = shutil.which("tesseract")

if TESSERACT_PATH:
    pytesseract.tesseract_cmd = TESSERACT_PATH
    st.sidebar.success(f"Tesseract found at: {TESSERACT_PATH}")
else:
    st.sidebar.error("Tesseract is not installed or not in PATH. Please ensure setup.sh installs it.")
    st.stop()

# Title and instructions
st.title("🦙 Llama OCR 2.0")
st.markdown("Upload an image to extract text using Tesseract OCR.")

# Upload image
uploaded_file = st.sidebar.file_uploader("Upload an image (PNG, JPG, JPEG)", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    if st.button("Extract Text"):
        with st.spinner("Extracting text..."):
            try:
                text = image_to_string(image, lang="eng")
                st.text_area("Extracted Text", text, height=300)
            except Exception as e:
                st.error(f"Error during OCR processing: {e}")
else:
    st.info("Please upload an image to start the OCR process.")

st.markdown("<footer style='text-align: center; margin-top: 20px; font-size: 0.9em; color: #90CAF9;'>Made with ❤️ using Streamlit | Designed by Kunikaa Dwivedi</footer>", unsafe_allow_html=True)
