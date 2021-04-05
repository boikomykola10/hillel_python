a = 123456789123456789
print(a)
print(bin(a))
print(oct(a))
print(hex(a))

print(chr(0x26bd))
print('\u26bd')     # \u - 2              \U - 4
print(chr(9917))

print(ord('⚽'))
print(hex(ord('⚽')))


string = 'Process finished with exit code 0'


#      0   1   2   3   4
#      H   E   L   L   O
#     -5  -4  -3  -2  -1

print(string[0])
print(string[len(string)-1])
print(string[-1])
# string[3] = 'A'
# print(string)

# string[start: stop: step]
# string[:]


s1 = 'Process finished with exit code 0'
print(s1[0])
print(s1[0:7])
print(s1[:7])
print(s1[8:])
print(s1[8:16:2])
print(s1[::-1])
print(s1[::-2])
print(s1[::2])

s = 'Process finished with exit code 0'
# len(s1)
print(len(s))

# find(sub, start, end)
# rfind
print(s.find('it', 25))

# replace(old, new, count)
s2 = s.replace('e', 'E', 1)
print(s2)

# count(sub, start, end)
print(s.count('e', 0, 8))

#capitalize()
s = 'finIshEd with eXit code 0'
print(s.capitalize())

# upper()
# lower()
s3 = s.upper()
print(s3)
print(s3.lower())

# strip(sub)
s = '    aaaaaafinished with exit code 0bbbbbb      '
print('(' + s + ')')
print('(' + s.strip() + ')')

# title
print(s.title())
