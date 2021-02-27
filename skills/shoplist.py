from core import speak

add = ("Добавь в список покупок следующее", "добавь в список покупок следующее", "Добавь в список покупок", "добавь в список покупок", "Добавь в мой список покупок следующее", "добавь в мой список покупок следующее", "Добавь в мой список покупок", "добавь в мой список покупок", "Добавить в список покупок следующее", "добавить в список покупок следующее", "Добавить в список покупок", "добавить в список покупок", "Добавить в мой список покупок", "добавить в мой список покупок")
show = ("Покажи список покупок", "покажи список покупок", "Покажи мой список покупок", "покажи мой список покупок", "Показать список покупок", "показать список покупок")
delete = ("Очисти список покупок", "очисти список покупок", "Очисти мой список покупок", "очисти мой список покупок", "Очистка списка покупок", "очистка списка покупок")
excludeList = ("Васисуалий", "Васисуали", "васисуалий", "васисуали", "Васян", "васян", "Васёк", "васёк", "Васися", "васися", "Васисяндра", "васисяндра", "Васька", "васька", "Вася", "вася", "Василий", "василий", "Пожалуйста", "пожалуйста")


def main(say, widget):
    for i in add:
        if i in say:
            try:
                toBuy = say.replace(i, "")
                for toExclude in excludeList:
                    toBuy = toBuy.replace(toExclude, "")
                shoplist = open("shoplist.txt", "a")
                shoplist.write(toBuy)
                shoplist.close()
                toSpeak = "Данные успешно добавлены в список покупок."
            except Exception:
                toBuy = say.replace(i, "")
                shoplist = open("shoplist.txt", "w")
                shoplist.write(toBuy)
                shoplist.close()
                toSpeak = "Данные успешно добавлены в список покупок."
            break
        else:
            toSpeak = ""
            
    for i in show:
        if i in say:
            try:
                shoplist = open("shoplist.txt", "r")
                toSpeak = "Вам нужно купить следующее:\n"
                for item in shoplist:
                    item = item.replace(" и ", "\n").replace(",", "\n")
                    toSpeak += item
                shoplist.close()
            except Exception:
                toSpeak = "Не удалось открыть файл со списком покупок."
            break
        
    for i in delete:
        if i in say:
            shoplist = open("shoplist.txt", "w")
            shoplist.write("")
            shoplist.close()
            toSpeak = "Список покупок очищен."
            break
                
            
    if toSpeak != "":
        speak.speak(toSpeak, widget)
    return toSpeak
