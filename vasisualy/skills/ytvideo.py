from ..core import speak
import webbrowser

trigger = ("Найди видео", "найди видео", "Поиск видео", "поиск видео", "Найти видео", "найти видео", "Включи видео", "включи видео", "Давай видео", "давай видео", "Ищи видео", "ищи видео") # Команды поиска видео в Youtube
excludeList = ("Васисуалий", "Васисуали", "васисуалий", "васисуали", "Васян", "васян", "Васёк", "васёк", "Васися", "васися", "Васисяндра", "васисяндра", "Васька", "васька", "Вася", "вася", "Василий", "василий", "Пожалуйста", "пожалуйста")

def main(say, widget):
    for i in trigger:
        if i in say:
            video_search = say.replace(i, '')
            for toExclude in excludeList:
                video_search = video_search.replace(toExclude, '')
            toSpeak = f'Ищу видео {video_search}.'
            try:
                webbrowser.open_new_tab(f"https://www.youtube.com/results?search_query={video_search}")
            except Exception:
                toSpeak = "Не удалось открыть браузер."
            break
        else:
            toSpeak = ""
            
    if toSpeak != "":
        speak.speak(toSpeak, widget)
    return toSpeak
