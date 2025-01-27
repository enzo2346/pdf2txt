import pytesseract # pytesseract is a wrapper for Google's Tesseract-OCR Engine: https://github.com/UB-Mannheim/tesseract/wiki
from pdf2image import convert_from_path # pdf2image is a wrapper for poppler, a PDF rendering library: https://github.com/oschwartz10612/poppler-windows/releases

file_path = r'file2convert.pdf'
output_path = r'converted_file.txt'

# Convert PDF to images for OCR processing
images = convert_from_path(file_path)

# Perform OCR on each image
ocr_text_by_page = [pytesseract.image_to_string(image, lang="fra") for image in images]

# Combine OCR results into a single text block
ocr_full_text = "\n".join(ocr_text_by_page)

# Write OCR results to a text file
with open(output_path, 'w', encoding='utf-8') as file:
    file.write(ocr_full_text)
