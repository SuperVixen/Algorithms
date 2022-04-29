# 8. Определить, является ли год, который ввел пользователем,
# високосным или невисокосным.


def leap_year(y):
    if (y % 4 == 0 or y % 400 == 0) and y % 100 != 0:
        print('Високосный год',y)
    else:
        print('Не високосный год',y)
        return


if __name__ == '__main__':
    year = int(input('Введите год: '))
    leap_year(year)
