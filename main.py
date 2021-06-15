#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# GUI
from .ui import design
from PyQt5 import QtWidgets
import sys
from qt_material import apply_stylesheet

# Core
from .core import (speak, talk, recognise)
import random

# Skills
from .skills import (skill_loader, time_date, exit, joke, weather, music, open, screenshot, search, poweroff, ytvideo,
                     resay, map, wiki, location, weather_no_city, translate, news, coin, upd_upg, shoplist, todolist,
                     netconnection, record, guess_num, rulette, math, audio, crystal_ball, random_num, timer,
                     show_about, show_settings, old_skills)


# Ответы на неизвестную команду.
wrong = ("Прости, я тебя не понимаю.", "Мне кажется ты несёшь какой-то бред.", "Что?",
         "Ты, наверное, ошибаешься. Я тебя не понимаю.",
         "Извини, я появился совсем недавно, я пока понимаю очень мало слов.",
         "Чего?", "А? Что? Я тебя не понимаю.", "Пожалуйста, не говори слов, которых я незнаю.",
         "Ты пытаешься оскорбить меня этим?", "Не издевайся надо мной, я знаю не так много слов.",
         "Извини, я не могу тебя понять.", "А?", "Объясни попроще.",
         "Пожалуйста, прочитай моё описание. Скорее всего я не умею делать то, что ты меня просишь или попробуй использовать синонимы.",
         "Ты ошибаешься.", "Я не понимаю твоего вопроса.", "Мне не понятен твой вопрос.",
         "Не могу понять о чём ты говоришь.", "Я не понимаю.", "О чём ты?", "Я не могу распознать вопрос.")

randnum = -1
isGuessNum = False
isRuLette = False


class Main(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Инициализация графического интерфейса
        super().__init__()
        self.setupUi(self)

        self.lineEdit.setFocus()
        # Передача информации, которую нужно озвучить и вывести на экран, модулю speak
        speak.speak("Привет, меня зовут Васисуалий. Чем могу быть полезен?", self.listWidget)

        skill_loader.load()  # Импорт "новых" навыков

        self.lineEdit.editingFinished.connect(self.vasmsg)
        self.pushButton.clicked.connect(self.recogniser)
        self.aboutMenu.triggered.connect(self.showAboutDialog)
        self.settingsMenu.triggered.connect(self.showSettingsDialog)

    def showAboutDialog(self):
        self.dialog = show_about.ShowAboutWindow()
        self.dialog.show()

    def showSettingsDialog(self):
        self.dialog = show_settings.ShowSettingsWindow()
        self.dialog.show()

    def vasmsg(self):
        # Функция берёт переданный в виджет lineEdit текст, очищает виджет и запускает программу
        self.say = self.lineEdit.text()
        self.lineEdit.clear()
        self.listWidget.scrollToBottom()
        self.say = self.say.capitalize()
        self.program()

    def recogniser(self):
        self.say = recognise.recognise(self, self.listWidget)  # Вызов функции распознавания речи
        self.program()

    def program(self):
        say = self.say
        skillUse = False
        
        if say == '' or say == ' ':
            pass
        else:
            # Вывод сообщения пользователя
            item = QtWidgets.QListWidgetItem(say)
            item.setTextAlignment(0x0002)
            self.listWidget.addItem(item)

        if old_skills.old_skills_activate(say, self.listWidget, self):
            skillUse = True

        elif guess_num.isTriggered(say):
            skillUse = True
            global randnum, isGuessNum
            randnum = guess_num.getRandomNum()
            isGuessNum = guess_num.startGame(self.listWidget)

        elif rulette.isTriggered(say):
            skillUse = True
            global isRuLette
            isRuLette = rulette.startGame(self.listWidget)

        elif skill_loader.run_skills(say, self.listWidget):
            skillUse = True
        
        elif say == 'stop' or say == 'Stop' or say == 'Стоп' or say == 'стоп':
            speak.tts_d.stop()
                
        elif isGuessNum:
            isGuessNum = guess_num.game(say, randnum, self.listWidget)
            
        elif isRuLette:
            isRuLette = rulette.game(say, self.listWidget)
            
        else:
            if talk.talk(say) != "" and not skillUse:
                speak.speak(talk.talk(say), self.listWidget)
            elif not skillUse:
                if say != "":
                    # Фразы для ответа на несуществующие команды
                    randwrong = random.choice(wrong)
                    speak.speak(randwrong, self.listWidget)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    apply_stylesheet(app, theme='dark_red.xml')
    window.show()
    app.exec_()
    speak.tts_d.close()


if __name__ == '__main__':
    main()
