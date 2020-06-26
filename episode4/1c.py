car = list(str(input("НОМЕР АВТОМОБИЛЯ: \n")
                .replace('-','')
                .replace('/','')
                .replace(' ','')
                .upper()))
res = [ ''.join(car[::-1][i:i+8])[::-1]
    for i in range(0,len(car),8)]
if len(car)>20:
    print("Недопустимое количество символов")
else:
    print(' / '.join(res[::-1]))

phone = input("\nТЕЛЕФОН:\n")
phone = phone.replace('-','').replace(' ','').replace(')','').replace('(','').strip()
print(phone)

name = str(input("\nИмя:\n"))
print(name.title().strip())