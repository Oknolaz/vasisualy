import subprocess
import os

print("Голосовой ассистент Васисуалий\n\n")
print("Доступные для установки дистрибутивы:\n1) Arch Linux     2) Debian/Ubuntu     3) Fedora/RedHat      4) OpenSuse     5) Alpine Linux")
choice = input("Введите цифру соответствующую вашему дистрибутиву (без скобок и прочих символов): ")


def arch_aur_deps(package):
    subprocess.run(["git", "clone", f"https://aur.archlinux.org/{package}.git"])
    os.chdir(f"./{package}")
    subprocess.run(["makepkg", "-sri"])
    os.chdir("..")


if choice == "":
    print("Вы не ввели номер дистрибутива!")


elif choice == "1":
    print(">>> Установка необходимых пакетов")
    subprocess.run(["sudo", "pacman", "-Sy", "--needed", "--noconfirm", "git", "base-devel", "python3", "python-pip", "python-pyqt5", "python-pyqt5-webengine", "pulseaudio", "python-pyaudio", "wget"])
    print(">>> Установка синтезатора речи RHVoice")
    arch_aur_deps("rhvoice")
    print(">>> Установка модуля VLC для Python")
    arch_aur_deps("python-vlc")
    print(">>> Установка необходимых модулей с помощью Pip")
    subprocess.run(["pip3", "install", "translate", "geocoder", "pyowm", "mss", "qt-material", "speechrecognition", "wikipedia", "lxml"])
    print(">>> Копирование desktop файла в директорию приложений")
    subprocess.run(["wget", "https://raw.githubusercontent.com/Oknolaz/vasisualy-additional-files/main/vasisualy.desktop"])
    subprocess.run(["sudo", "cp", "-r", "vasisualy.desktop", "/usr/share/applications/"])
    os.chdir("..")
    print(">>> Копирование исходного кода в корневую директорию")
    subprocess.run(["sudo", "cp", "-r", "vasisualy/", "/usr/share/"])
    subprocess.run(["rm", "-rf", "vasisualy/"])
    os.chdir("/usr/bin/")
    print(">>> Копирование исполняемых файлов")
    subprocess.run(["sudo", "rm", "vasisualy-pi", "vasisualy"])
    subprocess.run(["sudo", "wget", "https://raw.githubusercontent.com/Oknolaz/vasisualy-additional-files/main/vasisualy"])
    subprocess.run(["sudo", "chmod", "+x", "vasisualy"])
    os.chdir(os.path.expanduser("~"))
    subprocess.run(["git", "clone", "https://github.com/Oknolaz/vasisualy-pi"])
    subprocess.run(["sudo", "cp", "-r", "vasisualy-pi/", "/usr/share/"])
    subprocess.run(["rm", "-rf", "vasisualy-pi/"])
    os.chdir("/usr/bin/")
    subprocess.run(["sudo", "wget", "https://raw.githubusercontent.com/Oknolaz/vasisualy-additional-files/main/vasisualy-pi"])
    subprocess.run(["sudo", "chmod", "+x", "vasisualy-pi"])
    os.chdir(os.path.expanduser("~"))
    print(">>>\n>>>\n>>> Установка успешно завершена. Программу можно запустить командой vasisualy или vasisualy-pi для консольной версии.")

    
    
elif choice == "2":
    print(">>> Установка зависимостей с помощью APT")
    subprocess.run(["sudo", "apt", "install", "git", "python3", "python3-pip", "python3-pyqt5", "python3-pyqt5.qtwebengine", "python3-vlc", "python3-pyaudio", "apt-utils", "pulseaudio", "wget", "-y"])
    print(">>> Установка зависимостей с помощью Pip")
    subprocess.run(["pip3", "install", "translate", "geocoder", "pyowm", "mss", "qt-material", "speechrecognition", "wikipedia", "lxml"])
    print(">>> Копирование desktop файла в директорию приложений")
    subprocess.run(["wget", "https://raw.githubusercontent.com/Oknolaz/vasisualy-additional-files/main/vasisualy.desktop"])
    subprocess.run(["sudo", "cp", "-r", "vasisualy.desktop", "/usr/share/applications/"])
    os.chdir("..")
    print(">>> Копирование исходного кода в корневую директорию")
    subprocess.run(["sudo", "cp", "-r", "vasisualy/", "/usr/share/"])
    subprocess.run(["rm", "-rf", "vasisualy/"])
    os.chdir("/usr/bin/")
    print(">>> Копирование исполняемых файлов")
    subprocess.run(["sudo", "rm", "vasisualy-pi", "vasisualy"])
    subprocess.run(["sudo", "wget", "https://raw.githubusercontent.com/Oknolaz/vasisualy-additional-files/main/vasisualy"])
    subprocess.run(["sudo", "chmod", "+x", "vasisualy"])
    os.chdir(os.path.expanduser("~"))
    subprocess.run(["git", "clone", "https://github.com/Oknolaz/vasisualy-pi"])
    subprocess.run(["sudo", "cp", "-r", "vasisualy-pi/", "/usr/share/"])
    subprocess.run(["rm", "-rf", "vasisualy-pi/"])
    os.chdir("/usr/bin/")
    subprocess.run(["sudo", "wget", "https://raw.githubusercontent.com/Oknolaz/vasisualy-additional-files/main/vasisualy-pi"])
    subprocess.run(["sudo", "chmod", "+x", "vasisualy-pi"])
    os.chdir(os.path.expanduser("~"))
    print(">>>\n>>>\n>>> Установка успешно завершена. Программу можно запустить командой vasisualy или vasisualy-pi для консольной версии.")


elif choice == "3":
    print("На данный момент установка программы на Fedora/RedHat недоступна.")


elif choice == "4":
    print("На данный момент установка программы на OpenSuse недоступна.")


elif choice == "5":
    print("На данный момент запуск программы на Alpine Linux невозможен.")


else:
    print("Вы ввели неверный номер дистрибутива!")

