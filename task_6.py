# 6. Пользователь вводит номер буквы в алфавите.
# Определить, какая это буква.


if __name__ == '__main__':
    alphbet = list(map(chr, range(97, 123)))
    point_1 = int(input('Введите номер буквы алфавита (a-z): '))
    if point_1 > 26:
        print('У англичан всего 26 букв!!!')
    else:
        print('Это буква', alphbet[point_1 - 1])
