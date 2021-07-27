from googletrans import Translator
from unidecode import unidecode


def translate_text_en_ru(text):
    """
    works better if translate word by word, and when text doenst big
    :param text:
    :return:
    """
    assert len(text) != 0
    assert len(text) != text.count(' ')

    translator = Translator()
    translated_text = translator.translate(text, src='en', dest='ru').text
    return translated_text


def translate_text_ru_en(text):
    assert len(text) != 0
    assert len(text) != text.count(' ')

    translator = Translator()
    translated_text = translator.translate(text, src='ru', dest='en').text
    return translated_text

