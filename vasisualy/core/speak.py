import speechd
from ..ui import design
from PyQt5 import QtWidgets

tts_d = speechd.SSIPClient('Vasisya')
tts_d.set_output_module('rhvoice')
tts_d.set_language('ru')
tts_d.set_synthesis_voice('Artemiy')
tts_d.set_rate(30)
tts_d.set_punctuation(speechd.PunctuationMode.NONE)
tts_d.set_pitch(0)

def speak(string, widget):
    tts_d.speak(string)
    widget.addItem(string)
    widget.scrollToBottom()
