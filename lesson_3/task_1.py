N = int(input('Введите натуральное число число: '))
k = 1   # минимальное значение 2 ** 0 = 1
c = 0   # минимальная степень
while k * 2 <= N:
    k *= 2
    c += 1
print(c, k)
