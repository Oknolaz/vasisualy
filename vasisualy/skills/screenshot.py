from mss import mss
from ..core import speak

trigger = ("Экран", "экран", "Скрин", "скрин", "Скриншот", "скриншот", "Фото", "фото", "Снимок", "снимок", "Фотография",
           "фотография", "Сними", "сними", "Сфотографируй", "сфотографируй", "Сфотай", "сфотай", "Сфоткай", "сфоткай",
           "Фотай", "фотай", "Фоткай", "фоткай")  # Команды для создания скриншота


def main(say, widget):
    for i in trigger:
        if i in say:
            toSpeak = "Я сделал снимок экрана."
            with mss() as sct:
                sct.shot()  # Создание скриншота в файл monitor-1.png
            break
        else:
            toSpeak = ""
    
    if toSpeak != "":
        speak.speak(toSpeak, widget)
        
    return toSpeak
