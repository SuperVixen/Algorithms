# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.


def factory_counting():
    average_profit = float()
    unprofitable_enterprise = list()
    sum_profit = dict()
    factory_data = dict()
    factory_count = int(input('Введите количество предприятий для анализа: '))

    for i in range(1, factory_count + 1):
        print('Укажите название предприятия №', i, ': ', end='')
        factory_name = input()
        factory_data[factory_name] = list()
        sum_profit[factory_name] = 0

    for key in factory_data:
        print('Введите данные о прибыли за 4 квартала (т.е. 4 отдельных числа через пробел) для', key, ': ', end='')
        factory_data[key] = list(map(int, input().split()))

    for key in factory_data:
        sum_profit[key] = sum(factory_data[key])

    average_profit = sum(sum_profit.values()) / len(factory_data)

    print('У этих предприятий годовой доход выше среднего: ', end='')
    for key in factory_data:
        if average_profit < sum_profit[key]:
            print(key, ' ', end='')
        else:
            unprofitable_enterprise.append(key)
    print('')

    print('У этих предприятий годовой доход ниже среднего: ', end='')
    for elem in unprofitable_enterprise:
        print(elem, end=' ')



if __name__ == '__main__':
    factory_counting()

 # FIN
 
 
 Сложность алгоритма оцениваю как О(n) - линейная.
