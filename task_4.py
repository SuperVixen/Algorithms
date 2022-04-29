# 4. Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.


import random

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
