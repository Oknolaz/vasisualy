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

### Debian/Ubuntu
Для начала Вам понадобится установить синтезатор речи [RHVoice](https://github.com/Olga-Yakovleva/RHVoice/):
```
sudo add-apt-repository ppa:linvinus/rhvoice
sudo apt-get update
sudo apt-get install speech-dispatcher-rhvoice rhvoice-russian
```
Затем нужно нужно установить модуль speechd для Python, PyQt5 и VLC плеер с помощью менеджера пакетов в вашем дистрибутиве (например apt):
```
sudo apt-get install python3-speechd python3-pyqt5 vlc python3-pyqt5.qtwebengine python3-pyaudio python3-vlc
```
Клонируйте данный репозиторий с помощью Git:
```
git clone https://github.com/Oknolaz/vasisualy
cd vasisualy
```
Далее необходимо установить другие модули с помощью pip:
```
pip3 install -r requirements.txt
```
После этих действий можно запускать скрипт этой командой для Qt GUI версии:
```
python3 run.py
```

### Arch Linux
Для начала необходимо установить модули [RHVoice](https://aur.archlinux.org/packages/rhvoice) и [python-vlc](https://aur.archlinux.org/packages/python-vlc/) из [AUR](https://aur.archlinux.org/). Для установки с помощью [yay](https://aur.archlinux.org/packages/yay/) используйте:
```
yay -Sy rhvoice python-vlc
```
Установите необходимые пакеты с помощью [Pacman](https://wiki.archlinux.org/index.php/Pacman_(%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9)):
```
pacman -Sy python-pyaudio python-pyqt5 python-alsa speech-dispatcher qt5-webengine vlc python-pyqt5-webengine
```
Клонируйте данный репозиторий:
```
git clone https://github.com/Oknolaz/vasisualy
cd vasisualy
```
Затем установите зависимости с помощью Pip:
```
pip3 install -r requirements.txt
```
После этих действий можно запускать скрипт этой командой для Qt GUI версии:
```
python3 run.py
```
**Также доступен [AUR репозиторий](https://aur.archlinux.org/packages/vasisualy-git/) для установки в Arch Linux.**
### CLI для GNU/Linux
Для CLI версии с распознаванием речи, адаптированной для одноплатных компьютеров (Raspberry Pi, Orange Pi и др.):
```
git clone https://github.com/Oknolaz/vasisualy-pi
cd vasisualy-pi
python3 run.py
```
### Windows
Вам нужно установить [интерпретатор python3](https://python.org) и [VLC media player](https://videolan.org/).
Затем скачайте [данный репозиторий](https://github.com/Oknolaz/vasisualy-windows/), распакуйте скачанный архив и перейдите в папку с программой.
После установки этого - установите необходимые модули python с помощью pip:
```
pip install -r requirements.txt
```
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
