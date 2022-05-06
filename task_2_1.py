# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем.
# После выполнения вычисления программа не должна завершаться,
# а должна запрашивать новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
# то программа должна сообщать ему об ошибке и снова запрашивать знак операции.
# Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.

if __name__ == '__main__':


    def calculator():
        flag = True
        while flag:
            operation = str(input('Введите операцию (+, -, *, /, 0 - для выхода): '))

            if operation == '0':
                flag = False
            elif operation not in ('+', '-', '*', '/'):
                print('Неправильный знак операции.')
            elif operation == '+':
                operands = operandz()
                print(summ(operands[0], operands[1], 1))
            elif operation == '-':
                operands = operandz()
                print(summ(operands[0], operands[1], - 1))
            elif operation == '*':
                operands = operandz()
                print(multi(operands[0], operands[1]))
            elif operation == '/':
                operands = operandz()
                if operands[1] == 0:
                    print('На ноль делить нельзя!')
                else:
                    print(multi(operands[0], 1 / operands[1]))

        return

    def operandz():
        return list(map(float, input('Введите через пробел два числа: ').split()))

    def summ(a,b,k):
        return a + b * k

    def multi(a, b):
        return a * b



    calculator()
    print('Калькулятор закончил работу.')
# FIN
