# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560,
# то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).


if __name__ == '__main__':


    def even_and_odd_calculator():

        numbers = list(map(int, input('Введите натуральное число: ')))
        odd, even = 0, 0
        for i in numbers:
            
            if i % 2 == 0:
                even += 1
            else:
                odd += 1

        print('Нечетных -',odd,', четных -', even)
        return

    even_and_odd_calculator()
