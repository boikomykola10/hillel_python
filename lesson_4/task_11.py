s = input('Введите строку: ')
b = s.find('h')     # первое вхождение 'h'
e = s.rfind('h')    # последние вхождение 'h'
s2 = s[b+1: e]      # строка между первым и последним вхождением
s3 = s2.replace('h', 'H')
s4 = s[: b+1] + s3 + s[e:]
print(s4)
