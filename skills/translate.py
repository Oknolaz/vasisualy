from translate import Translator
from core import speak

trigger = ("Переведи слово", "переведи слово", "Переведи слова", "переведи слова", "Переведи фразу", "переведи фразу", "Переведи предложение", "переведи предложение", "Переведи текст", "переведи текст", "Переведи", "переведи")
excludeList = ("Васисуалий", "Васисуали", "васисуалий", "васисуали", "Васян", "васян", "Васёк", "васёк", "Васися", "васися", "Васисяндра", "васисяндра", "Васька", "васька", "Вася", "вася", "Василий", "василий", "Пожалуйста", "пожалуйста")

def main(say, widget):
    for i in trigger:
        if i in say:
            trans_text = say.replace(i, ' ')
            for toExclude in excludeList:
                trans_text = trans_text.replace(toExclude, '')
            isTranslated = False
            for i in ("на английский", "по-английски", "по английски", "на английском"):
                if i in trans_text:
                    trans_text = trans_text.replace(i, "", 1)
                    translator = Translator(to_lang = "en", from_lang = "ru")
                    toSpeak = translator.translate(trans_text)
                    isTranslated = True
            for i in ("на русский", "на русском", "по-русски", "по русски"):
                if i in trans_text:
                    trans_text = trans_text.replace(i, "", 1)
                    translator = Translator(to_lang = "ru")
                    toSpeak = translator.translate(trans_text)
                    isTranslated = True
            for i in ("на французский", "на французском", "по-французски", "по французски"):
                if i in trans_text:
                    trans_text = trans_text.replace(i, "", 1)
                    translator = Translator(to_lang = "fr", from_lang = "ru")
                    toSpeak = translator.translate(trans_text)
                    isTranslated = True
            for i in ("на немецкий", "на немецком", "по-немецки", "по немецки"):
                if i in trans_text:
                    trans_text = trans_text.replace(i, "", 1)
                    translator = Translator(to_lang = "de", from_lang = "ru")
                    toSpeak = translator.translate(trans_text)
                    isTranslated = True
            for i in ("на украинский", "на украинском", "по-украински", "по украински"):
                if i in trans_text:
                    trans_text = trans_text.replace(i, "", 1)
                    translator = Translator(to_lang = "uk", from_lang = "ru")
                    toSpeak = translator.translate(trans_text)
                    isTranslated = True
            for i in ("на португальский", "на португальском", "по-португальски", "по португальски"):
                if i in trans_text:
                    trans_text = trans_text.replace(i, "", 1)
                    translator = Translator(to_lang = "pt", from_lang = "ru")
                    toSpeak = translator.translate(trans_text)
                    isTranslated = True
            for i in ("на итальянский", "на итальянском", "по-итальянски", "по итальянски"):
                if i in trans_text:
                    trans_text = trans_text.replace(i, "", 1)
                    translator = Translator(to_lang = "it", from_lang = "ru")
                    toSpeak = translator.translate(trans_text)
                    isTranslated = True
            for i in ("на испанский", "на испанском", "по-испански", "по испански"):
                if i in trans_text:
                    trans_text = trans_text.replace(i, "", 1)
                    translator = Translator(to_lang = "es", from_lang = "ru")
                    toSpeak = translator.translate(trans_text)
                    isTranslated = True
            if trans_text in ('', ' ', '  ', '   '):
                toSpeak = "Укажите текст, который нужно перевести."
            elif not isTranslated:
                translator = Translator(to_lang = "en", from_lang = "ru")
                toSpeak = translator.translate(trans_text)
            break
        else:
            toSpeak = ""
            
    if toSpeak != "":
        speak.speak(toSpeak, widget)
    return toSpeak
