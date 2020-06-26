# Кости
# Демонстрирует генерацию случайных чисел
import random
# создаем случайные числа из диапазона 1 - 6

diel1 = random.randint(1, 6)
diel2 = random.randrange(6) + 1
total = diel1 + diel2
print("При вашем броске выпало", diel1, "и", diel2, "очков, в сумме", total)
input("\n\nНажмите Enter, чтобы выйти.")