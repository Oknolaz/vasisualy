import wikipedia
from ..core import speak
from ..core import defaults
import os

trigger = ("Что такое", "что такое", "Что это такое", "что это такое", "Чем является", "чем является", "Кем является", "кем является", "Кто такой", "кто такой", "Кто такая", "кто такая", "Кто такие", "кто такие", "Кто это такой", "кто это такой", "Кто это такая", "кто это такая", "Кто эти такие", "кто эти такие", "Кто он такой", "кто он такой", "Кто она такая", "кто она такая", "Кто они такие", "кто они такие", "Кто это", "кто это", "Кто эти", "кто эти", "Кто он", "кто он", "Кто она", "кто она", "Кто они", "кто они") # Команды вывода информации из википедии
excludeList = ("Васисуалий", "Васисуали", "васисуалий", "васисуали", "Васян", "васян", "Васёк", "васёк", "Васися", "васися", "Васисяндра", "васисяндра", "Васька", "васька", "Вася", "вася", "Василий", "василий", "Пожалуйста", "пожалуйста")

wikipedia.set_lang("ru")  # Установка русского языка для Википедии

def main(say, widget):
    for i in trigger:
        if i in say:
            question = say.replace(i, " ")
            for toExclude in excludeList:
                question = question.replace(toExclude, '')
            if question == "" or question == " " or question == "  ":
                toSpeak = "Я не могу ответить на отсутствующий вопрос! Задайте вопрос!"
            else:
                try:
                    try:
                        appDir = os.path.dirname(os.path.realpath(__file__))
                        os.chdir(f"{appDir}/../..")
                        config = open("vasisualy.conf", "r")
                        for line in config:
                            if "sentences:" in line:
                                sentencesCount = int(line.replace("sentences:", ""))
                    except Exception:
                        sentencesCount = defaults.defaults["sentences"]
                    answer = wikipedia.summary(question, sentences=sentencesCount)  # Получение первых sentencesCount предложений из статьи, соответствующей запросу
                    toSpeak = answer
                except ValueError:
                    toSpeak = "Я такого не знаю."
            break
        else:
            toSpeak = ""
            
    if toSpeak != "":
        speak.speak(toSpeak, widget)
    return toSpeak
