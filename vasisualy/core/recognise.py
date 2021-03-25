from . import speak
import speech_recognition
from PyQt5 import QtGui

def recognise(cls, widget):
    mic_on = QtGui.QIcon.fromTheme("mic-on")
    mic_off = QtGui.QIcon.fromTheme("mic-off")
    cls.pushButton.setIcon(mic_on)
        
    recognizer = speech_recognition.Recognizer()
    recognizer.pause_threshold = 0.5
    mph = speech_recognition.Microphone()
        
    print("[sys] Говорите...")
        
    with mph as source:
        say = recognizer.listen(source)
        
    print("[sys] Речь распознаётся...")
        
    try:
        say = recognizer.recognize_google(say, language="ru-RU")
        say = say.capitalize()
        print("[sys] Речь распознана.")
    except Exception:
        say = ''
        print("[sys] Не удалось распознать речь. Нет подключения к интернету или не подключен микрофон.")
        speak.speak("Речь не распознана.", widget)
    cls.pushButton.setIcon(mic_off)
    return say
