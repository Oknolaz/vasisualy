from ..core import speak
from threading import Thread
import datetime
from ru_word2number import w2n
from time import sleep
import vlc
from plyer import notification
import os

inst = vlc.Instance()
player = inst.media_player_new()
time = 0
listWidget = None

trigger = ("Поставь таймер на ", "поставь таймер на ", "Включи таймер на ", "включи таймер на ", "Поставь таймер",
           "поставь таймер", "Включи таймер", "включи таймер")


def timerProcess():
    sleep(time)
    try:
        notification.notify(title="Время вышло!", message="Таймер сработал.", timeout=20)
    except Exception:
        pass
    appDir = os.path.dirname(os.path.realpath(__file__))
    media = inst.media_new(f"{appDir}/../assets/beep.wav")
    player.set_media(media)
    player.play()
    speak.speak("Таймер сработал.", listWidget)


def main(say, widget):
    for i in trigger:
        if i in say:
            global time, listWidget
            now = datetime.datetime.now().strftime("%H %M %S")
            time = []
            for word in say.split():
                try:
                    num = w2n.word_to_num(word)  # Преобразование слов из входящего сообщения в числа
                    time.append(num)
                except ValueError:
                    pass
                
            while len(time) > 1:
                time.pop()
                
            if len(time) == 0 or int(time[0]) == 0:
                workTime = 30
            else:
                if "секунд" in say:
                    workTime = int(time[0])
                elif "минут" in say:
                    workTime = int(time[0]) * 60
                elif "час" in say:
                    workTime = int(time[0]) * 60 * 60
                elif "день" in say or "дней" in say or "дня" in say or "сутки" in say or "суток" in say:
                    workTime = int(time[0]) * 60 * 60 * 24
                else:
                    workTime = int(time[0]) * 60
            
            if workTime >= 60:
                toSpeak = "Таймер запущен на " + str(workTime / 60) + " минут."
            elif workTime >= 3600:
                toSpeak = "Таймер запущен на " + str(workTime / 3600) + " часов."
            elif workTime >= 86400:
                toSpeak = "Таймер запущен на " + str(workTime / 86400) + " дней."
            else:
                toSpeak = "Таймер запущен на " + str(workTime) + " секунд."
            time = workTime
            listWidget = widget
            th = Thread(target=timerProcess)
            th.start()
            break
        else:
            toSpeak = ""
    
    if toSpeak != "":
        speak.speak(toSpeak, widget)
    return toSpeak
