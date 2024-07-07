import re
from pdfminer.high_level import extract_text

# Improved regular expression for email extraction
# This pattern is more comprehensive and accounts for a wider range of valid email formats
EMAIL_REG = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF file using PDFMiner.

    Parameters:
    pdf_path (str): The path to the PDF file.

    Returns:
    str: The extracted text.
    """
    return extract_text(pdf_path)

def extract_emails(resume_text):
    """
    Extracts email addresses from the given text using a regular expression.

    Parameters:
    resume_text (str): The text to search for email addresses.

    Returns:
    list: A list of email addresses found.
    """
    return re.findall(EMAIL_REG, resume_text)

if __name__ == '__main__':
    # Specify the path to your PDF resume
    pdf_path = 'ResumeData.pdf'
    text = extract_text_from_pdf(pdf_path)
    emails = extract_emails(text)

    if emails:
        print("Email addresses found:")
        for email in emails:
            print(email)
    else:
        print("No email addresses found.")
