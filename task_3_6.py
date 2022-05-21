# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и
# максимальным элементами. Сами минимальный и максимальный элементы в сумму не
# включать.

from random import randint

def sum_between_min_max():
    lst = [randint(-30, 30) for i in range(20)]

    print(lst)

    a_max_index = lst.index(max(lst))
    a_min_index = lst.index(min(lst))

    print('Максимальный элемент списка', max(lst), 'на позиции', a_max_index + 1)
    print('Минимальный элемент списка', min(lst), 'на позиции', a_min_index + 1)

    if a_min_index < a_max_index:
        del lst[a_max_index:]
        del lst[0:a_min_index + 1]

    elif a_min_index > a_max_index:
        del lst[a_min_index:]
        del lst[0: a_max_index + 1]
    else:
        return print('Между максимальным и минимальным элементами ничего нет')
    return print('Массив между максимальным и минимальным элементами:', lst, ', сумма его элементов', sum(lst))

    
if __name__ == '__main__':
    sum_between_min_max()

# FIN
