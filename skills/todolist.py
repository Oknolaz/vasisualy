from core import speak

add = ("Добавь в список дел следующее", "добавь в список дел следующее", "Добавь в список дел", "добавь в список дел", "Добавь в мой список дел следующее", "добавь в мой список дел следующее", "Добавь в мой список дел", "добавь в мой список дел", "Добавить в список дел следующее", "добавить в список дел следующее", "Добавить в список дел", "добавить в список дел", "Добавить в мой список дел", "добавить в мой список дел")
show = ("Покажи список дел", "покажи список дел", "Покажи мой список дел", "покажи мой список дел")
delete = ("Очисти список дел", "очисти список дел", "Очисти мой список дел", "очисти мой список дел", "Удали мой список дел", "удали мой список дел", "Удали список дел", "удали список дел")
excludeList = ("Васисуалий", "Васисуали", "васисуалий", "васисуали", "Васян", "васян", "Васёк", "васёк", "Васися", "васися", "Васисяндра", "васисяндра", "Васька", "васька", "Вася", "вася", "Василий", "василий", "Пожалуйста", "пожалуйста")


def main(say, widget):
    for i in add:
        if i in say:
            try:
                todo = say.replace(i, "")
                for toExclude in excludeList:
                    todo = todo.replace(toExclude, "")
                todolist = open("todolist.txt", "a")
                todolist.write(todo)
                todolist.close()
                toSpeak = "Данные успешно добавлены в список дел."
            except Exception:
                todo = say.replace(i, "")
                todolist = open("todolist.txt", "w")
                todolist.write(todo)
                todolist.close()
                toSpeak = "Данные успешно добавлены в список дел."
            break
        else:
            toSpeak = ""
            
    for i in show:
        if i in say:
            try:
                todolist = open("todolist.txt", "r")
                toSpeak = "Вам нужно сделать следующее:\n"
                for item in todolist:
                    item = item.replace(" и ", "\n").replace(",", "\n")
                    toSpeak += item
                todolist.close()
            except Exception:
                toSpeak = "Не удалось открыть файл со списком дел."
            break
        
    for i in delete:
        if i in say:
            todolist = open("todolist.txt", "w")
            todolist.write("")
            todolist.close()
            toSpeak = "Список дел очищен."
            break
            
    if toSpeak != "":
        speak.speak(toSpeak, widget)
    return toSpeak
            
