# Голосовой ассистент Васисуалий :+1:
Васисуалий - это простой голосовой помощник, уважающий вашу свободу, для GNU/Linux, Windows и [Android](https://github.com/Oknolaz/vasisualy-android). Поддерживается только русский язык.
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
sudo apt-get install python3-speechd python3-pyqt5 vlc python3-pyqt5.qtwebengine python3-pyaudio python3-vlc
```
Далее необходимо установить другие модули с помощью pip:
```
pip3 install -r requirements.txt
```
Клонируйте данный репозиторий с помощью Git:
```
git clone https://github.com/Oknolaz/vasisualy
cd vasisualy
```
После этих действий можно запускать скрипт этой командой для Qt GUI версии:
```
python3 run.py
```
**Также доступен [AUR пакет](https://aur.archlinux.org/packages/vasisualy-git/) для установки в Arch Linux.**
### CLI для GNU/Linux
Для CLI версии с распознаванием речи, адаптированной для одноплатных компьютеров (Raspberry Pi, Orange Pi и др.):
```
git clone https://github.com/Oknolaz/vasisualy-pi
cd vasisualy-pi
python3 run.py
```
### Windows
Вам нужно установить [интерпретатор python3](https://python.org) и [VLC media player](https://videolan.org/). После установки интерпретатора - установите необходимые модули python с помощью pip:
```
pip install pyowm mss qt-material jinja2 pyttsx3 python-vlc pyqtwebengine wikipedia geocoder beautifulsoup4 lxml SpeechRecognition pyaudio translate
```
Затем скачайте [данный репозиторий](https://github.com/Oknolaz/vasisualy-windows/), распакуйте скачанный архив и перейдите в папку с программой.
Далее просто запустите скрипт командой:
```
python main.py
```
Поздравляю Вас! :+1:

## Лицензия
Vasisualy - это свободное программное обеспечение: вы можете использовать и изменять его по условиям лицензии GNU General Public License 3.0.

## Обратная связь
Telegram: [@oknolaz_dev](https://t.me/oknolaz_dev)

Matrix: [@oknolaz:matrix.org](https://matrix.to/#/@oknolaz:matrix.org)


## Пожертвования
**Bitcoin**: bc1qjv3zkfdn62tegn2nc36p722pxnup2fpm8lteq0
