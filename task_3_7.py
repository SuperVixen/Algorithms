# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть
# как равны между собой (оба являться минимальными), так и различаться.

from random import randint

def twin_littlz():
    lst = [randint(-30, 30) for i in range(20)]

    print(lst)

    a_min_index = lst.index(min(lst))
    a = min(lst)
    del lst[a_min_index]
    b = min(lst)

    return print('Минимальные элементы списка', a, 'и', b)

if __name__ == '__main__':
    twin_littlz()

# FIN
