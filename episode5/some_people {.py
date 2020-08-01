import random
import numpy as np
import p

#some_people = {"0" : "Петров", "1" : "Рябцев", "2" : "Табуреткин", "3" : "Скворцов", "4" : "Иванов", "5" : "Сидоров"}
#
#random.choice(list(some_peopled.keys())) 
#print(some_people)
#capital = random.choice(list(d.items()))
#import random 
#d = {"0" : "Петров", "1" : "Рябцев", "2" : "Табуреткин", "3" : "Скворцов", "4" : "Иванов", "5" : "Сидоров"} 
#country, capital = random.choice(list(d.items()))
#print(country, capital)

#print(some_people["1"])
Z = np.ones((16,16))
k = 4
S = np.add.reduceat(np.add.reduceat(Z, np.arange(0, Z.shape[0], k), axis=0),
                                        np.arange(0, Z.shape[1], k), axis=1)