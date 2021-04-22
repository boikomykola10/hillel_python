a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = input('Введите операцию: ')


def arithmetic(number1, number2, c):
    if c == '+':
        return number1 + number2
    elif c == '-':
        return number1 - number2
    elif c == '*':
        return number1 * number2
    elif c == '/':
        return number1 / number2
    else:
        return "Неизвестная операция"


print(arithmetic(a, b, c))
