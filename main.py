from googletrans import Translator
from unidecode import unidecode


# def translate_text(text):
#
#     translator = Translator()
#     language = translator.detect_legacy(unidecode(text))
#     print(language)
#
#     if language.lang == "en":
#         translated_text = translator.translate(text, src='en', dest='ru').text
#         return translated_text
#
#     elif language.lang == "ru":
#         translated_text = translator.translate(text, src='ru', dest='en').text
#         return translated_text


def translate_text_en_ru(text):
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


def translit_names(text):
    lower_case_letters = {
        u'а': u'a',
        u'б': u'b',
        u'в': u'v',
        u'г': u'g',
        u'д': u'd',
        u'е': u'e',
        u'ё': u'e',
        u'ж': u'zh',
        u'з': u'z',
        u'и': u'i',
        u'й': u'y',
        u'к': u'k',
        u'л': u'l',
        u'м': u'm',
        u'н': u'n',
        u'о': u'o',
        u'п': u'p',
        u'р': u'r',
        u'с': u's',
        u'т': u't',
        u'у': u'u',
        u'ф': u'f',
        u'х': u'h',
        u'ц': u'ts',
        u'ч': u'ch',
        u'ш': u'sh',
        u'щ': u'sch',
        u'ъ': u'',
        u'ы': u'y',
        u'ь': u'',
        u'э': u'e',
        u'ю': u'yu',
        u'я': u'ya'
    }

    eng_lower_case = {
        u'a': u'',
        u'b': u'b',
        u'v': u'v',
        u'g': u'g',
        u'd': u'd',
        u'е': [u'e', u'ё'],
        u'zh': u'ж',
        u'z': u'z',
        u'и': u'i',
        u'й': u'y',
        u'к': u'k',
        u'л': u'l',
        u'м': u'm',
        u'н': u'n',
        u'о': u'o',
        u'п': u'p',
        u'р': u'r',
        u'с': u's',
        u'т': u't',
        u'у': u'u',
        u'ф': u'f',
        u'х': u'h',
        u'ц': u'ts',
        u'ч': u'ch',
        u'ш': u'sh',
        u'щ': u'sch',
        u'ъ': u'',
        u'ы': u'y',
        u'ь': u'',
        u'э': u'e',
        u'ю': u'yu',
        u'я': u'ya'

    }

    translit_string = ''

    for index, char in enumerate(text.lower()):
        if char in lower_case_letters.keys():
            char = lower_case_letters[char]

        translit_string += char

    return translit_string.capitalize()



