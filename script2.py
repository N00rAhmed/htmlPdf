from translate import Translator
from bs4 import BeautifulSoup
import pdfkit

output_pdf_path = "output.pdf"

options = {
    'page-size': 'A4',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
}

# Read the HTML content from a file
html_file_path = "F:\htmlPdf\input1.html"
with open(html_file_path, 'r', encoding='utf-8') as html_file:
    html_content = html_file.read()

# Parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Find text elements
text_elements = soup.find_all(['p', 'div', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'span', 'a'])

# Initialize the translator
translator = Translator(to_lang='de')  # 'de' for German

# Translate and replace text in elements
for element in text_elements:
    original_text = element.get_text()
    translated_text = translator.translate(original_text)
    element.string = translated_text

# Reconstruct modified HTML
translated_html = soup.prettify()

# Save the translated HTML to a file (e.g., translated.html)
with open('translated.html', 'w', encoding='utf-8') as html_file:
    html_file.write(translated_html)

# Convert the HTML to PDF
# pdfkit.from_file('translated.html', output_pdf_path, options=options)

# print(f'PDF saved to {output_pdf_path}')
