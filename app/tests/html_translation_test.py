import unittest
from html_translation import HTMLTranslator

class TestHTMLTranslator(unittest.TestCase):

    def test_translation(self):
        translator = HTMLTranslator()
        input_html = "<p>Hello</p>"
        translated_html = translator.translate_html(input_html, "en", "fr")
        self.assertIn("Bonjour", translated_html)

if __name__ == "__main__":
    unittest.main()
