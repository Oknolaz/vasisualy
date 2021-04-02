from ..core import speak
import random

trigger = ("Кристальный шар", "кристальный шар", "Свет мой зеркальце", "свет мой зеркальце")

def main(say, widget):
    for i in trigger:
        if i in say:
            if say == i:
                toSpeak = "Мне нужен вопрос, чтобы ответить на него."
            else:
                toSpeak = random.choice(("Да.", "Конечно!", "Несомненно.", "Спроси в следующий раз.", "Нет конечно!", "Нет.", "Я бы не рассчитывал на это.", "Возможно.", "Это невозможно."))
            break
        else:
            toSpeak = ""
            
    if toSpeak != "":
        speak.speak(toSpeak, widget)
    return toSpeak
