import unittest
from unittest.mock import MagicMock
from translation_api import TranslationAPI

class TestTranslationAPI(unittest.TestCase):

    def test_successful_translation(self):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"translatedText": "Translated Text"}

        api = TranslationAPI()
        api._session.post = MagicMock(return_value=mock_response)

        translation = api.translate_text("Hello", "en", "fr")
        self.assertEqual(translation, "Translated Text")

    def test_failed_translation(self):
        mock_response = MagicMock()
        mock_response.status_code = 400

        api = TranslationAPI()
        api._session.post = MagicMock(return_value=mock_response)

        translation = api.translate_text("Hello", "en", "fr")
        self.assertIsNone(translation)

if __name__ == "__main__":
    unittest.main()
