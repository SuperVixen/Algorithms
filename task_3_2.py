# 2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если
# дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1,
# 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. именно в этих позициях первого
# массива стоят четные числа.

from random import randint

def even_indexes():
    lst = [randint(1, 30) for i in range(20)]
    even_lst = []
    for x in range(0, len(lst)):
        if lst[x] % 2 == 0:
            even_lst.append(x + 1)
    print(lst)
    print(even_lst)
    return
if __name__ == '__main__':
    even_indexes()

# FIN
