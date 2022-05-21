# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import randint

def max_from_min():

    lst = [[randint(0, 100) for i in range(10)] for j in range(10)]
    for i in range(10):

        for j in range(10):
            print(lst[i][j], end=' ')

        print(' ', sep='/n')

    min_column = ([min(lst[i][j] for i in range(10)) for j in range(10)])
    print(min_column)
    print(max(min_column))

if __name__ == '__main__':
    max_from_min()

# FIN
