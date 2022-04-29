#1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

def sum_multiplication(number):
    sum = 0
    multiplication = 1
    while (number != 0):
        sum = sum + number % 10
        multiplication = multiplication * (number % 10)
        number = number // 10
    return str(sum) + " и " + str(multiplication)

if __name__ == '__main__':
    numbers = int(input('Введите трехзначное число: '))
    print('Сумма и произведение цифр числа',numbers,'равны', sum_multiplication(numbers))


