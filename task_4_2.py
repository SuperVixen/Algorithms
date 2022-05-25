import time

def simple_number(num):
    simple_numberz = [2]
    n = 3
    time_s = time.time()

    while simple_numberz.index(simple_numberz[-1]) < num:
        flag = True
        for i in range(2, n // 2):
            if n % i == 0:
                flag = False
                break

        if flag:
            simple_numberz.append(n)

        n += 1
    time_f = time.time()
    # print(time_f - time_s)
    # я не могу понять в чем ошибка, но у меня в последовательность простых чисел вклинилась 4.
    # из за этого страдает нумерация на одну позицию, для 2, 3 всё верно, для последующих чисел - показывает простое число на предыдущей позиции.
    # simple_numberz.remove(4)


    if  num >= 3:   #Это адовый костыль
        simple_numberz.remove(4)
        print(simple_numberz)
        return print('Простое число №', num, 'это', (simple_numberz[-1]))
    return print('Простое число №', num, 'это', (simple_numberz[-2]))


def simple_number_reweto_eratosfena(num):
    sieve = set()
    prost_set = set()
    for i in range(1, num):
        sieve = set(range(2, 10*i))
        # prost_set = set()

    while sieve:
        prime = min(sieve)
        prost_set.add(prime)
        sieve -= set(range(prime, i + 1, prime))
    return print(*sieve)

if __name__ == '__main__':
    number = int(input('Введите порядковый номер простого числа: '))
    simple_number(number)
    # simple_number_reweto_eratosfena(number)
 # FIN
    
    
# Асимптотический анализ:
#   выполняется проверка соответствия порядкового номера простого числа и введённого пользователем требуемого номера простого числа, простая единичная операция
#   затем проводится перебор делением всех чисел, от 2 до целой половины последующего числа в цикле, n**2 операций
# Оцениваю сложность алгоритма как О(n**2) - квадратичная сложность.

# Введите порядковый номер простого числа: 1500
# 0.5033364295959473

# 
#
#
#
