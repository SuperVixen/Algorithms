# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из
# чисел в диапазоне от 2 до 9.

if __name__ == '__main__':

    def multiples():
        j_nums = 0
        nums = [n for n in range(2, 100)]
        multiplier = [i for i in range(2, 10)]
        for i in nums:
            i_nums = 0

            for j in multiplier:

                if i % j == 0:
                    i_nums += 1
                    
            if i_nums != 0:
                j_nums += 1
                print(i, 'кратна числам из списка от 0 до 9', i_nums, 'раз')      
        print('Всего из списка от 2 до 99 кратны каждому из чисел в диапазоне от 2 до 9', j_nums, 'чисел')     

    multiples()
# FIN
