import unittest
from unittest.mock import MagicMock
from main import run_translation_workflow

class TestMain(unittest.TestCase):

    def test_run_translation_workflow(self):
        mock_translator = MagicMock()
        mock_translator.translate_html.return_value = "<p>Bonjour</p>"

        run_translation_workflow("English", "French", mock_translator)

        mock_translator.translate_html.assert_called_once()

if __name__ == "__main__":
    unittest.main()
