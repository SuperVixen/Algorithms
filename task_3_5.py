# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и
# позицию (индекс) в массиве.

from random import randint

def kogo_6olwe():
    lst = [randint(-30, 30) for i in range(20)]

    print(lst)

    return print('Максимальный отрицательный элемент', min(lst), 'на позиции', lst.index(min(lst)) + 1)

if __name__ == '__main__':
    kogo_6olwe()

# FIN
