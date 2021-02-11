from core import speak
from bs4 import BeautifulSoup
import requests

trigger = ("Какие новости", "какие новости", "Что нового в мире", "что нового в мире", "Что интересного расскажешь", "что интересного расскажешь", "Что происходит в мире", "что происходит в мире", "Что творится в мире", "что творится в мире", "Какие на сегодня новости", "какие на сегодня новости", "Что сегодня нового", "что сегодня нового")

def main(say, widget):
    for i in trigger:
        if i in say:
            try:
                site = requests.get("https://ru.wikinews.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%9E%D0%BF%D1%83%D0%B1%D0%BB%D0%B8%D0%BA%D0%BE%D0%B2%D0%B0%D0%BD%D0%BE")
                site = site.text
                soup = BeautifulSoup(site, 'lxml')
                heads = soup.find("ul").find_all("a")
                list_news = []
                cnt_parse = 0
                for head in heads:
                    if cnt_parse < 5:
                        list_news.append(head.string + ".")
                        cnt_parse += 1
                toSpeak = "Вот, что сегодня нового: "
                for new in list_news:
                    toSpeak += f"\n{new}"
            except Exception:
                toSpeak = "Для сообщения новостей мне необходим интернет."
            break
        else:
            toSpeak = ""
            
    if toSpeak != "":
        speak.speak(toSpeak, widget)
    return toSpeak
