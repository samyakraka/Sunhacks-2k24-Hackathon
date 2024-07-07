from pdfminer.high_level import extract_text

def extract_text_from_pdf(pdf_path):
    text = extract_text(pdf_path)
    with open('ResumeData.docx', 'w') as file:
        file.write(text)
    return text

if __name__ == '__main__':
    print(extract_text_from_pdf('./ResumeData.pdf'))
 # noqa: T001