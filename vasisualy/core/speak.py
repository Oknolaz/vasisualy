import speechd
from . import defaults

# Настройка синтезатора речи
tts_d = speechd.SSIPClient('Vasisya')
tts_d.set_output_module('rhvoice')
tts_d.set_language('ru')
try:
    voice = defaults.get_value("voice")
    speed = defaults.get_value("speed")
    pitch = defaults.get_value("pitch")
except FileNotFoundError:
    voice = defaults.defaults["voice"]
    speed = defaults.defaults["speed"]
    pitch = defaults.defaults["pitch"]

tts_d.set_synthesis_voice(voice)
tts_d.set_rate(speed)
tts_d.set_punctuation(speechd.PunctuationMode.SOME)
tts_d.set_pitch(pitch)


def speak(message, widget):
    '''Выводит сообщение пользователю и озвучивает его.
    :param message: сообщение, которое нужно вывести и озвучить (string).
    :param widget: виджет, в который нужно вывести сообщение (QWidget).
    '''
    tts_d.speak(message)  # Озвучка переданного сообщения с помощью синтеза речи
    widget.addItem(message)  # Вывод переданного сообщения в графический интерфейс
    widget.scrollToBottom()  # Прокрутка виджета с сообщениями до конца
