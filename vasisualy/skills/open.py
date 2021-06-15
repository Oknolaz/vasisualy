import webbrowser
from ..core import speak
import subprocess

launch = ("Интернет", "интернет", "Браузер", "браузер", "Сеть", "сеть", "Включи интернет", "включи интернет",
          "Открой браузер", "открой браузер", "Включи браузер", "включи браузер", "Открой интернет", "открой интернет",
          "Включи сеть", "включи сеть", "Включи интернет сеть", "включи интернет сеть", "Всемирная паутина",
          "всемирная паутина", "Открой сеть", "открой сеть", "Подключись", "подключись", "Подключи", "подключи",
          "Подключи меня к сети", "подключи меня к сети", "Подключи сеть", "подключи сеть", "Подключи интернет",
          "подключи интернет", "Открой", "открой", "Запусти", "запусти", "Запуск", "запуск", "Программа", "программа",
          "Приложение", "приложение", "Включи", "включи")  # Команды открытия чего-либо

excludeList = ("Васисуалий", "Васисуали", "васисуалий", "васисуали", "Васян", "васян", "Васёк", "васёк", "Васися", "васися", "Васисяндра", "васисяндра", "Васька", "васька", "Вася", "вася", "Василий", "василий", "Пожалуйста", "пожалуйста")


def main(say, widget):
    for i in launch:
        if i in say:

            for net in ("Браузер", "браузер", "Интернет", "интернет", "Сеть", "сеть", "Паутина", "паутина"):
                if net in say:
                    try:
                        # Открытие браузера
                        speak.tts_d.speak("Я открыл браузер.")
                        webbrowser.open_new_tab("https://github.com/Oknolaz/Vasisualy")
                        toSpeak = "..."
                    except Exception:
                        toSpeak = "Не удалось открыть веб-браузер"
                            
            for yt in ("Youtube", "youtube", "Ютуб", "ютуб", "Ютьюб", "ютьюб", "Ютюб", "ютюб", "Утуб", "утуб"):
                if yt in say:
                    try:
                        speak.tts_d.speak("Открываю YouTube.")
                        webbrowser.open_new_tab('https://youtube.com/')
                        toSpeak = "..."
                    except Exception:
                        toSpeak = "Не удалось открыть YouTube."
                            
            for win in ("Окно", "окно", "Окошко", "окошко", "Дверь", "дверь", "Замок", "замок"):
                if win in say:
                    toSpeak = "Очень смешно..."
                    
            for fm in ("Файловый менеджер", "файловый менеджер", "Файлы", "файлы"):
                if fm in say:
                    toSpeak = "Открываю файловый менеджер."
                    try:
                        subprocess.Popen(["xdg-open", "/"])
                    except Exception:
                        toSpeak = "Не удалось открыть файловый менеджер."
                            
            for game in ("Игру", "игру", "Игра", "игра", "Игрушку", "игрушку", "Игрушка", "игрушка", "Майнкрафт",
                         "майнкрафт", "Манкрафт", "манкрафт", "Манкруфт", "манкруфт"):
                if game in say:
                    toSpeak = "Я не могу включать тебе игры. Сам включай!"
                    
            for goo in ("Google", "google", "Гугл", "гугл", "Гугаль", "гугаль", "Гугол", "гугол"):
                if goo in say:
                    try:
                        toSpeak = "Открываю сайт Google"
                        webbrowser.open_new_tab("https://google.com/")
                    except Exception:
                        toSpeak = "Не удалось открыть сайт Google."
                        
            for office in ("Офис", "офис", "LibreOffice", "libreoffice", "OpenOffice", "openoffice", "MicrosoftOffice",
                           "microsoftoffice"):
                if office in say:
                    toSpeak = "Открываю офисный пакет..."
                    try:
                        subprocess.Popen("libreoffice")
                    except Exception:
                        subprocess.Popen("openoffice")
                    except Exception:
                        toSpeak = "Не удалось открыть офисный пакет"
                        
            for writer in ("Текстовый процессор", "текстовый процессор", "Текстовый редактор", "текстовый редактор",
                           "Mousepad", "mousepad", "Kate", "kate", "KWrite", "kwrite", "Блокнот", "блокнот", "Notepad",
                           "notepad", "Редактор текста", "редактор текста"):
                if writer in say:
                    toSpeak = "Открываю текстовый редактор..."
                    try:
                        subprocess.Popen(["xdg-open", "README.md"])
                    except Exception:
                        toSpeak = "Не удалось открыть текстовый редактор."
                        
            for github in ("GitHub", "Github", "github", "Гитхаб", "гитхаб"):
                if github in say:
                    toSpeak = "Открываю сайт GitHub..."
                    try:
                        subprocess.Popen(["xdg-open", "https://github.com/"])
                    except Exception:
                        toSpeak = "Не удалось открыть сайт GitHub."
                        
            for terminal in ("Терминал", "терминал", "Командная строка", "командная строка", "Эмулятор терминала",
                             "эмулятор терминала", "Командную строку", "командную строку"):
                if terminal in say:
                    toSpeak = "Открываю терминал..."
                    try:
                        subprocess.Popen("x-terminal-emulator")
                    except Exception:
                        toSpeak = "Не удалось открыть эмулятор терминала."
                        
            for appStore in ("Центр программ", "центр программ", "аппстор", "апстор", "ап стор", "аппсторе", "апсторе",
                             "ап сторе", "апп стор", "апп сторе", "эппстор", "эппсторе", "эпп стор", "эпп сторе",
                             "эпстор", "эпсторе", "эп стор", "эп сторе", "Центр приложений", "центр приложений",
                             "Магазин программ", "магазин программ", "Магазин приложений", "магазин приложений",
                             "Установщик программ", "установщик программ", "Установщик приложений",
                             "установщик приложений", "Софтвэйр", "софтвэйр", "Софтвар", "софтвар", "Софтваре",
                             "софтваре", "Software", "software"):
                if appStore in say:
                    toSpeak = "Запускаю центр приложений..."
                    try:
                        subprocess.Popen("gnome-software")
                    except Exception:
                        subprocess.Popen("plasma-discover")
                    except Exception:
                        toSpeak = "Не удалось запустить центр приложений."
                            
            try:
                app = say.split()
                open_index = app.index(i)
                app = app[open_index + 1:]
                app = str(app)
                app = app.replace(i, '').replace(' ', '').replace("[", "").replace("]", "").replace('\'', "").replace(
                    ",", " ")
                subprocess.Popen(app)  # Запуск программы
                toSpeak = f"Я открыл {app}."
                break
            except Exception:
                pass
            break
        else:
            toSpeak = ""
    if toSpeak != "":
        speak.speak(toSpeak, widget)
    return toSpeak
