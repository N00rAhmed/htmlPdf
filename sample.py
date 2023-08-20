from translate import Translator

# Initialize the translator
translator = Translator(to_lang='de')  # 'de' for German

# Regular text to be translated
text_to_translate = "Hello, how are you?"

# Translate the text
translated_text = translator.translate(text_to_translate)

# Print the original and translated text
print("Original:", text_to_translate)
print("Translated:", translated_text)
