import random
from random import randint, uniform
try:
    n, m = int(input()), int(input())
    if n > 0 and m > 0:
        matrix = [[random.randint(1, 10) for _ in range(m)] for _ in range(n)] #Менять значение
        m1, m2 = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))], [[0 for i in range(m)] for j in range(n)]
        print('Исходная матрица')
        for row in matrix:
            print(*row, sep='  ')
        print()
        if len(matrix) == 1:
            print('Измененная матрица')
            for row in matrix:
                print(*row, sep='  ')
        else:
            for i in range(1, len(matrix), 2):
                mat = list()
                for j in range(len(matrix[i]) - 1, -1, -1):
                    mat.append(matrix[i][j])
                matrix[i] = mat
            print()
            print('Измененная матрица')
            for row in matrix:
                print(*row, sep='  ')
except ValueError:
    print()