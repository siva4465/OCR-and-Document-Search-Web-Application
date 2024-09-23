
import streamlit as st
import pytesseract
from PIL import Image
import cv2
import numpy as np
import re

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'




# Streamlit app title
st.title("OCR and Document Search Web Application")

# Function to extract text from the image using Tesseract
def extract_text_from_image(image):
    # Convert the image into an OpenCV-compatible format
    img = np.array(image)

    # Convert to grayscale for better OCR performance
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Perform OCR on the image
    extracted_text = pytesseract.image_to_string(gray, lang='eng+hin')
    return extracted_text

# Function to search for a keyword in the extracted text and highlight it
def highlight_keyword(extracted_text, keyword):
    if keyword:
        # Create a regex pattern for the keyword (case insensitive)
        pattern = re.compile(re.escape(keyword), re.IGNORECASE)
        highlighted_text = pattern.sub(f'<span style="background-color: white; color: black;">{keyword}</span>', extracted_text)
        return highlighted_text
    return extracted_text

# Upload image section
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_image is not None:
    # Display the uploaded image
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Extract text from the image
    st.write("Extracting text from the image...")
    extracted_text = extract_text_from_image(image)
    
    # Display the extracted text
    st.subheader("Extracted Text:")
    st.write(extracted_text)

    # Search functionality
    keyword = st.text_input("Enter a keyword to search in the extracted text:")

    if keyword:
        highlighted_text = highlight_keyword(extracted_text, keyword)
        st.success(f"Keyword '{keyword}' found in the extracted text!")
        st.markdown(highlighted_text, unsafe_allow_html=True)
    else:
        st.error(f"Keyword '{keyword}' not found in the extracted text.")
else:
    st.write("Please upload an image to start the OCR process.")
