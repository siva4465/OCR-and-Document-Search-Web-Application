# OCR and Document Search Web Application

This project is an OCR and Document Search Web Application built using Python, Streamlit, and Tesseract OCR. The application allows users to upload images, extract text from them, and search for specific keywords within the extracted text.

## Deliverables

1. **Code Submission**: Python scripts for the web application, including the OCR processing and search functionality.
2. **Live Web Application**: [Live Application URL](https://ocr-and-document-search-web-application-by-siva.streamlit.app/)
3. **Extracted Text and Search Output**: JSON or plain text output of the extracted text from the uploaded image, along with demonstration of the search functionality with example keywords.

## Features

- **Text Extraction**: Extracts text in both English and Hindi from uploaded images.
- **Keyword Search**: Allows users to search for keywords in the extracted text and highlights the occurrences.

## Evaluation Criteria

- **Accuracy**: The OCR model effectively extracts text from both Hindi and English sections of the image.
- **Functionality**: The web application handles image uploads, text extraction, and keyword searches correctly.
- **User Interface**: The web interface is simple, intuitive, and functional.
- **Deployment**: The application is accessible online, demonstrating a reliable deployment process.
- **Clarity**: The documentation is clear and concise, with a well-structured codebase.
- **Completeness**: All deliverables are submitted, demonstrating the required functionality.

## Requirements

To run the application locally, you need to set up the environment and install the required packages.

### Environment Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/siva4465/OCR-and-Document-Search-Web-Application.git
   cd OCR-and-Document-Search-Web-Application

2. **Install Tesseract OCR**:
   - For **Windows**, download the installer from [Tesseract at UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki).
   - For **Linux**:
     ```bash
     sudo apt install tesseract-ocr tesseract-ocr-hin
     ```
   - For **macOS**:
     ```bash
     brew install tesseract
     brew install tesseract-lang
     ```
     
3. **Install Python packages**:
   Create a `requirements.txt` file in the project directory with the following content:
   ```plaintext
   streamlit
   pytesseract
   Pillow
   opencv-python-headless
   numpy

4. **Then, install the dependencies using**:
   ```bash
   pip install -r requirements.txt
   
5. **Running the Application Locally**
   ```bash
   streamlit run ocr_web_app.py
   
