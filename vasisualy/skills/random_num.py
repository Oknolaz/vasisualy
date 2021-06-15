from ..core import speak
from ru_word2number import w2n
import random

trigger = ("Число от ", "число от ")
answer = ("Это ", "Ответ ", "Это число ")


def main(say, widget):
    for i in trigger:
        if i in say:
            nums = []
            for word in say.split():
                try:
                    num = w2n.word_to_num(word)  # Преобразование слов из входящего сообщения в числа
                    nums.append(num)
                except ValueError:
                    pass
            while len(nums) > 2:
                nums.pop()  # Если получено больше двух чисел - удаляются следующие после второго
            if len(nums) == 1:
                # Завершение навыка в том случае, если передано только одно число
                toSpeak = "Мне нужно второе число!"
                break
            elif len(nums) == 0:
                # Завершение, если не передано ни одного числа
                toSpeak = "Мне нужны два числа!"
                break
            num1 = int(nums[0])
            num2 = int(nums[1])
            randnum = random.randint(num1, num2)  # Получение случайного числа из диапозона
            toSpeak = random.choice(answer) + str(randnum) + "."
            break
        else:
            toSpeak = ""
            
    if toSpeak:
        speak.speak(toSpeak, widget)
    return toSpeak
