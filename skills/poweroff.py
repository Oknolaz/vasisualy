import subprocess
from core import speak

poweroff = ("Выключи пк", "выключи пк", "Выключи ПК", "выключи ПК", "Выключи компьютер", "выключи компьютер") # Команды выключения пк
reboot = ("Перезагрузи пк", "перезагрузи пк", "Перезагрузи ПК", "перезагрузи ПК", "Перезагрузи компьютер", "перезагрузи компьютер", "Перезагрузка", "перезагрузка") # Команды перезагрузки пк

def main(say):
    for i in poweroff:
        if i in say:
            speak.tts_d.speak("Я выключаю компьтер. До свидания.")
            subprocess.run("systemctl", "poweroff")
        
    for i in reboot:
        if i in say:
            speak.tts_d.speak("До встречи!")
            subprocess.run("systemctl", "reboot")
        else:
            toSpeak = ""
            
    return toSpeak
