import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from html_translation import HTMLTranslator
from translation_api import TranslationAPI

class TranslationGUI:
    def __init__(self, supported_languages):
        self.supported_languages = supported_languages

        self.my_w = tk.Tk()
        self.my_w.geometry("400x350")
        self.my_w.title('HTML to PDF Translator')
        self.my_font1 = ('times', 18, 'bold')
        
        self.l1 = tk.Label(self.my_w, text='Choose Source Language:', width=30, font=self.my_font1)
        self.l1.grid(row=1, column=1)

        self.n = tk.StringVar()
        self.source_lang_choose = ttk.Combobox(self.my_w, width=27, textvariable=self.n)
        self.source_lang_choose['values'] = [lang['name'] for lang in self.supported_languages]
        self.source_lang_choose.grid(row=2, column=1)
        self.source_lang_choose.bind("<<ComboboxSelected>>", lambda _: self.update_target_language_options())

        self.m = tk.StringVar()
        self.l2 = tk.Label(self.my_w, text='Choose Target Language:', width=30, font=self.my_font1)
        self.l2.grid(row=3, column=1)

        self.target_lang_choose = ttk.Combobox(self.my_w, width=27, textvariable=self.m)
        self.target_lang_choose.grid(row=4, column=1)

        self.b1 = tk.Button(self.my_w, text='Translate and Generate PDF', width=25, command=lambda: self.translate_and_generate_pdf())
        self.b1.grid(row=5, column=1)

        self.input_html_file = ''

        self.b2 = tk.Button(self.my_w, text='Open HTML File', width=20, command=self.open_html_file)
        self.b2.grid(row=6, column=1)

    def update_target_language_options(self):
        source_lang = self.n.get()
        target_languages = [lang['name'] for lang in self.supported_languages if lang['name'] != source_lang]
        self.target_lang_choose['values'] = target_languages
        self.target_lang_choose.current(0)

    def open_html_file(self):
        global input_html_file
        input_html_file = filedialog.askopenfilename(filetypes=[('HTML Files', '*.html')])
        print(f'Selected HTML file: {input_html_file}')

        if input_html_file:
            self.b1.config(state=tk.NORMAL)
        else:
            self.b1.config(state=tk.DISABLED)

    def translate_and_generate_pdf(self):
        source_lang = self.source_lang_choose.get()
        target_lang = self.target_lang_choose.get()

        if not source_lang or not target_lang:
            print("Please select both source and target languages.")
            return

        input_html_file = filedialog.askopenfilename(filetypes=[("HTML Files", "*.html")])
        if not input_html_file:
            return

        output_file = "translated_pdf.pdf"
        translator = HTMLTranslator(self.supported_languages)
        translator.translate_html_to_pdf(source_lang, target_lang, output_file, input_html_file)
        print(f"Translated PDF saved to {output_file}")

#gui
if __name__ == "__main__":
    base_url = 'http://localhost:5000'
    api = TranslationAPI(base_url)
    supported_languages = api.fetch_supported_languages()

    gui = TranslationGUI(supported_languages)
    gui.my_w.mainloop()
