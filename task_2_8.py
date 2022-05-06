# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

if __name__ == '__main__':

    def numberrz(n):
        spisok = []
        a = int(input('Введите цифру, которую будем считать: '))
        for i in n:
            spisok += list(str(i))
        spisok_off_a = list(filter((str(a)).__ne__, spisok))
        return print('Цифра', a, 'встречается в введённых числах',len(spisok) - len(spisok_off_a) , 'раз.')

    numberrz(list(map(int, input('Введите через пробел числа: ').split())))

# FIN
