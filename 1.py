def isleapyear(y):
    if y % 400 == 0:
        return True
    if y % 100 == 0:
        return False
    if y % 4 == 0:
        return True
    return False
years = []
for i in range(5):  
    number = int(input())  
    years.append(number)

    print(isleapyear(number))
    if i == 6:
        break
