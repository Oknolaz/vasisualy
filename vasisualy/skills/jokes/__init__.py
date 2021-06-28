from vasisualy.skills.vas_skill.vas_skill import Skill  # Импорт родительского класса навыков
import requests
from bs4 import BeautifulSoup
import random


class Jokes(Skill):
    def get_jokes(self):
        site = requests.get("http://anekdotme.ru/random")
        bs = BeautifulSoup(site.text, "html.parser")
        selections = bs.select(".anekdot_text")

        jokes = []

        for selection in selections:
            selections = (selection.getText().strip())
            jokes.append(selections)

        return jokes

    def main(self, user_message):
        if super(Jokes, self)._is_triggered(user_message, super(Jokes, self)._get_triggers()):
            toSpeak = random.choice(self.get_jokes())
            return toSpeak
        else:
            return ''

def main(user_message):
    skill = Jokes("jokes", user_message)  # Вывод сообщения, переданного навыком, пользователю.
    return skill.main(user_message)
