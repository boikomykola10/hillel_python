from pprint import pprint
from random import randint


m = int(input('Введите число столбцов: '))
n = int(input('Введите число строк: '))

lst = [[randint(10, 50) for x in range(n)] for i in range(m)]
for i in lst:
    s = 0
    for j in i:
        print('{:>4}'.format(j), end='')
        s += j
    print('{:>8}'.format(s), end='')
    print()
print()
for i in range(n):
    s = 0
    for j in range(m):
        s += lst[j][i]
    print('{:>4}'.format(s), end='')

