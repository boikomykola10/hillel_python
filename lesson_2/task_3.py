number = int(input('Введите трёхзначное число: '))
n1 = number // 100  # первая цифра
n2 = number // 10 % 10  # вторая цифра
n3 = number % 10    # последняя цифра
print(n3, n2, n1, sep='')
