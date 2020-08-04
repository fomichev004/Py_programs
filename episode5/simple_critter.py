class Critter(object):
    """Виртуальный питомец"""
    def talk(self):
        print("Привет. Я Зверюшка - экземпляр Critter.")
#Основная часть
crit = Critter()
crit.talk()
input("\n\n Нажмите энтер, чтобы выйти")