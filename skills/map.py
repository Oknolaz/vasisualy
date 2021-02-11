from core import speak
from ui import map
from PyQt5 import QtWidgets

trigger = ("Карта", "карта", "Карты", "карты", "Навигатор", "навигатор") # Команды вызова окна OpenStreetMap


# Окно для показа OpenStreetMap            
class OpenVasMap(QtWidgets.QWidget, map.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


def main(say, widget):
    for i in trigger:
        if i in say:
            toSpeak = "Я открыл OpenStreetMap."
            break
        else:
            toSpeak = ""
            
    if toSpeak != "":
        speak.speak(toSpeak, widget)
    return toSpeak
            

