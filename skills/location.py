import geocoder
from core import speak

trigger = ("Где я", "где я", "Моё местоположение", "моё местоположение", "Что за место", "что за место")

geo = geocoder.ip('me')

def main(say, widget):
    for i in trigger:
        if i in say:
            toSpeak = f"Ты находишься в {geo.country}, {geo.city}."
            break
        else:
            toSpeak = ""
            
    if toSpeak != "":
        speak.speak(toSpeak, widget)
    return toSpeak
