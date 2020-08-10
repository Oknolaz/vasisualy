# Vasisualy voice assistant :+1:
Vasisualy it's a simple russian voice assistant written on python 3 only for GNU/Linux. 
Vasisualy can tell the current time, tell about himself, make a funny story, tell about the weather, turn on music, open a browser, take screenshot, found your question in the web and send you to hell. Script supported only russian language.
## Getting Started
First, to run this script, you need to install the [RHVoice](https://github.com/Olga-Yakovleva/RHVoice/) speech synthesizer. Then you need to install the speechd module for python and VLC player using package manager for your distribution (like apt):
```
sudo apt-get install python3-speechd vlc
```
Next, you need to install the necessary modules via pip:
```
pip3 install pyowm playsound shell mss
```
Clone this repo with Git and go to the directory:
```
git clone https://github.com/Oknolaz/vasisualy
cd vasisualy
```
After these steps, just run the script in the terminal with this command for voice input:
```
python3 voice.py
```
Or for text input:
```
python3 text.py
```
Congratulations! :+1:

# Голосовой ассистент Васисуалий :+1:
Васисуалий - это простой голосовой ассистент, написанный на Python 3 и разработанный только для GNU/Linux.
Васисуалий может рассказать Вам текущее время, сказать о себе пару слов, заставить Вас смеяться от его смешных анекдотов, рассказать о текущей погоде в любом городе мира, включить любую вашу музыку, открыть браузер, сделать скриншот, искать заданный вопрос в интернете или послать Вас очень далеко за оскорбления. Программа поддерживает только русский язык.
## Установка
Для начала Вам понадобится установить синтезатор речи [RHVoice](https://github.com/Olga-Yakovleva/RHVoice/) (для инструкций по установке переходите по ссылке). Затем нужно нужно установить модуль speechd для Python и VLC плеер с помощью менеджера пакетов в вашем дистрибутиве (например apt):
```
sudo apt-get install python3-speechd vlc
```
Далее необходимо установить другие модули с помощью pip:
```
pip3 install pyowm playsound shell mss
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
Или этой для текстового ввода:
```
python3 text.py
```
Поздравляю Вас! :+1:
