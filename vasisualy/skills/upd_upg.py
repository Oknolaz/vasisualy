from ..core import speak
import subprocess

update = ("Обнови репозитории", "обнови репозитории", "Обновление репозиториев", "обновление репозиториев", "Обновление репозитория", "обновление репозитория")
upgrade = ("Обнови программы", "обнови программы", "Обнови систему", "обнови систему", "Обновление программ", "обновление программ", "Обновление системы", "обновление системы")

def main(say, widget):
    for i in update:
        if i in say:
            toSpeak = "Обновляю репозитории... Смотри вывод в терминале."
            try:
                subprocess.run("apt")
                subprocess.Popen(["pkexec", "apt", "update"])
            except Exception:
                subprocess.run("dnf")
                subprocess.Popen(["pkexec", "dnf", "update"])
            except Exception:
                subprocess.run("apk")
                subprocess.Popen(["pkexec", "apk", "update"])
            except Exception:
                subprocess.run("yum")
                subprocess.Popen(["pkexec", "yum", "-y", "update"])
            except Exception:
                subprocess.run("pacman")
                subprocess.Popen(["pkexec", "pacman", "-Sy"])
            except Exception:
                toSpeak = "Не удалось обновить репозитории."
            break
        else:
            toSpeak = ""
            
    for i in upgrade:
        if i in say:
            toSpeak = "Обновляю систему... Смотри вывод в терминале."
            try:
                subprocess.run("apt")
                subprocess.Popen(["pkexec", "apt", "upgrade", "-y"])
            except Exception:
                subprocess.run("dnf")
                subprocess.Popen(["pkexec", "dnf", "upgrade"])
            except Exception:
                subprocess.run("apk")
                subprocess.Popen(["pkexec", "apk", "upgrade"])
            except Exception:
                subprocess.run("yum")
                subprocess.Popen(["pkexec", "yum", "-y", "upgrade"])
            except Exception:
                subprocess.run("pacman")
                subprocess.Popen(["pkexec", "pacman", "-Syu", "--noconfirm"])
            except Exception:
                toSpeak = "Не удалось обновить систему."
            
    if toSpeak != "":
        speak.speak(toSpeak, widget)
    return toSpeak
