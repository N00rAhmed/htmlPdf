from bs4 import BeautifulSoup
import concurrent.futures
from translation_api import TranslationAPI
import pdfkit

class HTMLTranslator:
    def __init__(self, supported_languages):
        self.languages_map = {lang['name']: lang for lang in supported_languages}

    def translate_and_replace(self, element, source_lang, target_lang, translation_cache):
        original_text = element.get_text()
        translated_text = TranslationAPI().translate(original_text, source_lang, target_lang)
        
        if translated_text:
            translation_cache[original_text] = translated_text
            element.string = translated_text

    def translate_html_to_pdf(self, source_lang_name, target_lang_name, output_file, input_html_file):
        source_lang_code = self.languages_map[source_lang_name]['code']
        target_lang_code = self.languages_map[target_lang_name]['code']

        with open(input_html_file, 'r', encoding='utf-8') as file:
            html_content = file.read()

        soup = BeautifulSoup(html_content, 'html.parser')

        translatable_tags = ['p', 'h1', 'h2', 'h3', 'span', 'a', 'h4', 'h5', 'h6', 'strong', 'label', 'li', 'button', 'table', 'thead', 'th', 'tr', 'tbody', 'br', 'title', 'ul', 'small', 'td', 'i', 'button']
        tag_elements = []

        for tag in translatable_tags:
            tag_elements.extend(soup.find_all(tag))

        translation_cache = {}

        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            executor.map(lambda elem: self.translate_and_replace(elem, source_lang_code, target_lang_code, translation_cache), tag_elements)

        translated_html = soup.prettify()

        translated_html_file = 'translated_html.html'
        with open(translated_html_file, 'w', encoding='utf-8') as file:
            file.write(translated_html)

        pdfkit.from_file(translated_html_file, output_file)
