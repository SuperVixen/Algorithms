# 9. Вводятся три разных числа.
# Найти, какое из них является средним
# (больше одного, но меньше другого).

def tri_compare(n):
    n.sort()
    return print('Среднее из них: ', n[1])



if __name__ == '__main__':
    numbers = list(map(float, input('Введите через пробел три числа: ').split()))
    tri_compare(numbers)
