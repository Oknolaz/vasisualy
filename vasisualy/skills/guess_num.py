import random
from ..core import speak

trigger = ("Угадай число", "угадай число", "Поиграем в число", "поиграем в число", "Играть в угадай число", "играть в угадай число", "Играть в число", "играть в число", "Угадать число", "угадать число", "Угадывать число", "угадывать число")

def isTriggered(say):
    for i in trigger:
        if i in say:
            triggered = True
            break
        else:
            triggered = False
    
    return triggered

def getRandomNum():
    randnum = random.randint(0, 100)  # Опеределение случайного числа
    return randnum

def startGame(widget):
    speak.speak("Я загадал число от 0 до 100. Угадай его.", widget)
    isGuessNum = True
    return isGuessNum

def game(say, num, gameState, widget):
    usrnum = -1
    gameState = True
    guessTry = 0
    try:
        usrnum = int(say)  # Преобразование пользовательского ввода в целое число
    except Exception:
        pass  # Если пользователь не ввёл число - ничего не делать
    if usrnum == -1:
        pass
    elif usrnum < num:
        speak.speak("Моё число больше.", widget)
        guessTry += 1
    elif usrnum > num:
        speak.speak("Моё число меньше.", widget)
        guessTry += 1
    elif usrnum == num:
        speak.speak(f"Поздравляю, ты выиграл затратив на это {str(guessTry+1)} попытки.", widget)
        gameState = False  # Конец игры
        guessTry = 0
    return gameState
