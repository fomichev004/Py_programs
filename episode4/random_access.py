# Случайные буквы
# Демонстрирует индексацию строк

import random
import time

word = "Индекс"
print("В переменной word хранится слово: ", word, "\n")
high = len (word)
low =-len(word)
for i in range (10):
    position = random.randrange(low, high)
    print("word[", position, "]\t", word[position])
    time.sleep(1)
input("\n\n")