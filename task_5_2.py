# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
# Примечание: для решения задач попробуйте применить какую-нибудь коллекцию из модуля collections

from collections import deque

def hex_sum(x, y):
    hex_num = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
               0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
               10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    result = deque()
    transfer = 0

    if len(y) > len(x):
        x, y = deque(y), deque(x)
    else:
        x, y = deque(x), deque(y)

    while x:
        if y:
            res = hex_num[x.pop()] + hex_num[y.pop()] + transfer
        else:
            res = hex_num[x.pop()] + transfer

        transfer = 0

        if res <= 15:
            result.appendleft(hex_num[res])
        else:
            result.appendleft(hex_num[res - 16])
            transfer = 1

    if transfer:
        result.appendleft('1')

    print('Сумма равна: ', end='')
    for elem in result:
        print(elem, end='')
    print()
    return

def hex_multiple(x, y):
    hex_num = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
               0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
               10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    result = deque()
    spam = deque([deque() for _ in range(len(y))])

    x, y = x.copy(), deque(y)

    for i in range(len(y)):
        m = hex_num[y.pop()]

        for j in range(len(x) - 1, -1, -1):
            spam[i].appendleft(m * hex_num[x[j]])

        for _ in range(i):
            spam[i].append(0)

    transfer = 0

    for _ in range(len(spam[-1])):
        res = transfer

        for i in range(len(spam)):
            if spam[i]:
                res += spam[i].pop()

        if res <= 15:
            result.appendleft(hex_num[res])
        else:
            result.appendleft(hex_num[res % 16])
            transfer = res // 16

    if transfer:
            result.appendleft(hex_num[transfer])

    print('Произведение равно: ', end='')
    for elem in result:
        print(elem, end='')
    print()
    return

if __name__ == '__main__':

    a = list(input('Введите первое шестнадцатеричное число: ').upper())
    b = list(input('Введите второе шестнадцатеричное число: ').upper())

    hex_sum(a, b)
    hex_multiple(a, b)
    
# FIN

# Асимптотический анализ:
#   Сложность алгоритма оцениваю как О(n) - линейная сложность
#
