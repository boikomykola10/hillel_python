number = int(input())
n1 = number // 100  # первая цифра
n2 = number // 10 % 10  # вторая цифра
n3 = number % 10    # последняя цифра
print(str(n3) + str(n2) + str(n1))

