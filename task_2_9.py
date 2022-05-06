# 9. Среди натуральных чисел, которые были введены,
# найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

if __name__ == '__main__':

    def numberrz(n):
        sum_spisok =[]

        for i in n:
            sum_spisok.append(sum(map(int, list(str(i)))))

        a = sum_spisok.index(max(sum_spisok))
        return print('Число', n[a], 'с максимальной суммой цифр', sum_spisok[a])

    numberrz(list(map(int, input('Введите через пробел числа: ').split())))

# FIN
