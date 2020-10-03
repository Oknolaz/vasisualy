# Vasisualy voice assistant :+1:
Vasisualy it's a simple russian voice assistant written on python 3 only for GNU/Linux. 
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
First, to run this script, you need to install the [RHVoice](https://github.com/Olga-Yakovleva/RHVoice/) speech synthesizer. Then you need to install the speechd module for python, PyQt5 and VLC player using package manager for your distribution (like apt):
```
sudo apt-get install python3-speechd python3-pyqt5 vlc python3-pyqt5.qtwebengine
```
Next, you need to install the necessary modules via pip:
```
pip3 install pyowm shell mss pyqt5_material pyqt5-notificator
```
Clone this repo with Git and go to the directory:
```
git clone https://github.com/Oknolaz/vasisualy
cd vasisualy
```
After these steps, just run the script in the terminal with this command for voice input:
```
python3 vasisualy-voice.py
```
For GUI Qt version:
```
python3 vasisualy-qt.py
```
Congratulations! :+1:

# Голосовой ассистент Васисуалий :+1:
Васисуалий - это простой голосовой ассистент, написанный на Python 3 и разработанный только для GNU/Linux.
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
Для начала Вам понадобится установить синтезатор речи [RHVoice](https://github.com/Olga-Yakovleva/RHVoice/). Затем нужно нужно установить модуль speechd для Python, PyQt5 и VLC плеер с помощью менеджера пакетов в вашем дистрибутиве (например apt):
```
sudo apt-get install python3-speechd python3-pyqt5 vlc python3-pyqt5.qtwebengine
```
Далее необходимо установить другие модули с помощью pip:
```
pip3 install pyowm shell mss pyqt5_material pyqt5-notificator
```
Клонируйте данный репозиторий с помощью Git:
```
git clone https://github.com/Oknolaz/vasisualy
cd vasisualy
```
После этих действий можно запускать скрипт этой командой для голосового ввода:
```
python3 voice.py
```
Для версии с GUI:
```
python3 vasisualy-qt.py
```
Поздравляю Вас! :+1:
