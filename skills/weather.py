import random
from core import speak
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'

trigger = ("Какая погода во", "какая погода во", "Какая погода в", "какая погода в", "Погода во", "погода во", "Погода в", "погода в", "За окном в", "за окном в", "На улице в", "на улице в", "Погода на сегодня в", "погода на сегодня в", "Расскажи о погоде в", "расскажи о погоде в", "Расскажи про погоду в", "расскажи про погоду в", "Вэзэр в", "вэзэр в", "Везер в", "везер в", "Веазер в", "веазер в")

excludeList = ("Васисуалий", "Васисуали", "васисуалий", "васисуали", "Васян", "васян", "Васёк", "васёк", "Васися", "васися", "Васисяндра", "васисяндра", "Васька", "васька", "Вася", "вася", "Василий", "василий", "Пожалуйста", "пожалуйста")

def main(say, widget):
    for i in trigger:
        if i in say:
            weather_city = say.replace(i, '')
            weather_city = weather_city.replace(' ', '')
            for toExclude in excludeList:
                weather_city = weather_city.replace(toExclude, '')
            try:
                id = OWM('e45bc007f87a48d597d60091779f2d88', config_dict)  # API ключ Open weather map
                mgr = id.weather_manager()
                last = weather_city[-1]
                if last == 'е':
                    try:
                        city = weather_city.replace(weather_city[-1], "а")
                        observation = mgr.weather_at_place(city)
                        w = observation.weather
                        toSpeak = "В " + weather_city + " сейчас " + str(int(w.temperature('celsius')['temp'])) + " градусов по цельсию, " + w.detailed_status + "."
                        if float(w.temperature('celsius')['temp']) >= 20:
                            toSpeak += "\nСейчас на улице жарко. Идите загорать."
                        elif float(w.temperature('celsius')['temp']) <= 19 and float(w.temperature('celsius')['temp']) >= 10:
                            toSpeak += "\nЗа окном прохладно. Оденьте куртку."
                        elif float(w.temperature('celsius')['temp']) <= 9 and float(w.temperature('celsius')['temp']) >= 0:
                            toSpeak += "\nНа улице холодно. Оденьтесь в осеннюю одежду."
                        else:
                            toSpeak += "\nНа улице очень холодно, лучше туда не ходить. Выпейте горячего чаю."
                    except Exception:
                        pass
                    try:
                        city = weather_city[:-1]
                        observation = mgr.weather_at_place(city)
                        w = observation.weather
                        toSpeak = "В " + weather_city + " сейчас " + str(int(w.temperature('celsius')['temp'])) + " градусов по цельсию, " + w.detailed_status + "."
                        if float(w.temperature('celsius')['temp']) >= 20:
                            toSpeak += "\nСейчас на улице жарко. Идите загорать."
                        elif float(w.temperature('celsius')['temp']) <= 19 and float(w.temperature('celsius')['temp']) >= 10:
                            toSpeak += "\nЗа окном прохладно. Оденьте куртку."
                        elif float(w.temperature('celsius')['temp']) <= 9 and float(w.temperature('celsius')['temp']) >= 0:
                            toSpeak += "\nНа улице холодно. Оденьтесь в осеннюю одежду."
                        else:
                            toSpeak += "\nНа улице очень холодно, лучше туда не ходить. Выпейте горячего чаю."
                    except Exception:
                        pass
                    try:
                        city = weather_city.replace(weather_city[-1], "ь", count=1)
                        observation = mgr.weather_at_place(city)
                        w = observation.weather
                        toSpeak = "В " + weather_city + " сейчас " + str(int(w.temperature('celsius')['temp'])) + " градусов по цельсию, " + w.detailed_status + "."
                        if float(w.temperature('celsius')['temp']) >= 20:
                            toSpeak += "\nСейчас на улице жарко. Идите загорать."
                        elif float(w.temperature('celsius')['temp']) <= 19 and float(w.temperature('celsius')['temp']) >= 10:
                            toSpeak += "\nЗа окном прохладно. Оденьте куртку."
                        elif float(w.temperature('celsius')['temp']) <= 9 and float(w.temperature('celsius')['temp']) >= 0:
                            toSpeak += "\nНа улице холодно. Оденьтесь в осеннюю одежду."
                        else:
                            toSpeak += "\nНа улице очень холодно, лучше туда не ходить. Выпейте горячего чаю."
                    except Exception:
                        pass
                    try:
                        city = weather_city
                        observation = mgr.weather_at_place(city)
                        w = observation.weather
                        toSpeak = "В " + weather_city + " сейчас " + str(int(w.temperature('celsius')['temp'])) + " градусов по цельсию, " + w.detailed_status + "."
                        if float(w.temperature('celsius')['temp']) >= 20:
                            toSpeak += "\nСейчас на улице жарко. Идите загорать."
                        elif float(w.temperature('celsius')['temp']) <= 19 and float(w.temperature('celsius')['temp']) >= 10:
                            toSpeak += "\nЗа окном прохладно. Оденьте куртку."
                        elif float(w.temperature('celsius')['temp']) <= 9 and float(w.temperature('celsius')['temp']) >= 0:
                            toSpeak += "\nНа улице холодно. Оденьтесь в осеннюю одежду."
                        else:
                            toSpeak += "\nНа улице очень холодно, лучше туда не ходить. Выпейте горячего чаю."
                    except Exception:
                        pass
                    
                elif last == 'о':
                    try:
                        city = weather_city
                        observation = mgr.weather_at_place(city)
                        w = observation.weather
                        toSpeak = "В " + weather_city + " сейчас " + str(int(w.temperature('celsius')['temp'])) + " градусов по цельсию, " + w.detailed_status + "."
                        if float(w.temperature('celsius')['temp']) >= 20:
                            toSpeak += "\nСейчас на улице жарко. Идите загорать."
                        elif float(w.temperature('celsius')['temp']) <= 19 and float(w.temperature('celsius')['temp']) >= 10:
                            toSpeak += "\nЗа окном прохладно. Оденьте куртку."
                        elif float(w.temperature('celsius')['temp']) <= 9 and float(w.temperature('celsius')['temp']) >= 0:
                            toSpeak += "\nНа улице холодно. Оденьтесь в осеннюю одежду."
                        else:
                            toSpeak += "\nНа улице очень холодно, лучше туда не ходить. Выпейте горячего чаю."
                    except Exception:
                        pass
                        
                elif last == 'и':
                    try:
                        city = weather_city.replace(weather_city[-1], "ь")
                        observation = mgr.weather_at_place(city)
                        w = observation.weather
                        toSpeak("В " + weather_city + " сейчас " + str(int(w.temperature('celsius')['temp'])) + " градусов по цельсию, " + w.detailed_status + ".")
                        if float(w.temperature('celsius')['temp']) >= 20:
                            toSpeak += "\nСейчас на улице жарко. Идите загорать."
                        elif float(w.temperature('celsius')['temp']) <= 19 and float(w.temperature('celsius')['temp']) >= 10:
                            toSpeak += "\nЗа окном прохладно. Оденьте куртку."
                        elif float(w.temperature('celsius')['temp']) <= 9 and float(w.temperature('celsius')['temp']) >= 0:
                            toSpeak += "\nНа улице холодно. Оденьтесь в осеннюю одежду."
                        else:
                            toSpeak += "\nНа улице очень холодно, лучше туда не ходить. Выпейте горячего чаю."
                    except Exception:
                        pass
                        
                else:
                    try:
                        city = weather_city
                        observation = mgr.weather_at_place(city)
                        w = observation.weather
                        toSpeak = "В " + weather_city + " сейчас " + str(int(w.temperature('celsius')['temp'])) + " градусов по цельсию, " + w.detailed_status + "."
                        if float(w.temperature('celsius')['temp']) >= 20:
                            toSpeak += "\nСейчас на улице жарко. Идите загорать."
                        elif float(w.temperature('celsius')['temp']) <= 19 and float(w.temperature('celsius')['temp']) >= 10:
                            toSpeak += "\nЗа окном прохладно. Оденьте куртку."
                        elif float(w.temperature('celsius')['temp']) <= 9 and float(w.temperature('celsius')['temp']) >= 0:
                            toSpeak += "\nНа улице холодно. Оденьтесь в осеннюю одежду."
                        else:
                            toSpeak += "\nНа улице очень холодно, лучше туда не ходить. Выпейте горячего чаю."
                    except Exception:
                        pass

            except Exception:
                toSpeak = "Такого города не существует или у меня нет подключения к интернету!"
            break
        else:
            toSpeak = ""
            
    if toSpeak != "":
        speak.speak(toSpeak, widget)
            
    return toSpeak
