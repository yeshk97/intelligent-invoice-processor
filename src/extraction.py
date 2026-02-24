"""
Invoice Text Extraction Module

This module handles OCR (Optical Character Recognition) and text extraction
from PDF and image files.

Functions:
    extract_text_from_pdf: Extract text from PDF files
    extract_text_from_image: Extract text from image files (JPG, PNG)
    preprocess_image: Clean and enhance images before OCR
"""

# Standard library imports
import os
from pathlib import Path
from typing import Optional

# Third-party imports (in order of usage)
from pdf2image import convert_from_path
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract


def extract_text_from_pdf(pdf_path: str, dpi: int = 300) -> str:
    """
    Extract text from a PDF file using OCR.
    
    This function converts each page of the PDF to an image,
    then uses Tesseract OCR to extract text from those images.
    
    Args:
        pdf_path (str): Path to the PDF file
        dpi (int): DPI for PDF to image conversion (higher = better quality, slower)
                   Default 300 is good balance of quality and speed
    
    Returns:
        str: Extracted text from all pages combined
    
    Raises:
        FileNotFoundError: If the PDF file doesn't exist
        Exception: For any OCR processing errors
    
    Example:
        >>> text = extract_text_from_pdf("invoice.pdf")
        >>> print(text)
        "INVOICE #12345\\nDate: 2024-01-15\\n..."
    """
    # Step 1: Check if file exists
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")
    
    try:
        # Step 2: Convert PDF pages to images
        images = convert_from_path(pdf_path, dpi=dpi)
        
        # Step 3: Extract text from each page
        extracted_text = []
        
        for page_num, image in enumerate(images, start=1):
            # Step 4: Preprocess image to improve OCR accuracy
            processed_image = preprocess_image(image)
            
            # Step 5: Run OCR on the processed image
            page_text = pytesseract.image_to_string(processed_image)
            
            # Step 6: Add page separator for multi-page documents
            extracted_text.append(f"--- Page {page_num} ---\\n{page_text}")
        
        # Step 7: Combine all pages into single string
        full_text = "\\n\\n".join(extracted_text)
        
        return full_text.strip()
    
    except Exception as e:
        raise Exception(f"Error extracting text from PDF: {str(e)}")


def extract_text_from_image(image_path: str) -> str:
    """
    Extract text from an image file using OCR.
    
    Supports common image formats: JPG, JPEG, PNG, BMP, TIFF
    
    Args:
        image_path (str): Path to the image file
    
    Returns:
        str: Extracted text from the image
    
    Raises:
        FileNotFoundError: If the image file doesn't exist
        Exception: For any OCR processing errors
    
    Example:
        >>> text = extract_text_from_image("invoice.jpg")
        >>> print(text)
        "INVOICE #12345\\nDate: 2024-01-15\\n..."
    """
    # Step 1: Check if file exists
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")
    
    try:
        # Step 2: Open the image
        image = Image.open(image_path)
        
        # Step 3: Preprocess to improve OCR accuracy
        processed_image = preprocess_image(image)
        
        # Step 4: Extract text using Tesseract
        text = pytesseract.image_to_string(processed_image)
        
        return text.strip()
    
    except Exception as e:
        raise Exception(f"Error extracting text from image: {str(e)}")


def preprocess_image(image: Image.Image) -> Image.Image:
    """
    Preprocess an image to improve OCR accuracy.
    
    Applies several image enhancement techniques:
    - Converts to grayscale (removes color noise)
    - Increases contrast (makes text sharper)
    - Applies slight sharpening filter
    
    Args:
        image (PIL.Image): Input image
    
    Returns:
        PIL.Image: Processed image ready for OCR
    
    Example:
        >>> from PIL import Image
        >>> img = Image.open("invoice.jpg")
        >>> clean_img = preprocess_image(img)
        >>> # clean_img now has better contrast and sharpness
    """
    # Step 1: Convert to grayscale
    # Why? Color adds noise - black and white text is easier to read
    image = image.convert('L')
    
    # Step 2: Increase contrast
    # Why? Makes text darker against white background
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2.0)  # 2.0 = double the contrast
    
    # Step 3: Apply slight sharpening
    # Why? Makes blurry text edges clearer
    image = image.filter(ImageFilter.SHARPEN)
    
    return image


# Test function - useful for development
if __name__ == "__main__":
    """
    This block only runs when you execute this file directly:
    python src/extraction.py
    
    Useful for testing during development.
    """
    print("Invoice Text Extraction Module")
    print("=" * 50)
    print("\\nUsage:")
    print("  from src.extraction import extract_text_from_pdf")
    print("  text = extract_text_from_pdf('invoice.pdf')")
    print("\\nOr for images:")
    print("  from src.extraction import extract_text_from_image")
    print("  text = extract_text_from_image('invoice.jpg')")
