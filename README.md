# Vasisualy voice assistant :+1:
Vasisualy it's a simple russian voice assistant written on python 3 for GNU/Linux and Windows. 
Vasisualy can tell the current time, tell about himself, make a funny story, tell about the weather, turn on music, open a browser, take screenshot, found your question in the web and send you to hell. Script supported only russian language.
## Vasisualy can:
- Tell the current date and time.
- Tell a joke.
- Tell about the current weather in any city.
- Turn on the radio (hip-hop, pop, rock, dance, etc.).
- Open browser, web site (like YouTube).
- Launch the app installed on your PC.
- Make a screenshot.
- Search for information on the Internet.
- Shutdown or reboot your PC.
- Search for videos on YouTube.
- Repeat your words like a parrot.
- Flip a coin.
- Say a tongue twister.
- Launch OpenStreetMap.
- Find answer for your question on [Wikipedia](https://wikipedia.org/).
- Tell where you are.
- Translate any text from all languages to Russian, Spanish, Deutch, English, Francais and other.
- Tell news from [Wikinews](https://wikinews.org/).
- Play Guess the number game and Russian roulette with you.
- Communicate primitively.
- And more...
## Getting Started
### GNU/Linux
First, to run this script, you need to install the [RHVoice](https://github.com/Olga-Yakovleva/RHVoice/) speech synthesizer (for Ubuntu):
```
sudo add-apt-repository ppa:linvinus/rhvoice
sudo apt-get update
sudo apt-get install speech-dispatcher-rhvoice rhvoice-russian
```
Then you need to install the speechd module for python, PyQt5 and VLC player using package manager for your distribution (like apt):
```
sudo apt-get install python3-speechd python3-pyqt5 python3-pyqt5.qtwebengine python3-vlc
```
Next, you need to install the necessary modules via pip:
```
pip3 install pyowm shell mss pyqt5_material pyqt5-notificator jinja2 wikipedia geocoder googletrans
```
Clone this repo with Git and go to the directory:
```
git clone https://github.com/Oknolaz/vasisualy
cd vasisualy
```
After these steps, just run the script in the terminal with this command for Qt GUI version without speech recognition:
```
python3 vasisualy-qt.py
```
For CLI version with speech recognition, adapted for single board computers:
```
python3 vasisualy-pi.py
```
### Windows
You need to install [python3 interpreter](https://python.org) and [VLC media player](https://videolan.org/). After that install python modules via pip:
```
pip install pyowm mss pyqt5_material jinja2 pyqt5-notificator pyttsx3 python-vlc
 pyqtwebengine wikipedia geocoder googletrans
```
Next, just run the following command to launch the app:
```
python vasisualy-win.py
```
Congratulations! :+1:

# Голосовой ассистент Васисуалий :+1:
Васисуалий - это простой голосовой помощник, уважающий вашу свободу, для GNU/Linux и Windows. Поддерживается только русский язык.
## Васисуалий может:
- Сказать текущую дату и время.
- Рассказать анекдот.
- Сказать о текущей погоде в любом городе мира.
- Включить радио (хип-хоп, поп, рок, техно и др.).
- Открыть браузер или веб-сайт (например, YouTube).
- Запустить программу, установленную на вашем ПК.
- Сделать снимок экрана.
- Искать информацию в Итернете.
- Выключить или перезагрузить компьютер.
- Искать видео на YouTube.
- Повторять ваши слова, как попугай.
- Подкинуть монетку.
- Сказать скороговорку.
- Открыть карты (OpenStreetMap)
- Искать ответ на ваш вопрос в [Википедии](https://wikipedia.org).
- Сказать где вы.
- Перевести текст с любого языка на русский, испанский, английский, французский, итальянский и др..
- Рассказать новости с [Wikinews](https://wikinews.org/).
- Сыграть в Угадай число и Русскую рулетку с вами.
- Примитивно общаться.
- И многое другое...
## Начало работы
### GNU/Linux
Для начала Вам понадобится установить синтезатор речи [RHVoice](https://github.com/Olga-Yakovleva/RHVoice/) (для Ubuntu):
```
sudo add-apt-repository ppa:linvinus/rhvoice
sudo apt-get update
sudo apt-get install speech-dispatcher-rhvoice rhvoice-russian
```
Затем нужно нужно установить модуль speechd для Python, PyQt5 и VLC плеер с помощью менеджера пакетов в вашем дистрибутиве (например apt):
```
sudo apt-get install python3-speechd python3-pyqt5 vlc python3-pyqt5.qtwebengine
```
Далее необходимо установить другие модули с помощью pip:
```
pip3 install pyowm shell mss pyqt5_material pyqt5-notificator jinja2 wikipedia geocoder googletrans
```
Клонируйте данный репозиторий с помощью Git:
```
git clone https://github.com/Oknolaz/vasisualy
cd vasisualy
```
После этих действий можно запускать скрипт этой командой для Qt GUI версии без распознавания речи:
```
python3 vasisualy-qt.py
```
Для CLI версии с распознаванием речи, адаптированной для одноплатных компьютеров (Raspberry Pi, Orange Pi и др.):
```
python3 vasisualy-pi.py
```
### Windows
Вам нужно установить [интерпретатор python3](https://python.org) и [VLC media player](https://videolan.org/). После установки интерпретатора - установите необходимые модули python с помощью pip:
```
pip install pyowm mss pyqt5_material jinja2 pyqt5-notificator pyttsx3 python-vlc pyqtwebengine wikipedia geocoder googletrans
```
Далее просто запустите скрипт командой:
```
python vasisualy-win.py
```
Поздравляю Вас! :+1:

## Обратная связь
Telegram: @oknolaz_dev

Matrix: @oknolaz:matrix.org
