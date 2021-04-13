from ..core import speak
from ru_word2number import w2n

trigger = ("Посчитай", "посчитай", "Сколько будет", "сколько будет", "Результат выражения", "результат выражения")
mathSymbols = ("+", "-", "*", "/", ":")
mathWords = {
    "плюс": "+",
    "прибавить": "+",
    "сложить": "+",
    "минус": "-",
    "вычесть": "-",
    "умножить": "*",
    "разделить": "/"
}

def getNums(mathExpression):
    expressionWithNums = ""
    for word in mathExpression.split():
        try:
            # Преобразование слов в числа
            num = w2n.word_to_num(word)
            expressionWithNums += f" {str(num)}"
        except ValueError:
            expressionWithNums += f" {word}"
    return expressionWithNums

def clear(mathExpression):
    cleanedExpression = ""
    for word in mathExpression.split():
        if word.isdigit() or word in mathSymbols:
            cleanedExpression += word  # Запись чисел и математических знаков в выражение
        elif word in mathWords:
            word = mathWords.get(word) # Получение математического знака по слову
            cleanedExpression += word
    return cleanedExpression

def calculate(say, widget):
    for i in trigger:
        if i in say:
            withNums = getNums(say)
            cleaned = clear(withNums)
            try:
                toSpeak = str(eval(cleaned)) # Счёт выражения
            except Exception:
                toSpeak = "Не удалось посчитать выражение."
            break
        else:
            toSpeak = ""
            
    if toSpeak != "":
        speak.speak(toSpeak, widget)
    return toSpeak
