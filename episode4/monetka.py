import random
import time

throws =1
count1 =0
count2 =0
while throws <=100:
    monetka = random.randint(1, 100)
    monetka %= 2

    if monetka == 1:
        print("орёл, бросок №", throws)
        #time.sleep(1)
        count1 +=1
    else:
        print("решка, бросок №",throws)
        #time.sleep(1)
        count2 += 1
    throws +=1
print("\nОрёл :", count1, "Решка :", count2)
