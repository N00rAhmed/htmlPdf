import unittest
import tkinter as tk
from tkinter import ttk
from unittest.mock import MagicMock
from gui import TranslatorApp

class TestTranslatorApp(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.app = TranslatorApp(self.root)

    def test_gui_elements(self):
        self.assertIsInstance(self.app.source_lang_choose, ttk.Combobox)
        self.assertIsInstance(self.app.target_lang_choose, ttk.Combobox)
        self.assertIsInstance(self.app.b1, tk.Button)
        self.assertIsInstance(self.app.b2, tk.Button)

    def test_translation_button(self):
        self.app.source_lang_choose.set("English")
        self.app.target_lang_choose.set("French")
        self.app.input_html_file = "test_input.html"
        self.app.translate_and_generate_pdf = MagicMock()

        self.app.translate_and_generate_pdf()
        self.app.translate_and_generate_pdf.assert_called_once()

if __name__ == "__main__":
    unittest.main()
