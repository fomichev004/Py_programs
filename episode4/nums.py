#Напишите проrрамму, которая бы считала по просьбе пользователя. Надо позволить пользователю ввести
#начапо и конец счета, а также интервал между называемыми целыми числами.
import time


print("Итак, начнем!")
print("Ведите началос счета, конец, а так же интервал!")

#задаем данные программе
start = int(input("введите цифру, с которой начнётся счет: "))
stop = int(input("введите цифру, с которой закончится счет: "))
step = int(input("укажите шаг счета: "))


for i in range(start, stop, step):
    print(i)
    time.sleep(1)





