from core import speak
import requests

trigger = ("Проверь подключение", "проверь подключение", "Проверить подключение", "проверить подключение")

def main(say, widget):
    for i in trigger:
        if i in say:
            try:
                requests.get("http://google.com")
                toSpeak = "Имеется подключение к сети."
            except Exception:
                toSpeak = "Нет подключения к сети."
            break
        else:
            toSpeak = ""
            
    if toSpeak != "":
        speak.speak(toSpeak, widget)
    return toSpeak
