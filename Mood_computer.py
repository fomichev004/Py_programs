# Компьютерный датчик настроения
#Демонстрирует использование elif
import random

print("Я ощущаю вашу энергетику. От моего жкрана не скрито ни одно из ваших чувств.")
print ("Итак, ваше настроение...")
mood = random.randint(1, 3)
if mood ==1:
    #happy
    print(":)")
elif mood ==2:
    #so so
    print(":|")
elif mood ==3:
    #bad
    print(":(")

input("\n\nPress the enter key to exit.")