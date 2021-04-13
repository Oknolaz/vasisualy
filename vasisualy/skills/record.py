from ..core import speak
from scipy.io.wavfile import write
import sounddevice
import vlc
import time

record = ("Запиши аудио", "запиши аудио", "Запиши с микрофона", "запиши с микрофона", "Запиши звук с микрофона", "запиши звук с микрофона", "Сделай аудиозапись", "сделай аудиозапись")
play = ("Воспроизведи аудиозапись", "воспроизведи аудиозапись", "Включи аудиозапись", "включи аудиозапись")

def main(say, widget):
    for i in record:
        if i in say:
            fs = 44100 # Частота
            seconds = 5 # Время записи
            audio = sounddevice.rec(int(seconds * fs), samplerate=fs, channels=2) # Запись аудио с микрофона
            sounddevice.wait()
            write("audio_record.wav", fs, audio) # Запись в файл
            toSpeak = "Я сделал аудиозапись."
            break
        else:
            toSpeak = ""
            
    for i in play:
        if i in say:
            try:
                player = vlc.MediaPlayer("audio_record.wav") # Воспроизведение записанного
                player.play()
                time.sleep(5)
                toSpeak = "Сейчас была воспроизведена аудиозапись."
            except Exception:
                toSpeak = "Не удалось воспроизвести аудиозапись. Возможно ты её не создал."
            break
            
    if toSpeak != "":
        speak.speak(toSpeak, widget)
    return toSpeak
            
