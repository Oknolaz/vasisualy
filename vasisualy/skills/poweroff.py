import subprocess
from ..core import speak
from threading import Thread
from ru_word2number import w2n
from time import sleep
from plyer import notification

# Команды выключения пк
poweroff = ("Выключи пк", "выключи пк", "Выключи ПК", "выключи ПК", "Выключи компьютер", "выключи компьютер")
reboot = ("Перезагрузи пк", "перезагрузи пк", "Перезагрузи ПК", "перезагрузи ПК", "Перезагрузи компьютер",
          "перезагрузи компьютер", "Перезагрузка", "перезагрузка")  # Команды перезагрузки пк

time = 0
listWidget = None


def poweroffProcess():
    sleep(time)
    try:
        notification.notify(title="Выключение устройства.",
                            message="Программа Васисуалий завершает работу устройства.",
                            timeout=10)
    except Exception:
        pass
    sleep(2)
    speak.speak("Выключаю компьютер. До свидания.", listWidget)
    subprocess.Popen("systemctl", "poweroff")  # Выключение ПК
    exit()


def rebootProcess():
    sleep(time)
    try:
        notification.notify(title="Перезагрузка устройства.",
                            message="Программа Васисуалий перезагружает устройство.",
                            timeout=10)
    except Exception:
        pass
    sleep(2)
    speak.speak("Перезагружаю компьютер.", listWidget)
    subprocess.Popen("systemctl", "reboot")
    exit()


def main(say, widget):
    for i in poweroff:
        if i in say:
            times = []
            for word in say.split():
                try:
                    num = w2n.word_to_num(word)  # Преобразование слов из входящего сообщения в числа
                    times.append(num)
                except ValueError:
                    pass

            while len(times) > 1:
                times.pop()  # Удаление лишних чисел

            if len(times) == 0 or int(times[0]) == 0:
                offTime = 0
            else:
                if "секунд" in say:
                    offTime = int(times[0])
                elif "минут" in say:
                    offTime = int(times[0]) * 60
                elif "час" in say:
                    offTime = int(times[0]) * 60 * 60
                elif "день" in say or "дней" in say or "дня" in say or "сутки" in say or "суток" in say:
                    offTime = int(times[0]) * 60 * 60 * 24
                else:
                    offTime = int(times[0]) * 60

            if offTime >= 60:
                toSpeak = "Устройство будет выключено через " + str(offTime / 60) + " минут."
            elif offTime >= 3600:
                toSpeak = "Устройство будет выключено через " + str(offTime / 3600) + " часов."
            elif offTime >= 86400:
                toSpeak = "Устройство будет выключено через " + str(offTime / 86400) + " дней."
            else:
                toSpeak = "Устройство будет выключено через " + str(offTime) + " секунд."
            global time, listWidget
            time = offTime
            listWidget = widget
            th = Thread(target=poweroffProcess)  # Инициализация потока
            th.start()  # Запуск потока
            break
        else:
            toSpeak = ""

        for i in reboot:
            if i in say:
                times = []
                for word in say.split():
                    try:
                        num = w2n.word_to_num(word)  # Преобразование слов из входящего сообщения в числа
                        times.append(num)
                    except ValueError:
                        pass

                while len(times) > 1:
                    times.pop()  # Удаление лишних чисел

                if len(times) == 0 or int(times[0]) == 0:
                    offTime = 0
                else:
                    if "секунд" in say:
                        offTime = int(times[0])
                    elif "минут" in say:
                        offTime = int(times[0]) * 60
                    elif "час" in say:
                        offTime = int(times[0]) * 60 * 60
                    elif "день" in say or "дней" in say or "дня" in say or "сутки" in say or "суток" in say:
                        offTime = int(times[0]) * 60 * 60 * 24
                    else:
                        offTime = int(times[0]) * 60

                if offTime >= 60:
                    toSpeak = "Устройство будет перезагружено через " + str(offTime / 60) + " минут."
                elif offTime >= 3600:
                    toSpeak = "Устройство будет перезагружено через " + str(offTime / 3600) + " часов."
                elif offTime >= 86400:
                    toSpeak = "Устройство будет перезагружено через " + str(offTime / 86400) + " дней."
                else:
                    toSpeak = "Устройство будет перезагружено через " + str(offTime) + " секунд."
                time = offTime
                listWidget = widget
                th = Thread(target=rebootProcess)  # Инициализация потока
                th.start()  # Запуск потока
                break

    if toSpeak:
        speak.speak(toSpeak, widget)
    return toSpeak
