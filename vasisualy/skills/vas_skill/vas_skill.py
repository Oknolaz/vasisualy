import os
import sys
from pathlib import Path


class Skill:
    '''Родительский класс для всех "новых" и сторонних навыков.
    :param: name - название навыка. Должно быть как название директории, содержащей навык (string).
    :param: use_settings - определяет использует ли навык собственные настройки (boolean) - на данный момент недоступно!
    '''
    def __init__(self, name, use_settings=False):
        self.name = name
        self.root = os.path.dirname(os.path.abspath(sys.modules[self.__module__].__file__))  # Определение расположения навыка
        if use_settings:
            self.settings_path = Path(self.root)

    def _get_triggers(self):
        # Считывание триггеров навыка из файла trigger в его директории
        file = open(f"{str(Path(self.root))}/{self.name}.trigger")
        triggers = []
        for line in file:
            if line != "\n":
                triggers.append(line.replace("\n", ''))
        return triggers

    @staticmethod
    def _is_triggered(user_message, triggers):
        # Проверяет соответствует ли сообщение, переданное пользователем, триггеру.
        for trigger in triggers:
            if trigger in user_message:
                triggered = True
                break
            else:
                triggered = False
        return triggered
