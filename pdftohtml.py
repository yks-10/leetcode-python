import pdfplumber

# Function to convert PDF to HTML
def pdf_to_html(pdf_path):
    html_content = '<html><body>'
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            html_content += f'<p>{text}</p>'
    html_content += '</body></html>'
    return html_content

# Usage
pdf_path = 'PCHFL & FISPL All Set Tamil.pdf'
html_output = pdf_to_html(pdf_path)
print(html_output)
