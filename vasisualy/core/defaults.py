import json

defaults = {
    "voice": "Artemiy",
    "speed": 30,
    "pitch": 0,
    "wiki_sentences": 4,
    "music": "music/",
    "theme": "Dark Red",
    "from_lang": "ru",
    "to_lang": "en",
    "weather_api": "",
    "weather_city": "Лондон"
}


def get_value(param):
    '''
    Получение параметра из файла настройки JSON.
    :param param: нужный параметр.
    :return: значение, соответствующее параметру.
    '''
    with open("vasisualy.json", "r") as f:
        settings = json.load(f)
        value = settings[param]
    return value