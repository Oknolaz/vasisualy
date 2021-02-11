from core import speak
import random

trigger = ("Подкинь монетку", "подкинь монетку", "Подкинь монету", "подкинь монету", "Орёл и решка", "орёл и решка", "Орел и решка", "орел и решка", "Монетка", "монетка") # Команды подкидывания монеты

def main(say, widget):
    for i in trigger:
        if i == say:
            random_coin = random.choice(("орёл", "решка"))
            toSpeak = f"Я подкинул монету - на монете {random_coin}."
            break
        else:
            toSpeak = ""
    
    if toSpeak != "":
        speak.speak(toSpeak, widget)
    return toSpeak
