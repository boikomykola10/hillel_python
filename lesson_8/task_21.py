# Первый незакрашенный треугольник
h = int(input('Введите высоту треугольника: '))
m = h
for i in range(h):
    for j in range(2 * m - 1):
        if j == h - 1 - i or j == h - 1 + i or i == m - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()

# Второй закрашенный треугольник
h = int(input('Введите высоту треугольника: '))
m = h
for i in range(h):
    for j in range(2 * m - 1):
        if h - 1 - i <= j <= h - 1 + i or i == m - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()

# Ромб без высоты
h = int(input('Введите высоту ромба: ')) // 2 + 1
m = h
for i in range(h):
    for j in range(2 * m - 1):
        if h - 1 - i <= j <= h - 1 + i or i == m - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
for i in range(h - 1):
    for j in range(2 * m):
        if i == j - 1 or j == 2 * m - i - 3:
            print('*', end='')
        else:
            print(' ', end='')
    print()

# Ромб с высотой
h = int(input('Введите высоту ромба: ')) // 2 + 1
m = h
for i in range(h):
    for j in range(2 * m - 1):
        if h - 1 - i <= j <= h - 1 + i or i == m - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
for i in range(h - 1):
    for j in range(2 * m):
        if i == j - 1 or j == 2 * m - i - 3 or j == m - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()