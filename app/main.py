from translation_api import TranslationAPI
from gui import TranslationGUI

if __name__ == "__main__":
    base_url = 'http://192.168.43.147:5000'
    api = TranslationAPI(base_url)
    supported_languages = api.fetch_supported_languages()

    gui = TranslationGUI(supported_languages)
    gui.my_w.mainloop()
