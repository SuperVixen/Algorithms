# 5. Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят
# и сколько между ними находится букв.


if __name__ == '__main__':
    alphbet = list(map(chr, range(97, 123)))
    point_1 = str(input('Введите начальную букву диапазона (a-z): '))
    point_2 = str(input('Введите конечную букву диапазона (a-z): '))
    print('Буква', point_1,'по алфавиту на позиции', alphbet.index(point_1) + 1)
    print('Буква', point_2, 'по алфавиту на позиции', alphbet.index(point_2) + 1)
    print('Между ними', alphbet.index(point_2) - alphbet.index(point_1) - 1, 'символа(-ов):')
    print(alphbet[alphbet.index(point_1) + 1:alphbet.index(point_2)])
