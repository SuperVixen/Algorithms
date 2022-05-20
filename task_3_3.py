# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный
# элементы.

from random import randint

def change_indexes():
    lst = [randint(1, 30) for i in range(10)]
    a_min = min(lst)
    a_max = max(lst)
    a_max_index = lst.index(a_max)
    a_min_index = lst.index(a_min)

    print(lst)
    print('Максимальный элемент списка',a_max, 'на позиции', lst.index(a_max) + 1)
    print('Минимальный элемент списка', a_min, 'на позиции', lst.index(a_min) + 1)


    lst.remove(a_min)
    lst.insert(a_min_index, a_max)

    lst.remove(a_max)
    lst.insert(a_max_index, a_min)

    print(lst)
    return

if __name__ == '__main__':
    change_indexes()
# FIN
