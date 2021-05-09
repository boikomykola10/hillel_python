from pprint import pprint
from random import randint


m = int(input('Введите число столбцов: '))
n = int(input('Введите число строк: '))

lst = [[randint(10, 50) for _ in range(m)] for _ in range(n)]
ext_lst = [0] * m
for i in range(n):
    s = 0
    for j in range(m):
        print('{:>4}'.format(lst[i][j]), end='')
        s += lst[i][j]
        ext_lst[j] += lst[i][j]
    print('{:>8}'.format(s), end='')
    print()
print()

for i in range(m):
    print('{:>4}'.format(ext_lst[i]), end='')


