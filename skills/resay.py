from core import speak

trigger = ("Повтори", "повтори", "Повторяй", "повторяй", "Повтори за мной", "повтори за мной") # Команды повторения
excludeList = ("Васисуалий", "Васисуали", "васисуалий", "васисуали", "Васян", "васян", "Васёк", "васёк", "Васися", "васися", "Васисяндра", "васисяндра", "Васька", "васька", "Вася", "вася", "Василий", "василий", "Пожалуйста", "пожалуйста")

def main(say, widget):
    for i in trigger:
        if i in say:
            hesay = say.replace(i, "")
            for toExclude in excludeList:
                hesay = hesay.replace(toExclude, '')
            toSpeak = hesay
            break
        else:
            toSpeak = ""
    
    if toSpeak != "":
        speak.speak(toSpeak, widget)
    return toSpeak
