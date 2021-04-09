import random

lst = [random.randrange(1, 20, 1) for _ in range(15)]
print(lst)
for i in range(5, len(lst)):
    lst.insert(0, lst[i])

print(lst)


