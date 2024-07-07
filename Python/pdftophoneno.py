import re
from pdfminer.high_level import extract_text

# Regular expression pattern for phone numbers
PHONE_REG = re.compile(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]')

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    return extract_text(pdf_path)

def extract_phone_number(resume_text):
    """Extract phone numbers from the given text."""
    phone_numbers = re.findall(PHONE_REG, resume_text)
    if phone_numbers:
        # Return the first phone number found
        return phone_numbers[0]
    return None

if __name__ == '__main__':
    # Path to the PDF file
    pdf_path = 'ResumeData.pdf'
    
    # Extract text from the PDF
    text = extract_text_from_pdf(pdf_path)
    
    # Extract phone number from the text
    phone_number = extract_phone_number(text)
    
    if phone_number:
        print(f"Phone Number: {phone_number}")
    else:
        print("No phone number found.")
