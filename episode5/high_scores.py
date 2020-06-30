#рекорды
#Демонстрирует спсочные методы
scores =[]
choice = None
while choice != "0":
    print(
    """     
    Рекорды
    0 - Выйти
    1 - Показать рекорды
    2 - Добавить рекорд
    3 - Удалить рекорд
    4 - Сортировать список        
    """
    )
    choice = input("Ваш выбор: ")
    print()
# Выход из программы
    if choice == "0":
        print("До свидания.")
    #вывод лучших результатов на экран
    elif choice == "1":
        print("Рекорды")
        for score in scores:
            print(score)
    #Добавление рекорда
    elif choice == "2":
        score = int(input("Впишите свой рекорд: "))
        scores.append(score)
    #Delete score
    elif choice == "3":
        score = int(input("Какой из рекордов удалить?: "))
        if score in scores:
            scores.remove(score)
        else:
            print("Результат", score, "не содержится в списке рекордов.")
    #Сортировка рекордов
    elif choice == "4":
        scores.sort(reverse=True)
    else:
        print("в меню не данного пункта", choice)