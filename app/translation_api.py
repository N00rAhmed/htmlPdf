import requests

class TranslationAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def fetch_supported_languages(self):
        response = requests.get(f"{self.base_url}/languages")
        
        if response.status_code == 200:
            return response.json()
        else:
            return []

    def translate(self, text, source_lang, target_lang):
        response = requests.post(f"{self.base_url}/translate", json={
            "q": text,
            "source": source_lang,
            "target": target_lang
        })

        if response.status_code == 200:
            translated_text = response.json()["translatedText"]
            return translated_text
        else:
            return None
