s = input('Введите строку: ')
ch = input('Введите символ: ')
k = 0
for i in s:
    v = s.find(i, k)
    if i == ch:
        print(v, end=' ')
    k += 1

