# Vasisualy voice assistant :+1:
Vasisualy it's a simple russian voice assistant written on python 3 for GNU/Linux and Windows. 
Vasisualy can tell the current time, tell about himself, make a funny story, tell about the weather, turn on music, open a browser, take screenshot, found your question in the web and send you to hell. Script supported only russian language.
## Automatic installation for Debian
### Installer work only on Debian/Ubuntu distros!
For automatic graphical installation, download the archive with the installer from the [Releases](https://github.com/Oknolaz/vasisualy/releases) page.
![Image alt](https://github.com/Oknolaz/vasisualy/blob/master/install.png)
Unpack the folder inside it to your home directory. It should look like this: /home/user/vasisualy-installer/. This can be done with the command:
```
tar -xf vasisualy-installer.tar.bz2
```
Change to the directory that appears:
```
cd vasisualy-installer
```
Then run the executable file vasisualy-install in your graphical environment or with the command:
```
./vasisualy-install
```
Just follow the instructions and enter your password every time you are asked, otherwise the installation will fail.
## Getting Started
### GNU/Linux
First, to run this script, you need to install the [RHVoice](https://github.com/Olga-Yakovleva/RHVoice/) speech synthesizer. Then you need to install the speechd module for python, PyQt5 and VLC player using package manager for your distribution (like apt):
```
sudo apt-get install python3-speechd python3-pyqt5 python3-pyqt5.qtwebengine python3-vlc
```
Next, you need to install the necessary modules via pip:
```
pip3 install pyowm shell mss pyqt5_material pyqt5-notificator jinja2
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
 pyqtwebengine
```
Next, just run the following command to launch the app:
```
python vasisualy-win.py
```
Congratulations! :+1:

# Голосовой ассистент Васисуалий :+1:
Васисуалий - это простой голосовой ассистент, написанный на Python 3 для GNU/Linux и Windows.
Васисуалий может рассказать Вам текущее время, сказать о себе пару слов, заставить Вас смеяться от его смешных анекдотов, рассказать о текущей погоде в любом городе мира, включить любую вашу музыку, открыть браузер, сделать скриншот, искать заданный вопрос в интернете или послать Вас очень далеко за оскорбления. Программа поддерживает только русский язык.
## Автоматический установщик для Debian
### Установщик работает только на дистрибутивах Debian и их производных (Ubuntu)!
Для автоматической графической установки необходимо загрузить архив с установщиком со страницы [Releases](https://github.com/Oknolaz/vasisualy/releases).
![Image alt](https://github.com/Oknolaz/vasisualy/blob/master/install.png)
Распакуйте папку, находящуюся внутри него в домашнюю директорию. Должно получиться так: /home/user/vasisualy-installer/. Это можно сделать командой:
```
tar -xf vasisualy-installer.tar.bz2
```
Перейдите в появившуюся директорию:
```
cd vasisualy-installer 
```
Далее запустите исполняемый файл vasisualy-install в своей графической среде или командой:
```
./vasisualy-install
```
Просто следуйте инструкциям и вводите пароль каждый раз, когда вас спросят, иначе установка не произойдёт.
## Запуск без установки
### GNU/Linux
Для начала Вам понадобится установить синтезатор речи [RHVoice](https://github.com/Olga-Yakovleva/RHVoice/). Затем нужно нужно установить модуль speechd для Python, PyQt5 и VLC плеер с помощью менеджера пакетов в вашем дистрибутиве (например apt):
```
sudo apt-get install python3-speechd python3-pyqt5 vlc python3-pyqt5.qtwebengine
```
Далее необходимо установить другие модули с помощью pip:
```
pip3 install pyowm shell mss pyqt5_material pyqt5-notificator jinja2
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
pip install pyowm mss pyqt5_material jinja2 pyqt5-notificator pyttsx3 python-vlc pyqtwebengine
```
Далее просто запустите скрипт командой:
```
python vasisualy-win.py
```
Поздравляю Вас! :+1:

## Обратная связь
Telegram: @oknolaz_dev

matrix.org: @oknolaz
