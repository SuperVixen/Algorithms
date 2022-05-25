
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
    print(time_f - time_s)
    # я не могу понять в чем ошибка, но у меня в последовательность простых чисел вклинилась 4.
    # из за этого страдает нумерация на одну позицию, для 2, 3 всё верно, для последующих чисел - показывает простое число на предыдущей позиции.
    # simple_numberz.remove(4)

    print(simple_numberz)
    return print('Простое число №', num, 'это', (simple_numberz[-2]))

if __name__ == '__main__':
    number = int(input('Введите порядковый номер простого числа: '))
    simple_number(number)
   
 # FIN

# Введите порядковый номер простого числа: 1500
# 0.5033364295959473
