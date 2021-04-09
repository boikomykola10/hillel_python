import random

lst = [random.randrange(1, 20, 1) for _ in range(15)]
print(lst)
for i in range(5, len(lst)):
    lst[0] = lst[len(lst)-1]

print(lst)


