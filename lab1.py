import random

while True:
    try:
        n = int(input('Введите натуральное число больше 1:   '))
        if n > 1:
            break
        else:
            print('необходимо ввести число больше 1')
    except:
        print('Это не натуральное число')

mat = [[random.randint(-10, 10) for j in range(n)] for i in range(n)]

for el in mat:
    print(el)

s = 0

for i in range(n):
    for j in range(n):
        eq = True
        if i == 0:
            if mat[i][j] >= mat[i + 1][j]:
                eq = False
        elif i == (n-1):
            if mat[i][j] >= mat[i - 1][j]:
                eq = False
        elif i > 0 and i < (n-1):
            if mat[i][j] >= mat[i + 1][j] or mat[i][j] >= mat[i - 1][j]:
                eq = False

        if j == 0:
            if mat[i][j] >= mat[i][j+1]:
                eq = False
        elif j == (n-1):
            if mat[i][j] >= mat[i][j-1]:
                eq = False
        elif j != 0 and j != (n-1):
            if mat[i][j] >= mat[i][j+1] or mat[i][j] >= mat[i][j-1]:
                eq = False

        if eq == True:
            s += 1

print('Кол-во локальных минимумов:  ' + str(s))