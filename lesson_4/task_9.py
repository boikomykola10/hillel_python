s = input('Введите строку: ')
ch = input('Введите символ: ')
k = 0
for i in s:
    v = s.find(ch, k)
    if v != -1:
        print(v, end=' ')
        k = v + 1

