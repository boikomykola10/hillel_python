import random

# randrange
for _ in range(15):
    print(random.randrange(1, 10, 1), end=', ')
print()

for _ in range(15):
    print(random.randint(1, 10), end=', ')
print()

for _ in range(15):
    print(random.random(), end=', ')
print()

for _ in range(15):
    print(random.uniform(0.1, 9.9), end=', ')
print()

lst = [random.randint(1,20) for _ in range(15)]
print(lst)
count = 0
for i in range(1, len(lst)-1):
    if lst[i - 1] < lst[i] < lst[i + 1]:
        count += 1
print(count)