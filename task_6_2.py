import random
from sys import getsizeof

if __name__ == '__main__':
    choice = int(input('Введите тип данных (1 - целые числа, 2 - вещественные числа, 3 - символы): '))
    if choice == 1:
        point_1 = int(input('Введите начало интервала случайных величин: '))
        point_2 = int(input('Введите конец интервала случайных величин: '))
        print('Случайное число из диапазона',point_1,'-', point_2, ':', random.randint(point_1, point_2))
    elif choice == 2:
        point_1 = float(input('Введите начало интервала случайных величин: '))
        point_2 = float(input('Введите конец интервала случайных величин: '))
        print('Случайное число из диапазона', point_1, '-', point_2, ':', point_1 + (point_2 - point_1) * random.random())
    elif choice == 3:
        point_1 = str(input('Введите начало интервала случайных величин: '))
        point_2 = str(input('Введите конец интервала случайных величин: '))
        print('Случайный символ из диапазона', point_1, '-', point_2, ':', chr(int(ord(point_1) + (ord(point_2) - ord(point_1)) * random.random())))
    else:
        print('Необъяснимая ошибка, программа завершает работу')

    print(getsizeof(choice))
    print(getsizeof(point_1))
    print(getsizeof(point_2))

# Для целых чисел: 3 * 28 байт, итого 84 байта
# Для вещественных чисел: 28 + 2 * 24 байта, итого 76 байт (вообще не понятно, почему на вещественные числа выделяется меньший объём памяти)
# Для символов: 28 + 2 * 50 байт, итого 128 байт

# Python 3.7.8rc1, Windows 8 Профессиональная, 64-разрядная операционная система, процессор х64
# Intel(R) Xeon(R) CPU E5-2650 v2 @ 2.60GHz
# Пространственная сложность постоянная O(1)
