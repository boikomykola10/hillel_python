s = input('Введите строку: ')
ch = input('Введите символ: ')
for i in range(len(s)-1):
    if s[i] == ch:
        print(i, end=' ')
