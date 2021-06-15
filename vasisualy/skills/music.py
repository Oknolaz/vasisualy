import random
import vlc
import os
from ..core import speak
from ..core import defaults

# Инициализация VLC плеера
inst = vlc.Instance()
player = inst.media_player_new()
is_paused = False
musicIsPlayed = False

trigger = ("Музыка", "музыка", "Включи музыку", "включи музыку", "Танцы", "танцы", "Танец", "танец", "Потанцуй",
           "потанцуй", "Хочу танцевать", "хочу танцевать", "Хочу плясать", "хочу плясать", "Музыку", "музыку", "Песня",
           "песня", "Включи песню", "включи песню", "Музычка", "музычка", "Музончик", "музончик", "Танцульки",
           "танцульки", "Радио", "радио", "Станция", "станция", "Рэдио", "рэдио", "Музыку", "музыку", "Музычку",
           "музычку", "Мьюзик", "мьюзик", "Танцуй", "танцуй", "Песню", "песню", "Зажги", "зажги", "Зажигай", "зажигай",
           "Зажгём", "зажгём", "Отжиг", "отжиг", "Музон", "музон", "Музло", "музло")

stop_music = ("Стоп музыка", "стоп музыка", "Стоп воспроизведение", "стоп воспроизведение", "Останови музыку",
              "останови музыку", "Выключи музыку", "выключи музыку", "Останови воспроизведение",
              "останови воспроизведение", "Остановка музыки", "остановка музыки", "Выключи радио", "выключи радио")

nextSong = ("Следующий трек", "Следующая песня", "Следующая музыка", "Следующее воспроизведение", "Следующий")


def main(say, widget):
    for i in trigger:
        if i in say:
            radiostation = say.replace(i, '')
            try:
                if "рок" in radiostation:
                    radiostation = "http://pub0302.101.ru:8000/stream/trust/mp3/128/69?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpcCI6IjUxLjE1OC4xNDQuMzIiLCJ1c2VyYWdlbnQiOiJNb3ppbGxhXC81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NDsgcnY6NjguMCkgR2Vja29cLzIwMTAwMTAxIEZpcmVmb3hcLzY4LjAiLCJ1aWRfY2hhbm5lbCI6IjY5IiwidHlwZV9jaGFubmVsIjoiY2hhbm5lbCIsImV4cCI6MTU5NjI3MzUzMn0.04mOBSZ4tirBXTQdbWYpGs8YuJE6Dw7fM7a-zbP-PTs"
                    media=inst.media_new(radiostation)  # Передача интернет-потока радио в качестве источника VLC
                    player.set_media(media)
                    player.play()  # Воспроизведение потока
                elif "поп" in radiostation:
                    radiostation = "http://pub0302.101.ru:8000/stream/pro/aac/64/155?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpcCI6IjUxLjE1OC4xNDQuMzIiLCJ1c2VyYWdlbnQiOiJNb3ppbGxhXC81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NDsgcnY6NjguMCkgR2Vja29cLzIwMTAwMTAxIEZpcmVmb3hcLzY4LjAiLCJ1aWRfY2hhbm5lbCI6IjE1NSIsInR5cGVfY2hhbm5lbCI6ImNoYW5uZWwiLCJleHAiOjE1OTYyNzM2NDh9.9nrmdE85O78l_SWG8ZIbcBb81rlMfjWEFZtyU54v240"
                    media=inst.media_new(radiostation)
                    player.set_media(media)
                    player.play()
                elif "хип-хоп" in radiostation or "хипхоп" in radiostation or "рэп" in radiostation:
                    radiostation = "http://pub0202.101.ru:8000/stream/pro/aac/64/8?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpcCI6IjUxLjE1OC4xNDQuMzIiLCJ1c2VyYWdlbnQiOiJNb3ppbGxhXC81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NDsgcnY6NjguMCkgR2Vja29cLzIwMTAwMTAxIEZpcmVmb3hcLzY4LjAiLCJ1aWRfY2hhbm5lbCI6IjgiLCJ0eXBlX2NoYW5uZWwiOiJjaGFubmVsIiwiZXhwIjoxNTk2MjczNzM0fQ.CFeZY0sd_dE8A-Fb_cJDvmfoE03TfentLDYUNc2o5wY"
                    media=inst.media_new(radiostation)
                    player.set_media(media)
                    player.play()
                elif "танц" in radiostation or "танец" in radiostation:
                    radiostation = "http://pub0202.101.ru:8000/stream/trust/mp3/128/5?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpcCI6IjUxLjE1OC4xNDQuMzIiLCJ1c2VyYWdlbnQiOiJNb3ppbGxhXC81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NDsgcnY6NjguMCkgR2Vja29cLzIwMTAwMTAxIEZpcmVmb3hcLzY4LjAiLCJ1aWRfY2hhbm5lbCI6IjUiLCJ0eXBlX2NoYW5uZWwiOiJjaGFubmVsIiwiZXhwIjoxNTk2MjczODgyfQ.gyZu0VQMMYfnUhbsD8_I6l2UByX4C757joVrJJGiN9o"
                    media=inst.media_new(radiostation)
                    player.set_media(media)
                    player.play()
                elif "техно" in radiostation or "электро" in radiostation:
                    radiostation = "http://pub0202.101.ru:8000/stream/trust/mp3/128/18?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpcCI6IjUxLjE1OC4xNDQuMzIiLCJ1c2VyYWdlbnQiOiJNb3ppbGxhXC81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NDsgcnY6NjguMCkgR2Vja29cLzIwMTAwMTAxIEZpcmVmb3hcLzY4LjAiLCJ1aWRfY2hhbm5lbCI6IjE4IiwidHlwZV9jaGFubmVsIjoiY2hhbm5lbCIsImV4cCI6MTU5NjI3NDIzM30.QgEVxowg5isL-Bx21mGRHlJtQVrlBMpPGMYedjxzAQM"
                    media=inst.media_new(radiostation)
                    player.set_media(media)
                    player.play()
                elif "джаз" in radiostation:
                    radiostation = "http://pub0202.101.ru:8000/stream/pro/aac/128/85?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpcCI6IjUxLjE1OC4xNDQuMzIiLCJ1c2VyYWdlbnQiOiJNb3ppbGxhXC81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NDsgcnY6NjguMCkgR2Vja29cLzIwMTAwMTAxIEZpcmVmb3hcLzY4LjAiLCJ1aWRfY2hhbm5lbCI6Ijg1IiwidHlwZV9jaGFubmVsIjoiY2hhbm5lbCIsImV4cCI6MTU5NjI3NDMzM30.qMRUJuGhdAWRkuWJ9l4NscxmsKy26y8q0risQrU_Nt0"
                    media=inst.media_new(radiostation)
                    player.set_media(media)
                    player.play()
                elif say in stop_music:
                    pass
                else:
                    toSpeak = "Включаю музыку из твоей папки. Если хочешь слушать радио - то скажи \"включи (жанр) музыку\"."
                    playFromDir()
            except Exception:
                if say in stop_music:
                    pass
                else:
                    toSpeak = "Не удалось воспроизвести музыку."
            break
        else:
            toSpeak = ""
            
            
    for i in stop_music:
        if i == say:
            global usrPlayer
            toSpeak = "Проигрыватель остановлен."
            player.pause()  # Остановка проигрывателя
            usrPlayer.stop()
            
    for i in nextSong:
        if i == say:
            toSpeak = "Переключаю..."
            playFromDir()
            break
    
    if toSpeak != "":
        speak.speak(toSpeak, widget)
    return toSpeak
        


def playFromDir():
    global musicIsPlayed, usrPlayer
    try:
        appDir = os.path.dirname(os.path.realpath(__file__))
        os.chdir(f"{appDir}/../..")
        config = open("vasisualy.conf", "r")
        for line in config:
            if "music:" in line:
                musicDir = line.replace("music:", "")
    except Exception:
        musicDir = defaults.defaults["music"]
    playlist = os.listdir(musicDir)  # Получение списка файлов из директории music в корне проекта
    if musicIsPlayed:
        usrPlayer.stop()
        usrPlayer = vlc.MediaPlayer(f'{musicDir}/{random.choice(playlist)}')
        usrPlayer.play()
    else:
        # Воспроизведение музыки из папки music
        usrPlayer = vlc.MediaPlayer(f'{musicDir}/{random.choice(playlist)}')
        usrPlayer.play()
        musicIsPlayed = True
