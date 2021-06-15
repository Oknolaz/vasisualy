import speechd
from . import defaults
import os

# Настройка синтезатора речи
tts_d = speechd.SSIPClient('Vasisya')
tts_d.set_output_module('rhvoice')
tts_d.set_language('ru')
try:
    appDir = os.path.dirname(os.path.realpath(__file__))
    os.chdir(f"{appDir}/../../")
    config = open("vasisualy.conf", "r")
    for line in config:
        if "voice:" in line:
            voice = line.replace("voice:", "")
        elif "speed:" in line:
            speed = int(line.replace("speed:", ""))
        elif "pitch:" in line:
            pitch = int(line.replace("pitch:", ""))
except Exception:
    voice = defaults.defaults["voice"]
    speed = defaults.defaults["speed"]
    pitch = defaults.defaults["pitch"]

tts_d.set_synthesis_voice(voice)
tts_d.set_rate(speed)
tts_d.set_punctuation(speechd.PunctuationMode.NONE)
tts_d.set_pitch(pitch)

def speak(message, widget):
    '''Выводит сообщение пользователю и озвучивает его.
    :param message: сообщение, которое нужно вывести и озвучить (string).
    :param widget: виджет, в который нужно вывести сообщение (QWidget).
    '''
    tts_d.speak(message)  # Озвучка переданного сообщения с помощью синтеза речи
    widget.addItem(message)  # Вывод переданного сообщения в графический интерфейс
    widget.scrollToBottom()  # Прокрутка виджета с сообщениями до конца
