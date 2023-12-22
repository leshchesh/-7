def addleftdigit(d, к):
    к = к * 10 + d
    return к
число = int(input("Введите число: "))
while True:
    цифра = int(input("Введите цифру для добавления: "))
    число = addleftdigit(цифра, число)
    print("Результат:", число)
    продолжить = input("Хотите добавить еще цифру? (да/нет): ")  
    if продолжить.lower() != "да":
        break
