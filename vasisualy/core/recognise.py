from . import speak
import vosk
from PyQt5 import QtGui
import queue
import sounddevice as sd
import sys
import json

q = queue.Queue()

device_info = sd.query_devices(0, 'input')
# soundfile expects an int, sounddevice provides a float:
samplerate = int(device_info['default_samplerate'])


def callback(indata, frames, time, status):
    # This is called (from a separate thread) for each audio block.
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))


def recognise(_cls, widget):
    '''Распознаёт речь пользователя.
    :param _cls: класс UI
    :param widget: виджет, в который выводятся сообщения об ошибках
    :return: возвращает распознанный текст
    '''
    mic_on = QtGui.QIcon.fromTheme("mic-on")  # Иконка для состояния распознавания речи
    mic_off = QtGui.QIcon.fromTheme("mic-off")  # Иконка для состояния покоя
    _cls.pushButton.setIcon(mic_on)  # Установка иконки во время распознавания речи
    
    print("[sys] Говорите...")

    try:    
        with sd.RawInputStream(samplerate=samplerate, blocksize = 8000, device=0, dtype='int16',
            channels=1, callback=callback):
            model = vosk.Model("model")
            rec = vosk.KaldiRecognizer(model, samplerate)
            print("[sys] Речь распознаётся...")
            while True:
                data = q.get()
                if rec.AcceptWaveform(data):
                    detect = json.loads(rec.Result())
                    say = detect["text"].capitalize()
                    print("[sys] Речь распознана.")
                    break
    except Exception as err:
        print(f"[sys] Не удалось распознать речь. Ошибка {err}.")
        speak.speak("Кажется, у меня проблемы со слухом. Не могу понять что ты говоришь.", widget)
        say = ''
    _cls.pushButton.setIcon(mic_off)  # Установка иконки спокойствия
    return say
