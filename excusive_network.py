# Эксклюзивная сеть
# Демонстрирует составные условия и логические операторы
print("\tЭксклюзивная комрьютерная сеть")
print("\tТолько для зарегестрированных пользователей!\n")
seurity = 0
username =""
while not username:
    username = input("Логин:\n")
password =""
while not password:
        password = input("Пароль:\n")
if username == "M. Dawson" and password == "secret":
    print("Привет, Майк.")
    seurity = 5
elif username == "S. Meier" and password == "secret3":
    print("Здравстввуй, Сигеру")
    seurity = 3
elif username == "S. Miyamoto" and password == "mariobros":
    print("Здравстввуй, Сид")
    seurity = 3
elif username == "S. Meier" and password == "secret2":
    print("Здравстввуй, Сид")
    seurity = 3
else:
    print("Войти в систему не удалось. Должно быть, вы не очень-то эксклюзивный гражданин.\n")
input("\n\nHaжмитe Enter. чтобы выйти.")
