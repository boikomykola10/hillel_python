import random

s = set('Hello World!')
print(s, type(s))
s = set([1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
print(s)
# lst = []
d = {}
print(d, type(d))
s = {1, 3, 56, 7, 8, 5.6, 'Test'}
print(s, type(s))

for element in s:
    print(element, end=' ')
print()

s.add(45)
print(s)

s = {1, 2, 3, 4, 5, 6, 7, 8}

# len(set)
print(len(s))

# add(value)
s.add(8)
print(s)

# pop()
x = s.pop()
print(x, s)

a = {10, 12, 13, 14, 15, 16, 17, 18, 20, 21, 24, 25, 27, 29, 30, 31, 34, 35, 36, 44, 46, 48, 50}
b = {13, 15, 16, 19, 20, 22, 23, 24, 28, 29, 30, 31, 32, 34, 37, 38, 39, 40, 41, 43, 48}
# a = {random.randint(10, 50) for _ in range(30)}
# print(a)
print('len A:', len(a))
print('len B:', len(b))
# A | B         A.union(B)
# A |= B        A.update(B)
c = a | b
print(len(c), c)

# A & B         A.intersection(B)
# A &= B        A.intersection_update(B)
c = a & b
print(len(c), c)

# A - B         A.difference(B)
# A -= B        A.difference_update(B)
c = a - b
print(len(c), c)

# A ^ B         A.symmetric_difference(B)
# A ^= B        A.symmetric_difference_update(B)
c = a ^ b
print(len(c), c)
c1 = a - b
c2 = b - a
c3 = c1 | c2
print(len(c3), c3)


fs = frozenset()
print(fs, type(fs))
fs = frozenset('Hello World!')
print(fs)

a = {1, 2, 3}
b = {3, 1, 2}
print(a == b)

a = {3, 3, 3}
b = {3}
print(a == b, a, b)

