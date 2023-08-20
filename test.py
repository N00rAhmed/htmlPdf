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
    'binary-path': '/path/to/wkhtmltopdf/executable'
}

# Dummy HTML content
dummy_html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>The Joy of Reading</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f9f9f9;
            margin: 0;
            padding: 0;
        }
        header {
            background-color: #333;
            color: #fff;
            text-align: center;
            padding: 10px;
        }
        article {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #fff;
            box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #333;
            margin-bottom: 10px;
        }
        p {
            line-height: 1.5;
            margin-bottom: 20px;
        }
        button {
            background-color: #333;
            color: #fff;
            padding: 8px 20px;
            border: none;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        button:hover {
            background-color: #555;
        }
        .highlight {
            background-color: #ffec80;
            padding: 5px;
        }
        @keyframes fadeIn {
            from {
                opacity: 0;
            }
            to {
                opacity: 1;
            }
        }
        .animated-text {
            animation: fadeIn 2s ease-in-out;
        }
    </style>
    <script>
        function toggleHighlight() {
            var highlightElements = document.querySelectorAll('.highlight');
            highlightElements.forEach(function (element) {
                element.classList.toggle('animated-text');
            });
        }
    </script>
</head>
<body>
    <header>
        <h1>The Joy of Reading</h1>
    </header>
    <article>
        <p>Reading is a magical journey that takes us to different worlds, cultures, and perspectives. It opens doors to imagination and knowledge, and is an essential tool for personal growth.</p>
        <p>Books are like portals to new adventures. Whether it's a thrilling mystery, a heartwarming romance, or a mind-bending science fiction novel, books have the power to transport us beyond our everyday lives.</p>
        <p><span class="highlight">Books</span> introduce us to characters we can relate to and learn from. They encourage empathy and broaden our understanding of the human experience. Through reading, we can walk in the shoes of people from all walks of life.</p>
        <p>Moreover, reading enhances our vocabulary, language skills, and cognitive abilities. It stimulates our minds and keeps our brains active and engaged. Researchers have found that reading can even help prevent cognitive decline as we age.</p>
        <p><span class="highlight">Reading</span> doesn't just improve our intellectual well-being; it can also be a source of pure joy and relaxation. Curling up with a good book is a form of self-care that allows us to unwind and escape the stresses of daily life.</p>
        <p>So, whether it's a thrilling novel, an inspiring biography, or an informative non-fiction book, make reading a part of your routine. Let the pages of a book take you on a journey of discovery and wonder.</p>
        <button onclick="toggleHighlight()">Toggle Highlight</button>
    </article>
</body>
</html>

"""

html_file_path = "F:\\htmlPdf\\target.html"
with open(html_file_path, 'r', encoding='utf-8') as html_file:
    html_content = html_file.read()


# Parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Find text elements
text_elements = soup.find_all(['p', 'div', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'span', 'a','title'])

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

# # Convert the HTML to PDF
# pdfkit.from_file('translated.html', output_pdf_path, options=options)

# print(f'PDF saved to {output_pdf_path}')
