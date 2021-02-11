from core import speak
from skills import location
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'

trigger = ("Погода", "погода", "Погода завтра", "погода завтра", "Погода сегодня", "погода сегодня", "Погода на завтра", "погода на завтра", "Погода на сегодня", "погода на сегодня", "Погода на неделю", "погода на неделю", "Погоду на сегодня", "Погоду на завтра", "Погоду на неделю", "Погоду")

def main(say, widget):
    for i in trigger:
        if i == say:
            id = OWM('e45bc007f87a48d597d60091779f2d88', config_dict) # API ключ Open weather map
            mgr = id.weather_manager()
            try:
                city = location.geo.city
                observation = mgr.weather_at_place(city)
                w = observation.weather
                toSpeak = "В " + city + " сейчас " + str(int(w.temperature('celsius')['temp'])) + " градусов по цельсию, " + w.detailed_status + "."
                if float(w.temperature('celsius')['temp']) >= 20:
                    toSpeak += "\nСейчас на улице жарко. Идите загорать."
                elif float(w.temperature('celsius')['temp']) <= 19 and float(w.temperature('celsius')['temp']) >= 10:
                    toSpeak += "\nЗа окном прохладно. Оденьте куртку."
                elif float(w.temperature('celsius')['temp']) <= 9 and float(w.temperature('celsius')['temp']) >= 0:
                    toSpeak += "\nНа улице холодно. Оденьтесь в осеннюю одежду."
                else:
                    toSpeak += "\nНа улице очень холодно, лучше туда не ходить. Выпейте горячего чаю."
            except Exception:
                toSpeak = "Пожалуйста, укажите название города!"
            break
        else:
            toSpeak = ""
            
    if toSpeak != "":
        speak.speak(toSpeak, widget)
    return toSpeak
