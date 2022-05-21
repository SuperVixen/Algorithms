
# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа
# должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю
# ячейку строки. В конце следует вывести полученную матрицу.

from random import randint

def sum_matrix():

    a = []
    for _ in range(5):
        row = input('Введите строчку значений (4 числа через пробел): ').split()

        for j in range(4):
            row[j] = int(row[j])

        a.append(row)
        row.append(sum(row))

    for i in range(5):
        for j in range(5):
            print(a[i][j], end=' ')
        print(' ', sep='/n')

    
if __name__ == '__main__':
    sum_matrix()

# FIN
